<template>
  <div class="home">
    <div class="banner">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-main"
        mode="horizontal"
        router
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="/">主页</el-menu-item>
        <el-menu-item index="/download">下载</el-menu-item>
        <el-menu-item index="/settings">设置</el-menu-item>
      </el-menu>
      <div class="search">
        <el-input
          v-model="searchKey"
          placeholder="搜索"
          @click.native="handleClick"
          @keyup.enter.native="handleSearch"
          size="mini"
        >
          <template slot-scope="{ item }">
            <div class="name">{{ item.value }}</div>
          </template>
          <el-select v-model="select" slot="prepend" placeholder="请选择" class="platform-select">
            <el-option label="抖音" value="1"></el-option>
            <el-option label="快手" value="2"></el-option>
          </el-select>
        </el-input>
      </div>
    </div>
    <keep-alive v-if="$route.meta.keepAlive">
      <router-view class="changing"/>
    </keep-alive>
    <search-dialog ref="searchDlg"></search-dialog>
  </div>
</template>

<script>
import SearchDialog from "@/components/SearchDialog";
export default {
  name: "home",
  components: {
    SearchDialog
  },
  data() {
    return {
      activeIndex: "/",
      searchKey: "",
      select: "2",
      searchSuggets: []
    };
  },
  methods: {
    handleClick() {
      this.$refs.searchDlg.dialogVisible = true;
    }
  }
};
</script>

<style lang="scss" scoped>
/deep/ .el-input-group__append,
/deep/ .el-input-group__prepend,
/deep/ .el-input__inner {
  background-color: transparent;
  font-family: "微软雅黑";
  color: rgba(256, 256, 256, 0.7);
}
.banner {
  font-family: "微软雅黑";
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #545c64;
  height: 60px;
}
.main-menu {
  width: 150px;
}
.el-menu-main {
  flex: auto;
}
.input-btn {
  font-family: "微软雅黑";
}
/deep/ .el-input-group__append {
  padding: 0 12px !important;
}

/deep/.el-select .el-input {
  width: 75px;
}
.search {
  flex: none;
  margin-right: 10px;
}
.search /deep/ .el-select {
  background-color: transparent;
}
</style>
