# minseung
import pendulum
import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator", # 화면에서 보이는 값인데, 파일명과 일치시키는게 좋음.
    schedule="30 6 * * *", # 크론 스케줄
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"), # 덱이 언제부터 돌건지, 한국시간으로
    catchup=False, # 덱이 처음 돌때 과거 데이터를 처리할지 여부(true는 상황에 따라 위험. 한번에 돈다)
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0, 3) # 0, 1, 2, 3 중 하나
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit,
    )

    py_t1