import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    downloadUrl: "", //当前下载导航栏对应的URL
    settingUrl: "", //当前设置导航栏对应的URL
    dataList: [] //当前视频列表
  },
  mutations: {
    SET_DOWNLOAD_URL: (state, url) => {
      state.downloadUrl = url;
    },
    SET_SETTING_URL: (state, url) => {
      state.settingUrl = url;
    },
    SET_DATA_LIST: (state, dataList) => {
      state.dataList = dataList;
    }
  },
  actions: {
    setDownloadUrl({ commit }, url) {
      commit("SET_DOWNLOAD_URL", url);
    },
    setSettingUrl({ commit }, url) {
      commit("SET_SETTING_URL", url);
    },
    setDataList({ commit }, dataList) {
      commit("SET_DATA_LIST", dataList);
    }
  }
});
