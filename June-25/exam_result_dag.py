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

def create_result_file():
    input_path = '/tmp/results.txt'
    content = [
        "Rahul, Pass\n",
        "Priya, Fail\n",
        "Amit, Pass\n",
        "Sneha, Pass\n",
        "Kiran, Fail\n",
        "Megha, Pass\n"
    ]
    
    with open(input_path, 'w') as f:
        f.writelines(content)
    print(f"Successfully created raw file at: {input_path}")

def count_pass_fail():
    input_path = '/tmp/results.txt'
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Source file {input_path} does not exist.")
        
    pass_count = 0
    fail_count = 0
    
    with open(input_path, 'r') as f:
        for line in f:
            if line.strip():
                name, status = line.split(',')
                status = status.strip().lower()
                
                if status == 'pass':
                    pass_count += 1
                elif status == 'fail':
                    fail_count += 1
                    
       summary_metrics = {
        'Total Pass': pass_count,
        'Total Fail': fail_count
    }
    return summary_metrics

def generate_result_summary(**kwargs):
    output_path = '/tmp/result_summary.txt'
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='count_pass_fail')
    
    if not metrics:
        raise ValueError("No summary data received from the calculation step.")
    with open(output_path, 'w') as f:
        f.write(f"Total Pass = {metrics['Total Pass']}\n")
        f.write(f"Total Fail = {metrics['Total Fail']}\n")
            
    print(f"Successfully generated final result report at: {output_path}")

with DAG(
    'exam_result_dag',
    default_args=default_args,
    schedule='@daily',catchup=False,
) as dag:

   task_create_file = PythonOperator(
        task_id='create_result_file',
        python_callable=create_result_file,
    )

    task_count_metrics = PythonOperator(
        task_id='count_pass_fail',
        python_callable=count_pass_fail,
    )

    task_generate_report = PythonOperator(
        task_id='generate_result_summary',
        python_callable=generate_result_summary,
    )

    
    task_create_file >> task_count_metrics >> task_generate_report