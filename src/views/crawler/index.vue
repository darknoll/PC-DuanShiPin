<template>
  <div class="crawler">
    <div class="content">
      <template v-for="(item, index) in dataList">
        <list-item
          :data-item="item"
          :key="index"
          class="data-item"
          @handlePlay="handlePlay"
        />
      </template>
    </div>
    <div class="play-video">
      <video-play-dialog
        ref="videoPlayDlg"
        key="videoPlayer"
      ></video-play-dialog>
    </div>
  </div>
</template>

<script>
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import { Message, MessageBox } from "element-ui";
import ListItem from "@/components/ListItem";
import VideoPlayDialog from "@/components/VideoPlayDialog";
NProgress.configure({ showSpinner: false });

export default {
  name: "Crawler",
  components: {
    ListItem,
    VideoPlayDialog
  },
  data() {
    return {
      userID: "",
      showMask: false,
      select: "2",
      dataList: [],
      searchList: [],
      playUrl: "",
      url: ""
    };
  },
  mounted() {
    this.url = this.$route.params.url;
    if (this.url === undefined) {
      NProgress.start();
      var spawn = require("child_process").spawn;
      var path = require("path");
      var pythonProcess = spawn("python", [
        path.join(__static, "scripts", "ks_hot_info.py")
      ]);
      pythonProcess.stdout.on("data", data => {
        var json = JSON.parse(data.toString());
        this.dataList = json["data"]["videoFeeds"]["list"];
        console.log(this.dataList);
        NProgress.done();
      });
      return;
    }
    let parts = this.url.split("/");
    if (parts.length === 0) {
      MessageBox({
        showClose: true,
        message: "获取用户ID出错！",
        type: "error"
      });
      return;
    }
    this.userID = parts[parts.length - 1];
    NProgress.start();
    var spawn = require("child_process").spawn;
    var path = require("path");
    var pythonProcess = spawn("python", [
      path.join(__static, "scripts", "ks_videos_info.py"),
      this.userID
    ]);
    pythonProcess.stdout.on("data", data => {
      var json = JSON.parse(data.toString());
      this.dataList = json["data"]["getProfileFeeds"]["list"];
      console.log(this.dataList);
      Message({
        showClose: true,
        message: "获取成功",
        type: "success",
        duration: 1000
      });
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
    handlePlay(playUrl) {
      this.playUrl = playUrl;
      this.$refs.videoPlayDlg.dialogVisible = true;
      this.$refs.videoPlayDlg.playUrl = playUrl;
    }
  }
};
</script>

<style lang="scss" scoped>
.crawler {
  margin-top: 20px;
}
.box-card {
  position: relative;
}
.masker {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
}
.content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  overflow: scroll;
  height: calc(100vh - 120px);
  padding: 0;
}
.data-item {
  width: 250px;
  height: 210px;
  margin-bottom: 30px;
}
</style>
