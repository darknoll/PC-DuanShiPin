<template>
  <div class="downloading">
    <downloading-top />
    <div class="items">
      <template v-for="(item, index) in 30">
        <downloading-item :key="index" />
      </template>
    </div>
  </div>
</template>
<script>
import DownloadingTop from "./DownloadingTop";
import DownloadingItem from "./DownloadingItem";
export default {
  components: {
    DownloadingTop,
    DownloadingItem
  }
};
</script>
<style lang="scss" scoped>
.downloading {
  overflow: hidden;
}
.items {
  overflow: scroll;
  height: calc(100vh - 50px);
}
</style>
