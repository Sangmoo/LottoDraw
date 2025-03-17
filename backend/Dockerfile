# Python 3.9 기반 FastAPI 실행 환경
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 소스 코드 복사
COPY . .

# 실행 명령 수정 (uvicorn 경로 확인)
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
