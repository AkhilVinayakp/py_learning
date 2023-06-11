# for scheduling purposes
from datetime import timedelta, datetime

from airflow import DAG

# operators for creating the task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# setting up default arguments
default_args = {
    'owner': "Ak",
    'start_date': datetime(2023, 4, 13),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

# initiating DAG
sampleDag = DAG('Sample_dag', default_args=default_args,
                description="Test DAG file",
                schedule_interval='* * * * *',
                catchup=False,
                tags=['sample']
                )

# function which will be called by the operator
# the task
def print_hai():
    return "Hi"

python_task = PythonOperator(python_callable=print_hai,task_id="pytask1", dag=sampleDag)
bash_task = BashOperator(task_id="bash1", bash_command="date", dag=sampleDag)

bash_task >> python_task