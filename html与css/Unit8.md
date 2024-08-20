# *柒*_CSS定位装饰
 
* [7.1_定位的作用和步骤](#7.1_定位的作用和步骤)
* [7.2_相对定位`relative`](#7.2_相对定位`relative`)
* [7.3_绝对定位`absolute`_相对于浏览器](#7.3_绝对定位`absolute`_相对于浏览器)
* [7.4_绝对定位`absolute`_相对于有定位的父级（祖先）](#7.4_绝对定位`absolute`_相对于有定位的父级（祖先）)
* [7.5_定位居中](#7.5_定位居中)
* [7.6_位移居中](#7.6_位移居中)
* [7.7_固定定位`fixed`](#7.7_固定定位`fixed`)
* [7.8_定位-显示层级](#7.8_定位-显示层级)
* [7.9_装饰-vertical-align](#7.9_装饰-vertical-align)
* [7.10_光标类型](#7.10_光标类型)
* [7.11_圆角边框](#7.11_圆角边框)
* [7.12_溢出部分显示方式`overflow`](#7.12_溢出部分显示方式`overflow`)
* [7.13_显示隐藏](#7.13_显示隐藏)
* [7.14_元素的整体透明度](#7.14_元素的整体透明度)
* [7.15_CSS使用精灵图](#7.15_CSS使用精灵图)
* [7.16_背景图缩放](#7.16_背景图缩放)
* [7.17_盒子阴影](#7.17_盒子阴影)
* [7.18_过渡](#7.18_过渡)

---

## 7.1_定位的作用和步骤

*页面中两个标签叠在一起*

*学成在线中精品推荐里的'hot'标签*

*标准流+浮动+定位配合才完美实现网页的布局*

**作用**

* 可以让标签摆放在**网页任意位置**
* 定位之后的元素**层级**最高，可以层叠**在其他盒子之上**
* 可以让盒子始终**固定在屏幕中的某个位置**

**使用步骤**

1. 设置定位方式 <br> <ul><li>CSS属性名:`position`</li><li>常见属性值:静态定位(不定位)`static`,**相对定位**`relative`,**绝对定位**`absolute`,**固定定位**`fixed`</li></ul>
2. 设置偏移值 <br> <ul><li>偏移量分为两个方向，水平和垂直方向各选一个</li><li>一般就近选择 CSS属性`left` `right` `top` `bottom` 属性值 `数字+px` or `百分比`</li></ul>

## 7.2_相对定位`relative`

*相对**自己**之前的位置进行移动*

***Emmet** por*

**注意**

* **相对定位**后在页面中仍占(原有)位置，没有脱标
* **相对定位**只有`position`属性，**没有方位属性，不会生效于自身（位置，脱标等），但算作自身已定位(对子级的绝对定位有影响)**
* 同时设置 `bottom` 和 `top` 以 `top` 为准，`bottom` 不生效
* 同时设置 `left` 和 `right` 以 `left` 为准，`right` 不生效


.html
```html
<body>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <div class="box">box</div>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
</body>
```

.css
```css
.box{
    position: relative;
    left: 100px;
    top: 200px;

    /* 
        1. 占用原来的位置 
        2. 仍然具备标签原有的显示模式(块级定位后，仍为块级，独占一行)
        3. 改变位置参照自己原来的位置
    */

    width: 200px;
    height: 200px;
    background-color: pink;
}
```

## 7.3_绝对定位`absolute`_相对于浏览器

*相对于**非静态定位的父元素（祖先）**进行定位，如**不存在这样的父级**，则相对于浏览器*

***Emmet** poa*

**注意**

* **绝对定位**查找的父元素**实际为祖先元素**，从父级开始向上查找，直到找到已定位的祖先，根据其进行绝对定位，否则根据浏览器窗口定位
* **绝对位置**脱标，不占位置
* **绝对定位**只有`position`属性，**没有方位属性，会生效:位置不变，脱标**
* 改变标签的显示模式特点: 具备**行内块显示特点**(可在一行共存，宽高生效,标签**默认由内容撑开 *注意***)

.html
```html
<body>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <div class="box">box</div>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
</body>
```

.css
```css
.box{
    /* 绝对定位:
        先找已经定位的父级，如果有这样的父级，就以这个父级为参照物进行定位。
        如果有父级，但是父级未定位，以浏览器窗口为参照进行定位。
    */
    position: absolute;
    /* left: 50px; */
    left: 0;
    top: 0;

    /* 
    1. 脱标，不占位
    2. 改变标签的显示模式特点: 具备行内块显示特点(可在一行共存，宽高生效)
    */

    width: 200px;
    height: 200px;
    background-color: pink;
}
```

*项目中通常不会采取这种相对于浏览器的定位方式*

## 7.4_绝对定位`absolute`_相对于有定位的父级（祖先）

*项目中常用*

* 项目中一般父级相对定位模式，子级绝对定位模式 **子绝父相**

.html
```html
<body>
    <div class="father">
        <div class="son">
            <div class="sun"></div>
        </div>
    </div>
</body>
```

.css
```css
.father{
    position: relative;
    width: 400px;
    height: 400px;
    background-color: pink;
}

.son{
    /* 相对，绝对 */
    /* 项目中一般父级相对定位模式，子级绝对定位模式 子绝父相*/
    /* position: relative; */
    /* position: absolute; */
    width: 300px;
    height: 300px;
    background-color: skyblue;
}

.sun{
    position: absolute;
    /* left: 20px;
    top: 30px; */
    right: 20px;
    bottom: 50px;
    width: 200px;
    height: 200px;
    background-color: green;
}
```

## 7.5_定位居中

*以前通过margin auto实现标签居中(适用于标准流)*

*当绝对定位后,margin auto失效*

*可以绝对定位配合margin居中（水平垂直均可）*

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    /* 绝对定位的盒子不能使用左右margin auto居中 */
    position: absolute;
    /* margin: 0 auto; */
    /* 相对于定位的父级，没有，相对于浏览器移动浏览器大小的一半 */
    left: 50%;
    top: 50%;
    /* 上面把基线调到浏览器的正中间 */
    /* margin配合把中心调到浏览器的正中间 */
    margin-left: -150px;
    margin-top: -150px;
    
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

## 7.6_位移居中

*CSS中对于尺寸不支持手动计算的小数，可以通过位移间接表示*

*同时位移居中也方便修改代码*


* `transform:translate(a,b);`
* **Emmet** `tft`

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    /* 绝对定位的盒子不能使用左右margin auto居中 */
    position: absolute;
    /* margin: 0 auto; */
    /* 相对于定位的父级，没有，相对于浏览器移动浏览器大小的一半 */
    left: 50%;
    top: 50%;
    /* 上面把基线调到浏览器的正中间 */
    /* margin配合把中心调到浏览器的正中间 */
    /* margin-left: -150.5px;  */
    /* 位移:自己宽度高度的一半 */
    transform:translate(-50%,-50%);
    /* margin-top: -150px; */
    width: 401px;
    height: 300px;
    background-color: pink;
}
```

## 7.7_固定定位`fixed`

*相对于(浏览器)视口固定，不随浏览器的滚动等移动*

* **Emmet** `pof`

**注意**

* **固定定位** 脱标，不占位置
* **固定定位** 不写方位不生效
* **具备行内块特点** **脱标后由内容撑开，注意设置尺寸**

.html
```html
<body>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <div class="box">box</div>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
</body>
```

.css
```css
.box{
    position: fixed;
    left: 0;
    top: 0;

    /* 
        1. 脱标，不占位置
        2. 改变位置参考浏览器窗口
        3. 具备行内块特点
    */

    width: 200px;
    height: 200px;
    background-color: pink;
}
```

## 7.8_定位-显示层级

**不同布局方式**

*标准流 < 浮动 < 定位*

**相同布局方式**

*标准流和浮动没有这种问题*

**对于定位**

* 默认取决于**HTML文件**中的书写顺序，后来者居上
* 可以通过`z-index:整数;`修改在上的优先级，优先级大的在上 <br> z-index的默认值是`0`
* `z-index`**必须配合定位**

.html
```html
<body>
    <div class="two">two</div>
    <div class="one">one</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
}

.one{
    position: absolute;
    left: 20px;
    top: 50px;
    background-color: pink;
}

.two{
    position: absolute;
    left: 50px;
    top: 100px;
    background-color: skyblue;
    /* z-index: 999; */
}

/* 
    默认情况下，定位的盒子 后来者居上(HTML文件中)
    z-index:整数; 取值越大，显示顺序越靠上
*/
```

## 7.9_装饰-vertical-align

**基线**

* 浏览器**文字类型元素**排版中存在**用于对齐**的基线

*浏览器处理**行内和行内块**元素默认按文字解析*

**修改默认对齐方式**

* CSS属性 `vertical-align`
* **Emmet** `va`
* 属性值 <br> `baseline`默认，基线对齐方式 <br> `top` 顶部对齐 <br> `middle` 中部对齐 **常用** <br> `bottom` 底部对齐
* 对行内、行内块添加，都是行内/行内块对**较大的添加即可**

**给图片垂直居中的方式**

* 给父级设置行高(与父级高度相同)
* 给图片设置`va-middle`

## 7.10_光标类型

*设置鼠标在元素上的显示样式*

**语法**

* CSS属性 `cursor`
* **Emmet** cu
* 属性值 <br> `default` 默认值，通常箭头 <br> `pointer` 小手效果，提示用户可以点击 <br> `text` 工字型，提示用户可以选择文字 <br> `move` 十字光标，提示用户可以移动

.html
```html
<body>
    <div>div</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
    background-color: pink;

    /* 手型 */
    cursor: pointer;

    /* 工字型，表示可以复制 */
    cursor: text;

    /* 十字型，表示可以移动 */
    cursor: move;
}
```

## 7.11_圆角边框

*让盒子的四个角变光滑，增加页面细节，提升用户体验*

**语法**

* CSS属性`border-radius`
* **Emmet** `bdrs`
* 属性值 <br> 数字+px ，百分比（半径） 最大值为盒子宽/高的一半
* 从**左上**开始赋值，无赋值看对角（1个值表示全都四个角都赋为该值 **常用**）

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    margin: 50px auto;
    width: 200px;
    height: 200px;
    background-color: pink;
    /* 一个值: 表示4个角是相同的 */
    border-radius: 10px;
    /* 4值: 左上 右上 右下 左下 -- 从左上顺时针转一圈*/
    border-radius: 10px 20px 40px 80px;

    border-radius: 10px 40px 80px;

    border-radius: 10px 80px;
}
```

**常见应用**

* 画一个正圆 <br> <ol style="list-style:decimal;"><li>盒子需要是正方形</li><li>设置边框圆角为盒子宽高的一半(50%)</li></ol>
* 胶囊按钮 <br> <ol style="list-style:decimal;"><li>盒子要求长方形</li><li>设置->border-radius: 盒子高度的一半</li></ol>

## 7.12_溢出部分显示方式`overflow`

*当盒子的**内容部分**超过盒子范围时的效果*

**语法**

* CSS属性`overflow`
* 属性值 <br> `visible` 默认值，溢出部分可见 <br> `hidden` 溢出部分隐藏 <br> `scroll` 无论是否溢出，都显示滚动条 <br> `auto` 根据是否溢出，自动显示或隐藏滚动条

.html
```html
<body>
    <div class="box">我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果</div>
</body>
```

.css
```css
.box{
    width: 300px;
    height: 300px;
    background-color: pink;
    /* 溢出隐藏（常用） */
    overflow: hidden;
    /* 无论是否超出都显示滚动条(不常用) */
    overflow: scroll;
    /* 自动，根据是否溢出显示滚动条(不常用) */
    overflow: auto;
}
```

## 7.13_显示隐藏

*元素自身的隐藏 如hover时显示子菜单*

**语法**

* `visibility: hidden`不常用 <br> **Emmet** `v` <br> 隐藏后仍占位
* `display: none`常用 <br> 隐藏后不占位

.html
```html
<body>
    <div class="one">one</div>
    <div class="two">two</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
}

.one{
    /* 占位隐藏 */
    /* visibility: hidden; */
    /* ****不占位隐藏 */
    display: none;
    background-color: pink;
}

.two{
    background-color: green;
}
```

## 7.14_元素的整体透明度

*修改元素整体（包括内容）的透明度*

**语法**

* CSS属性`opacity`
* **Emmet** `op`
* 属性值 0-1
* 常和js配合使用

.html
```html
<body>
    <div>
        <img src="../study/images/course02.png" alt="">
        这个字透明吗
    </div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    background-color: green;

    opacity: 0.5;
}

img{
    vertical-align: bottom;
}
```

## 7.15_CSS使用精灵图

*项目中将多张小图片，合并成一张大图片(精灵图)*

*减少服务器发送次数，减轻服务器压力，提高页面加载速度*

**精灵图的使用步骤**

1. 创建盒子，盒子**尺寸和小图相同**
2. 将**精灵图**设置为盒子的**背景图**片
3. 修改背景图位置 <br> 通过pxcook测量**图片左上角距离精灵图左上角水平垂直长度**，分别**取负值**给盒子的`background-position ： x，y`

.html
```html
<body>
    <!-- 一般精灵图标签，用行内标签,后修改显示模式 -->
    <span class="phone"></span>
    <span class="animal"></span>
</body>
```

.css
```css
.phone{
    display: block;
    width: 18px;
    height: 24px;
    background-image: url(./资料—前端HTML5+CSS3/day09-小兔鲜项目/day09/01-案例/images/taobao.png);
    /* 背景图位置属性 */
    /* 水平方向位置 垂直方向位置 */
    /* 想左侧上侧移动图片，取负数 */
    background-position: -3px 0;
}

.animal{
    display: block;
    width: 24px;
    height: 21px;
    background-image: url(./资料—前端HTML5+CSS3/day09-小兔鲜项目/day09/01-案例/images/taobao.png);
    background-position: 0 -90px;
}
```

## 7.16_背景图缩放

*不改变盒子大小的情况下，设置背景图片的大小*

**语法**

* CSS属性`background-size`
* 属性值<br> `数字+px` `数字+px` 宽高 <br> `百分比` `百分比` 相对于**当前盒子自身**的宽高百分比 <br> `contain` 包含，将背景图**等比例缩放**，直到**不超过盒子的最大**  <br> `cover` 覆盖，将背景图**等比例缩放**，直到刚搞填满**整个盒子没有空白**

**background复合属性**

 * 完整写法`background: color image repeat position/size` 无顺序，可省略
 * 一般不用，复合前四个，bgs单独写

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    width: 400px;
    height: 300px;
    background-color: pink;
    background-image: url(./资料—前端HTML5+CSS3/day09-小兔鲜项目/day09/01-案例/images/1.jpg);
    background-repeat: no-repeat;
    background-size: 300px;
    background-size: 50%;
    /* 可能导致盒子有留白 */
    background-size: contain;
    /* 可能导数图片不全 */
    background-size: cover;
    /* 项目中图的比例和盒子的比例通常相同 contain和cover效果相同 */
}
```

## 7.17_盒子阴影

**语法**

* CSS复合属性属性`box-shadow`
* 属性值 <br> `h-shadow` 必须，水平偏移量，可负 `v-shadow` 必须，垂直偏移量，可负 `blur` 可选，模糊度 `spread` 可选，阴影扩大 `color` 可选,阴影颜色（常为黑色） `inset` 可选，将阴影改成内部阴影
* 属性值**按顺序书写**，空格隔开
* 除后两个属性值外，都为数字+px

*CSS书写顺序* 定位 浮动/显示模式 盒子模型 文字格式 装饰

**文字阴影** 

* `text-shadow: h-shadow必须 v-shadow必须 blur可选 color可选`

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    height: 200px;
    width: 200px;
    background-color: pink;
    /* 注意: 外阴影，不能添加outset,添加会报错 */
    box-shadow: 5px 10px 20px 10px green inset;
}
```

## 7.18_过渡

***逐渐**变化的效果*

*一般配合`hover`*

**语法**

* CSS复合属性`transition`
* **Emmet** `trs`
* 属性值  `过渡的属性` `过渡的时长+s`
* 过渡属性通常为`all`

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    width: 200px;
    height: 200px;
    background-color: pink;
    /* 从宽度两百到宽度六百，花费1s时长 */
    /* 谁变化(变化前)，谁添加 */
    /* transition: width 1s, background-color 2s; */
    transition: all 1s;
}

.box:hover{
    background-color: blue;
    border-radius: 50%;
}
```

