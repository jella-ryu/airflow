import pendulum
import datetime
from airflow import DAG

with DAG(
    dag_id="example_complex", # 화면에서 보이는 값인데, 파일명과 일치시키는게 좋음.
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag: