# AJAX

https://www.jsdelivr.com  *A free CDN for open source projects*



*AJAX是异步的JavaScript和XML。使用`XMLHttpRequest`对象**与服务器通信***

**axios库**

* 基于`XMLHttpRequest`对象封装

## 壹 axios 基本使用

### 1.1 axios().then() 向服务器请求数据

>引入js文件 \<script src="https://cdn.jsdelivr.net/npm/axios@1.6.8/dist/axios.min.js"></script>

**使用`axios`函数**

>axios({url: '目标资源地址'}).then(result => //对服务器返回数据后续处理)

*简单使用axios获取服务器返回的数据*
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="./axios.min.js"></script>
</head>
<body>
    <script>
        axios({url: "http://hmajax.itheima.net/api/province"}).then(result => {
            console.log(result);
        })
    </script>
</body>
</html>
```

* `result.data`为返回的对象

### 1.2 params 属性 指定查询参数

*浏览器提供给服务器的**额外信息**, 让服务器返回浏览器想要的数据*

> http://xxxx.com/xxx/xxx?参数名1=值&参数名2=值


> axios({
 url: "目标资源地址",
 params: {
 参数名: 值
 }
 }).then(result => {})


*查询参数的使用*
```js
const p = document.querySelector("p");
axios({
    url: "http://hmajax.itheima.net/api/city",
    params: {
        pname: "辽宁省"
    }
}).then(resule => {
    const str = resule.data.list.join("<br>");
    p.innerHTML = str;
})
```

### 1.3 method data属性 设置请求方法

* GET 获取数据
* POST 提交数据
* PUT 修改数据(全部)
* DELETE 删除数据
* PATCH 修改数据(部分)

> http://xxxx.com/xxx/xxx?参数名1=值&参数名2=值
 axios({
 url: "目标资源地址",
 method: "请求方法", // get可以省略
 data: {参数名: 值} // 提交数据
 }).then(result => {})

*POST方法注册账号*
```js
axios({
    url: "http://hmajax.itheima.net/api/register",
    method: "post",
    data: {
        username: "Galaxies",
        password: "xxxxxx"
    }
}).then(result => {
    console.log(result);
})
```

### 1.4 .catch 错误处理

>axios().then().catch(err => {
    // 错误处理
})

*catch错误处理, 弹出提示框*
```js
axios({
    url: "http://hmajax.itheima.net/api/register",
    method: "post",
    data: {
        username: "Galaxies111",
        password: "xxxxxx"
    }
}).then(result => {
    console.log(result);
}).catch(err => {
    alert(err.message);
});
```


### 1.5 HTTP协议

*规定了浏览器发送及服务器返回内容的格式*

#### 请求报文

浏览器按照HTTP协议要求的格式, 发送给服务器的内容

* **请求行** 携带**请求方法**, **URL**, 协议
* **请求头** 以键值对的格式携带的额外信息, 如`Content-Type`(携带的内容类型)
* **请求体** 发送的请求资源

#### 1.5.2 响应报文

服务器按照HTTP协议要求的格式, 发送给浏览器的内容

* **响应行** 协议, **HTTP响应状态码**, 状态信息
  
* **响应头** 以键值对的格式携带的额外信息, 比如`Content-Type`
* **响应体** 返回的资源

*报文均可在网络中查看*

#### 1.5.3 HTTP响应状态码

* **HTTP响应状态码** 表明是否成功
    * 1xx 信息
    * 2xx 成功
    * 3xx 重定向消息
    * 4xx 客户端错误 404服务器找不到资源
    * 5xx 服务端错误 

### 1.6 serialize() form-serialize收集表单

*用于快速批量收集表单元素的值*

* 需要引入

>const data = serialize(form, {hash: true, empty: true});

* `form` 表单对象
* 配置对象
  * `hash`属性 设置获取到的设置结构
    * 值`true` 获取到js对象
    * 值`false` 查询字符串型 `key1=value&key2=value` 
  * `empty`属性 设置是否获取空值 
* 把**表单对象范围内**表单内容收集为**对象**
* **返回的对象属性值由表单元素的`name`属性决定**

### 1.7 FormData 文件上传

>const fd = new FormData();
fd.append(参数名, 值);

*上传图片并显示*

```js
<input type="file" name="" id="">
<img src="" alt="">
<script>
    const input = document.querySelector("input")
    .addEventListener("change", e => {
        const file = e.target.files[0]; // 文件对象
        const fd = new FormData();
        fd.append("img", file); // 属性名+携带文件
        axios({
            url: "http://hmajax.itheima.net/api/uploadimg",
            method: "post",
            data: fd
        }).then(result => {
            const img = document.querySelector("img");
            img.src = result.data.data.url;
        })
    })
</script>
```

*跨域指的是 协议名, 域名, 端口号 三者有一个或多个不同, 而请求后获取不到发送回的数据, 应有后端解决*