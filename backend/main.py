from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import hashlib

app = FastAPI()

# ✅ CORS 설정 추가 (Vue.js와 연결하기 위함)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 프론트엔드 도메인 추가
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # OPTIONS도 자동으로 허용됨
    allow_headers=["*"],
)

class UserInput(BaseModel):
    name: str
    birthdate: str  # YYYY-MM-DD 형식

def generate_lotto_numbers(seed_value):
    random.seed(hashlib.md5(seed_value.encode()).hexdigest())  # 해시 기반 시드 설정
    return sorted(random.sample(range(1, 46), 6))  # 1~45 중 6개 선택

@app.post("/generate-lotto/")
def generate_lotto(user: UserInput):
    seed_value = user.name + user.birthdate
    numbers = generate_lotto_numbers(seed_value)
    return {"lotto_numbers": numbers}
