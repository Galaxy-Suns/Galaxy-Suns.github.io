# Node.js

*js的运行需要**运行环境**, 比如浏览器就是一种环境， 它提供了js操作DOM, BOM等的内置函数, 因此可以做前端开发*

*而Node.js也是一种运行环境, js可以在其中做后端开发*

## 壹 Node.js 基础使用

*Node是一个基于Chrome V8引擎的JavaScript运行环境*

### 1.1 Node.js的运行环境

**组成部分**

* **V8引擎** 解析和执行js代码
* **内置API** 给予js后端开发的能力

*与浏览器环境不同, Node.js中无法调用DOM, BOM等浏览器内置API*

### 1.2 Node.js运行js文件

**步骤**

1. 在**文件所在目录下**打开终端
2. 输入命令`node 文件名.js`

*`node-v`可查看Node.js的版本号*

**终端相关**

* *`tab`快速补全路径*
* *`esc`快速清空当前输入命令*
* *`cls`清空页面*

### 1.3 fs文件操作模块

*Node.js官方提供用于操作文件的模块*

**Node.js中, 使用模块前需要导入** `const fs = require('fs');`

#### 1.3.1 fs.readFile() 读取指定文件的内容

* `fs.readFile(path[, options], callback)`
* `path` **必选** 字符串, 表示文件存放路径
* `options` *可选* 读取时的编码格式
* `callback` **必选** 通过此回调函数, 拿到读取结果
  * 回调函数第一个参数 `err` 为出错对象, 正常执行则为`null`, 打印`err.message`出错信息字符串 
  * 回调函数第二个参数 `dataStr` 为成功读取后的信息, 失败为`undefined`


*文件读取*
```js
const fs = require('fs');
fs.readFile('./test.txt', 'utf-8', (err, dataStr) => {
    console.log(err);
    console.log(dataStr);
})
```

>null
Hello Node!
Hello fs!


*文件错误处理*
```js
const fs = require('fs');
fs.readFile('./test.xt', 'utf-8', (err, dataStr) => {
    if(err){
        console.log("读取失败" + err.message);
        return;
    }
    console.log(dataStr);
})
```

>读取失败ENOENT: no such file or directory, open 'C:\code\galaxy_web\node_js\test.xt'

#### 1.3.2 fs.writeFile() 向指定文件写入内容

* `fs.writeFile(file, data[, options], callback)`
* `file` **必选** 表示文件存放路径
* `data` **必选** 写入内容
* `options` *可选* 以什么格式写入文件 默认值`utf8`
* `callback` **必选** 文件写入后的回调函数
  * 参数`err`写入错误对象, 没有出错为`null`, 否则可以用`err.message`打印出错信息

*以**覆盖**形式写入, 如果文件**不存在, 则创建文件***


*错误处理*
```js
const fs = require("fs")

fs.writeFile('R:/text.txt', "Hello f", err => {
    if(err) console.log("写入失败" + err.message);
    else console.log("DONE");
})
```

#### 1.3.3 __dirname 处理fs路径问题

*以`./`或者`../`开头的相对路径, 容易出现错误 原因是**代码在执行时, 会以执行node命令时所处的目录, 动态拼接出被操作文件的完整路径***

*一种解决方法是提供绝对路径...但移植性差，不利于维护*

**`__dirname`表示当前文件所在的目录** 这种方法用拼接的方法保证了使用**绝对路径**, 而由于`__dirname`会随本文件存放位置的变化而改变, 保留了**相对路径的优点**

*`__dirname`拼接动态绝对路径*
```js
const fs = require("fs");

fs.readFile(__dirname + "/test.txt", "utf-8" ,(err, dataStr) => {
    dataStr = dataStr.replaceAll(" ", "\n");
    dataStr = dataStr.replaceAll("=", ", ");
    fs.writeFile(__dirname + "/test.txt", dataStr, err => {
        if(!err) console.log("DONE");
    })
})
```

### 1.4 path路径模块

*Node.js官方提供模块, 用于处理路径问题*

#### 1.4.1 path.join() 路径拼接

* `path.join(path_str...)` 
* `path_str...` 存放路径片段 若干
* 返回值 `String` 拼接后的路径

*路径拼接*
```js
const path = require("path");

const pathStr = path.join("/a", "/b", "../", "/c", "./d");
console.log(pathStr);
```

>\a\c\d

*配合`__dirname`*

#### 1.4.2 path.basename() 获取路径中的文件名

*获取路径的最后部分 一般为文件名*

* `path.basename(pathStr[, ext])`
* `pathStr` **必选** 路径
* `ext` *可选* 表示文件扩展名
* 返回值 `String` 表示路径的最后一部分

