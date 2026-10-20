# airflow_env.sh - Airflow 실습용 환경 설정 (터미널을 열 때 자동으로 불러와집니다)
_LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 가상환경 켜기 (airflow 명령어가 이 안에 설치되어 있습니다)
source "$_LAB_DIR/.venv/bin/activate"

# Airflow 가 설정/로그/DB 를 보관하는 폴더 (DAG 는 airflow_home/dags 에 있습니다)
export AIRFLOW_HOME="$_LAB_DIR/airflow_home"

# 예제 DAG 수십 개가 화면에 뜨지 않게 끈다 (내 DAG 만 보기 위해)
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# Codespaces 실습용: 로그인 화면 없이 바로 들어간다 (포트는 내 GitHub 계정만 접근 가능)
export AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_ALL_ADMINS=True
