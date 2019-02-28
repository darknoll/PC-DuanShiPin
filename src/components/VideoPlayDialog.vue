<template>
  <div>
    <el-dialog
      :visible.sync="dialogVisible"
      width="500px"
      :before-close="handleClose"
      class="video-dialog"
    >
      <div class="video-player">
        <video
          width="500"
          height="700"
          controls
          autoplay
          :src="playUrl"
        ></video>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false,
      playUrl: ""
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
/deep/ .el-dialog__body {
  padding: 0;
}
</style>