*获取文件名*
```js
const path = require("path")
const pathStr = path.join("a", "b", "c.html")

console.log(pathStr);

console.log(path.basename(pathStr));

console.log(path.basename(pathStr, '.html'));
```
>a\b\c.html
c.html
c

#### 1.4.3 path.extname() 获取路径中的文件扩展名

* `path.extname(pathStr)`
* `pathStr` **必选** 路径
* 返回值 `String` 扩展名

```js
const path = require("path")
const pathStr = path.join("a", "b", "c.html")
console.log(path.extname(pathStr));
```

>.html

### 1.5 http 模块

*由Node.js官方提供, 用于**创建web服务器的模块***

*域名使得服务器的访问变得方便, 127.0.0.1的域名为localhost*

*一个服务器可以运行成百上千个web服务, **每个web服务对应一个唯一的端口号**, 客户端的请求通过端口号准确交给对应的web服务, 80端口可以省略*

#### 1.5.1 创建基本的web服务器

##### http.creatServer() 创建web服务器实例

* `const server = http.creatServer()`


##### server.on() 为服务器实例绑定 request 事件

* `server.on('request', (req, res) => {});`
* 有客户端向服务器发送请求, 就会触发`request`事件, 调用回调函数
* 回调函数`req`参数 
  * **请求对象** 服务器接收到客户端请求, 会调用`serve.on()`为服务器绑定的事件处理函数, **而与客户端相关的数据或属性, 可在*请求对象*中获得** 
  * `url`属性 客户端请求的 url 地址
  * `method`属性 客户端请求的 method 类型
* 回调函数`res`参数
  * **响应对象** 收到请求后, **访问与服务器相关的数据属性**
  * `res.setHeader()`设置响应头, **可解决中文乱码问题**`res.setHeader("Content-Type", "text/html; charset=utf-8");` 
  * `res.end()`方法, 向客户端发送响应内容, 并结束本次服务

*请求对象和响应对象完成服务*
```js
const http = require("http");

const server = http.createServer();

server.on("request", (req, res) => {
    console.log("someone visit our server");
    console.log("url: " + req.url);
    console.log("method: " + req.method);
    console.log("-----");
    res.end("Hello Client");
    console.log("serve end");
    console.log("------------------------");
});

server.listen(80, () => {
    console.log("server running at http://127.0.0.1");
})
```


>someone visit our server
url: /
method: GET
\-----
>serve end
\------------------------

##### server.listen() 启动web服务器实例

* `server.listen(port, () => {});`
* `port`web服务运行的端口
* 服务器启动成功, 会调用回调函数

*在终端`ctrl+c`可以结束当前运行*

*根据不同url相应不同内容*
```js
const http = require("http");

const server = http.createServer();

const map = {
    "/": "<h1>首页</h1>",
    "/index.html": "<h1>首页</h1>",
    "/about.html": "<h1>关于</h1>"
}

server.on("request", (req, res) => {
    let content = "<h1>404 Not Found!</h1>";
    if(map[req.url]) content = map[req.url];
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.end(content);
});

server.listen(80, () => {
    console.log("server running at http://127.0.0.1");
});
```

## 贰 Node.js 模块化

*把一个大文件拆成独立并相互依赖的多个小模块*

**Node.js 模块的分类**

* 内置模块
* 自定义模块
* 第三方模块

### 2.1 require() 模块的加载

* `const fs = require('fs');` 内置模块加载, 直接使用模块名
* `const custom = require('./custom')` 自定义模块加载, 需要**正确路径** *有无后缀名均可*
* `const moment = reuqire('moment')` 第三方模块加载, 下载后直接使用模块名

### 2.2 module.exports 向外共享模块作用域的成员

在自定义模块中定义的变量, 方法等成员, **只能在当前模块内被访问**, 这种模块级别的限制叫做模块作用域

*共享成员的方式?*

* 在每个js自定义模块中都有一个`module`对象, **存储和当前模块有关的信息**
* 通过`exports`属性来实现**向外共享**
  * 在**自定义模块中**, 修改`module.exports`对象将模块内成员共享, 供外界使用
  * 外界使用`require`导入模块得到的就是`module.exports`对象

*模块向外共享成员*
*demo.js*
```js
const fun = require('./fun');

console.log(fun);
console.log(fun.username);
fun.sayHello();
```

*fun.js*
```js
module.exports.username = "张三";
module.exports.sayHello = ()=>{
    console.log("hello");
}
```
>node demo.js
{ username: '张三', sayHello: [Function (anonymous)] }
张三
hello

*修改module.exports的指向, 向外共享的是新指向的对象*

