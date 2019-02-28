<template>
  <div id="app">
    <div class="topper">
      <div class="title">
        <span>PC短视频</span>
      </div>
      <div class="middle" style="-webkit-app-region: drag"></div>
      <div class="menu-container">
        <ul class="menu">
          <li @click="handleMin">
            <img src="@/assets/png/min.png" />
          </li>
          <li @click="handleMax">
            <img src="@/assets/png/max.png" />
          </li>
          <li @click="handleClose">
            <img src="@/assets/png/close.png" />
          </li>
        </ul>
      </div>
    </div>
    <router-view class="component" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      maxNormalImage: "@/assets/png/max.png",
      isNormal: true
    };
  },
  methods: {
    handleMin() {
      var election = require("electron");
      election.remote.getCurrentWindow().minimize();
    },
    handleMax() {
      var electron = require("electron");
      if (this.isNormal) {
        electron.remote.getCurrentWindow().maximize();
        this.maxNormalImage = "@/assets/png/normal.png";
        this.isNormal = false;
      } else {
        electron.remote.getCurrentWindow().unmaximize();
        this.maxNormalImage = "@/assets/png/max.png";
        this.isNormal = true;
      }
    },
    handleClose() {
      var electron = require("electron");
      electron.remote.getCurrentWindow().close();
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, "微软雅黑", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding: 0;
  margin: 0;
}
body {
  padding: 0;
  margin: 0;
  font-family: "微软雅黑";
  overflow: hidden;
}
.topper {
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: 32px;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title {
  margin-left: 10px;
  color: rgba(255, 255, 255, 0.5);
}
.middle {
  flex: 1;
  height: 100%;
}
.menu-container {
  height: 32px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.menu {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.menu li {
  list-style: none;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.menu li:hover {
  background-color: rgba(0, 0, 0, 0.65);
}
.menu li:active {
  background-color: orange;
}
.menu img {
  width: 16px;
  height: 16px;
}
//滚动条的宽度
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}
//滚动条的滑块
::-webkit-scrollbar-thumb {
  background-color: rgba(144, 147, 153, 0.3);
  border-radius: 5px;
}
</style>
