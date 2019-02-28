<template>
  <div @mouseenter="mouseEnter" @mouseleave="mouseLeave" @click="handleEnter">
    <el-card class="user-search-card" :class="searchClass">
      <div class="user-top">
        <div class="user-icon">
          <img :src="userData.image" />
        </div>
        <div class="user-info">
          <div class="user-name">{{ userData.name }}</div>
          <div class="user-counts">{{ userData.counts }}</div>
        </div>
      </div>
      <div class="user-desc">
        <el-tooltip :content="userData.desc" placement="top">
          <span>{{ cutString }}</span>
        </el-tooltip>
      </div>
    </el-card>
  </div>
</template>
<script>
import { InterceptString } from "@/utils/util";
export default {
  data() {
    return {
      isActive: false
    };
  },
  props: {
    userData: {
      type: Object,
      default: function() {
        return {
          name: "",
          url: "",
          image: "",
          counts: "",
          desc: ""
        };
      }
    }
  },
  computed: {
    cutString() {
      return InterceptString(this.userData.desc, 27);
    },
    searchClass() {
      return {
        "search-active": this.isActive
      };
    }
  },
  methods: {
    mouseEnter(event) {
      this.isActive = true;
    },
    mouseLeave(event) {
      this.isActive = false;
    },
    handleEnter() {
      this.$router.push({
        name: "crawler",
        params: { url: this.userData.url }
      });
    }
  }
};
</script>
<style lang="scss" scoped>
/deep/ .el-card {
  border-radius: 0;
}
.user-search-card {
  width: 100%;
  height: 100%;
}
.user-top {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 20px;
}
.user-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
  width: 50px;
  height: 50px;
}
.user-top img {
  width: 50px;
  height: 50px;
  border-radius: 50px;
}
.user-name {
  margin-bottom: 10px;
}
.user-counts {
  font-size: 14px;
}
.user-desc span {
  color: rgba(0, 0, 0, 0.65);
}
.search-active {
  background-color: rgba(0, 0, 0, 0.45);
  cursor: pointer;
}
</style>
