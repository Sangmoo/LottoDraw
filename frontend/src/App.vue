<template>
  <div id="app">
    <!-- <h1>AI 로또 번호 추천</h1> -->
    <LottoDraw />
  </div>
</template>

<script>
import LottoDraw from './components/LottoDraw.vue';

export default {
  components: {
    LottoDraw
  }
};
</script>

<style>
h1 {
  text-align: center;
  color: #333;
}
</style>
