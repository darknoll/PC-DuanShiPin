<template>
  <div class="transfer">
    <div class="download-pos">
      <div class="left">
        <span>下载文件位置:</span>
      </div>
      <div class="right">
        <div class="preview">
          <el-input size="mini" class="preview-input"></el-input>
          <el-button size="mini">浏览</el-button>
        </div>
        <div>
          <el-checkbox v-model="checked">默认此路径为下载路径</el-checkbox>
        </div>
      </div>
    </div>
    <div class="download-speed">
      <div class="left">
        <span>传输速度:</span>
      </div>
      <div class="right">
        <div class="speed">
          <el-radio v-model="radio" label="1">不限速</el-radio>
          <el-radio v-model="radio" label="2">
            限速为<el-input
              size="mini"
              style="width:80px; margin: 0 5px;"
            ></el-input
            >KB/s
          </el-radio>
          <el-button size="mini">高级设置</el-button>
        </div>
      </div>
    </div>
    <div class="proxy">
      <div class="left">
        <span>代理设置:</span>
      </div>
      <div class="right">
        <div class="type">
          <span class="span-text">类型</span>
          <el-select
            v-model="value"
            placeholder="请选择代理类型"
            size="mini"
            style="width: 100%"
          >
            <el-option
              v-for="item in options"
              :key="item"
              :label="item"
              :value="item"
              class="type-select"
            >
            </el-option>
          </el-select>
        </div>
        <div class="address">
          <span class="span-text">地址</span>
          <el-input size="mini"></el-input>
        </div>
        <div class="port">
          <span class="span-text">端口</span>
          <el-input size="mini"></el-input>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checked: false,
      radio: "1",
      options: ["不使用代理", "使用HTTP代理", "使用SOCK代理", "使用IE代理"],
      value: ""
    };
  }
};
</script>

<style lang="scss" scoped>
.transfer {
  color: rgba(255, 255, 255, 0.65);
}
.download-pos,
.download-speed,
.proxy {
  display: flex;
  margin-bottom: 20px;
}
.left {
  width: 120px;
  display: flex;
  justify-content: flex-start;
}
.right {
  width: 300px;
  flex: 1;
}
.preview {
  display: flex;
  width: calc(100vw - 300px);
  margin-bottom: 10px;
}
.preview-input {
  margin-right: 10px;
  flex: 1;
}
.download-speed {
  align-items: center;
}
.type,
.address,
.port {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.speed {
  display: flex;
  align-items: center;
  width: 300px;
}
.span-text {
  width: 50px;
}
</style>
