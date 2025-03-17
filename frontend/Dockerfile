# Node.js 최신 LTS 버전 사용
FROM node:18

# 작업 디렉터리 설정
WORKDIR /app

# 환경변수 설정
ENV NODE_ENV development
ENV ROLLUP_WATCH false

# package.json과 package-lock.json 복사 후 설치
COPY package.json package-lock.json ./

# ⚠️ rollup 관련 패키지가 설치되지 않도록 강제 설정
RUN npm install --legacy-peer-deps && npm uninstall rollup @rollup/rollup-linux-x64-gnu

# 프로젝트 코드 복사
COPY . .

# Vite 실행
CMD ["npm", "run", "dev", "--", "--host"]
