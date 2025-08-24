from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'owner',
    'start_date': days_ago(0),
    'email': ['owner@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'process_web_log',
    default_args = default_args,
    description = 'Apache Airflow Capstone Project',
    schedule_interval = timedelta(days=1),
)

extract_data = BashOperator(
    task_id='extract_ip_from_log',
    bash_command="cut -d ' ' -f1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt",
    dag=dag,
)

transform_data = BashOperator(
    task_id='filter_ip_address',
    bash_command="grep -v '198.46.149.143' /home/project/airflow/dags/capstone/extracted_data.txt > /home/project/airflow/dags/capstone/transformed_data.txt",
    dag=dag,
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf /home/project/airflow/dags/capstone/weblog.tar -C /home/project/airflow/dags/capstone transformed_data.txt',
    dag=dag,
)

extract_data >> transform_data >> load_data
