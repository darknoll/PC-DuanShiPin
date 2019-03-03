<template>
  <div class="download">
    <div class="navbar">
      <el-menu
        :router="true"
        default-active="/download/downloading"
        class="el-menu-vertical"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-menu-item
          index="/download/downloading"
          @click="handleMenuChange('/download/downloading')"
        >
          <i class="el-icon-download"></i>
          <span slot="title">{{ downloadingText }}</span>
        </el-menu-item>
        <el-menu-item
          index="/download/downloaded"
          @click="handleMenuChange('/download/downloaded')"
        >
          <i class="el-icon-check"></i>
          <span slot="title">{{ downloadText }}</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="main-content">
      <keep-alive v-if="$route.meta.keepAlive">
        <router-view />
      </keep-alive>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      downloadingNum: 1,
      downloadNum: 0
    };
  },
  activated() {
    const url = this.$store.state.downloadUrl;
    if (url === "") {
      this.$router.push("/download/downloading");
    } else {
      this.$router.push(url);
    }
  },
  computed: {
    downloadingText() {
      let text = "正在下载";
      if (this.downloadingNum != 0) {
        text += `(${this.downloadingNum})`;
      }
      return text;
    },
    downloadText() {
      let text = "完成下载";
      if (this.downloadNum != 0) {
        text += `(${this.downloadNum})`;
      }
      return text;
    }
  },
  methods: {
    handleMenuChange(url) {
      this.$store.dispatch("setDownloadUrl", url);
    }
  }
};
</script>

<style lang="scss" scoped>
.download {
  overflow: hidden;
  height: calc(100vh - 50px);
  display: flex;
}
.navbar {
  flex: none;
  width: 160px;
  height: calc(100vh - 60px);
}
.el-menu-vertical {
  height: 100%;
}
.main-content {
  flex: 1;
}
</style>
