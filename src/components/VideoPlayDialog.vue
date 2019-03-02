<template>
  <div>
    <el-dialog
      :lock-scroll="false"
      :visible.sync="dialogVisible"
      :before-close="handleClose"
      fullscreen
      class="video-dialog"
    >
      <div class="video-player">
        <video-player
          class="video-player-box"
          ref="videoPlayer"
          :options="playerOptions"
          :playsinline="true"
        >
        </video-player>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false,
      playUrl: "",
      playerOptions: {
        // videojs options
        height: 900,
        autoplay: true,
        loop: true,
        language: "zh-CN",
        playbackRates: [0.5, 1.0, 1.5, 2.0],
        sources: [
          {
            type: "video/mp4",
            src: ""
          }
        ],
        poster: ""
      }
    };
  },
  methods: {
    handleClose(done) {
      done();
    }
  }
};
</script>

<style lang="scss" scoped>
.video-player {
  display: flex;
  align-items: center;
  justify-content: center;
}
/deep/ .el-dialog {
  background-color: transparent;
}
/deep/ .el-dialog__body {
  padding: 0;
  background-color: transparent !important;
}
</style>
