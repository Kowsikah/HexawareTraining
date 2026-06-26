import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator 
def create_employee_file():
     with open("/tmp/employees.txt", "w") as f:
         f.write("Rahul,28\nPriya,31\nAmit,42\nSneha,26\nKiran,38")

def calculate():
     with open("/tmp/employees.txt", "r") as f:
         line = f.readline()
         highest_age = 0
         lowest_age = 100
         sum = 0
         count = 0
         
         while line:
            if line.strip():
                data = line.split(",")
                age_val = int(data[1].strip())
                
                sum += age_val
                count += 1
                
                if highest_age < age_val:
                      highest_age = age_val
                if lowest_age > age_val:
                      lowest_age = age_val
                      
            line = f.readline()
            
         average_age = sum / count
    return {"Young_age": lowest_age, "Old_age": highest_age, "average": average_age}

def generate_report(**kwargs): 

    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids="task_calculate")
    
    if not metrics:
        print("No data available")
        return
    
    with open("/tmp/age_report.txt", "w") as f:  # Added missing 'as f'
        # Replaced prints with actual file write statements to generate the report
        f.write(f"Youngest Employee = {metrics['Young_age']}\n")
        f.write(f"Oldest Employee = {metrics['Old_age']}\n")
        f.write(f"Average Age = {metrics['average']}\n")

with DAG(dag_id='ages_dag', start_date=datetime(2026, 6, 25), catchup=False) as dag:
    
    task_create_employee_file = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file
    )
    
    task_calculate = PythonOperator(
        task_id="task_calculate",
        python_callable=calculate
    )
    
    task_generate_report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )
   
    task_create_employee_file >> task_calculate >> task_generate_report