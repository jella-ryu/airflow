# minseung 

from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    send_email = EmailOperator(
        task_id="send_email",
        to="minseung.ryou@gmail.com",
        subject="Airflow 성공 Email",
        html_content="Airflow 이메일 보내기 성공했당."
    )