**exports对象** 为了简化写法, Node提供了一个`exports`变量指向和`module.exports`指向相同的是同一个对象, 因此用`exports`添加修改其中的挂载的属性, 也会改变`module.exports`指向的对象, 而向外共享的结果**始终以`module.exports`指向的对象为准**, 在修改`exports`或`module.exports`的指向时这点比较明显, 此时`exports`失效

### 2.3 npm 包的使用和管理

*Node.js中的第三方模块称为包, 由内置模块封装而来*

#### 2.3.1 npm i 包的下载和使用

https://npmjs.com 搜索需要的包

https://registry.nmpjs.org 从此服务器下载

通过包管理工具 **npm包管理工具进行下载**

> npm install 包的完整名称 #或者
> npm i 包的完整名称

*第三方包`moment`的简单使用*
```js
const moment = require("moment");

const dt = moment().format("YYYY-MM-DD HH:mm:ss");

console.log(dt);
```

>2024-03-16 12:42:13

**下载指定版本的包**

> npm i moment@2.22.2

*包的第一位版本号表示大版本(底层的重新设计), 第二位版本号表示功能版本(添加了新功能), 第三位为bug版本(修复一些bug), 前面的版本号增长, 后面重置为0*

*通过`npm uninstall 包名` 进行卸载* 

#### 2.3.2 package.json 多人协作开发时 项目和包的管理

*包占整个项目的大部分空间, 因此通常剔除包后再上传项目*

*记录依赖包的方式是**在根目录创建`package.json`文件**来记录项目中需要安装哪些包, 方便协作*

**把`node_modules`文件夹添加至`.gitignore`忽略文件**

**根据`package.json`安装所有依赖包** 

> npm i

*包的新增和卸载都会自动改变`package.json`*

**项目开发期间才会用到的包**

*一些包仅在开发时用到, 而项目上线后不会使用*

* 可以记录到`devDependencies`节点 通过安装时`npm -i 包 -D`
* 而开发时和上线后都会用到的包记录到`dependencies`节点
* **通过官网的说明具体判断**安装在哪里 *执行何种命令*

#### 2.3.3 npm 下载换源

##### npm config 换源

*npm默认使用国外的 https://registry.npmjs.org 服务器作为源*

*淘宝提供了镜像服务器, 自动同步国外的服务器数据*

*镜像是一种文件存储形式, 一个磁盘上的数据在另一个磁盘存在一个完全相同的副本即为镜像*

* 查看当前的下包镜像源 `npm config get registry`
* 设置镜像源 `npm config set registry=服务器地址` **淘宝服务器地址** https://registry.npm.taobao.org *这个源有时候会不好用*

##### nrm 管理镜像源

*更加方便切换镜像源*

**下载nrm, 全局可用**
> npm i nrm -g

**查看可用镜像源**
> nrm ls

> npm ---------- https://registry.npmjs.org/
  yarn --------- https://registry.yarnpkg.com/
  tencent ------ https://mirrors.cloud.tencent.com/npm/
  cnpm --------- https://r.cnpmjs.org/
  taobao ------- https://registry.npmmirror.com/
  npmMirror ---- https://skimdb.npmjs.com/registry/

*出现`nrm : 无法加载文件 ...，因为在此系统上禁止运行脚本。`报错可查看这篇博客* https://blog.csdn.net/qq_46008434/article/details/121263445

**切换相应服务器**
> nrm use taobao

#### 2.3.4 npm -g 全局包

*包分为项目包(根据是否有-D参数又分为开发依赖包和核心依赖包)和全局包*

*全局包默认安装到C:\Users\用户目录\AppData\Roaming\npm\node_modules*

**通过-g参数指定为全局**

> npm i 包名 -g
> npm uninstall 包名 -g #卸载全局包

*工具性质的包才有全局安装的必要性, **具体判断通过官网提供的安装命令***

#### 2.3.5 npm 包的结构

* 每个包以**单独目录**存在
* 每个包的顶级目录下必须包含`package.json`这个包管理配置文件
* `package.json` 中必须包含`name` `version` `main`三个属性
* `name`包的名字
* `version`版本号
* `main`入口 *外部通过require导入的文件的module.exports*

#### 2.3.6 npm 包的发布(待补充)

### 2.4 Node.js 中的模块加载机制

