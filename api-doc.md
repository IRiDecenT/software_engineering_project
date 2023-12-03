## 软件工程项目API文档

### 1. 登陆

1. 方法：POST
2. api：login/
3. JSON格式http报文，请求正文组成：

| username | password |
| -------- | -------- |
| 用户名   | 邮箱     |

4. 返回JSON格式响应，例如

   ```json
   {
       'code': 200,
       'msg': '登录成功',
       'id': user.id,
   }
   ```

   

### 2. 注册

1. 方法：POST
2. api：register/
3. JSON格式http报文，请求正文组成：

| Username | password |
| -------- | -------- |
| 用户名   | 密码     |

4. 返回json格式的响应

```json
{
	"code": 200
    "msg": “注册成功”
}
```



### 3. 获取用户信息

1. 方法：GET

2. api：getUserInfo/

3. JSON格式报文 正文例如

   ```json
   { "id" = 1 }
   ```

4. 
