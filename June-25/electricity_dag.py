import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 6, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def create_bill_file():
    input_path = '/tmp/electricity.txt'
    content = [
        "Rahul, 210\n",
        "Priya, 180\n",
        "Amit, 300\n",
        "Sneha, 150\n",
        "Kiran, 260\n"
    ]
    
    with open(input_path, 'w') as f:
        f.writelines(content)
    print(f"Successfully created raw file at: {input_path}")

def calculate_total_units():
    input_path = '/tmp/electricity.txt'
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Source file {input_path} does not exist.")
        
    total_units = 0
    customer_count = 0
    
    with open(input_path, 'r') as f:
        for line in f:
            if line.strip():
                name, units_str = line.split(',')
                total_units += int(units_str.strip())
                customer_count += 1
                
    average_units = total_units / customer_count if customer_count > 0 else 0
    metrics = {
        'Customers': customer_count,
        'Total Units': total_units,
        'Average Units': int(average_units)  # Stored as integer to match expected output format
    }
    return metrics

def generate_bill_summary(**kwargs):
     output_path = '/tmp/bill_summary.txt'
     ti = kwargs['ti']
     metrics = ti.xcom_pull(task_ids='calculate_total_units')
    
    if not metrics:
        raise ValueError("No metrics data received from the calculation step.")
    with open(output_path, 'w') as f:
        f.write(f"Customers = {metrics['Customers']}\n")
        f.write(f"Total Units = {metrics['Total Units']}\n")
        f.write(f"Average Units = {metrics['Average Units']}\n")
            
    print(f"Successfully generated final summary report at: {output_path}")

# DAG Definition
with DAG(
    'electricity_bill_dag',
    default_args=default_args,
    schedule='@daily',       
    catchup=False,
) as dag:

     task_create_file = PythonOperator(
        task_id='create_bill_file',
        python_callable=create_bill_file,
    )

    task_calculate_units = PythonOperator(
        task_id='calculate_total_units',
        python_callable=calculate_total_units,
    )

    task_generate_summary = PythonOperator(
        task_id='generate_bill_summary',
        python_callable=generate_bill_summary,
    )

    task_create_file >> task_calculate_units >> task_generate_summary