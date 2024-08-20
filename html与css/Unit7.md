# 学成在线项目-项目开发流程
 
* [准备工作](#准备工作)
* [版心_清除默认样式](#版心_清除默认样式)
* [logo和nav](#logo和nav)
* [搜索](#搜索)
* [用户区](#用户区)
* [轮播图](#轮播图)

---

## 准备工作

1. 创建根目录(英文名)，将来会上传服务器
2. 后续的所有素材也不可以出现中文名
3. 根目录下包含`images`、`css`文件夹(内含`index.css`)，html文件(名为`index.html`)

## 版心_清除默认样式

版心一般类名为`wrap`

清除默认样式常用代码
```css
/* 清除样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
li {
    list-style: none;
}
a {
    text-decoration: none;
}
.clearfix:before,.clearfix:after {
    content:"";
    display:table; 
}
.clearfix:after {
    clear:both;
}
```

## logo和nav

* logo布局 `h1>a>img`
* nav布局 `div.nav>ul>li>a`

*纯文字区域可以不给宽*

## 搜索

* 搜索布局 `div.search>form>input+button`

*使用表单，搜索图标用提交按钮(`button`双标签) 使用背景图*

**更改属性的CSS**

* `选择器::属性{CSS}`
* 如`input::placehorder{}`以更改placehorder文字的样式

## 用户区

* 布局 `div.user>img+span`

*包裹文字的span用来调节CSS，联动后台和数据*

*同样用户名不要给宽*

*调节图片垂直对齐方式采用`vertical-align:middle`*

## 轮播图

**布局**

* `.banner>.wrapper>.left+.right`

*右侧列表标题可以采用`h2`  列表采用`.right>h2+.(content>dl*3>dt+dd)+a.more`*


