## 软件工程项目API文档

### 1. 登陆（登陆认证相关后续系统功能全部实现后再考虑添加，现在处理的比较简单）

1. 方法：POST
2. api：login/
3. JSON格式http请求报文，请求正文组成：

| username | password |
| -------- | -------- |
| 用户名   | 邮箱     |

4. 返回JSON格式响应，例如

   ```json
   {
       'code': 200,
       'msg': '登录成功',
       'id': 1, // 用户id
   }
   ```

   

### 2. 注册

1. 方法：POST
2. api：register/
3. JSON格式http请求报文，请求正文组成：

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

2. api：getUserInfo/{用户id}

3. 返回json格式http报文

   ```json
   {
       "code": 200,
       "msg": "获取成功",
       "username": "yr",
       "avatar": "http://localhost:8000/static/avatars/defaultAvatar.jpg" // 头像的url
   }
   ```



### 4. 创建相册

1. 方法：POST

2. api ：createAlbum/

3. JSON格式http请求报文，请求正文组成：

   ```json
   {
       "name": "第三个测试相册",
       "discription": "这是第三个测试创建相册api的相册",
       "uid": "1" // 用户id
   }
   ```

4. 返回JSON格式http报文

   ```json
   {
       "code": 200,
       "msg": "创建成功"
   }
   ```



### 5. 获取相册信息

1. 方法：GET

2. api：getAlbums/{用户id}/

3. 返回JSON类型的数组，例如

   ```json
   [
       {
           "id": 1, // 相册id
           "name": "Test", // 相册名
           "discription": "这是一个测试创建相册api的相册",
           "create_time": "2023-12-01T03:00:08.050Z",
           "forePage": "http://localhost:8000/static/images/defaultAlbumForePage.png" // 相册封面的url地址
       },
       {
           "id": 2,
           "name": "第二个测试相册",
           "discription": "这是第二个测试创建相册api的相册",
           "create_time": "2023-12-03T14:08:47.549Z",
           "forePage": "http://localhost:8000/static/images/defaultAlbumForePage.png"
       },
       {
           "id": 3,
           "name": "第三个测试相册",
           "discription": "这是第三个测试创建相册api的相册",
           "create_time": "2023-12-03T14:28:07.413Z",
           "forePage": "http://localhost:8000/static/images/defaultAlbumForePage.png"
       },
       {
           "id": 5,
           "name": "第四个测试相册",
           "discription": "这是第四个测试创建相册api的相册",
           "create_time": "2023-12-04T11:41:33.709Z",
           "forePage": "http://localhost:8000/static/images/defaultAlbumForePage.png"
       }
   ]
   ```

   

### 6. 更新用户头像

1. 方法：POST

2. api：updateAvatar/

3. 请求正文为表单类型

   ```json
   两个字段
   {
   	"uid": 用户id
   	"avatar": 头像图片文件
   }
   ```

4. 响应正文为JSON类型

   ```json
   {
       "code": 200,
       "msg": "更新成功",
       "filename": "avator1.JPG", // 上传的头像文件名
       "avatar": "http://localhost:8000/static/avatars/1-avator1.JPG" // 头像的url
   }
   ```



### 7. 上传图片（重复上传可能有bug？）

1. 方法：POST

2. api：uploadPhotos/

3. 请求正文为表单类型

   ```json
   三个字段
   {
   	"uid": 1 // 用户id
   	"aid":1 // 相册id
   	"photos": 多个图片文件
   }
   ```

4. 返回JSON格式报文

   ```json
   {
       "code": 200,
       "msg": "上传成功"
   }
   ```



### 8. 获取相册中的照片

1. 方法：GET

2. api：getPhotos/{相册id}/

3. 响应正文为json数组 如下示例

   ```json
   [
       {
           "id": 1,
           "name": "res1.JPG",
           "discription": "这个人很懒，什么都没有留下",
           "upload_time": "2023-12-04T12:23:43.605Z",
           "url": "http://localhost:8000/static/images/1-1-res1.JPG"
       },
       {
           "id": 2,
           "name": "res2.JPG",
           "discription": "这个人很懒，什么都没有留下",
           "upload_time": "2023-12-04T12:23:43.617Z",
           "url": "http://localhost:8000/static/images/1-1-res2.JPG"
       },
       {
           "id": 3,
           "name": "res3.JPG",
           "discription": "这个人很懒，什么都没有留下",
           "upload_time": "2023-12-04T12:23:43.624Z",
           "url": "http://localhost:8000/static/images/1-1-res3.JPG"
       }
   ]
   
   ```

   





























































