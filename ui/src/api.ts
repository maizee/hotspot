import { Request } from "./utils/request";
//用户注册
export function register(parameter: any) {
  return Request.axiosInstance({
    url: "API/register",
    method: "post",
    data: parameter,
  });
}
//用户登录
export function login(parameter: any) {
  return Request.axiosInstance({
    url: "API/login",
    method: "post",
    data: parameter,
    headers: { 'Content-Type': 'multipart/form-data' }
  });
}

//获取热门排行
export function getRank(site: string) {
  return Request.axiosInstance({
    url: "API/hot/" + site,
    method: "get",
  });
}
//获取用户信息
export function getUserInfo() {
  return Request.axiosInstance({
    url: "API/userinfo",
    method: "get",
  });
}

//添加用户浏览历史
export function updateHistory(data: {}) {
  return Request.axiosInstance({
    url: "/API/history/update",
    method: "post",
    data: data
  });
}

//获取用户浏览历史
export function getHistory() {
  return Request.axiosInstance({
    url: "/API/history/list",
    method: "get",
  });
}


//添加用户收藏
export function updateFavor(data: {}) {
  return Request.axiosInstance({
    url: "/API/favor/update",
    method: "post",
    data: data
  });
}

//获取用户收藏
export function getFavor() {
  return Request.axiosInstance({
    url: "/API/favor/list",
    method: "get",
  });
}