* **模块**优先从缓存中加载, 因此多次`require`不会导致模块的代码被执行多次
* **内置模块**优先加载, 在和*包*重名时, 加载的是*内置模块*
* **自定义模块**加载时必须以`./或者../`开头表示路径, 否则会视作*内置模块或第三方模块*
* **自定义模块**加载时, Node.js按照如下顺序尝试加载`确切的文件名 > js > json > .node后缀文件 > 报错`
* **第三方模块**加载时, Node.js先在*当前目录*中的`node_modules`文件夹中加载, 如果没有找到, 则*到当前目录的父目录中找`node_modules`, 直到文件系统的根目录*
* 将**目录**作为文件的标识符, 传给`require()`进行加载时, 现在加载的目录中寻找`package.json`, 寻找`main`属性, 作为入口。如果出现问题, 则试图加载目录下`index.js`文件。否则报错`Error:Cannot find xxx`

## 叁 Express包

*Express 是基于Node.js平台, 快速、开放、极简的Web开发框架*

*与内置的http模块类似, 用来创建Web服务器, 更加方便, 功能更加强大 又http模块封装而来*

**官网地址** https://expressjs.com.cn

### 3.1 express() 创建Web服务器

#### express() 创建服务器实例

> const app = express();

#### express.listen() 启动服务器实例

> express.listen(port, () => {})

* `port` 端口号
* `回调函数` 启动后执行

```js
const express = require('express');

const app = express();

app.listen(80, () => {
    console.log("express server running at http://127.0.0.1");
});
```

>express server running at http://127.0.0.1

### 3.2 express 监听客户端请求并响应

#### app.get() 监听get请求

> const app = express();
> app.get(href, (req, res) => {});

* `href` 用户请求的url后缀地址 `\user`
* 回调函数 监听到请求此url后调用
  * `req` 请求对象, 包含与请求相关属性和方法
  * `res` 响应对象, 包含与响应相关属性和方法

#### app.post() 监听post请求

> const app = express();
> app.post(href, (req, res) => {});

* `href` 用户请求的url后缀地址 `\user`
* 回调函数 监听到请求此url后调用
  * `req` 请求对象, 包含与请求相关属性和方法
  * `res` 响应对象, 包含与响应相关属性和方法

#### res.send() 响应客户端

> const app = express();
 app.post(href, (req, res) => {
 res.send(obj)
 });

* `obj`响应内容 文本, JSON等内容

```js
const express = require("express");

const app = express();

app.get("/user", (req, res) => {
    console.log("someone visit our server");
    res.send({name: "张三", age: 33});
});

app.listen(80, () => {
    console.log("express server running at http://127.0.0.1");
});
```

*终端*
>express server running at http://127.0.0.1
someone visit our server

*客户端*
>{
    "name": "张三",
    "age": 33
}

#### req.query 对象 获取url携带的查询参数

查询参数即为 url后`?name=zs&age=20` 这种键值对形式

**监听到请求后查询参数以属性形式自动解析到`req.query`对象上**

> const app = express();
app.get("/user", (req, res) => {
console.log(req.query);
})

*打印客户端发送的查询参数*
```js
const express = require("express");
const app = express();
app.get("/user", (req, res) => {
    console.log("someone visit our server");
    // 判断空对象的方法
    if(JSON.stringify(req.query) !== "{}") console.log("here are his information");
    for(k in req.query) console.log(k + ": " + req.query[k]);
    console.log("--------------------------------");
});
app.listen(80, () => {
    console.log("express server running at http://127.0.0.1");
})
```

*终端*
>express server running at http://127.0.0.1
someone visit our server
here are his information
name: zs
age: 19
\--------------------------------
someone visit our server
\--------------------------------
someone visit our server
here are his information
say: hello
\--------------------------------

#### req.params对象 获取url的动态参数

动态参数即为`\10010002`, `\10001`这种冒号后的不固定参数

**通过`app.get`的参数`href`中带有`\:id`来匹配携带动态参数的url** `id`表示`req.params`未来的属性名

**而后匹配到的动态参数会存到`req.params`对象**

> const app = express();
app.get("\user\\:id", () => {
console.log(req.params);  
})

*通过`req.params`获取动态参数*
```js
const express = require("express");
const app = express();
app.get("/user/:id", (req, res) => {
    console.log("someone visit our server");
    console.log(req.params);
    console.log("--------------------------------");
});
app.listen(80, () => {
    console.log("express server running at http://127.0.0.1");
});
```

*终端*
>express server running at http://127.0.0.1
someone visit our server
{ id: '1' }
\--------------------------------

#### req.body对象 获取请求体数据

从略, 如果不配置解析表单格式数据的中间件, 默认为`undifined`, 在中间件的分类一章有提及

*监听req的data事件, 可以获取到用户发送的数据*
>let str = ""; // 重复监听data事件, 因为用户的数据可能分批次送达
> req.on("data", data => {str += data}); 

*监听req的end事件, 意味着数据处理完毕*

### 3.3 express.static() 托管静态资源

