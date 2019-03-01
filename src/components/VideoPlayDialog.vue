<template>
  <div>
    <el-dialog
      :visible.sync="dialogVisible"
      width="500px"
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
          customEventName="customstatechangedeventname"
          @play="onPlayerPlay($event)"
          @pause="onPlayerPause($event)"
          @ended="onPlayerEnded($event)"
          @waiting="onPlayerWaiting($event)"
          @playing="onPlayerPlaying($event)"
          @loadeddata="onPlayerLoadeddata($event)"
          @timeupdate="onPlayerTimeupdate($event)"
          @canplay="onPlayerCanplay($event)"
          @canplaythrough="onPlayerCanplaythrough($event)"
          @statechanged="playerStateChanged($event)"
          @ready="playerReadied"
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
        width: 480,
        autoplay: true,
        loop: true,
        language: "zh-CN",
        fluid: false,
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
  width: 100%;
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
