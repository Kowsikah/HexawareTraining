from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Defining the task functions
def wake_up():
    print("Student woke up at 6 AM")

def attend_class():
    print("Student attended Python class")

def complete_assignment():
    print("Student completed Airflow assignment")

def exercise():
    print("Student completed morning exercise")

def sleep():
    print("Student went to sleep at 10 PM")

# DAG definition
with DAG(
    dag_id="student_daily_tasks_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["training"]
) as dag:

    # Task creation
    wake_up_task = PythonOperator(task_id="wake_up_task", python_callable=wake_up)
    exercise_task = PythonOperator(task_id="exercise_task", python_callable=exercise)
    attend_class_task = PythonOperator(task_id="attend_class_task", python_callable=attend_class)
    complete_assignment_task = PythonOperator(task_id="complete_assignment_task", python_callable=complete_assignment)
    sleep_task = PythonOperator(task_id="sleep_task", python_callable=sleep)

    # Dependencies (including the challenge task)
    wake_up_task >> exercise_task >> attend_class_task >> complete_assignment_task >> sleep_task