1. 로또번호 추천
- 사용자 입력(이름, 생년월일 등)을 기반으로 랜덤 로또 번호를 추천.

# backend
- mkdir backend
- cd backend
- python -m venv venv
- cd venv>cd Scripts
- activate
- pip install fastapi uvicorn
- cd backend
- (venv) ..\lotto-draw\backend> 
- uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# frontend
- npm create vite@latest frontend --template vue
- cd frontend
- npm install rollup --save-dev
- npm install
- npm run dev
- http://localhost:5173

# docker
- docker-compose up --build # 컨테이너 빌드 및 실행
- docker ps # 실행된 컨테이너 목록 확인
- docker-compose up frontend  # 프론트엔드만 실행
- docker-compose up backend   # 백엔드만 실행
- docker-compose down # 실행 중인 컨테이너 종료

# docker reBuild
- docker system prune -a # Docker 빌드 캐시 삭제
- docker-compose up --build