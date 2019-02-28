<template>
  <el-dialog
    :visible.sync="dialogVisible"
    width="90%"
    :before-close="handleClose"
    :modal-append-to-body="false"
    @open="handleOpen"
    class="search-dialog"
  >
    <el-input
      placeholder="请输入搜索内容"
      v-model="searchKey"
      class="input-with-select"
      ref="searchInput"
      clearable
      @keyup.enter.native="handleEnter"
    >
      <el-button
        slot="append"
        icon="el-icon-search"
        @click="handleSearch"
      ></el-button>
    </el-input>
    <div class="search">
      <template v-for="(item, index) in searchList">
        <user-search-item
          :user-data="item"
          :key="index"
          @sendUserInfo="handleUserInfo"
          class="search-item"
        ></user-search-item>
      </template>
    </div>
  </el-dialog>
</template>

<script>
import { Message } from "element-ui";
import Bus from '@/bus.js';
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import UserSearchItem from "@/components/UserSearchItem";
export default {
  components: {
    UserSearchItem
  },
  data() {
    return {
      dialogVisible: false,
      searchKey: "",
      searchList: []
    };
  },
  methods: {
    handleOpen() {
      this.$nextTick(() => {
        this.$refs.searchInput.$el.querySelector("input").focus();
        this.searchKey = "";
        this.searchList = [];
      });
    },
    handleClose(done) {
      done();
    },
    handleEnter() {
      this.handleSearch();
    },
    handleUserInfo(url) {
      this.dialogVisible = false;
      Bus.$emit('sendUserInfo', url);
    //   this.$router.push({
    //     name: "home",
    //     params: { url: url }
    //   });
    },
    handleSearch() {
      if (this.searchKey.trim() === "") {
        Message({
          showClose: true,
          message: "未输入！",
          type: "error"
        });
        return;
      }
      NProgress.start();
      var spawn = require("child_process").spawn;
      var path = require("path");
      var pythonProcess = spawn("python", [
        // eslint-disable-next-line no-undef
        path.join(__static, "scripts", "ks_search_result.py"),
        this.searchKey
      ]);
      pythonProcess.stdout.on("data", data => {
        this.searchList = JSON.parse(data.toString());
        NProgress.done();
      });
      pythonProcess.stderr.on("data", data => {
        Message({
          showClose: true,
          message: data.toString(),
          type: "error"
        });
        NProgress.done();
      });
    }
  }
};
</script>

<style lang="scss" scoped>
/deep/ .el-dialog {
  background-image: url("../assets/search-back.jpg");
}
.search-dialog {
  border-radius: 20px;
}
.search {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 20px;
  overflow: scroll;
  height: calc(100vh - 100px);
}
.search-item {
  width: 360px;
  margin-bottom: 30px;
}
</style>
