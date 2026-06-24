from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def create_marks_file():
    # Creating the input file /tmp/marks.txt
    with open('/tmp/marks.txt', 'w') as f:
        f.write("Math, 80\nScience, 75\nEnglish, 90\nPython, 95")

def calculate_average():
    # Reading the marks and calculating the average
    marks = []
    with open('/tmp/marks.txt', 'r') as f:
        for line in f:
            marks.append(int(line.split(',')[1].strip()))
    
    avg = sum(marks) / len(marks)
    print(f"Calculated Average = {avg}")
    return avg

def generate_result(ti):
    # Pulling the average from the previous task
    avg = ti.xcom_pull(task_ids='calculate_average')
    # Determining result status
    result = "EASS" if avg >= 85 else "FAIL"
    
    with open('/tmp/result.txt', 'w') as f:
        f.write(f"Average Marks = {avg}\nResult = {result}")

with DAG(
    'student_marks_processing',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(task_id='create_marks_file', python_callable=create_marks_file)
    task2 = PythonOperator(task_id='calculate_average', python_callable=calculate_average)
    task3 = PythonOperator(task_id='generate_result', python_callable=generate_result)

    # Defining the flow as specified in the exercise
    task1 >> task2 >> task3