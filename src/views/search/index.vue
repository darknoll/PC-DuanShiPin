<template>
  <div class="search-page">
    <div class="search-title">
      <el-card>
        <el-button
          icon="el-icon-back"
          @click="handlePrev"
          circle
          style="margin-right: 10px;"
        ></el-button>
        <span
          >"<span style="color:red">{{ keyWord }}</span
          >"的搜索结果</span
        >
      </el-card>
    </div>
    <div class="search">
      <template v-for="(item, index) in searchList">
        <user-search-item
          :user-data="item"
          :key="index"
          class="search-item"
        ></user-search-item>
      </template>
    </div>
  </div>
</template>

<script>
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import { Message } from "element-ui";
import UserSearchItem from "@/components/UserSearchItem";
export default {
  components: {
    UserSearchItem
  },
  data() {
    return {
      keyWord: "",
      searchList: []
    };
  },
  mounted() {
    this.keyWord = this.$route.params.keyWord;
    NProgress.start();
    var spawn = require("child_process").spawn;
    var path = require("path");
    var pythonProcess = spawn("python", [
      // eslint-disable-next-line no-undef
      path.join(__static, "scripts", "ks_search_result.py"),
      this.keyWord
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
  },
  methods: {
    handlePrev() {
      this.$router.go(-1);
    }
  }
};
</script>

<style lang="scss" scoped>
.search-page {
  position: relative;
}
.search-title {
  height: 70px;
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
