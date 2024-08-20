# *拾贰*_动画
 
  * [12_1_动画简介](#12_1_动画简介)
* [12_2_动画_from_to](#12_2_动画_from_to)
* [12_3_动画_百分比](#12_3_动画_百分比)
* [12_4_animation复合属性](#12_4_animation复合属性)
* [12_5_am拆分写法（不常用）](#12_5_am拆分写法（不常用）)
* [12_6_逐帧动画](#12_6_逐帧动画)
* [12_7_多组动画](#12_7_多组动画)

---

### 12_1_动画简介

**过渡的效果**

* 两个状态之间的变化过程

**动画的效果**

* 多个状态间的变化过程
* 动画中间过程可控(重复播放，最终画面，是否暂停)

**动画的本质**

* 大量相关联图片**连续播放**在脑中形成的画面
* 最小单元 **帧/动画帧**

## 12_2_动画_from_to

**动画实现步骤**

1.定义动画 <br> from to 两个状态<br> 百分比 多个状态


2.使用动画 <br> `animation 动画名称 动画花费时长;`<br>**Emmet** `am`

**定义动画:from to**

```css
@keyframes 动画名称{
    from {CSS属性}
    to {CSS属性}
}
```

* **Emmet** `@k`

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
    height: 100px;
    background-color: pink;
    /* 使用动画 */
    animation: change 2s;
}

/* 定义动画，从宽度两百变大到600 */
@keyframes change {
    from{
        width: 20px;
    }
    to{
        width: 600px;
    }
}
```

## 12_3_动画_百分比

```css
@keyframes 动画名称{
    0% {CSS属性}
    10% {CSS属性}
    50% {CSS属性}
    ...
    100% {CSS属性}
}
```


```css
/* 定义动画，从200到500*300再到800*500 */
/* 百分比指的是动画总时长的占比 */
@keyframes  change{
    0%{
        width: 200px;

    }
    50%{
        width: 500px;
        height: 300px;
    }
    100%{
        width: 800px;
        height: 500px;
    }
}
```

## 12_4_animation复合属性

*控制动画执行过程*

**语法**

* `animation 动画名称（必须） 动画时长（必须） 速度曲线 延迟时间 重复次数 动画方向 执行完毕时状态` 
* 无顺序
* **速度曲线**(不常用) 加速/减速/匀速`linear` `steps(n)`**分步动画**,把动画分成n步匀速执行
* **延迟时间** 一段时间后执行动画，控制动画的先后出场顺序
* **重复次数** 动画执行后，重复执行(不会延迟) **无限循环** `infinite`
* **动画方向** 正向/反向执行动画 `alternate`动画每次执行后反转方向
* **执行完毕时状态** 不可和`infinite`共用  `forwards`停留在结束状态
* 如果出现两个时间，第一个时间表示动画时长，第二个表示延迟时间

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
    height: 100px;
    background-color: pink;
    /* 使用动画 */
    animation: change 1s 3 alternate backwards;
}


@keyframes change {
    from{
        width: 0px;
    }
    to{
        width: 600px;
    }
}
```

## 12_5_am拆分写法（不常用）

**语法**

<table>
    <thead>
        <tr>
            <th style="background-color: #2d39a7;color: #fff;">属性</th>
            <th style="background-color: #2d39a7;color: #fff;">作用</th>
            <th style="background-color: #2d39a7;color: #fff;">取值</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background-color: #8a8fbb3a;">
            <td>animation-name</td>
            <td>动画名称</td>
            <td></td>
        </tr>
        <tr style="background-color: #8a8fbb0c;">
            <td>animation-duration</td>
            <td>动画时长</td>
            <td></td>
        </tr>
        <tr style="background-color: #8a8fbb3a;">
            <td>animation-delay</td>
            <td>延迟时间</td>
            <td></td>
        </tr>
        <tr style="background-color: #8a8fbb0c;color:red;font-weight:700;">
            <td>animation-fill-mode</td>
            <td>动画执行完毕时状态</td>
            <td>forwards:最后一帧状态</td>
        </tr>
        <tr style="background-color: #8a8fbb3a;">
            <td>animation-timing-function</td>
            <td>速度曲线</td>
            <td style="color:red;font-weight:700;">steps(数字):逐帧动画</td>
        </tr>
        <tr style="background-color: #8a8fbb0c;color:red;font-weight:700;">
            <td>animation-itreation-count</td>
            <td>重复次数</td>
            <td>infinite为无限循环</td>
        </tr>
        <tr style="background-color: #8a8fbb3a;color:red;font-weight:700;">
            <td>animation-direction</td>
            <td>动画执行方向</td>
            <td>alternate为反向</td>
        </tr>
        <tr style="background-color: #8a8fbb0c;">
            <td>animation-play-state</td>
            <td>暂停动画</td>
            <td>paused为暂停，通常配合:hover使用</td>
        </tr>
    </tbody>
</table>


## 12_6_逐帧动画

*了解补间动画->平滑和逐帧动画*

*绝大多数使用补间动画*

**语法**

* `animation-timing-function: steps();`

**逐帧动画使用场景**

* 配合**精灵图**时

**步骤**

1. 准备显示区域 <br> 设置盒子尺寸是**一张小图的尺寸**，背景图为当前精灵图
2. 定义动画 <br> 改变背景图位置(**移动距离为精灵图宽度（负值）** ** 不是right)
3. 使用动画 <br> 添加steps(**小图个数**) 无限重复 

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    margin: 100px auto;
    width: 140px;
    height: 140px;
    background-image: url(./资料/移动Web-Day12资料/day02/code/images/bg.png);
    animation: change 1s infinite  steps(12);
}

.box:hover{
    animation-play-state: paused;
}

@keyframes change {
    from{
        background-position: 0 0;
    }
    to{
        background-position: -1680px 0;
    }
}
```

## 12_7_多组动画

*给一个元素添加多组动画属性*

**语法**

```css
animation:
    动画1,
    动画2,
    ...
    动画N;
```

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    margin: 100px;
    width: 140px;
    height: 140px;
    background-image: url(./资料/移动Web-Day12资料/day02/code/images/bg.png);
    animation: 
        change 1s infinite  steps(12),
        box-move 3s forwards linear;

}

.box:hover{
    
}

@keyframes change {
    /* 如果动画的开始状态和盒子的默认样式是相同的，可以省略开始状态 */
    /* from{
        background-position: 0 0;
    } */
    to{
        background-position: -1680px 0;
    }
}

/* 定义一个盒子移动的动画 */
@keyframes box-move {
    from{
        transform: translate(0);
    }
    to{
        transform: translate(800px);
    }
}
```

