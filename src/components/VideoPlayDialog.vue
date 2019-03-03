<template>
  <div
    @keyup.left.native="handlePrev"
    @keyup.enter.native="handleNext"
    tabindex="0"
  >
    <el-dialog
      :lock-scroll="false"
      :visible.sync="dialogVisible"
      :before-close="handleClose"
      fullscreen
      class="video-dialog"
    >
      <el-button circle class="play-btn" @click="handlePrev">
        <img
          src="@/assets/png/previous.png"
          style="width: 48px; height: 48px;"
        />
      </el-button>
      <div class="video-player">
        <video-player
          class="video-player-box"
          ref="videoPlayer"
          :options="playerOptions"
          :playsinline="true"
        >
        </video-player>
      </div>
      <el-button circle class="play-btn" @click="handleNext">
        <img src="@/assets/png/next.png" style="width: 48px; height: 48px;" />
      </el-button>
    </el-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["dataList"])
  },
  data() {
    return {
      dialogVisible: false,
      playUrl: "",
      currID: 0,
      playerOptions: {
        // videojs options
        height: 800,
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
    },
    handlePrev() {
      if (this.currID === -1) return;
      if (this.currID === 0) return;
      this.currID -= 1;
      this.playerOptions.sources[0].src = this.dataList[this.currID].playUrl;
    },
    handleNext() {
      if (this.currID === -1) return;
      if (this.currID === this.dataList.length - 1) return;
      this.currID += 1;
      this.playerOptions.sources[0].src = this.dataList[this.currID].playUrl;
    }
  }
};
</script>

<style lang="scss" scoped>
/deep/ .el-dialog__body {
  display: flex;
  align-items: center;
  justify-content: center;
}
.play-btn {
  margin: 0 10px;
  background: transparent !important;
  border-width: 0 !important;
}
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
