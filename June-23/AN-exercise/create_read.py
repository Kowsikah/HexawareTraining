from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

# Define the functions
def create_file():
    with open('/tmp/message.txt', 'w') as f:
        f.write("Welcome to Apache Airflow\nLearning DAGS\nLearning Task Dependencies")

def read_file():
    with open('/tmp/message.txt', 'r') as f:
        print(f.read())

# DAG definition using the 'schedule' argument
with DAG(
    'exercise_1', 
    start_date=datetime(2026,06,23), 
    schedule=None,  # Updated from schedule_interval
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='create_file', 
        python_callable=create_file
    )
    
    task2 = PythonOperator(
        task_id='read_file', 
        python_callable=read_file
    )
    
    # Set task dependency
    task1 >> task2
