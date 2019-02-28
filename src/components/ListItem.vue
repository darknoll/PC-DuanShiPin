<template>
  <div class="list-item">
    <el-card :body-style="{ padding: '0px' }">
      <div
        class="img-container"
        @mouseenter="mouseEnter"
        @mouseleave="mouseLeave"
        @click="handlePlay"
      >
        <img :src="dataItem.poster" class="image" />
        <div class="masker" v-if="showPlayer">
          <img src="@/assets/player.svg" />
        </div>
        <div class="mark-down" v-if="isDownload">
          <el-button
            :type="downloadType"
            :icon="downloadIcon"
            circle
          ></el-button>
        </div>
      </div>

      <div style="padding: 14px;">
        <el-tooltip :content="dataItem.caption" placement="top">
          <span>{{ cutString }}</span>
        </el-tooltip>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
          <el-button
            type="text"
            class="button"
            icon="el-icon-download"
            circle
            @click="handleDownload"
          ></el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import { InterceptString, TimeTrans } from "@/utils/util";
export default {
  name: "ListItem",
  props: {
    dataItem: {
      type: Object,
      default: function() {
        return {
          caption: "",
          thumbnailUrl: "",
          timestamp: 0,
          playUrl: "",
          poster: ""
        };
      }
    }
  },
  data() {
    return {
      showPlayer: false,
      isDownload: false,
      downloadType: "",
      downloadIcon: ""
    };
  },
  computed: {
    cutString() {
      return InterceptString(this.dataItem.caption, 10);
    },
    currentDate() {
      return TimeTrans(this.dataItem.timestamp);
    }
  },
  methods: {
    mouseEnter(event) {
      this.showPlayer = true;
      this.$el.addEventListener("mousemove", this.mouseMove, false);
    },
    mouseLeave(event) {
      this.showPlayer = false;
    },
    handlePlay() {
      this.$emit("handlePlay", this.dataItem.playUrl);
    },
    handleDownload() {
      this.downloadIcon = "el-icon-loading";
      this.downloadType = "info";
      this.isDownload = true;
      setTimeout(() => {
        this.downloadIcon = "el-icon-check";
        this.downloadType = "success";
      }, 3000);
    }
  }
};
</script>

<style lang="scss" scoped>
/deep/ .el-card {
  border-radius: 5px;
}
.list-item {
  width: 100%;
  height: 100%;
}
.list-item img {
  width: auto;
  height: 150px;
  max-width: 100%;
  max-height: 100%;
}
.time {
  font-size: 13px;
  color: #999;
}
.img-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.65);
}
.img-container:hover {
  background-color: rgba(0, 0, 0, 0.8);
  cursor: pointer;
}
.masker {
  position: absolute;
}
.mark-down {
  position: absolute;
  right: 5px;
  top: 5px;
}
.image {
  width: 50%;
  height: auto;
}
.masker img {
  width: 64px;
  height: 64px;
}
.bottom {
  margin-top: 13px;
  line-height: 12px;
}
.button {
  padding: 0;
  float: right;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>
