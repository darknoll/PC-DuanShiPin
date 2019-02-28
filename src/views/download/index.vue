<template>
  <div class="download">
    <div class="navbar">
      <el-menu
        default-active="2"
        class="el-menu-vertical"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-menu-item index="2">
          <i class="el-icon-download"></i>
          <span slot="title">正在下载{{ downloadingNum }}</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-check"></i>
          <span slot="title">完成下载{{ downloadNum }}</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="main-content">
      <router-view />
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      downloadingNum: 0,
      downloadNum: 0
    };
  }
};
</script>

<style lang="scss" scoped>
.download {
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
