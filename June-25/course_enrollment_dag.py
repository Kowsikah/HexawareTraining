import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

# Default arguments for the DAG setup
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 6, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def create_enrollment_file():
    """Task 1: Creates the raw course enrollment data file."""
    input_path = "/tmp/enrollments.txt"
    with open(input_path, "w") as f:
        f.write("Java,Rahul\nPython,Priya\nJava,Amit\nPython,Sneha\nJava,Kiran\nPython,Megha")

def count_students():
    """Task 2: Counts student registration distributions per course platform."""
    input_path = "/tmp/enrollments.txt"
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Source file {input_path} does not exist.")
        
    java_count = 0
    python_count = 0
    
    with open(input_path, "r") as f:
        line = f.readline()
        while line:
            if line.strip():
                data = line.split(",")
                course = data[0].strip()
                
                if course == "Java":
                    java_count += 1
                elif course == "Python":
                    python_count += 1
                    
            line = f.readline()
            
    return {"Java": java_count, "Python": python_count}

def generate_enrollment_report(**kwargs):
    """Task 3: Compiles aggregate metrics and creates the final report file."""
    output_path = "/tmp/enrollment_report.txt"
    
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids="task_count_students")
    
    if not metrics:
        raise ValueError("No enrollment statistics found from the calculation pipeline.")
        
    with open(output_path, "w") as f:
        f.write(f"Java Course Enrollment = {metrics['Java']}\n")
        f.write(f"Python Course Enrollment = {metrics['Python']}\n")
        
    print(f"Successfully generated enrollment summary at: {output_path}")

# DAG Definition Block
with DAG(
    dag_id='enrollment_dag', 
    default_args=default_args,
    description='Exercise 14: Compiles student registration metrics by course program',
    schedule="@daily", 
    catchup=False
) as dag:
    
    task_create_file = PythonOperator(
        task_id="create_enrollment_file",
        python_callable=create_enrollment_file
    )
    
    task_count_students = PythonOperator(
        task_id="task_count_students",
        python_callable=count_students
    )
    
    task_generate_report = PythonOperator(
        task_id="generate_enrollment_report",
        python_callable=generate_enrollment_report
    )
    
    # Task Pipeline Sequencing Flow
    task_create_file >> task_count_students >> task_generate_report