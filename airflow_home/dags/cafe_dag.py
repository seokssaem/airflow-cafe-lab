"""cafe_dag.py - Airflow 개념 익히기 ①: 카페 주문 처리 (순서 · 병렬 · XCom)

흐름:  take_order ─┬─ make_coffee ───┬─ pack ── serve
                   └─ make_sandwich ─┘
"""
import time

import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import dag, task


@dag(
    dag_id="cafe_order",             # 웹 화면에 보이는 DAG 이름
    schedule=None,                   # None = 자동 실행 없음 (내가 버튼을 눌러야 실행)
    start_date=pendulum.datetime(2026, 10, 1, tz="Asia/Seoul"),
    catchup=False,                   # 과거 날짜 분량을 몰아서 실행하지 않음
    tags=["lecture", "concept"],     # 화면에서 DAG 를 분류하는 꼬리표
)
def cafe_order():
    # Task 1: 쉘 명령을 실행하는 Task (Operator 방식)
    take_order = BashOperator(
        task_id="take_order",
        bash_command="echo '주문 접수: 아메리카노 + 샌드위치'",
    )

    # Task 2, 3: 파이썬 함수에 @task 만 붙이면 Task 가 된다 (TaskFlow 방식)
    @task
    def make_coffee() -> str:
        print("커피 내리는 중...")
        time.sleep(10)               # 일하는 시간을 흉내 낸다 (10초)
        print("커피 완성!")
        return "아메리카노"           # return 값은 XCom(쪽지)으로 저장된다

    @task
    def make_sandwich() -> str:
        print("샌드위치 만드는 중...")
        time.sleep(10)               # 커피와 '동시에' 진행되므로 전체 시간은 10초 + 알파
        print("샌드위치 완성!")
        return "햄치즈 샌드위치"

    # Task 4: 앞의 두 Task 가 건네준 쪽지(XCom)를 인자로 받는다
    @task
    def pack(coffee: str, sandwich: str) -> str:
        box = f"[포장 완료] {coffee} + {sandwich}"
        print(box)
        return box

    # Task 5: 마지막 Task
    serve = BashOperator(
        task_id="serve",
        bash_command="echo '손님에게 전달 완료!'",
    )

    # 순서 정하기
    coffee = make_coffee()
    sandwich = make_sandwich()
    take_order >> [coffee, sandwich]     # 주문 접수 후 두 일이 '동시에' 시작
    pack(coffee, sandwich) >> serve      # 두 일이 모두 끝나면 포장 -> 전달


cafe_order()   # ★ 마지막에 반드시 호출! 빠트리면 DAG 가 화면에 나타나지 않습니다.
