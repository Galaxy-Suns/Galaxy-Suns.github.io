# *拾*_平面转换
 
* [10_1_平面转换简介](#10_1_平面转换简介)
* [10_2_位移](#10_2_位移)
* [10_3_绝对定位居中](#10_3_绝对定位居中)
* [10_4_平面旋转](#10_4_平面旋转)
* [10_5_转换原点](#10_5_转换原点)
* [10_6_多重转换](#10_6_多重转换)
* [10_7_缩放](#10_7_缩放)
* [10_8渐变](#10_8渐变)

---

## 10_1_平面转换简介

**作用**

* 改变盒子在平面内的布局（**位移（常用），旋转（不常用），缩放（常用）**）
* 2D转换

**平面**

* 水平 右+
* 垂直 下+

**语法**

* CSS属性`transform`
* **Emmet**`tf`

## 10_2_位移

**语法**

* `transform: translate(水平，垂直)`
* 取值正负均可:像素/百分比 <br> 百分比参照位移盒子的尺寸计算结果

.html
```html
<body>
    <div class="father">
        <div class="son"></div>
    </div>
</body>
```

.css
```css
.father{
    width: 500px;
    height: 300px;
    margin: 100px auto;
    border: 1px solid #000;
}

.son{
    width: 200px;
    height: 100px;
    background-color: pink;
    transition: all 0.5s;
}

/* 鼠标移动到父盒子，控制子盒子的位移 */
.father:hover .son{
    transform: translate(50px,100px);
    /* 如果是百分比，参考盒子自身尺寸计算结果 */
    transform: translate(-50%,-100%);
}
```

**单方向移动**

* `translate()给一个值,表示x轴移动距离`
* 单独设置某方向 `translateX()` `translateY()`

```css
transform: translate(50px);
transform: translateY(50px);
transform: translateX(50px);
```

## 10_3_绝对定位居中

*使绝对定位的盒子在已定位的父元素/浏览器内的垂直/水平居中效果*

.html
```html
<body>
    <div class="father">
        <div class="son"></div>
    </div>
</body>
```

.css
```css
.father{
    position: relative;
    width: 500px;
    height: 300px;
    margin: 100px auto;
    border: 1px solid #000;
}

.son{
    position: absolute;
    /* 此百分比参考的是绝对定位的参照盒子 */
    left: 50%;
    top: 50%;

    /* 改变盒子的位置 */
    /* margin-left: -100px;
    margin-top: -50px; */

    /* 位移 此百分比参考盒子自身尺寸计算结果*/
    transform: translate(-50%,-50%);
    width: 200px;
    height: 100px;
    background-color: pink;
}
```

## 10_4_平面旋转

**语法**

* `transform:rotate(角度)`
* 角度的单位 **deg(度)**
* 取值 数字+deg<br>顺时针+<br>逆时针-

.html
```html
<body>
    <img src="./资料/移动Web-Day11资料/移动Web-Day11资料/code/images/rotate.png" alt="">
</body>
```

.css
```css
img{
    width: 250px;
    transition: all 2s;
}

img:hover{
    transform: rotate(360deg);
    transform: rotate(-360deg);
}
```

## 10_5_转换原点

*默认转换原点是盒子的中心点*

**语法**

* CSS复合属性`transform-origin ：原点的水平位置 原点的垂直位置 `属性改变**转换原点**，*而不是旋转原点*，包括位移，旋转，缩放...
* **Emmet**`tfo`
* 属性取值 <br> **方位名词** `left` `top` `right` `bottom` `center` **常用** <br> 像素单位取值 <br> 百分比(参照转换原点所在盒子自身尺寸)
* 写在转换之前的盒子


.html
```html
<body>
    <img src="./资料/移动Web-Day11资料/移动Web-Day11资料/code/images/rotate.png" alt="">
</body>
```

.css
```css
img{
    width: 250px;
    border: 1px solid #000;
    transition: all 2s;
    /* 添加到标签本身，不要添加到hover */
    transform-origin: left bottom;
}

img:hover{
    transform: rotate(360deg);
    transform: rotate(-360deg);
}
```

## 10_6_多重转换

*某一个盒子同时具备多种形态变化如旋转和位移等等*

**语法**

* `tranform`复合属性
* 如: `transform: translate() rotate();`

**注意**

* **注意顺序** 先位移再旋转，否则因为旋转会改变坐标轴方向，导致位移方向改变，出现螺旋的情况
* 多重转换如果涉及到**旋转**，向**最后书写**
* 不可分开写（*只会有一个`transform`生效，层叠性*），只可采用**复合属性**

.html
```html
<body>
    <div class="box">
        <img src="./资料/移动Web-Day11资料/移动Web-Day11资料/code/images/tyre1.png" alt="">
    </div>
</body>
```

.css
```css
.box{
    border-radius: 100px;
    width: 800px;
    height: 200px;
    border: 1px solid #000;
}


img{
    width: 200px;
    transition: all 8s;
}

.box:hover img{
    transform: translateX(600px) rotate(720deg);

    /* 不行：旋转会改变坐标轴向 */
    /* transform: rotate(720deg) translateX(600px); */
}
```

## 10_7_缩放

*改变元素的尺寸*

**语法**

* `transform:scale(x轴缩放倍数,y轴缩放倍数)`
* `transform:scale(缩放倍数)` **常用**，xy轴等比例缩放，大于1放大，小于1所需

.html
```html
<body>
    <div class="father">
        <img src="./资料/移动Web-Day11资料/移动Web-Day11资料/code/images/product.jpeg" alt="">
    </div>
</body>
```

.css
```css
.father{
    margin: 100px auto;
    width: 300px;
    height: 210px;
    background-color: pink;
    /* overflow: hidden; */
    
}

img{
    width: 100%;
    transition: all 2s;
}

.father:hover img{
    /* width: 200px;
    height: 300px; */
    /* 放大 */
    transform: scale(1.2);
    /* 缩小 */
    transform: scale(0.8);
}
```

## 10_8渐变

*实现**多个颜色**逐渐变化的视觉效果，如盒子的背景*

**语法**

* `background-image: linear-gradient(颜色1，颜色2...)`
* `linear-gradient`打出`li`

.html
```html
<body>
    <div class="box">
        <div class="box"></div>
    </div>
</body>
```

.css
```css
.box{
    width: 300px;
    height: 200px;
    background-color: pink;
    background-image: linear-gradient(pink,green,blue);

    /* ***半透明渐变: 透明->rgba() 常用*/
    background-image: linear-gradient(
        transparent,rgba(0,0,0,.6)
    );
}
```

**注意**

* `.mask`表示遮罩层
* 注意透明颜色是`transparent`

