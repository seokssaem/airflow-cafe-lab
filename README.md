# ☕ Airflow 카페 주문 실습 (Codespaces)

설치 없이 브라우저에서 Airflow 를 실행하는 실습 환경입니다.

## 시작하기
1. 이 저장소 페이지에서 초록색 **Code** 버튼 → **Codespaces** 탭 → **Create codespace on main**
2. 화면이 열리고 아래쪽 터미널에 설치 로그가 올라갑니다. `설치 완료` 와 `3.3.2` 가 보일 때까지 **2~4분** 기다립니다.
3. 터미널에 입력합니다. (이 터미널은 실습 내내 켜 두세요)
   ```bash
   airflow standalone
   ```
4. 1~2분 뒤 아래쪽 **포트(Ports)** 탭의 `8080` 줄에서 **지구본 아이콘(브라우저에서 열기)** 을 누르면 Airflow 화면이 열립니다. 로그인 없이 바로 들어갑니다.
5. 이후는 노션 자료의 **4장(예제 ① 카페 주문)** 부터 그대로 합니다.
   - DAG 파일은 이미 `airflow_home/dags/` 안에 들어 있어서 만들 필요가 없습니다.
   - 새 터미널이 필요하면 터미널 오른쪽 위 **+** 를 누르세요. (환경이 자동으로 켜집니다)

## 끝낼 때
- 터미널에서 `Ctrl + C` 로 Airflow 를 끕니다.
- **Codespace 를 꼭 멈춥니다**: 왼쪽 아래 `Codespaces:` 표시 → **Stop Current Codespace**. (무료 사용 시간이 방치로 낭비되지 않게)
- 다시 쓸 때는 github.com/codespaces 에서 열고 `airflow standalone` 만 실행하면 됩니다.

## 막혔을 때
| 증상 | 해결 |
|---|---|
| `airflow: command not found` | 터미널을 새로 열거나 `source airflow_env.sh` |
| 포트 탭에 8080 이 없음 | `airflow standalone` 이 아직 시작 중입니다. 1~2분 기다리세요. |
| DAG 가 안 보임 | 1~2분 대기 후 새로고침, `airflow dags list-import-errors` |
| 트리거했는데 계속 queued | DAG 토글이 꺼져 있습니다(Paused). 켜세요. |
