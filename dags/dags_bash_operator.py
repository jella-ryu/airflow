import pendulum
import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # 화면에서 보이는 값인데, 파일명과 일치시키는게 좋음.
    schedule="0 0 * * *", # 크론 스케줄
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 덱이 언제부터 돌건지, 한국시간으로
    catchup=False, # 덱이 처음 돌때 과거 데이터를 처리할지 여부(true는 상황에 따라 위험. 한번에 돈다)
    tags=["example", "example2", "example3"], # 태그는 덱을 찾아주는 키워드(파란박스), 옵션
) as dag:
    bash_t1 = BashOperator(
            task_id="bash_t1", #화면에 나타난 태스크명
            bash_command="echo whoami", #어떤 쉘 스크립트를 수행하는지
        )

    bash_t2 = BashOperator(
            task_id="bash_t2",
            bash_command="echo $HOSTNAME",
        )

    bash_t1 >> bash_t2