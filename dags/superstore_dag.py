# superstore_dag.py
import importlib.util
import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Path to scripts folder inside Docker
SCRIPTS_PATH = "/opt/airflow/scripts"

def load_script_function(script_name, function_name):
    """
    Dynamically load a function from a Python script file.
    """
    script_path = os.path.join(SCRIPTS_PATH, f"{script_name}.py")
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script {script_path} not found in Docker container.")
    
    spec = importlib.util.spec_from_file_location(script_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if not hasattr(module, function_name):
        raise AttributeError(f"Function {function_name} not found in {script_name}.py")
    
    return getattr(module, function_name)

# Load ETL functions dynamically
download_csv = load_script_function("extract", "download_csv")
transform_data = load_script_function("transform", "transform_data")
load_data = load_script_function("load", "load_data")

# Default DAG args
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 19),
    'retries': 1
}

# Define the DAG
with DAG(
    dag_id='superstore_etl',
    default_args=default_args,
    schedule_interval=None,  # manual trigger
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=download_csv
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_data
    )

    # Task sequence
    extract_task >> transform_task >> load_task
