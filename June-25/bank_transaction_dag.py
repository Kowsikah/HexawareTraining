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

def create_transaction():
    input_path = "/tmp/transactions.txt"  # Matches prompt specifications
    with open(input_path, "w") as f:
         f.write("Deposit,10000\nWithdraw,2500\nDeposit,4000\nWithdraw,1500\nDeposit,2000")

def calculate_balance():
    input_path = "/tmp/transactions.txt"
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Source file {input_path} does not exist.")
        
    deposit = 0
    withdraw = 0
    
    with open(input_path, "r") as f:
         data = f.readline()
         while data:
             if data.strip():
                 line = data.split(",")
                 action = line[0].strip()
                 amount = int(line[1].strip())
                 
                 if action == "Deposit":
                      deposit += amount
                 elif action == "Withdraw": 
                      withdraw += amount
                      
             data = f.readline()  # Added to prevent infinite loop
       return {"deposit": deposit, "withdraw": withdraw}

def generate_account_report(**kwargs): 
    output_path = "/tmp/account_report.txt" 
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='calculate_balance')
    
    if not metrics:
        raise ValueError("No transaction data received from the calculation step.")
        
    total_deposit = metrics["deposit"]
    total_withdrawal = metrics["withdraw"]
    final_balance = total_deposit - total_withdrawal     with open(output_path, "w") as f:
        f.write(f"Total Deposit = {total_deposit}\n")
        f.write(f"Total Withdrawal = {total_withdrawal}\n")
        f.write(f"Final Balance = {final_balance}\n")
        
    print(f"Successfully generated financial statement report at: {output_path}")

# DAG Definition Block
with DAG(
    "bank_transaction_report_dag",
    default_args=default_args,
    schedule="@daily",
    catchup=False
) as dag:
    
    task_create_transaction = PythonOperator(
        task_id="create_transaction",
        python_callable=create_transaction
    )
    
    task_calculate_balance = PythonOperator(
        task_id="calculate_balance",
        python_callable=calculate_balance
    )
    
    task_generate_report = PythonOperator(
        task_id="generate_account_report",
        python_callable=generate_account_report
    )
  
    task_create_transaction >> task_calculate_balance >> task_generate_report