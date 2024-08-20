# *伍*_CSS盒子模型
 
* [5.1_CSS优先级](#5.1_CSS优先级)
* [5.2_权重(优先级)叠加计算](#5.2_权重(优先级)叠加计算)
* [5.3_盒子模型-组成](#5.3_盒子模型-组成)
* [5.4_内容的宽度和高度](#5.4_内容的宽度和高度)
* [5.5_边框border](#5.5_边框border)
* [5.6_内边距](#5.6_内边距)
* [5.7_自动内减](#5.7_自动内减)
* [5.8_外边距](#5.8_外边距)
* [5.9_清除默认内外边距](#5.9_清除默认内外边距)
* [5.10_版心居中](#5.10_版心居中)
* [5.11_块级元素外边距的问题](#5.11_块级元素外边距的问题)
* [5.12_行内元素的内外边距问题](#5.12_行内元素的内外边距问题)

## 5.1_CSS优先级

**特性**

* 不同的选择器有不同优先级，**优先级高的选择器样式会覆盖优先级低的选择器样式**

**选择器的优先级**

* 继承 < 通配符选择器 < 标签选择器 < 类选择器 < id选择器 < 行内样式 < !important
* 总结而言，**可以更精准选到某一标签的选择器优先**
* !important可以**提高除继承外任意一级优先级至最高** <br> 写在属性值后，;前

.html
```html
<body>
    <!-- 意义: 当一个标签使用多个选择器，样式冲突时，到底谁生效 -->
    <div class="box" id="box" style="color: pink;">测试优先级</div>
</body>
```

.css
```css
#box{ #box{
    color: orange;
}

.box{
    color: blue;
}

div{
    color: green;
}

*{
    color: skyblue !important;
}

body{
    color: red;
}

/* ！important不要给继承的添加，自己有样式无法继承父级样式 */
```

## 5.2_权重(优先级)叠加计算

*可表示同一标签的复合选择器要通过权重叠加计算方式来判断最终哪个选择器在这个标签生效*

**叠加计算方法**

* 依次比较`行内样式的个数` `id选择器的个数` `类选择器的个数` `标签选择器的个数` <br> 若**某一环节不同，则多的优先级大** <br> 最终所有环节**比较个数相同，则优先级相同，根据层叠性生效**

.html
```html
<body>
    <div class="father">
        <p class="son" id="one">我是一个标签</p>
    </div>
</body>
```

.css
```css
/* 行内 id 类 标签 */

div #one{
    color: orange;
}

.father .son{
    color: skyblue;
}

.father p{
    color: purple;
}

div p{
    color: pink;
}
```

*注意`!important`的最高优先级效果*

**都是继承的情况**

* **直接继承高于间接继承**（继承于父大于继承于祖）
* 都是直接或都是同级间接继承，**按照叠加顺序比较**

## 5.3_盒子模型-组成

**概念**

* **每个标签可以看做一个盒子**，通过盒子视角更**方便布局**
* 浏览器在渲染页面时，会将页面中的元素看做**一个个矩形区域**，我们也形象称之为**盒子**

**内容组成**

* 内容区域 `content`
* 内边距区域 `padding`
* 边框区域 `border`
* 外边距区域 `margin`

.html
```html
<body>
    <div>内容</div>
    <div></div>
</body>
```

.css
```css
div{
    /* 纸箱子，填充泡沫 */
    width: 300px;
    height: 300px;
    background-color: pink;
    /* 边框线 == 纸箱子*/
    border: 1px solid #000;
    /* 内边距 == 填充泡沫 : 出现在内容和盒子边缘之间*/
    padding: 20px;
    /* 外边距 : 出现在两个盒子之间，出现在盒子的外面 */
    margin: 50px;
}
```

## 5.4_内容的宽度和高度

*width和height默认设置为盒子内容content的大小*

**语法**

* `width: 数字px`
* `height: 数字px`

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
}
```

## 5.5_边框border

**语法**

* 复合属性
* `border: 线宽 线条种类(虚实...) 颜色`
* 线条种类 `solid` 实线 `dashed` 虚线 `dotted` 点线
* **不可省略**，不分先后顺序
* Emmet `bd`

**单方向设置**

* 只给盒子的某方向单独设置边框*
* `border-left/right/top/bottom: 线宽 线条种类(虚实...) 颜色`

**单个属性**

* 不常用
* `border(-方位)-width/style/color`

.html
```html
<body>
    <div>内容</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
    background-color: pink;
    
    /* solid : 实线 */
    /* dashed : 虚线 */
    /* dotted : 点线 */
    border: 1px solid #000;
    border: 5px dashed #000;
    border: 5px dotted green;
    /* 单方向 */
    border-left: 1px solid #000;
    border-right: 1px solid red;
    border-top: 1px solid blue;
    /* 单个属性 */
    border-bottom-style: solid;
}
```

*border会撑大盒子的尺寸*
*盒子尺寸要考虑到边框*

## 5.6_内边距

**语法**

* `padding :数字px`上下左右为相同内边距
* 也可作为复合属性 <br> `padding :数字px 数字px 数字px 数字px`分别设置上右下左内边距 <br> `padding :数字px 数字px 数字px`分别设置上右下内边距，左右内边距相同 <br> `padding :数字px 数字px`分别设置上右边距，上下边距相同，左右边距相同
* 也可以`padding-方位`单独设置某一方向内边距

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
    /* 添加了4个方向的内边距 */
    /* padding: 50px; */
    padding: 10px ;

    /* padding属性可以当做复合属性 : 表示单独设置某个方向的内边距 */
    /* 最多取4个值 从上开始，顺时针*/
    padding: 10px 20px 40px 80px;

    /* 三值 */
    padding: 10px 40px 80px;

    /* 两值 */
    padding: 10px 80px;
}
```

*和border类似，padding同样会扩大盒子，计算width和height时要减掉*

## 5.7_自动内减

*代替手动减去border和padding*

**语法**

* `box-sizing: border-box`
* 添加padding和border后，不扩大盒子，自动在内容中减去
* 此时width和height设置的是盒子的大小

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 100px;
    height: 100px;
    background-color: pink;
    border: 10px solid #000;
    padding: 20px;

    /* 内减模式 */
    box-sizing: border-box;
}
```

## 5.8_外边距


**语法**

* `margin`
* 与内边距设置方式完全相同

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 100px;
    height: 100px;
    background-color: pink;
    margin: 50px;
    margin-left: 100px;
}
```

## 5.9_清除默认内外边距

*浏览器会给一些标签提供默认的内外边距*

**具有默认内外边距的标签**

* body默认 `margin: 8px`
* p标签默认右上下的`margin`
* ul标签默认有上下`margin`和`padding-left`
* ...

**清除语法**

```css
*{
    margin: 0;
    padding: 0;
}
```

## 5.10_版心居中

*版心&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;网页的有效内容*

**语法**

* `margin: 0 auto`
* auto意为左右自动相等，浏览器自动计算出

.html
```html
<body>
    <div>版心</div>
</body>
```

.css
```css
div{
    width: 1000px;
    height: 300px;
    background-color: pink;
    margin: 0 auto;
}
```

## 5.11_块级元素外边距的问题

**外边距合并现象**

* 垂直布局的块级元素，上下的margin会合并,两者中国最大值会合并
* 解决方案 <br> 只给其中一个设置`margin`

.html
```html
<body>
    <div class="one"></div>
    <div class="two"></div>
</body>
```

.css
```css
div{
    width: 100px;
    height: 100px;
    background-color: pink;
}

.one{
    margin-bottom: 100px;
}

.two{
    margin-top: 60px;
}
```

**外边距塌陷问题**

* 互相嵌套的**块级元素**，子元素的`margin-top`会导致父元素一起下移
* 解决方案 <br> 1. 给父元素设置`border-top`或`padding-top`（分隔父子元素的`margin-top`）<br> 2. 给父元素设置 `overflow: hidden` **推荐使用** <br> 3. 转换为行内块元素 <br> 4. 设置浮动

.html
```html
<body>
    <div class="father">
        <div class="son">son</div>
    </div>
</body>
```

.css
```css
.father{
    width: 300px;
    height: 300px;
    background-color: pink;
    /* padding-top: 10px; */
    /* 如果设计稿没有border,不能使用这个方法 */
    /* border: 1px solid #000; */
    /* overflow: hidden; */
    display: inline-block;
}

.son{
    width: 100px;
    height: 100px;
    background-color: skyblue;
    margin-top: 50px;
}
```

## 5.12_行内元素的内外边距问题

**如果想要通过`margin`或`padding`改变行内标签垂直位置，无法生效**

* `margin-top` `margin-bottom`不生效
* `padding-top` `padding-bottom`不生效
* 解决方法<br> 行高`line-height`可以改变垂直位置

.html
```html
<body>
    <span>span</span>
    <span>span</span>
</body>
```

.css
```css
span{
    /* margin: 100px; */
    padding: 100px;
}
```

