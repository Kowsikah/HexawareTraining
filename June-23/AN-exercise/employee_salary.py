from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def create_salary_file():
    with open('/tmp/employees.txt', 'w') as f:
        f.write("Rahul, 45000\nPriya, 52000\nAmit, 61000\nSneha, 48000")

def calculate_salary():
    total = 0
    with open('/tmp/employees.txt', 'r') as f:
        for line in f:
            # Splits the line by comma and adds the salary value
            total += int(line.split(',')[1].strip())
    print(f"Total Salary = {total}")
    return total

def generate_report(ti):
    # Pulls the returned value from the task 'calculate_total_salary'
    total = ti.xcom_pull(task_ids='calculate_total_salary')
    with open('/tmp/report.txt', 'w') as f:
        f.write(f"Salary Report\nEmployees = 4\nTotal Salary = {total}")

with DAG(
    'employee_salary_report',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='create_salary_file', 
        python_callable=create_salary_file
    )
    
    task2 = PythonOperator(
        task_id='calculate_total_salary', 
        python_callable=calculate_salary
    )
    
    task3 = PythonOperator(
        task_id='generate_report', 
        python_callable=generate_report
    )

    # Define dependencies
    task1 >> task2 >> task3