*`express.static()可以方便地创建一个静态资源服务器, 将一些css, js, 图片对外开放访问`*

#### 托管单个目录

> const app = express();
app.use(express.static('./public'));

* `public` 静态资源文件夹名称

*外界在访问资源时, 存放静态资源的目录不会出现在url*

```js
const express = require("express");
const app = express();
app.use(express.static('./subwaybj'));

app.listen(80, () => {
    console.log("server running at http://127.0.0.1");
})
```

#### 托管多个目录

**多次调用`app.use(express.static())`**

> app.use(express.static(目录1));
app.use(express.static(目录2));

**如果在第一个目录中找到需要的文件, 则不会再进入第二个目录**

#### 挂载路径前缀

*希望在静态资源访问路径前, **挂载目录的前缀, 可以在`app.use()`中添加一个参数***

> app.use("/public", express.static("./public"));

*有一些问题*

### 3.4 nodemon 包 的使用

*自动监听代码的变动, 重启项目*

> nodemon 执行文件路径

当执行文件变动时, 自动重启

> nodemon .\demo.js

>[nodemon] 3.1.0
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `node .\demo.js`
server running at http://127.0.0.1
[nodemon] restarting due to changes...
[nodemon] starting `node .\demo.js`
server running at http://127.0.0.1
[nodemon] restarting due to changes...
[nodemon] starting `node .\demo.js`
server running at http://127.0.0.1

### 3.5 Express 路由

***客户端请求** 与 **服务器处理函数** 之间的 **映射关系***

在Express中由三部分组成

> .METHOD(PATH, HANDLER)

* `METHOD` 请求类型
* `PATH` 请求url地址
* `HANDLER` 处理函数

*客户端的请求到达服务器后, 由路由按照"转发表"匹配**请求类型**和**请求url**, 匹配成功后调用**处理函数***

#### 3.5.1 app.METHOD() 路由挂载到服务器实例

> const app = express();
app.METHOD(PATH, HANDLER)

*把路由挂载到服务器实例*
```js
const app = express();
app.get("/", () => {});
app.post("/", () => {});
```

#### 3.5.2 express.Router() 路由模块化

*为方便对路由进行模块化的管理, 直接挂载路由到`app`上不是很好的方案, 建议抽离为单独模块*

1. 创建模块对应js文件
2. 调用`express.Router()`创建路由实例对象
3. 向路由对象上挂载具体路由
4. 使用`module.exports`向外共享路由对象
5. 使用`app.use()`函数注册路由模块

*路由模块 router.js*
```js
const express = require("express");

const router = express.Router();

router.get("/user", (req, res) => {
    console.log("someone getting");
    res.send("hi");
});
router.post("/user", (req, res) => {
    console.log("someone posting");
    res.send("hello");
});

module.exports = router;
```


*入口 demo.js*
```js
const router = require("./router");
const express = require("express");

const app = express();

app.use(router);

app.listen(80, () => {
    console.log("server running at http://127.0.0.1");
});
```

*`app.use()`的作用是注册全局中间件*

**同样使用`app.use('/user', router)`添加前缀地址**

### 3.6 Express 中间件

*中间件是请求和响应之间的, 具有输入输出的一些步骤*

*请求到达服务器后, 可以连续调用多个中间件, 从而对这次请求进行**预处理***

#### 3.6.1 next 中间件的格式

>(req, res, next) => {.. next()};

*与路由处理函数的差异在于`next`参数*

