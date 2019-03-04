<template>
  <div class="basic-setting">
    <div class="basic">
      <div class="left">
        <span>基本:</span>
      </div>
      <div class="right">
        <el-checkbox v-model="checked1" class="check-item"
          >开机时启动PC短视频(推荐)</el-checkbox
        >
        <el-checkbox v-model="checked2" class="check-item"
          >在我的电脑中显示PC短视频</el-checkbox
        >
        <el-checkbox v-model="checked3" class="check-item"
          >启动软件自动升级</el-checkbox
        >
      </div>
    </div>
    <div class="backup">
      <div class="left">
        <span>自动备份:</span>
      </div>
      <div class="right">
        <div style="margin:0 10px">管理自动备份的文件夹</div>
        <el-button size="mini" plain @click="handleManage">管理</el-button>
      </div>
    </div>
    <div class="lock">
      <div class="left">
        <span>客户端锁定:</span>
      </div>
      <div class="right">
        <el-checkbox v-model="checked4" class="check-item">
          锁定软件热键:
          <el-input
            size="mini"
            v-model="shortCut"
            style="width: 130px; margin: 0 5px"
          >
          </el-input>
          (直接按键可修改)
        </el-checkbox>
        <el-checkbox v-model="checked5" class="check-item">
          自动锁定设置：鼠标键盘无动作
          <el-input
            size="mini"
            v-model="lockTime"
            style="width: 50px; margin: 0 5px"
          ></el-input
          >分钟后自动锁定软件
        </el-checkbox>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      check1: false,
      check2: false,
      check3: false,
      check4: false,
      shortCut: "",
      lockTime: 10
    };
  },
  methods: {
    handleManage() {
      alert("test");
    }
  }
};
</script>

<style lang="scss" scoped>
.basic-setting {
  color: rgba(255, 255, 255, 0.65);
}
.check-item {
  display: block;
  margin-bottom: 20px;
  margin-left: 10px;
}
.basic,
.backup,
.lock {
  display: flex;
  justify-content: flex-start;
}
.backup {
  align-items: center;
  margin-bottom: 20px;
}
.backup .right {
  display: flex;
  align-items: center;
}
.left {
  width: 100px;
}
.basic-setting /deep/ .el-checkbox {
  color: rgba(255, 255, 255, 0.65);
}
/deep/ .el-button {
  color: white;
  font-family: "微软雅黑";
  background-color: rgba(0, 0, 0, 0.35) !important;
}
</style>
