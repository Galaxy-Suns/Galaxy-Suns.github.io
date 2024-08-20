# 小兔鲜项目
 
* [文件和目录准备](#文件和目录准备)
* [代码准备](#代码准备)

---

## 文件和目录准备

1. 创建项目文件夹 xxx-pc-client(根目录)
2. 准备favicon.ico到项目目录
3. 在根目录创建两个图片文件夹<br>images存放网站中固定使用的图片素材（logo,样式修饰图片等） <br>uploads存放网站中非固定使用的图片素材（商品，宣传图片等）
4. 在根目录新建index.html文件
5. 在根目录新建css文件夹，在其中创建<br>base.css基础公共样式<br>common.css 该网站中多个网页相同模块的重复样式，如头部、底部<br>index.css首页样式

## 代码准备

1. 按照base-common-网页的**顺序链接**好样式表(*层叠性*)
2. SEO三大标签以及连接好favicon
3. cv完成base.css

base.css
```css
/* 清除默认样式的代码 */
/* 去除常见标签默认的 margin 和 padding */
body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
ul,
ol,
li,
dl,
dt,
dd,
input {
  margin: 0;
  padding: 0;
}

/* 內减模式 */
* {
    box-sizing: border-box;
}

/* 设置网页统一的字体大小、行高、字体系列相关属性 */
body {
  font: 16px/1.5 "Helvetica Neue", Helvetica, Arial, "Microsoft Yahei",
    "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  color: #333;
}

/* 去除列表默认样式 */
ul,
ol {
  list-style: none;
}

/* 去除默认的倾斜效果 */
em,
i {
  font-style: normal;
}

/* 去除a标签默认下划线，并设置默认文字颜色 */
a {
  text-decoration: none;
  color: #333;
}

/* 设置img的垂直对齐方式为居中对齐，去除img默认下间隙 */
img {
  vertical-align: middle;
}

/* 去除input默认样式 */
input {
  border: none;
  outline: none;
  color: #333;
}

/* 左浮动 */
.fl {
  float: left;
}

/* 右浮动 */
.fr {
  float: right;
}

/* 双伪元素清除法 */
.clearfix::before,
.clearfix::after {
  content: "";
  display: table;
}
.clearfix::after {
  clear: both;
}
```

