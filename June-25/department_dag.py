from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import os

INPUT_FILE = '/tmp/departments.txt'
OUTPUT_FILE = '/tmp/department_report.txt'

def create_file():
    data = "IT, 45000\nHR, 35000\nFinance, 50000\nIT, 55000\nFinance, 40000\nHR, 30000"
    with open(INPUT_FILE, 'w') as f:
        f.write(data)

def calculate_data():
    results = {}
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            dept, salary = line.strip().split(', ')
            results[dept] = results.get(dept, 0) + int(salary)
    
    # Store results in a file to be picked up by the next task
    with open('/tmp/calc_results.txt', 'w') as f:
        for dept, total in results.items():
            f.write(f"{dept}={total}\n")

def generate_report():
    with open('/tmp/calc_results.txt', 'r') as f:
        report = f.read()
    with open(OUTPUT_FILE, 'w') as f:
        f.write("Department Salary Report\n")
        f.write("========================\n")
        f.write(report)

with DAG(
    'department_salary_dag',
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id='create_department_file', python_callable=create_file)
    t2 = PythonOperator(task_id='calculate_department_salary', python_callable=calculate_data)
    t3 = PythonOperator(task_id='generate_department_report', python_callable=generate_report)

    t1 >> t2 >> t3