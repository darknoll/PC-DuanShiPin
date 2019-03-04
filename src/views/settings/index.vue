<template>
  <div class="settings">
    <el-menu
      class="settings-menu"
      :router="true"
      default-active="/settings/basic"
    >
      <el-menu-item
        index="/settings/basic"
        @click="handleMenuChange('/settings/basic')"
      >
        <i class="el-icon-info"></i>
        <span>基本</span>
      </el-menu-item>
      <el-menu-item
        index="/settings/transfer"
        @click="handleMenuChange('/settings/transfer')"
      >
        <i class="el-icon-sort"></i>
        <span>传输</span>
      </el-menu-item>
    </el-menu>
    <div class="main-content">
      <keep-alive v-if="$route.meta.keepAlive">
        <router-view />
      </keep-alive>
    </div>
    <div class="fun-btns">
      <el-button size="mini" class="fun-btn">确定</el-button>
      <el-button size="mini" class="fun-btn">取消</el-button>
      <el-button size="mini" class="fun-btn">应用</el-button>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  activated() {
    if (this.settingUrl === "") {
      this.$router.push("/settings/basic");
    } else {
      this.$router.push(this.settingUrl);
    }
  },
  computed: {
    ...mapState(["settingUrl"])
  },
  methods: {
    handleMenuChange(url) {
      this.$store.dispatch("setSettingUrl", url);
    }
  }
};
</script>
<style lang="scss" scoped>
@import "@/styles/vars.scss";
.settings {
  position: relative;
  display: flex;
  height: calc(100vh - 80px);
}
.settings-menu {
  width: $settingNavbarWidth;
  height: 100%;
}
.main-content {
  padding: 20px 40px;
}
.fun-btns {
  width: calc(100vw - 150px);
  position: absolute;
  bottom: 440px;
  right: 0;
  padding: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
/deep/ .el-button {
  color: white;
  font-family: "微软雅黑";
  background-color: rgba(0, 0, 0, 0.35) !important;
}
</style>
