//定制请求的实例

//导入axios  npm install axios
import axios from 'axios';
//定义一个变量,记录公共的前缀  ,  baseURL
// 直接给后端的url会存在浏览器跨域问题，需要在vue.config.js中配置代理
//const baseURL = 'http://localhost:8000';
const baseURL = '/api';
const instance = axios.create({baseURL})


//添加响应拦截器
instance.interceptors.response.use(
    result=>{
        return result.data;
    },
    err=>{
        alert('服务异常');
        return Promise.reject(err);//异步的状态转化成失败的状态
    }
)

export default instance;