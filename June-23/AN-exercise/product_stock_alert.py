from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def create_inventory():
    # Creating the initial inventory file
    with open('/tmp/inventory.txt', 'w') as f:
        f.write("Rice, 50\nOil, 7\nSoap, 35\nSugar, 10\nTea, 5")

def find_low_stock():
    # Rule: Stock < 15
    low_stock_items = []
    with open('/tmp/inventory.txt', 'r') as f:
        for line in f:
            item, stock = line.split(',')
            if int(stock.strip()) < 15:
                low_stock_items.append(item.strip())
    # Return the filtered list to be used by the next task
    return low_stock_items

def generate_alert(ti):
    # Retrieve the list from the 'find_low_stock' task
    items = ti.xcom_pull(task_ids='find_low_stock')
    # Write the output to /tmp/alerts.txt
    with open('/tmp/alerts.txt', 'w') as f:
        f.write("\n".join(items))

with DAG(
    'product_stock_alert',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(task_id='create_inventory', python_callable=create_inventory)
    task2 = PythonOperator(task_id='find_low_stock', python_callable=find_low_stock)
    task3 = PythonOperator(task_id='generate_alert', python_callable=generate_alert)

    # Workflow dependencies
    task1 >> task2 >> task3