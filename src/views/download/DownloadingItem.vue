<template>
  <div class="downloading-item">
    <div class="left">
      <div class="file-icon">
        <img src="@/assets/png/video.png" />
      </div>
      <div class="title">
        <div style="margin-bottom: 10px">{{ title }}</div>
        <div>{{ sizeInfo }}</div>
      </div>
    </div>
    <div class="middle"></div>
    <div class="time-left">
      <span>{{ currTimeLeft }}</span>
    </div>
    <div class="right">
      <div class="progress">
        <el-progress :percentage="80" color="#8e71c7"></el-progress>
        <div style="margin-top: 5px">{{ currSpeed }}</div>
      </div>
      <div class="btns">
        <div @click="handlePlayOrPlause">
          <img src="@/assets/png/play.png" />
        </div>
        <div @click="handleDelete">
          <img src="@/assets/png/delete.png" />
        </div>
        <div @click="handleOpenFolder">
          <img src="@/assets/png/folder.png" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      title: "短视频001",
      size: 93.84,
      downloaded: 74.55,
      timeLeft: -1,
      speed: -1,
      status: "pause"
    };
  },
  computed: {
    sizeInfo() {
      return `${this.downloaded}MB/${this.size}MB`;
    },
    currTimeLeft() {
      if (this.timeLeft === -1) {
        return "--";
      }
      return "12:05:06";
    },
    currSpeed() {
      if (this.status === "pause") {
        return "暂停中...";
      }
      if (this.speed === -1) {
        return "";
      }
      return `${this.speed} KB/s`;
    }
  },
  methods: {
    handlePlayOrPlause() {
      alert("handlePlayOrPlause");
    },
    handleDelete() {},
    handleOpenFolder() {}
  }
};
</script>
<style lang="scss" scoped>
.downloading-item {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.65);
  height: 50px;
  font-size: 13px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}
.left,
.right {
  display: flex;
  justify-content: center;
  align-items: center;
}
.file-icon img {
  width: 16px;
  height: 16px;
  margin-right: 5px;
}
.title {
  color: rgba(0, 0, 0, 0.65);
}
.middle {
  flex: 1;
}
.time-left {
  margin: 0 50px;
}
.progress {
  margin: 0 10px;
  width: 300px;
}
.btns {
  display: flex;
  margin-left: 30px;
}
.btns div {
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 10px;
}
.btns div img {
  width: 16px;
  height: 16px;
}
.btns div:hover {
  background-color: rgba(0, 0, 0, 0.3);
  cursor: pointer;
}
.btns div:active {
  background-color: rgba(0, 0, 0, 0.5);
}
</style>
