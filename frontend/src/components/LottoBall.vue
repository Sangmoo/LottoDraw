<template>
  <div class="lotto-ball"
       :style="{ backgroundColor: colors[number % colors.length] }"
       :class="{ 'appear': show }">
    {{ number }}
  </div>
</template>

<script>
export default {
  props: ["number", "delay"],
  data() {
    return {
      colors: ["#FF5733", "#33FF57", "#3357FF", "#F4D03F", "#A569BD", "#17A589"],
      show: false
    };
  },
  mounted() {
    setTimeout(() => {
      this.show = true;
    }, this.delay * 1000); // ✅ 0.5초 간격으로 공 등장
  }
};
</script>

<style>
/* ✅ 로또 공 스타일 */
.lotto-ball {
  display: inline-flex;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  font-weight: bold;
  color: white;
  margin: 10px;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

/* ✅ 공이 나타나는 애니메이션 */
.appear {
  transform: scale(1);
}
</style>
