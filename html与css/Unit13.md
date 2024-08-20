# *拾壹*_空间转换
 
* [11_1_空间位移](#11_1_空间位移)
* [11_2_透视属性](#11_2_透视属性)
* [11_3_空间旋转](#11_3_空间旋转)
* [11_4_立体呈现](#11_4_立体呈现)
* [11_5_空间缩放](#11_5_空间缩放)

---

*与平面转换类似，实现元素在空间内的位移、旋转、缩放等效果*

*三D转换*

**语法** 仍为`transform`

**z轴** 用户视线方向**相对，指向屏幕外**（*不符合数学意义上的右手定则*）

## 11_1_空间位移

**语法**

* `transform:translate3d(水平位移，垂直位移，用户视线位移)`
* `reansform:translateX/Y/Z`
* 取值 像素/百分比 +-

**注意**

* 默认情况下，无法看出z轴的位移

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
    margin: 100px auto;
    background-color: pink;
    transition: all 0.5s;
}

.box:hover{
    /* 默认情况下，无法看出z轴的位移 */
    transform: translate3d(50px,100px,200px);
    transform: translateX(100px);
    transform: translateY(100px);
    /* 暂无效果 */
    transform: translateZ(100px);
}
```

## 11_2_透视属性

*近大远小 近实远虚*

**语法**

* CSS属性`perspective:值` 
* 打出`per`
* 作用:产生近代远小，近实远虚的视觉效果
* 属性添加给**要实现空间转换元素的父级**
* 取值，像素单位数组，一般在800-1200(最满足人的生活习惯)

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
body{
    perspective: 800px;
}


.box{
    width: 200px;
    height: 200px;
    margin: 100px auto;
    background-color: pink;
    transition: all 0.5s;
}

.box:hover{
    transform: translateZ(200px);
    transform: translateZ(-200px);
}
```

**原理**

* 设置的值是**视距** -- *人眼到屏幕的距离*
* 设置之后，里人眼近之后，'拉近的实际物体'在人眼上投影变大

## 11_3_空间旋转

**语法**

* `transfrom:rotateX/Y/Z(值);`
* 代表沿X/Y/Z轴旋转
* 方向和xyz关系一样，遵循“反右手定则（左手定则）”

**注意**

* 沿X/Y旋转加透视

.html
```html
<body>
    <div class="box a">
        <img src="./资料/移动Web-Day12资料/day02/code/images/hero.jpeg" alt="无">
    </div>
    <div class="box b">
        <img src="./资料/移动Web-Day12资料/day02/code/images/hero.jpeg" alt="无">
    </div>
    <div class="box c">
        <img src="./资料/移动Web-Day12资料/day02/code/images/hero.jpeg" alt="无">
    </div>
</body>
```

.css
```css
.box{
    width: 300px;
    margin: 20px auto;
    perspective: 1000px;
}

img{
    width: 300px;
    transition: all 2s;
    box-shadow: 10px 10px 20px 8px;
}

.a img:hover{
    transform: rotateZ(360deg);
}

.b img:hover{
    transform: rotateX(60deg);
}

.c img:hover{
    transform: rotateY(60deg);
}
```

**rotate3D**

* `rotate3D x,y,z 角度度数`
* 作用 设置自定义旋转轴，以及旋转角度
* x,y,z取0-1间数据

## 11_4_立体呈现

*呈现一个真正的立体图形*

*per..只能模拟一个近大远小的效果*

**语法**

* `transform-style:preserve-3d`
* **Emmet** `tfs`
* 使**子元素**处于真正的3d空间(子元素通常为各个面)
* `transform-style`默认值`flat`，表示子元素处于2D平面内呈现

**呈现立方体步骤**

1. 创建父子集关系
2. 添加`trs`属性
3. 分离各个子集(定位，位移，旋转)
4. 给父级添加hover

.html
```html
<body>
    <div class="cube">
        <div class="front">前面</div>
        <div class="back">后面</div>
    </div>
</body>
```

.css
```css
.cube{
    position: relative;
    margin: 100px auto;
    width: 200px;
    height: 200px;
    background-color: pink;
    transition: all 2s;
    transform-style: preserve-3d;
}

.cube:hover{
    transform: rotateY(180deg);
}

.cube div{
    width: 200px;
    height: 200px;
}

.front{
    position: absolute;
    left: 0;
    top: 0;
    background-color: orange;
    transform: translateZ(200px);
}

.back{
    background-color: green;
}
```

**注意**

* *其一* 父级3D化后，旋转原点不变（要使得3D化图形中心仍为原来2D图形中心）
* *其二* 实现各子元素在各个面要保证父元素`preserve-3d`,且最后hover的是`preserve-3d`的父元素

## 11_5_空间缩放

**语法**

* `transform:scaleX/Y/Z(倍数)`
* `transform:scale3d(x倍数,y倍数,z倍数)`

.html
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>立体呈现</title> 
    <link rel="stylesheet" href="./iconfont/iconfont.css">
    <link rel="stylesheet" href="./try.css">  
</head>
<body>
    <div class="nav">
        <ul >
            <li><a href="#">
                <div class="front">首页</div>
                <div class="top">Index</div>
            </li></a>
            <li><a href="#">
                <div class="front">登录</div>
                <div class="top">Login</div>
            </li></a>
            <li><a href="#">
                <div class="front">注册</div>
                <div class="top">Register</div>
            </li></a>
        </ul>
    </div>
</body>
</html>
```

.css
```css
*{
    margin: 0;
    padding: 0;
    list-style: none;
    text-decoration: none;
    box-sizing: border-box;
}

.nav{
    width: 450px;
    height: 50px;
    /* background-color: pink; */
    
}

.nav ul{
    transform-style: preserve-3d;
}

.nav div{
    position: absolute;
    left: 0;
    top: 0;
    height: 50px;
    width: 150px;
}

.nav .front{
    background-color: green;
    transform: translateZ(25px);
}

.nav .top{
    background-color: orange;
    transform: translateY(-25px) rotateX(90deg);
}


.nav li{
    position: relative;
    float: left;
    width: 150px;
}

.nav a:hover{
    transform: rotateX(-90deg);
}

.nav a{
    display: block;
    transform-style: preserve-3d;
    width: 150px;
    height: 50px;
    text-align: center;
    line-height: 50px;
    color: #fff;
    transition: all 1s;

    /* 测试缩放 */
    transform: scale3d(0.5,1.1,2);
}
```