>app.get("/, (req, res, next) => {.. next()}); // 中间件传入app.get()中

**`next`函数是多个中间件连续调用的关键, 把流转关系转交给下一个中间件或路由**

#### 3.6.2 app.use() 全局生效的中间件

客户端发起的**任何请求, 到达服务器之后, 都会触发的中间件**, 叫做全局生效的中间件, 通过`app.use()`创建

> app.use(中间件函数);

*全局中间件*
```js
const express = require("express");

const app = express();

const mv = (req, res, next) => {
    console.log("我是中间件");
    next();
};

app.use(mv);

app.get("/", (req, res) => {
    res.send("Home");
});

app.get("/user", (req, res) => {
    res.send("User");
});

app.listen(80, () => {
    console.log("running at http://127.0.0.1");
})
```

*服务器收到请求后, 先交给了全局中间件mv, mv通过next函数交给了对应路由, 如果没有对应路由则报错*

##### 中间件的作用

* *多个中间件之间共享同一份`req`, `res`可以在上游的中间件中, 统一为`req`, `res`添加自定义属性, 方法, 供下层使用*
* *不同的url请求, 处理时均相同的部分可以放在全局中间件进行*

##### 定义多个全局中间件

通过多次调用`app.use(中间件)`, 调用是会按定义顺序, 决定中间件的顺序

>app.use((req, res, next) => {..1 next();});
app.use((req, res, next) => {..2 next();});

#### 3.6.3 局部生效的中间件

*在路由中传入, 表示只在当前路由生效*

>app.get('/', mv1, (req, res) => {});

*局部中间件*
```js
const express = require("express");

const app = express();

const mv1 = (req, res, next) => {
    console.log("我是Home的中间件");
    next();
};

app.get("/", mv1 , (req, res) => {
    res.send("Home");
});

app.get("/user", (req, res) => {
    res.send("User");
});

app.listen(80, () => {
    console.log("running at http://127.0.0.1");
})
```

##### 定义多个局部中间件

> app.get('/', mv1, mv2, mv3..., (req, res) => {});
> app.get('/', [mv1, mv2, mv3...], (req, res) => {});

*按照定义顺序连续调用, 最后传给路由*

#### 3.6.4 中间件的注意

* 要在**路由之前**注册中间件
* 主要要`next();`
* **连续调用**(*一条链*)的中间件, 共享`req`, `res`

**调用顺序问题**

>我是入口文件的全局中间件1
我是入口文件的全局中间件2
我是入口文件的全局中间件3
我是路由模块的全局中间件1
我是路由模块的全局中间件2
我是路由模块的全局中间件3
我是隶属于路由a的中间件
我是路由模块的路由a, 我发出错误
我是路由模块的错误中间件

*可见挂载到路由实例的全局中间件, 局部中间件, 错误中间件在入口文件调用`app.use(router)`注册全局中间件后进行*

#### 3.6.5 中间件的类别

##### 绑定到服务器实例 应用级别的中间件

*通过`app.use()`或`app.get()`或`app.post()`, 绑定到app实例的中间件*

>app.use((req, res, next) => (..next()));
>app.get('/', mv1, (req, res) => {});

##### 绑定到路由实例 路由级别中间件

> const router = express.Router();
> router.use((req, res, next) => (..next())); //路由级别的全局中间件
> router.get('/', mv1, (req, res) => {});

*由**路由实例挂载相应方法**(**`.use()`注册全局中间件、`.get` `.post`挂载路由)*

##### err参数 错误级别的中间件

*用来**捕获整个项目中发生的异常错误**, 从而防止项目异常崩溃的问题*

> (err, req, res, next) => {.. next};

*比一般的中间件多了一个`err`参数*

**要定义在所有路由之后, 只可定义一个, 其余不生效, 路由及之前出现错误时调用**

*错误级别中间件捕获异常防止程序崩溃*
```js
const express = require("express");

const app = express();

app.get("/", (req, res) => {
    throw new Error('服务器内部发生错误！');
    res.send("Home");
})

app.use((err, req, res, next) => {
    console.log("Error: " + err.message);
    res.send("Error: " + err.message);
});

app.listen(80, () => {
    console.log("serve running at http://127.0.0.1");
});
```

##### Express 内置中间件

* `express.static` 快速托管静态资源 **无兼容要求**
* `express.json` 解析`json`格式的请求体数据 **4.16.0后可用**
> app.use(express.json());
* `express.urlencoded` 解析`url-encoded`格式请求体数据 **4.16.0后可用**
> app.use(express.urlencoded({extend:false}));



##### 第三方中间件

* 和包的使用一致, 可到官网查询

## 肆 编写接口

### 4.1 了解跨域问题

* 跨域问题指的是在 Web 应用程序中，由于**同源策略**的限制，导致浏览器无法发送跨域请求，也无法获取跨域响应的问题。
* 同源策略是浏览器的一种安全策略，它要求 **Web 应用程序只能访问与当前页面具有相同协议、主机名和端口号的资源**。
* 如果不同源的 Web 应用程序需要通信，就需要进行跨域请求。但由于同源策略的限制，浏览器不允许跨域请求。在此情况下，如果**前端需要访问其他域名(协议, 端口号)下的资源，就会出现跨域问题。**
* 默认情况下**跨域资源在服务器发送响应到客户端后, 会被浏览器拦截**

*推荐使用CORS中间件解决, JSONP只能解决GET请求*

### 4.2 app.use(cors()) 跨域资源共享

#### 4.2.1 cores() 注册全局中间件

***在注册路由中间件之前**为cores注册全局中间件*

> const cors = require('cors');
> app.use(cors());

**服务器配置了CORS后, 客户端无需做任何配置, 即可请求开启了CORS的接口**

**CORS的工作主要是更改响应头, 对响应的信息加以说明**

#### 4.2.2 res.setHeader 响应头部

* `Access-Control-Allow-Origin`字段
  * **指定允许访问本服务器资源的外域url**
  * `res.setHeader('Access-Control-Allow-Origin', 'http://itcast.cn');` 允许此网站
  * `res.setHeader('Access-Control-Allow-Origin', '*');` 所有网站
* `Access-Control-Allow-Headers`
  * 默认情况下, CORS仅支持**客户端向服务器**发送如下的9个请求头
  >Accept , Accept - Language 、 Content - Language 、 DPR 、 Downlink 、 Save - Data 、 Viewport - Width 、 Width 、 Content - Type （值仅限于 text / plain 、 multipart / form - data application / x - www - form - urlencoded 三者之一）
  * 若客户端发送了额外的请求头信息, 需要在服务器端, **通过次字段, 对额外的请求头声明**, 否则请求头会失败
  * `res.setHeader("Access-Control-Allow-Headers", 'Content-Type, X-Custom-Header')`
* `Access-Control-Allow-Methods`
  * 默认情况下, CORS仅支持客户端发起`GET`, `POST`, `HEAD`请求, 如果客户端希望通过`PUT`, `DELETE`等方式请求服务器资源, 需要在服务器端**使用此字段, 指明实际请求所允许使用的HTTP方法**
  * **通配符**支持所有请求方式
  

#### 4.2.3 简单请求和预检请求

**简单请求**

* 请求方式`GET`, `POST`, `HEAD`之一
* 头部信息为以下9个之一
  >Accept , Accept - Language 、 Content - Language 、 DPR 、 Downlink 、 Save - Data 、 Viewport - Width 、 Width 、 Content - Type （值仅限于 text / plain 、 multipart / form - data application / x - www - form - urlencoded 三者之一）

**预检请求**

*至少满足一些条件之一*

* 请求方式为`GET`, `POST`, `HEAD`之外
* 请求头中**含自定义头部字段**
* 向服务器发送了`application/json`格式的数据

*浏览器和服务器正式通信前, 浏览器**先发送OPTION请求进行预检**, 来获知服务器是否允许该实际请求, 所以这次的OPTION成为预检请求。服务器**成功响应预检请求后, 浏览器发送真正的请求**, 并携带真实数据*

## 伍 MySQL

* MySQL, Oracle, SQL Server 关联型
* Mongodb 非关联型 
* 两种数据库相互补充弥补 

*每个项目对应独立数据库*

*项目的不同信息, 存到不同表中, 用户数据存到users, 图书数据存到books..*

* MySQL由**数据库-数据表-数据行-字段**组成

### 5.1 MySQL workbench 创建数据库/表 字段的数据类型

* `int` 整数类型
* `varchar` 字符串类型
* `tinyint` 布尔类型

#### 5.1.1 字段常见设置

* 主键 唯一标识 `pk`
* 值非空 `NN`
* 值唯一:  `UQ`
* 自动增长 `AI`
* 默认值 `Default`

### 5.2 sql语句

* `sql`即使用编程语句对**关系型数据库**进行增删改查
* `-- ...`注释
* **关键字**对大小写不敏感

### 5.2 select 查询数据

* `SELECT 列名称 FROM 表名称`
* `SELECT * FROM 表名称` * 表示所有列
* 查询的结果存储在一个结果表(结果集)中 在MySQL workbench中为下方的`Result Grid`中

```sql
-- 通过 * 查询 users 表中所有数据 注意使用前先选中数据库（MySQL Workbench中双击左侧相应数据库）
-- SELECT * FROM users

-- 从 users 表中查询 username password
SELECT username, password FROM users
```

### 5.3 insert into 向数据表插入新的数据行

* `INSERT INTO table_name (字段1, 字段2,...) VALUES (字段1值, 字段2值,...)`

```sql
-- 向 users 表中插入新数据 username: tony stark password: 098123
INSERT INTO users (username, password) VALUES ('tont stark', '098123')
```

### 5.4 update 修改表中的数据

* `UPDATE 表名称 SET 某字段 = 新值 WHERE 某字段 = 某值`
* 更新多个字段, `,`隔开 `UPDATE 表名称 SET 字段1 = 新值, 字段2 = 新值 WHERE 某字段 = 某值`

```sql
-- 将 id 为 4 的用户密码，更新成 88888888
-- UPDATE users SET password = 88888888 WHERE id = 4
-- SELECT * FROM users

-- 将 id 为 2 的用户，用户密码更新为 admin123，用户的状态更新为 1
UPDATE users SET password = 'admin123', status = 1 WHERE id = 2
-- SELECT * FROM users
```

### 5.5 delete from 删除表中的数据行

* `DELETE FROM 表名称 WHERE 某字段 = 某值`

```sql
-- 删除 users 表中，id 为 4 的用户
DELETE FROM users WHERE id = 4
-- SELECT * FROM users
```

### 5.6 where 子句 限定选择的标准

* 可用于`select`, `update`, `delete`

```sql
SELECT 某字段 FROM 表名称 WHERE 某字段 _运算符_ 某值 
UPDATE 表名 SET 某字段 = 新值 WHERE 某字段 _运算符_ 某值 
DELETE FROM 表名 WHERE 某字段  _运算符_ 某值 
```

* 运算符包括 
* `=`等于
* `<>`不等于（一些版本支持`!=`）
* `>`大于
* `<`小于
* `>=`大于等于
* `<=`小于等于
* `BETWEEN`在某范围内
* `LIKE`搜索某种模式（模糊匹配）

```sql
-- WHERE 子句
-- SELECT * FROM users WHERE status = 1
-- SELECT * FROM users WHERE id > 2
SELECT * FROM users WHERE username != 'ls'
```

### 5.7 and or 运算符 where子句中连接多个条件

```sql
-- 使用 AND 运算符显示所有状态为 0 且 id 小于 3 的用户 
-- SELECT * FROM users WHERE status = 0 AND id < 3

-- 使用 OR 运算符显示所有状态为 1 或 id 等于 3 的用户 
SELECT username, password FROM users WHERE status = 1 OR username = 'zs'
```

### 5.8 order by 子句 根据指定字段对查询结果排序

#### 5.8.1 ASC DESC 升序降序

* 配合`select`
* 默认为升序排序
* 降序使用`DESC`关键字
* `SELECT 语句 ORDER BY 字段名`
* `SELECT 语句 ORDER BY 字段名 DESC`降序排序

```sql
-- 对 users 表中的数据按照 status 字段 升序排序
-- SELECT username, password, status FROM users ORDER BY status

-- 对 users 表中的数据按照 status 字段 降序排序
SELECT username, password, status FROM users ORDER BY status DESC
```

#### 5.8.2 多重排序

* 先按照a字段排序, 当a字段相同时按照b字段排序
* `SELECT语句 ORDER BY a字段 (ASC)/DESC, b字段 (ASC)/DESC`

```sql
-- 对 users 表中的数据按照 status 字段 升序排序
-- SELECT username, password, status FROM users ORDER BY status

-- 对 users 表中的数据按照 status 字段 降序排序
SELECT username, password, status FROM users ORDER BY status DESC
```

### 5.9 count(*)函数 返回查询结果的数据条数

* 配合`select`
* `SELECT COUNT(*) FROM 表名称`
* 结果为一个结果表，具有字段名`COUNT(*)`

```sql
-- 使用 COUNT(*) 统计 users 表中状态为 0 用户的总数量 
SELECT COUNT(*) FROM users WHERE status = 0
```

### 5.10 as 关键字 给查询出的字段名设置别名

* 配合`select`
* 可用于`count(*)`统计数据个数时给结果表的`COUNT(*)`字段起别名
* `SELECT 字段名 AS 别名 FROM 表名`

```sql
-- 使用 AS 关键字给列取别名
-- SELECT COUNT(*) AS cnt FROM users WHERE status = 0 

SELECT username AS name, password AS p FROM users
```

### 5.11 node.js mysql 模块

安装
> npm i mysql

导入
> const mysql = require('mysql')

#### 5.11.1 mysql.createPool 连接数据库

```js
const db = mysql.createPool({
    host: '127.0.0.1',
    user: 'root',
    password: '123456',
    database: 'my_db_01'
})
```

注意! 此模块(2.18.1)不支持新版本MySQL的新的身份验证方式，可能出现错误`Client does not support authentication protocol requested by server; consider upgrading MySQL client`

* 解决方法 `cmd`登录`mysql` 执行`alter user root@'localhost' identified with mysql_native_password by "123456";` 可以解决本地访问

#### 5.11.2 db.query 执行 sql 语句

```js
db.query(sql语句, (err, res) => {
    ...
})
```

```js
db.query('SELECT * FROM users', (err, res) => {
  if(!err) console.log(res);
  else console.log(err);
})
```

得到数组
```js
[
  RowDataPacket {
    id: 1,
    username: 'zs',
    password: '123456',
    status: 0
  },
  RowDataPacket {
    id: 2,
    username: 'ls',
    password: 'admin123',
    status: 1
  },
  RowDataPacket {
    id: 3,
    username: 'xh',
    password: '654321',
    status: 0
  }
]
```

#### 5.11.3 db.query 查询数据

如上

#### 5.11.4 db.query 插入数据