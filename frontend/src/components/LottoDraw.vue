<template>
  <div class="lotto-container">
    <h2>🎯 AI 로또 번호 추천 🎯</h2>
    
    <div class="input-container">
      <input type="text" v-model="name" placeholder="이름을 입력하세요">
      <input type="date" v-model="birthdate">
      <button @click="fetchLottoNumbers" :disabled="loading">
        {{ loading ? "추첨 중..." : "추천 받기" }}
      </button>
    </div>

    <div class="balls">
      <LottoBall v-for="(num, index) in lottoNumbers"
                 :key="index"
                 :number="num"
                 :delay="index * 0.5" />
    </div>
  </div>
</template>

<script>
import LottoBall from "./LottoBall.vue";

export default {
  components: {
    LottoBall
  },
  data() {
    return {
      name: "",
      birthdate: "",
      lottoNumbers: [],
      loading: false
    };
  },
  methods: {
    async fetchLottoNumbers() {
      if (!this.name || !this.birthdate) {
        alert("이름과 생년월일을 입력해주세요.");
        return;
      }
      this.loading = true;
      this.lottoNumbers = [];

      try {
        const response = await fetch("http://localhost:8000/generate-lotto/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name: this.name, birthdate: this.birthdate })
        });

        if (!response.ok) {
          throw new Error(`서버 응답 오류: ${response.status}`);
        }

        const data = await response.json();

        // ✅ 0.5초 간격으로 공이 하나씩 나오도록 설정
        data.lotto_numbers.forEach((num, index) => {
          setTimeout(() => {
            this.lottoNumbers.push(num);
          }, index * 500);
        });

      } catch (error) {
        console.error("API 요청 오류:", error);
        alert("서버와의 연결에 문제가 발생했습니다.");
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
/* ✅ 전체 컨테이너 가운데 정렬 및 스타일 조정 */
.lotto-container {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-size: 1.5rem; /* 글씨 크기 증가 */
}

/* ✅ 입력 필드와 버튼 디자인 개선 */
.input-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 20px;
}

input {
  padding: 12px;
  width: 300px;
  font-size: 1.2rem;
  border-radius: 8px;
  border: 2px solid #ccc;
  text-align: center;
}

button {
  padding: 12px 20px;
  font-size: 1.2rem;
  background-color: #ff5733;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.3s;
}

button:hover {
  background-color: #e64a19;
}

.balls {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
