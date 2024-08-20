# *陆*_CSS浮动
 
* [6.1_结构伪类选择器](#6.1_结构伪类选择器)
* [6.2_伪元素](#6.2_伪元素)
* [6.3_标准流](#6.3_标准流)
* [6.4_体验行内块问题](#6.4_体验行内块问题)
* [6.5_浮动的作用](#6.5_浮动的作用)
* [6.6_浮动的特点](#6.6_浮动的特点)
* [6.7_CSS属性书写顺序](#6.7_CSS属性书写顺序)
* [6.8_清除浮动](#6.8_清除浮动)
* [6.9_清除浮动-额外标签](#6.9_清除浮动-额外标签)
* [6.10_单伪元素清除法](#6.10_单伪元素清除法)
* [6.11_双伪元素清除法](#6.11_双伪元素清除法)
* [6.12_清除浮动`overflow-hidden`](#6.12_清除浮动`overflow-hidden`)

---

## 6.1_结构伪类选择器

*通过元素的结构关系查找元素*

*减少对类的依赖*

**语法**

* `E:first-child{}`
* `E:last-child{}`
* `E:nth-child(n){}` **重点** 某父级元素下的第n个，且为E元素
* `E:nth-last-child(n){}`

.html
```html
<body>
    <ul>
        <li>这是第1个li</li>
        <li>这是第2个li</li>
        <li>这是第3个li</li>
        <li>这是第4个li</li>
        <li>这是第5个li</li>
        <li>这是第6个li</li>
        <li>这是第7个li</li>
        <li>这是第8个li</li>
    </ul>
</body>
```

.css
```css
/* 选中第一个 */
/* li:first-child{
    background-color: green;
} */

/* 最后一个 */
/* li:last-child{
    background-color: green;
} */

/* 任意一个 */
/* li:nth-child(5){
    background-color: green;
} */

/* 倒数第xx个 */
li:nth-last-child(1){
    background-color: blue;
}
```

**公式写法**

* 用来筛选一些**有明显数学关系**的子元素
* `E:nth-child(n){}`中的n可以去取值为公式 <br> 2n 偶数 <br> 2n+1/2n-1 奇数 <br> -n+5 前五个数 *n在前* <br> n+5 第五个及以后
* 在公式中 n的取值从0开始一直自增，能取到的子选择器即为筛选到的

.html
```html
<body>
    <ul>
        <li>这是第1个li</li>
        <li>这是第2个li</li>
        <li>这是第3个li</li>
        <li>这是第4个li</li>
        <li>这是第5个li</li>
        <li>这是第6个li</li>
        <li>这是第7个li</li>
        <li>这是第8个li</li>
    </ul>
</body>
```

.css
```css
/* 偶数 */
/* li:nth-child(2n){
    background-color: green;
} */
/* 奇数 */
/* li:nth-child(2n+1){
    background-color: green;
} */
/* 前三个 */
/* li:nth-child(-n+3){
    background-color: green;
} */
/* 选中4,8 */
li:nth-child(4n){
    background-color: green;
}
```

## 6.2_伪元素

*元素&nbsp;&nbsp;&nbsp;HTML设置的标签<br>伪元素&nbsp;&nbsp;&nbsp;由CSS**模拟**出的标签效果*


*一些装饰性图案可以使用伪元素*

**语法**

* `::before` 在父元素**内容**最前添加一个伪元素
* `::after` 在父元素**内容**最后添加一个伪元素

**注意**

* 必须设置`content`属性才能生效
* 默认为行内元素

.html
```html
<body>
    <!-- 通过CSS创建标签， 装饰性的不重要的小图 -->

    <!-- 找父级，在这个父级里面创建子级标签 -->

    <div class="father">爱</div>

    <!-- 老鼠爱大米 -->
</body>
```

.css
```css
.father{
    width: 300px;
    height: 300px;
    background-color: pink;
}

.father::before{
    /* 内容 */
    /* content必须添加，否则伪元素不生效 */
    content: '老鼠';
    color: green;
    width: 100px;
    height: 100px;
    background-color: blue;
    /* 默认是行内元素，宽高不生效 */
    display: block;
}

.father::after{
    content: '大米';
}
```

## 6.3_标准流

*又称文档流 **显示模式***

**介绍**

* 是浏览器渲染显示网页内容的默认的一套**排版规则**，规定了应该以何种方式排列元素
* 如何更改 **浮动**  **定位**

## 6.4_体验行内块问题

**浮动的作用**

* 让块级元素完美地排在一行
* inline-block会有间距的问题，利用浮动代替

.html
```html
<body>
    <div class="one">one</div><div class="two">two</div>
</body>
```

.css
```css
div{
    /* 浏览器解析行内块或行内标签时，如果标签换行书写会产生一个空格的距离 */
    display: inline-block;
    margin: 0;
    width: 100px;
    height: 100px;
}

.one{
    background-color: pink;
}

.two{
    background-color: skyblue;
}
```

## 6.5_浮动的作用

* 最初的目的&nbsp;&nbsp;&nbsp;图文环绕
* 现在的目的&nbsp;&nbsp;&nbsp;网页布局

**语法**
* `float: left/right`

.html
```html
<body>
    <!-- 1、图文环绕 -->
    <img src="./1.jpg">的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生
    <br>
    <br>   

    <div class="one">one</div>
    <div class="two">two</div>
</body>
```

.css
```css
img{
    width: 150px;
    float: left;
}

div{
    width: 100px;
    height: 100px;
}

.one{
    background-color: pink;
    float: left;
}

.two{
    background-color: skyblue;
    /* flr */
    float: right;
    float: left;
}
```

## 6.6_浮动的特点

* 浮动的标签会脱离标准流的控制（脱标），在**标准流中不占位置**
* 浮动元素比标准流高**半个级别**，可以覆盖标准流中的元素,（**无法覆盖文字**）
* **浮动找浮动**，下一个浮动元素会在上一个浮动元素的左右浮动
* 特殊显示效果 <br> <ul><li>一行可以显示多个</li><li>可以设置宽高</li></ul>

**注意**

* 浮动的元素不能通过`text-align: center`或`margin: auto`

.html
```html
<body>
    <div class="one">one</div>
    <div class="two">two</div>
    <div class="three">three</div>
</body>
```

.css
```css
/* 浮动的标签  顶对齐 */
/* 浮动: 在一行排列，宽高生效--浮动后的标签具备行内块的特点 */
.one{
    width: 100px;
    height: 100px;
    background-color: pink;
    float: left;
    margin-top: 50px;
    margin-right: 10px;
}

.two{
    width: 200px;
    height: 200px;
    background-color: skyblue;
    float: left;
    /* 因为有浮动,不能生效 */
    margin: 0 auto;
}

.three{
    width: 300px;
    height: 300px;
    background-color: orange;
}
```

## 6.7_CSS属性书写顺序

*代码清晰化&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行效率高*

1. `float/display`
2. 盒子模型相关属性`margin` `border` `padding` 宽度高度背景色
3. 文字样式

## 6.8_清除浮动

*清除浮动给别的标签带来的影响*

**影响**

* 子元素浮动不能撑开标准流的块级父元素

.html
```html
<body>
    <!-- 父子级标签，子级浮动，父级没有高度，后面的标准流盒子会受影响，显示到上面的位置 -->
    <div>
        <div class="top">
            <div class="left"></div>
            <div class="right"></div>
        </div>
        <div class="bottom"></div>
    </div>
</body>
```

.css
```css
.top{
    margin: 0 auto;
    width: 1000px;
    height: 300px;
    background-color: pink;
}

.bottom{
    height: 100px;
    background-color: green;
}

.left{
    float: left;
    width: 200px;
    height: 300px;
    background-color: #ccc;
}

.right{
    float: right;
    width: 790px;
    height: 300px;
    background-color: skyblue;
}
```

## 6.9_清除浮动-额外标签

**方法**

1. 在父元素内容的最后添加一个**块级元素**
2. 给添加的块级元素设置`clear:both` <br> clear的属性值 <br> `left`清除左浮动的影响<br>`right` 清除右浮动的影响  <br> `both` 清除左右浮动的影响

**缺点**

* 会在页面中添加额外的标签，会让页面的HTML结构变复杂

.html
```html
<body>
    <!-- 父子级标签，子级浮动，父级没有高度，后面的标准流盒子会受影响，显示到上面的位置 -->
    <div>
        <div class="top">
            <div class="left"></div>
            <div class="right"></div>
            <div class="clearfix"></div>
        </div>
        <div class="bottom"></div>
    </div>
</body>
```

.css
```css
.top{
    margin: 0 auto;
    width: 1000px;
    /* height: 300px; */
    background-color: pink;
}

.bottom{
    height: 100px;
    background-color: green;
}

.left{
    float: left;
    width: 200px;
    height: 300px;
    background-color: #ccc;
}

.right{
    float: right;
    width: 790px;
    height: 300px;
    background-color: skyblue;
}

.clearfix{
    clear: both;
}
```

## 6.10_单伪元素清除法

*将额外元素转为伪元素*

*可额外标签法的原理相同*

*项目中常用*

```css
.clearfix::after{
    content: '';

    /* 伪元素默认添加行内元素，要求块 */
    display: block;
    clear: both;

    /* 为了兼容性 */
    height: 0;
    visibility: hidden;
}
```

*给父标签添加`clearfix`类即可清除浮动*

## 6.11_双伪元素清除法

*项目中常用*

*既可以清除浮动又可以解决块级标签外边距塌陷问题*

```css
/* .clearfix::before的作用在于解决外边距塌陷问题 */
/* 外边距塌陷: 父子标签，都是块级，子级加margin会影响父级的位置 */
.clearfix::before,.clearfix::after{
    content: '';
    display: table;
}
/* 真正清除浮动的标签 */
.clearfix::after{
    clear: both;
}
```

*给父标签添加`clearfix`类即可清除浮动*

## 6.12_清除浮动`overflow-hidden`

给父元素设置`overflow-hidden`

*可以清除浮动和避免塌陷*

