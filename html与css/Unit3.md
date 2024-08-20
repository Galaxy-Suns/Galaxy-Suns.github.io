# *叁*_CSS基础
 
* [3_1_体验CSS](#3_1_体验CSS)
* [3_2_CSS其它引入方式](#3_2_CSS其它引入方式)
* [3_3_CSS选择器](#3_3_CSS选择器)
  * [标签选择器](#标签选择器)
  * [类选择器](#类选择器)
  * [id选择器](#id选择器)
  * [通配符选择器](#通配符选择器)
* [3_4_文字基本样式](#3_4_文字基本样式)
  * [字体大小](#字体大小)
  * [字体粗细](#字体粗细)
  * [字体倾斜](#字体倾斜)
* [3_5_字体](#3_5_字体)
* [3_6_CSS的层叠性](#3_6_CSS的层叠性)
* [3_7_font复合属性](#3_7_font复合属性)
* [3_8_文本缩进](#3_8_文本缩进)
* [2_9_文本水平对齐方式](#2_9_文本水平对齐方式)
* [2_10_文本修饰线](#2_10_文本修饰线)
* [2_11_行高](#2_11_行高)
* [2_12_颜色常见取值](#2_12_颜色常见取值)
* [2_13_标签水平居中方法总结](#2_13_标签水平居中方法总结)

https://caniuse.com 查看适配性

---

## 3_1_体验CSS

**CSS** 

* 层叠样式表
* 美化网页

**CSS写在哪**

* style双标签内
* style标签在head标签内(title下)

**写法**

* 选择器+{属性 : 属性值;...}
* 选择器: 标签名

**注释**

* `/**/`
* vscode中的快捷键同样为`ctrl`+`/`

```html
<head>
    <meta charset="UTF-8">
    <!-- 3s自动刷新 -->
    <meta http-equiv="refresh" content="1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>体验CSS</title>
    <style>
        /* CSS的注释 */
        /* 这里写的都是CSS */
        /* 选择器 {CSS属性} */
        /* 选择器：查找标签 */
        p{
            /* 文字颜色变成红色 */
            color: red;
            /* 字变大 px:像素*/
            font-size: 30px;
            /* 背景颜色 */
            background-color: green;
            /* width height */
            width: 400px;
            height: 400px;
        }
    </style>
</head>
<body>
    <p>这是一个p标签</p>
</body>
```

## 3_2_CSS其它引入方式

* 内嵌式 在head标签内的style标签内
* 外联式 写在独立的.css文件中(常用)，通过link标签在html文件中引入 <br> link单标签在head标签内(title下)
* 行内式 写在标签的style属性中，属性值为前两种写法{}内的内容，后续配合js使用

.html
```html
<head>
    <meta charset="UTF-8">
    <!-- 3s自动刷新 -->
    <meta http-equiv="refresh" content="1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS的引入方式</title> 
    <!-- 关系: 样式表 -->
    <link rel="stylesheet" href="./try.css">   
</head>
<body>
    <!-- css到底能写在哪里 -->
    <p>这是一个p标签</p>
    <div style="color: blue; font-size: 30px;">这是div标签</div>
    <div>这个div是什么颜色</div>
</body>
```

.css
```css
/* 选择器{} */
p{
    color: red;
}
```

## 3_3_CSS选择器

*如何找到要规定样式的标签*

### 标签选择器

* 标签名{CSS属性名:属性值;}
* **所有的**这个标签都生效

.html
```html
<body>
    <p>ppppp</p>
    <p>这个p是什么颜色呢</p>
    <p>22222</p>
</body>
```

.css
```css
/* 选择器{} */
/* 标签选择器 就是 以标签名命名的选择器 */
p{
    color: red;
}
```

### 类选择器

* 定义(CSS中)  `.类名{CSS属性名:属性值;}`
* 使用(html中) `标签身上设置class属性 属性值为类名(无.)`

**注意**

* 类名可以由数字字母下划线中划线组成，但**只能以字母和下划线**开头
* 一个标签可同时拥有多个类名，**类名之间以空格隔开（仍在前面的class属性值内）**

.html
```html
<body>
    <!-- 类选择器 需要定义和使用-->
    <!-- 一个标签可以使用多个类名，空格隔开即可 -->
    <p class="red size">111</p>
    <p>222</p>
    <div class="red">这个标签文字也要变红</div>
</body>
```

.css
```css
/* 选择器{} */
/* 标签选择器 就是 以标签名命名的选择器 */
.red{
    color: red;
}

.size{
    font-size: 66px;
}
```

### id选择器

*id和类相似，但id的作用一般不是CSS，而在后续JS中使用*

* 定义在CSS `#id属性值{CSS属性名:属性值;}`
* 使用在HTML `设置标签的id属性值`

**注意**

* id属性类似身份证号码，在一个页面是**唯一不可重复的**
* **一个标签上只能有一个id属性值**

.html
```html
<body>
    <div id="blue">这个div是蓝色的</div>
    <!-- <p id="blue">111</p> -->
</body>
```

.css
```css
/* 定义id选择器 */
#blue{ #blue{
    color: skyblue;
}
```

### 通配符选择器

* `*{CSS属性名:属性值;}`
* 作用为找到页面中的所有标签，设置样式
* 特殊情况下才会使用 如: 清空所有标签的内外边距

.html
```html
<body>
    <div>div</div>
    <p>pppp</p>
    <h1>h1</h1>
    <span>span</span>
</body>
```

.css
```css
*{
    color: red;
}
```

## 3_4_文字基本样式

### 字体大小

**语法**

* `font-size : 数字 + px`
* 默认字号为31px

.html
```html
<body>
    <!-- 浏览器当中默认字号为16px -->
    <p>段落文字</p>
</body>
```

.css
```css
p{
    font-size: 30px;
}
```

### 字体粗细

**语法**

* `font-weight : 数字(100-900整百数)`推荐
* `font-weight : normal/bold`
* 默认正常为400，加粗为700

.html
```html
<body>
    <div>这是div</div>
    <h1>一级标题</h1>
</body>
```

.css
```css
div{
    font-weight: 700;
}

h1{
    font-weight: 400;
}
```

### 字体倾斜

**语法**

* `font-style : normal/italic`

.html
```html
<body>
    <div>div文字</div>
    <em>em</em>
</body>
```

.css
```css
div{
    font-style: italic;
}
em{
    font-style: normal;
}
```

## 3_5_字体

**语法**

* `font-family : 具体字体`
* windows默认字体为**微软雅黑**

**常见字体**

* 无衬线字体 类微软雅黑 笔画均匀，无笔锋 **常用** <br> sans-serif
* 衬线字体 类宋体 笔画粗细不均，有笔锋 <br> serif
* 等宽字体 每个字母占据宽度相同 <br> monospace

.html
```html
<body>
    <div>这是一个div标签</div>
</body>
```

.css
```css
div{
    /* 如果用户电脑没有安装微软雅黑，那么就按黑体显示文字 */
    /* 如果黑体也没安装，那么按任意一种非衬线字体系列显示 */
    font-family:微软雅黑,黑体,sans-serif;
}
```

## 3_6_CSS的层叠性

*给同一个标签设置了相同的样式，最下面的会生效*

.html
```html
<body>
    <p>pppppp</p>
</body>
```

.css
```css
p{
    /* 基于层叠性，后面的覆盖前面的 */
    color: red;
    color:blue;
}
```

## 3_7_font复合属性

*字体相关属性仅用一个属性即可完成*

**语法**

* `font:style weight size family`

**注意**

* **只能省略前两个**(style weight)，省略表示默认值

.html
```html
<body>
    <p>这是p标签</p>
    <div>div</div>
</body>
```

.css
```css
p{
    /* font:style weight size family */
    font:italic 700 66px 微软雅黑;
    font-style: normal;

    /* 一个属性冒号后面书写多个值的写法 -- 复合属性 */
}

div{
    font: 100px 微软雅黑;
}
```

## 3_8_文本缩进

*应用场景&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;常用于段落开头的两个空格*

**语法**

* text-indent:数字+px
* text-indent:数字+em **推荐** (1em = 当前标签的font-size)

.html
```html
<body>
    <p>达奇先生的离世也引起了众多粉丝和同行的惋惜和追思。他的逝去意味着华语电影界损失了一位重要的艺术家，让人倍感惋惜。然而，在这个充满悲痛的时刻，我们应该深思一下这位艺术家为华语电影界所做的贡献。无论是在电影剧情中，还是在人物角色的塑造上，他都以其出色的才华和专业的态度给观众们带来了无尽的欢乐和震撼。</p>
</body>
```

.css
```css
p{
    /* 首行缩进2个字大小 */
    /* 默认字号16px */
    text-indent: 32px;
    font-size: 20px;
    /* em 一个字大小 */
    text-indent: 2em;
}
```

## 2_9_文本水平对齐方式

**语法**

* text-align:left/center/right

**适用对象**

* 文本
* span标签,a标签
* input标签，img标签
* ...

**注意**

* 要居中谁，则要给**包裹住居中对象的标签**加

.html
```html
<body>
    <h1>新闻标题</h1>
    <div>
        <img src="./1.gif">
    </div>
</body>
```

.css
```css
h1{
    text-align: left;
    text-align: right;
    text-align: center;
}

div{
    text-align: center;
    
}
```

## 2_10_文本修饰线

*控制下划线，删除线，上划线的有无*
*常用于清楚a标签的下划线*

**语法**

* text-decoration:underline/line-through/overline/none

.html
```html
<body>
    <div>div</div>
    <p>ppp</p>
    <h2>h2</h2>
    <a href="./jmphtml.html">跳转</a>
</body>
```

.css
```css
div{
    text-decoration: underline;
}
p{
    text-decoration: line-through;
}
h2{
    text-decoration: overline;
}
a{
    text-decoration: none;
}
```

## 2_11_行高

*控制两行文字间距离&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上间距+文本高度+下间距*

**语法**

* line-height:数字px
* lint-height:数字&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;表示font-size的倍数

*vscode中查看-自动换行设置分多行显示*

**注意**

* font复合属性中size可以加line-height
* 写法 font : style weight size **/** line-height family

.html
```html
<body>
    <p>2019年，事件视界望远镜团队让世界首次看到了黑洞的样子。不过，研究人员公布的这张发光环形物体的图像并不是传统的图片，而是经过计算获得的。利用位于美国、墨西哥、智利、西班牙和南极地区的射电望远镜所得到的数据，研究人员进行了数学转换，最终合成了这张标志性的图片。研究团队还发布了实现这一壮举所用的编程代码，并撰文记录这一发现，其他研究者也可以在此基础上进一步加以分析。</p>
</body>
```

.css
```css
p{
    line-height:50px;
    line-height: 1.5;
    font-size: 32px;
    font: italic 700 66px/2 宋体;
}
```

## 2_12_颜色常见取值

* 关键词写法 `red blue yellow...`
* rgb表示法 `rgb(..,..,..)`
* raba表示法 `rgba(..,..,..,..)` <br> a表示透明度 0-1 其余 0-255
* 十六进制表示法 `#...` <br> 六位数 两两分组 分别为r,g,b 如果全部组中每组两个数都一样，可以简写为一个

## 2_13_标签水平居中方法总结

*text-align : center;是让内容水平居中*

**外部标签水平居中的方法**

* margin : 0 auto;
* 0 表示上下居中
* auto 表示左右居中

