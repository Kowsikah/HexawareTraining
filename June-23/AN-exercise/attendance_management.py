from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def create_attendance():
    with open('/tmp/attendance.txt', 'w') as f:
        f.write("Rahul, Present\nPriya, Present\nAmit, Absent\nSneha, Present\nKiran, Absent")

def count_attendance(ti):
    present = 0
    absent = 0
    with open('/tmp/attendance.txt', 'r') as f:
        for line in f:
            if "Present" in line:
                present += 1
            else:
                absent += 1
    ti.xcom_push(key='present', value=present)
    ti.xcom_push(key='absent', value=absent)

def generate_summary(ti):
    present = ti.xcom_pull(key='present', task_ids='count_attendance')
    absent = ti.xcom_pull(key='absent', task_ids='count_attendance')
    total = present + absent
    with open('/tmp/attendance_report.txt', 'w') as f:
        f.write(f"Total Students = {total}\nPresent = {present}\nAbsent = {absent}")

with DAG('attendance_report', start_date=datetime(2026, 1, 1), schedule=None, catchup=False) as dag:
    task1 = PythonOperator(task_id='create_attendance', python_callable=create_attendance)
    task2 = PythonOperator(task_id='count_attendance', python_callable=count_attendance)
    task3 = PythonOperator(task_id='generate_summary', python_callable=generate_summary)
    task1 >> task2 >> task3