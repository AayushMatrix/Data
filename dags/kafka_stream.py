from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'airscholar',
    'start_date':datetime(2023,8,3,10,00)
}