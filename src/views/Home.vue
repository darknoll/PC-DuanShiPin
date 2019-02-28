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
        <el-autocomplete
          v-model="searchKey"
          :fetch-suggestions="querySearch"
          :trigger-on-focus="false"
          placeholder="请输入关键字搜索"
          clearable
          @keyup.enter.native="handleSearch"
          size="mini"
        >
          <template slot-scope="{ item }">
            <div class="name">{{ item.value }}</div>
          </template>
          <el-select v-model="select" slot="prepend" placeholder="请选择">
            <el-option label="抖音" value="1"></el-option>
            <el-option label="快手" value="2"></el-option>
          </el-select>
          <el-button
            slot="append"
            type="success"
            icon="el-icon-search"
            class="input-btn"
            @click="handleSearch"
          ></el-button>
        </el-autocomplete>
      </div>
    </div>
    <keep-alive v-if="$route.meta.keepAlive">
      <router-view class="changing" />
    </keep-alive>
  </div>
</template>

<script>
import { Message } from "element-ui";
export default {
  name: "home",
  data() {
    return {
      activeIndex: "/",
      searchKey: "",
      select: "2",
      searchSuggets: []
    };
  },
  methods: {
    handleOK() {
      //      var remote = require('electron').remote;
      // // 获取主进程中的 BrowserWindow 对象
      // var BrowserWindow = remote.BrowserWindow;
      // // 创建一个渲染进程
      // var win = new BrowserWindow({ width: 800, height: 600 });
      // win.loadURL('http://nodejh.com');

      this.$router.push("/crawler");
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
      this.$router.push({
        name: "search",
        params: { keyWord: this.searchKey }
      });
    },
    querySearch(queryString, cb) {
      this.searchSuggets = [];
      var spawn = require("child_process").spawn;
      var path = require("path");
      var pythonProcess = spawn("python", [
        path.join(__static, "scripts", "ks_search_suggest.py"),
        queryString
      ]);
      pythonProcess.stdout.on("data", data => {
        var json = JSON.parse(data.toString());
        let result = json["data"]["searchSuggest"]["suggestKeywords"]["list"];
        for (let i = 0; i < result.length; i++) {
          let resultItem = {};
          resultItem["value"] = result[i];
          this.searchSuggets.push(JSON.stringify(resultItem));
        }
        console.log(this.searchSuggets);
        cb(this.searchSuggets);
      });
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
/deep/.el-select .el-input {
  width: 75px;
}
/deep/ .el-input-group__append {
  padding: 0 12px !important;
}
.search {
  flex: none;
  margin-right: 10px;
}
.search /deep/ .el-select {
  background-color: transparent;
}
</style>
