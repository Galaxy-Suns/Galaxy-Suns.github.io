# *肆*_CSS进阶
 
* [4.1_选择器-后代](#4.1_选择器-后代)
* [4.2_子代选择器](#4.2_子代选择器)
* [4.3_并集选择器](#4.3_并集选择器)
* [4.4_交集选择器](#4.4_交集选择器)
* [4.5_hover伪类选择器](#4.5_hover伪类选择器)
* [4.6_Emmet语法](#4.6_Emmet语法)
* [4.7_背景色](#4.7_背景色)
* [4.8_背景图片](#4.8_背景图片)
* [4.9_背景平铺](#4.9_背景平铺)
* [4.10_背景位置](#4.10_背景位置)
* [4.11_background复合属性](#4.11_background复合属性)
* [4.12_img和背景图区别](#4.12_img和背景图区别)
* [4.13_元素显示模式-块](#4.13_元素显示模式-块)
* [4.14_元素显示模式-行内](#4.14_元素显示模式-行内)
* [4.15_元素显示模式-行内块](#4.15_元素显示模式-行内块)
* [4.16_元素显示模式转换](#4.16_元素显示模式转换)
* [4.17_标签的嵌套规范](#4.17_标签的嵌套规范)
* [4.18_CSS继承性](#4.18_CSS继承性)
* [4.19_CSS层叠性](#4.19_CSS层叠性)

---

## 4.1_选择器-后代

*根据HTML标签的嵌套关系，选择父元素后代中满足条件的元素*

**语法**

* `选择器1 选择器2 ...{CSS}`
* 从祖先开始找到满足这种嵌套关系的所有选择器
* 可以是标签名，类名，id，通配符

.html
```html
<body>
    <!-- 儿子，孙子，重孙子...... -->
    <p>这是一个p标签</p>
    <span>
        <div>
            <p>这是div的儿子</p>
        </div>
    </span>
</body>
```

.css
```css
/* 找到div的儿子，设置文字颜色为红色 */
/* 父选择器 后代选择器{} */
body div p{
    color: red;
}
```

## 4.2_子代选择器

*与后代不同，子代选择器只能选择儿子*

**语法**

* `选择器1>选择器2>...`
* 从祖先开始找到下一代中的选择器，继续找子代...
* 可以是标签名，类名，id，通配符

.html
```html
<body>
    <div>
        父级
        <a href="#">这是div里面的a</a>
        <p>
            <a href="#">这是div里面的p里面的a</a>
        </p>
    </div>
</body>
```

.css
```css
/* 空格隔开的是后代，儿子，孙子，重孙子(满足嵌套关系) */
/* div a{
    color: red;
} */

/* 只想选中儿子a */
/* div的儿子a文字颜色是红色 */
div>a{
    color: red;
}
```

## 4.3_并集选择器

*同时选择多组标签，设置一样的样式*

**语法**

* `选择器1，选择器2，...{CSS}`
* 每个选择器,结束**换行**
* 可以是标签名，类名，id，通配符

.html
```html
<body>
    <p>ppp</p>
    <div>div</div>
    <span>span</span>
    <h1>h1</h1>
    <h2>h2</h2>
</body>
```

.css
```css
/* p div span h1 文字颜色是红色 */

p,
div,
span,
h1{
    color: red;
}
```

## 4.4_交集选择器

*有些情况仅从类名或标签名无法找到，这时两者都需要*

**语法**

* `选择器标签名类名..`*连写*

.html
```html
<body>
    <!-- 找到第一个p，带box类的，设置文字颜色是红色 -->
    <p class="box">这是p标签:box</p>
    <p>ppppp</p>
    <div class="box">这是div标签</div>
</body>
```

.css
```css
/* p{
    color: red;
} */

/* .box{
    color: red;
} */

/* 必须是p标签，而且添加了box类 */

p.box{
    color: red;
}
```

## 4.5_hover伪类选择器

*设置鼠标悬停在元素上的状态样式*

**语法**

* `选择器:hover{CSS}`
  
.html
```html
<body>
    <a href="#">这是超链接</a>
    <!-- 任何标签都可以添加伪类 -->
    <div>div</div>
</body>
```

.css
```css
/* 悬停的时候文字是红色 */
a:hover{
    color:red;
    background-color: green;
}
/* 鼠标悬停到div的时候文字是绿色 */
div:hover{
    color: green;
}
```

## 4.6_Emmet语法

*vscode的功能，通过简写，快速生成代码*

.html
```html
<body>
    <!-- div -->
    <div></div>
    <!-- h1 -->
    <h1></h1>

    <!-- 生成div 带类名 -->
    <!-- .box -->
    <div class="box"></div>

    <!-- p.box -->
    <p class="box"></p>

    <!-- #fun -->
    <div id="fun"></div>

    <!-- p#box -->
    <p id="box"></p>

    <!-- p#box.red -->
    <p id="box" class="red"></p>

    <!-- div 同级 p -->
    <!-- div+p -->
    <div></div>
    <p></p>
    
    <!-- 父子> -->
    <!-- div>p -->
    <div>
        <p></p>
    </div>

    <!-- ul>li -->
    <ul>
        <li></li>
    </ul>

    <!-- ul有3个li -->
    <!-- ul>li*3 -->
    <ul>
        <li></li>
        <li></li>
        <li></li>
    </ul>

    <!-- ul里面有3个li,li里面有文字 {}-->
    <!-- ul>li{111}*3 -->
    <ul>
        <li>11</li>
        <li>11</li>
        <li>11</li>
    </ul>

    <!-- ul里面有3个li,li里面文字1,2,3 -->
    <!-- ul>li{$}*3 -->
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
</body>
```

.css
```css
div{
    /* font-size: ; */
    /* fsz */
    font-size: ;
    /* 提示CSS属性：单词的首字母 */
    /* fw700 */
    font-weight: 700;
    /* w */
    width: ;
    /* h */
    height: ;
    /* bgc */
    background-color: #fff;
    /* lh */
    line-height: ;

    /* 宽度300，高度200，背景色粉色 */
    /* w300+h200+bgc */
    width: 300px;
    height: 200px;
    background-color: pink;
}
```

## 4.7_背景色

**语法**

* `background-color : 关键字/rgb/rgba/十六进制`
* Emmet `bgc`

**注意**

* 背景色默认为透明 rgba(0,0,0,0)

.html
```html
<body>
    <div>div</div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    /* background-color: pink; */
    /* background-color: #ccc; */
    /* 红绿蓝是三原色，a是透明度0-1 */
    /* background-color: rgba(0,0,0,0.5); */
    background-color: rgba(0,0,0,.5);
}
```

## 4.8_背景图片

**语法**

* `background-image : url(图片的路径)`
* Emmet `bgi`

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
    background-image: url(./1.jpg);
}
```

## 4.9_背景平铺

*当盒子尺寸比背景大，会出现复制现象，通过修改背景平铺方式来修改*

**语法**

* `background-repeat : repeat/no-repeat/repeat-x/repeat-y`
* Emmet `bgr`
* 默认为 `repeat`  

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
    background-image: url(./1.gif);
    /* background-repeat: repeat; */
    background-repeat: no-repeat;
    background-repeat: repeat-x;
    background-repeat: repeat-y;
}
```

## 4.10_背景位置

*对于no-repeat的背景图默认为背景的左上*

**语法**

* `background-position: 水平方向放置 竖直方向放置`
* Emmet `bgp`
* 属性值 <br> 水平方向放置 `left` `center` `right` <br> 竖直方向放置 `top` `center` `bottom` <br> 数字px 原点为左上 x正方向 右 y正方向 下 

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    background-color: pink;
    background-image: url(./1.gif);
    background-repeat: no-repeat;
    background-position: right 0;
    background-position: right bottom;
    background-position: center center;
    background-position: center;
    background-position: 50px 100px;
    background-position: -30px -10px;

    /* 正数：向右向下移动，正数：向左向上移动 */
    /* 注意：背景色和背景图只显示在盒子的里面 */
}
```

## 4.11_background复合属性

**语法**

* `background: color image repeat position`
* Emmet `bg`
* 可按需求省略

.html
```html
<body>
    <div></div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    background: pink url(./1.gif) no-repeat center;
}
```

## 4.12_img和背景图区别

**都可实现在网页中显示一张图的效果**

* img标签
* div设置背景图

**区别-宽高的设置**

* img标签不设置宽高默认以图片的尺寸显示
* div背景图，需要**设置div的宽高**

**使用场景**

* img-插入图，用来实现较重要的图片
* bgi-背景图，用来实现修饰性图片(没有不影响使用)、可替代的交互效果等

## 4.13_元素显示模式-块

*标签也可以叫做标记、元素*

*显示模式 独占一行 一行可多个...*

**显示特点**

* 独占一行(一行只显示一个)
* 宽度**默认是父元素的宽度**，高度默认由内容撑开
* 可以设置宽高

**代表标签**

* **div**
* **p**
* **h系列**
* ul dl li ... form header

.html
```html
<body>
    <!-- 块:独占一行;宽度默认是父级的100%;添加宽高都生效 -->
    <div>11111</div>
    <br>
    <div>22222</div>
</body>
```
.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

## 4.14_元素显示模式-行内

**显示特点**

* 一行可以显示多个
* 宽度和高度默认由内容撑开
* **不可以设置宽高**

**代表标签**

* **a span** b u i s strong ins em del...

.html
```html
<body>
    <span>span</span>
    <span>span</span>
</body>
```

.css
```css
/* 行内:不换行;设置宽高不生效;尺寸和内容的大小相同 */
span{
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

## 4.15_元素显示模式-行内块

**显示特点**

* 一行可以显示多个
* **可以设置宽高**

**代表标签**

* **input textarea** button select
* img有行内块特点，但Chrome调试工具中显示inline

.html
```html
<body>
    <img src="1.gif" alt="">
    <img src="1.gif" alt="">
</body>
```

.css
```css
/* 行内块:一行显示多个;加宽高生效 */
img{
    width: 100px;
    height: 100px;
}
```

## 4.16_元素显示模式转换

*让元素符合另一种显示模式的布局要求*

**语法**

* `diaplay:block` 转换为块级元素 常用
* `display:inline-block` 转换为行内块元素 
* `display:inline` 转换为行内 很少用

.html
```html
<body>
    <div>11111</div>
    <div>22222</div>
    <span>span</span>
    <span>span</span>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;

    /* 转换为行内块 */
    display: inline-block;

    /* 转为行内 */
    display: inline;
}

span{
    width: 200px;
    height: 200px;
    background-color: pink;

    /* 转换为行内块 */
    display: inline-block;

    /* 转换为块 */
    display: block;
}
```

## 4.17_标签的嵌套规范

**大的准则&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;块套其它一般ok（p不套块），但行内，行内块一般不套块**

<br><br>

**块级元素一般作为大元素，可以嵌套文本，块级元素，行内元素，行内块元素等**

* 但是**p标签中不要嵌套div，p，h等块级元素**
* **h标签中也不能嵌套p标签**

<br><br>

**a标签内部可以嵌套除a标签外的任意标签**

```html
<body>
    <!-- p和h标题不能相互嵌套 -->
    <!-- <p>
        <h1>一级标题</h1>
    </p> -->

    <!-- p里面不能包含div -->
    <!-- <p>
        <div>divdiv</div>
    </p> -->

    <!-- a标签内部可以除a外嵌套任意元素 -->
    <!-- <a href="#">
        aaa
        <a href="#">aaa</a>
    </a> -->
</body>
```

## 4.18_CSS继承性

**特性**

* 子元素默认继承父元素的样式特点

**常见的可继承属性**

* 文字控制属性都可继承
* color
* font类
* text类
* line-height
* ...
* 不是控制文字的都不能继承

**特殊情况**

* a标签的color不从父级继承
* h系列标签的font-size不从父级继承

*自己有就不继承*

.html
```html
<body>
    <div>
        这是div里面的文字
        <span>这是div里面的span</span>
    </div>
    <div>
        <a href="#">这是超链接</a>
        <h1>一级标题</h1>
    </div>
</body>
```

.css
```css
/* 控制文字的属性都能继承，不是控制文字的属性都不能继承 */
div{
    color: pink;
    font-size: 30px;
    height: 300px;
}

a{
    color: red;
}
```

## 4.19_CSS层叠性

**特性**

* 给同一个标签设置不同的样式->层叠->共同作用在标签
* 给同一个标签设置相同样式->层叠->最终写在最后的样式生效

**注意**

* 样式冲突时，只有**选择器优先级相同**时，才能通过层叠判断

*vscode中`Alt`同时选择多个位置写*

