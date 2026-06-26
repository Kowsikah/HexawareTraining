import os
import csv
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

def create_orders():
    input_path = '/tmp/orders.csv'
    headers = ['product', 'quantity', 'price']
    rows = [
        ['Laptop', '1', '70000'],
        ['Mouse', '4', '500'],
        ['Monitor', '2', '12000'],
        ['Keyboard', '3', '1500']
    ]
    
    with open(input_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"Successfully created CSV raw file at: {input_path}")

def calculate_order_value():
    input_path = '/tmp/orders.csv'
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Source file {input_path} does not exist.")
        
    total_revenue = 0
    highest_revenue = 0
    highest_selling_product = ""
    with open(input_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row['product'].strip()
            quantity = int(row['quantity'].strip())
            price = int(row['price'].strip())
            product_revenue = quantity * price
            total_revenue += product_revenue
            if product_revenue > highest_revenue:
                highest_revenue = product_revenue
                highest_selling_product = product
    sales_metrics = {
        'Total Revenue': total_revenue,
        'Highest Selling Product': highest_selling_product
    }
    return sales_metrics

def generate_sales_report(**kwargs):
     output_path = '/tmp/sales_report.txt'
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='calculate_order_value')
    
    if not metrics:
        raise ValueError("No sales data received from the calculation step.")
    with open(output_path, 'w') as f:
        f.write(f"Total Revenue = {metrics['Total Revenue']}\n")
        f.write(f"Highest Selling Product = {metrics['Highest Selling Product']}\n")
            
    print(f"Successfully generated final sales report at: {output_path}")

# DAG Definition
with DAG(
    'online_orders_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as dag:
    task_create_orders = PythonOperator(
        task_id='create_orders',
        python_callable=create_orders,
    )

    task_calculate_value = PythonOperator(
        task_id='calculate_order_value',
        python_callable=calculate_order_value,
    )

     task_generate_report = PythonOperator(
        task_id='generate_sales_report',
        python_callable=generate_sales_report,
    )

    task_create_orders >> task_calculate_value >> task_generate_report