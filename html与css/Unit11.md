# *玖*_字体图标
 
* [9_1_字体图片简介](#9_1_字体图片简介)
* [9_2_字体图标的下载](#9_2_字体图标的下载)
* [9_3_字体图标的使用](#9_3_字体图标的使用)
* [9_4_字体图标上传](#9_4_字体图标上传)

---

*简单的小图案*

## 9_1_字体图片简介

*展示的是图，但本质是文字*

**作用**

* 处理简单的，颜色单一的图片

**优点**

*相比于**css精灵***

* 灵活性高 通过更改文字属性即可改变外观
* 体积小，轻量，渲染速度快
* 兼容性好
* 使用方便<br>1. 下载字体包<br>2. 使用字体包

## 9_2_字体图标的下载

**地点**

* <a href="http://www.iconfont.cn" title="阿里巴巴矢量字体图标库">www.iconfont.cn</a>

**方法**

1. 素材库的官方图表库(<strong style="color:red;">免费!</strong>)
2. 选购，<span style="color:orange;">添加至购物车</span>
3. 选购完成，点击购物车，<span style="color:orange;">添加至项目</span>
4. <span style="color:orange;">统一</span>下载到本地
5. 解压

## 9_3_字体图标的使用

**方法**

1.引入字体图标的样式表<span style="color:orange;">iconfont.css</span>
2.调用图标对应的类名，<span style="color:orange;">必须调用两个类名:iconfont icon-xxx</span>

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>字体图标基本使用-类名</title> 
    <!-- 1、引入样式表  2、调用类名-->
    <link rel="stylesheet" href="./try.css">  
    <link rel="stylesheet" href="./iconfont/iconfont.css">
</head>
<body>
    <!-- iconfont是固定 -->
    <span class="iconfont icon-dingwei"></span>
</body>
</html>
```

## 9_4_字体图标上传

*在iconfont上传.svg矢量图转换为字体图标*

**步骤**

1. 准备好.svg
2. 打开iconfont的上传界面
3. 添加（可多选），**去除颜色并提交**
4. 审核通过后我的图标库->批量操作->添加购物车->同下载图标后续操作

