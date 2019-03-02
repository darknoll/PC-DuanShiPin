<template>
  <div class="downloading-top">
    <span>下载总进度</span>
    <el-progress
      :text-inside="true"
      :stroke-width="12"
      :percentage="percentage"
      class="downloading-progress"
    ></el-progress>
    <span>{{ downloadSpeed }}</span>
    <el-button-group class="downloading-btns">
      <el-button type="primary" size="mini">{{ startOrPause }}</el-button>
      <el-button type="primary" size="mini">全部取消</el-button>
    </el-button-group>
  </div>
</template>
<script>
export default {
  data() {
    return {
      percentage: 50,
      speed: -1,
      status: "pause"
    };
  },
  computed: {
    downloadSpeed() {
      if (this.speed === -1) {
        return "下载请求中...";
      }
      return `${this.speed} KB/s`;
    },
    startOrPause() {
      if (this.status === "start") {
        return "全部暂停";
      } else if (this.status === "pause") {
        return "全部开始";
      }
      return "";
    }
  }
};
</script>
<style lang="scss" scoped>
.downloading-top {
  background-color: rgba(255, 255, 255, 0.6);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  padding: 5px 10px;
}
.downloading-progress {
  flex: 1;
  margin: 0 10px;
}
.downloading-btns {
  margin: 0 0 0 10px;
  font-family: "微软雅黑";
}
</style>
