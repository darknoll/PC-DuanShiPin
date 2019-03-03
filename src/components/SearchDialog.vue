<template>
  <el-dialog
    :lock-scroll="false"
    :visible.sync="dialogVisible"
    width="400px"
    :before-close="handleClose"
    :modal-append-to-body="false"
    @open="handleOpen"
    :custom-class="searchDialog"
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
        :loading="isBtnLoading"
        @click="handleSearch"
      ></el-button>
    </el-input>
    <div
      class="search"
      v-loading="loading"
      element-loading-background="transparent"
      element-loading-text="加载中"
    >
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
import { Message, MessageBox } from "element-ui";
import Bus from "@/bus.js";
import UserSearchItem from "@/components/UserSearchItem";
export default {
  components: {
    UserSearchItem
  },
  data() {
    return {
      dialogVisible: false,
      searchKey: "",
      searchList: [],
      loading: false,
      isBtnLoading: false
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
      Bus.$emit("sendUserInfo", url);
      //   this.$router.push({
      //     name: "home",
      //     params: { url: url }
      //   });
    },
    handleSearch() {
      this.isBtnLoading = true;
      if (this.searchKey.trim() === "") {
        Message({
          showClose: true,
          message: "未输入！",
          type: "error"
        });
        this.isBtnLoading = false;
        return;
      }
      this.searchList = [];
      this.loading = true;
      var spawn = require("child_process").spawn;
      var path = require("path");
      var pythonProcess = spawn("python", [
        // eslint-disable-next-line no-undef
        path.join(__static, "scripts", "ks_search_result.py"),
        this.searchKey
      ]);
      pythonProcess.stdout.on("data", data => {
        this.searchList = JSON.parse(data.toString());
        if (this.searchList.length === 0) {
          MessageBox({
            showClose: true,
            message: "未找到关键字对应的用户！",
            type: "info"
          });
        }
        this.loading = false;
        this.isBtnLoading = false;
      });
      pythonProcess.stderr.on("data", data => {
        Message({
          showClose: true,
          message: data.toString(),
          type: "error"
        });
        this.loading = false;
        this.isBtnLoading = false;
      });
    }
  }
};
</script>

<style lang="scss" scoped>
/deep/ .el-dialog {
  background-image: url("../assets/search-back.jpg");
}
.searchDialog {
  border-radius: 20px;
}
.search {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 20px;
  overflow-x: hidden;
  overflow-y: scroll;
  height: calc(60vh);
}
.search-item {
  width: 360px;
  margin-bottom: 30px;
}
</style>
