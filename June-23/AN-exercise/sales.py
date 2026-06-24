import csv
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def create_csv():
    with open('/tmp/sales.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['product', 'quantity', 'price'])
        writer.writerow(['Laptop', 2, 70000])
        writer.writerow(['Mouse', 5, 500])
        writer.writerow(['Keyboard', 3, 1200])

def calculate_revenue():
    results = {}
    total_rev = 0
    with open('/tmp/sales.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rev = int(row['quantity']) * int(row['price'])
            results[row['product']] = rev
            total_rev += rev
    return results, total_rev

def create_summary(ti):
    results, total = ti.xcom_pull(task_ids='calculate_revenue')
    with open('/tmp/sales_summary.txt', 'w') as f:
        for prod, rev in results.items():
            f.write(f"{prod} = {rev}\n")
        f.write(f"Total Revenue = {total}")

with DAG('csv_processing', start_date=datetime(2026, 1, 1), schedule=None, catchup=False) as dag:
    task1 = PythonOperator(task_id='create_csv', python_callable=create_csv)
    task2 = PythonOperator(task_id='calculate_revenue', python_callable=calculate_revenue)
    task3 = PythonOperator(task_id='create_summary', python_callable=create_summary)
    task1 >> task2 >> task3