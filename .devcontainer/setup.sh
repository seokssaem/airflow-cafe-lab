#!/usr/bin/env bash
# setup.sh - Codespace 가 처음 만들어질 때 한 번 실행된다 (uv + Airflow 설치)
set -euo pipefail

AIRFLOW_VERSION=3.3.2
cd "$(dirname "$0")/.."          # 저장소 루트

pip install --quiet uv
uv venv --python 3.12 .venv
source .venv/bin/activate

PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
uv pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# 새 터미널을 열 때마다 환경이 자동으로 켜지게 한다
LINE="source $(pwd)/airflow_env.sh"
grep -qxF "$LINE" ~/.bashrc || echo "$LINE" >> ~/.bashrc

source airflow_env.sh
airflow version
echo "설치 완료. 터미널에서 'airflow standalone' 을 실행하세요."
