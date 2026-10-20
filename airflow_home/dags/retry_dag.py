"""retry_dag.py - Airflow 개념 익히기 ②: 실패와 자동 재시도

첫 번째 시도는 '일부러' 실패하고, 10초 뒤 자동으로 다시 시도해서 성공한다.
"""
import os
from datetime import timedelta

import pendulum
from airflow.sdk import dag, task

MARKER = "/tmp/airflow_retry_demo.marker"   # '이미 한 번 실패했다'는 표시 파일


@dag(
    dag_id="retry_demo",
    schedule=None,
    start_date=pendulum.datetime(2026, 10, 1, tz="Asia/Seoul"),
    catchup=False,
    # 실패하면 10초 뒤에 최대 2번까지 다시 시도한다
    default_args={"retries": 2, "retry_delay": timedelta(seconds=10)},
    tags=["lecture", "concept"],
)
def retry_demo():
    @task
    def flaky_job():
        if not os.path.exists(MARKER):
            open(MARKER, "w").close()                  # 표시 파일을 만들고
            raise RuntimeError("일부러 실패! (첫 번째 시도)")   # 실패시킨다
        os.remove(MARKER)                              # 표시 파일을 지우고
        print("두 번째 시도에서 성공!")                   # 성공한다

    flaky_job()


retry_demo()
