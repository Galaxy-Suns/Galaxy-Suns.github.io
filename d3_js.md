# D3.js

*支持图元级别的可视化*

*框架依赖于Vscode中的Live Server*

*使用d3.js前需要导入(类似import)*

## 壹 基础

---

### 1.1 SVG 可缩放矢量模型

**作用**

* d3用来绘制的**画布**
* 缩放**不会发生失真**
* 也是容纳所有**图元的容器**

```html
<svg style='display: block; margin: 0 auto;'>
    <g transform='translate(0,60)'>
        <rect width=100 height=100 fill='#EEEEEE' />
        <circle r=15 fill='#72bf67' cx=25 cy=30 />
        <circle r=15 fill='rgb(100, 149, 237)' cx=75 cy=30 />
        <g transform='translate(15,60) rotate(10)'>
            <path d="M0,0 A40,40 10 0,0 65,0" fill='none' stroke='gray' stroke-width=5 />
        </g>
    </g>
</svg>
```


### 1.2 D3查询SVG

**语法**

* `d3.select(...)` **只找一个**, 若有重名只返回第一个
* `d3.selectAll(...)` 有多少返回多少

*和 CSS 选择器规则相同*


```js
const svg = d3.select('#mainsvg');
```

### 1.3 D3设置SVG元素属性

**常见属性**

* `id`, `class`
* `x`, `y`矩形左上角的位置, `cx`, `cy`圆形(椭圆)中心位置
* `fill`, `stroke`
* `height`, `width`, `r`圆的半径
* `transform(translate, rotate, scale)`

*详细属性查阅* https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute

**坐标轴**

* 以**左上为原点**
* x轴正方向向右
* y轴正方向向下


**.attr获取设置元素属性**

* `element.attr('attr_name')` 获取元素属性
* `element.attr('attr_name', 'attr_value')` 设置元素属性 *返回的是图元本身, 因此支持链式调用*

```js
const svg = d3.select('.mainsvg')
const rect = d3.select('.mainsvg rect')

svg.attr('width', 400).attr('height', 200)

rect.attr('x', '100').attr('y', '50').attr('width', '50').attr('height', '80').attr('fill', 'pink')
```

### 1.4 D3添加删除SVG元素

*通常不需要自己添加删除*

**添加语法**

* `element.append(标签名)` 添加元素, 添加在父节点下面
* *返回添加的图元, 因此支持链式调用*

**删除语法**

* `element.remove()`
* *小心使用, 会直接删除掉整个标签*
* `opacity`属性设置为0也会有视觉上的删除效果

```js
svg.append('circle').attr('cx', '20').attr('cy', '30').attr('r', '10').attr('fill', 'skyblue')
```

### 1.5 D3读取CSV数据

**语法**

* `d3.csv(file).then(func)`
* 读取目标路径下的`.csv`文件, **后执行相应逻辑**
* `func`函数**接收的参数, 为读取后的数据**
* `.csv()`为异步函数, 及时没有读取好数据, 也不会阻塞后续程序
* `.csv()`后返回一个`Promise`对象, 意义是**不停询问数据是否读好**, 而后执行后续操作`.then()`


### 1.6 D3常用数据接口

**常用接口**

* `d3.min(arr[, rule])`
* `d3.max(arr[, rule])`
* `d3.extent(arr[, rule])` 同时返回最大值最小值，返回一个数据`[最小值, 最大值]`
* `rule`函数是一个规则, 传入参数为每一个数据, 返回值为比较的是它的什么部分`d => d.age`

### 1.7 比例尺

*真实与虚拟比例的转换*

**线性比例尺**

* **线性范围映射到线性范围**
* `let scale = d3.scaleLinear()` 返回值为一个**函数**
* `scale.domain([min_in, max_in]).range([min_out, max_out])`**将数据范围映射到像素范围**
* `out = scale(in)` 设置完毕后, **函数调用**

*常结合d3 min max 接口使用*

**条带比例尺**

* **离散范围映射到连续范围**
* `let scale = d3.scaleBand()` 返回值为一个**函数**
* **支持链式编程**`const scale = d3.scaleBand().domain(['a', 'b', 'c']).range([0, 120])` 
* `scale('b') // a - 40 b - 80 c - 120`

*多配合`array.map`方法进行提取对象的部分属性*

* `scale.padding(0.1)` **设置条带间距占*各自区域*的比重** *常用于柱状图的间隙*
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_1.jpg)

* `scale.bandwidth():` 返回条带的长度

### 1.8 坐标轴

*是一系列的图元 因此可做任意修改*

**介绍**

* **一个坐标轴为一个`group`(`<g></g>`)**, 通常需要两个坐标轴
* 坐标轴中的内容: 
  * 一个`<path>`用于横跨坐标轴的覆盖范围
  * 若干刻度(`.tick`) 
    * *每一个刻度又是一个`group`*
    * 每一个刻度**下属包含一个`<line>`**(显示坐标轴线 *如左到右/上到下*)和**一个`<text>`**(展示坐标刻度值 *实数/姓名/日期*)
  * 一个**可选的**用来描述坐标轴的标签
* 坐标轴**需要比例尺来定义**


**D3中的定义**

* `const yAxis = d3.axisLeft(yScale)` 左侧坐标轴
* `const xAxis = d3.axisBottom(xScale)` 底侧坐标轴

*结果为函数*

**绘制到真实页面**

* *在某一个**g标签下调用**`.call(axis)`*
* `const yAxisGroup = g.append('g').call(yAxis)`
* 结果是发现`<g>`下**多了坐标轴相关元素**
* 坐标轴会**默认放在坐标原点, 需要进一步平移** 
* *左侧坐标轴可采用顶部坐标轴->下移->逆时针转方法获得* (或许也可以用.text()方法改变?待测试)

*修改属性只需要 select 到相应图元 attr 相应属性即可*

* `d3.selectAll('.tick text').attr('font-size', '2em')`

**小 tips**

* *表示坐标轴意义的文本没有提供*, 如需要, **在g标签下`append`**
* 纵坐标轴需要`.attr('transform', rotate(-90))`(会出现**x,y颠倒或者取值相反**)
* **text标签默认继承**了p标签的`fill`属性`none`, 需要设置文本的`fill`为`black`
* **text的文字通过`.text()`设置**

**坐标轴的 margin**

*由于坐标轴初始在父节点的左上角, 而SVG范围外的内容不会显示, 因此SVG一定范围内再进行绘制*
t innerWidth = width - margin.left - margin.right 计算实际可绘制的宽高
const g = svg.append('g').attr('id', 'maingroup').attr('transform', 'translate(${margin.left}, ${margi
* `const margin = {top: 60, right: 30, bottom: 60, left: 200}`定义margin
* `const innerWidth = width - margin.left - margin.right` 计算实际可绘制的宽高
* `const g = svg.append('g').attr('id', 'maingroup').attr('transform', 'translate(${margin.left}, ${margin.top})')` SVG下额外定义一个组表示实际的可绘制空间

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_2.jpg)

### 1.9 数据绑定 data-join 接口

*使得图元随着数据的改变而改变, 不是必要操作, 但会使可视化编程更简洁*

**语法**

* `d3Elements.data(dataArr)` `dataArr`为数据数组, 将**该图元和这个数据数组绑定**, *具体绑定后如何修改数据，后续说明*
* **注意** `.data(..)`只能用于**数据和图元数目相同的前提**, *因此一般用`d3.selectAll(..)`获取一个以上的图元*
* 如何**数据和图元个数不匹配**, 可以使用`d3Elements.data(dataArr).join('图元标签')`进行**补全/删除图元**, 在**新增/删除/修改数据时, 都会对图元*自动*进行相应操作** *支持链式编程*


*data-join 数据绑定中`.attr`函数设置图元属性*

* 值设置 `d3Elements.attr('attrbuteName', 'value')`
* **函数设置** `d3Elements.attr('attrbuteName', (d[, i]) => {})` 
  * 函数的输入`d`为`.data(..)`绑给**每个图元的数据** ***常用***
  * 函数的输入`i`为目前设置的是**第几个图元**
  * 函数的返回值为**绑定图元得到的属性**
  * 函数可以省略掉输入`i`


### 1.10 D3的配色方案接口

*一些数组*

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_3.jpg)




## 贰 动画

---

*可以任意设定任意图元的运动方案*

### 2.1 基本语法

*使用`transition`模块*

**语法**

* `selections.transition().duration(ms).attr(type, value)`
* `transition()`使得`selections`有了一层包装, 因此后续的`attr`才会对动画后状态进行设置
* 此语句的意义是**经过多少`ms`渐变为后面`attr`的效果**
* `transition()`**后**的`attr`才有动画效果
* **支持链式调用** `.transition().duration(ms).attr().attr()...` **都会有动画效果, 且同时进行** *因为包装过了, 所以不是原来的`selections`了*

### 2.2 动画的过渡

*使用`ease`函数*

**语法**

* **链式调用**在`transition().duration(ms)后`
* `transition().duration(ms).ease(d3.easeLinear)`

**关于`ease(..)`的参数**

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_5.jpg)

*也可以自定义*

### 2.3 动画的同步

*强制使得一些图元一起开始结束动画*

**语法**

* `let transition = d3.transition().duration(ms)` **事先定义动画对象**
* `rects.transition(transition).attr(..)`
* `circles.transition(transition).attr(..)`
* 这些`selections`共享了输入的`transition`的`ID`
* `await transition.end()` **强制等待异步函数执行完毕**

### 2.4 动画的继承

*使得某些图元先执行一个动画，**结束后**再执行另一个*

**语法**

* `selections.transition().attr(..).transition().attr(..)` 前一个动画**执行完毕后才会执行下一个**
* 后面的`transition`可以继承前一个的内容`duration`,`ease`等

### 2.5 动画的插值

*因为动画的过渡实际上的0-1的过渡, 而并非所有属性都有0-1的默认过渡方式, 需要自行提供一些插值函数*

**语法**

* `selection.tween('属性名', 返回函数的函数)`
* **返回函数**的函数中的**返回函数** `t => {}` 参数代表`0 - 1`的值, 根据目前的动画处于`0 - 1`的哪一状态返回该状态的属性值
* 返回函数的**函数**中的**函数**  生成**返回的函数**, 定义函数的**前后端点值, 插值方式**等

*待理解补充 3-16:00*

### 2.6 动画的循环

*利用`transition.on`和`d3.sctive()`接口*

**语法**

* `transition.on('start', func repeat(){...})` 某个渐变刚开始时调用`repeat()`函数
* 在`repeat()`里面设置`attr`, 如何拿到`transation`? `d3.active(this)`
* 如 `d3.active(this).attr(..).transation().attr(..)`
* 开启下一轮 在最后在 `.on('start', repeat)` 递归


## 叁 Path

---

*饼图, 折线图等绘制都基于Path图元*

### 3.1 Path介绍

**简介**

* 是`SVG`中非常强大的**图元**, 可用来**绘制多种形状**
* `d`属性, `<path>`勾勒的方式, 即**笔顺** *起笔位置, 勾勒方向, 停笔位置, 如何勾勒*
* `stroke`属性 描边颜色
* `stroke-width`属性 描边宽度

**`d`属性**

* 代表**勾勒方式**
* 属性值为 若干 `命令 + 参数`的**序列**
* `M 10 10 H 90 V 90 H 10 L 10 20 Z` 
  1. 10 10起笔
  2. 水平移动到 90 10
  3. 竖直移动到 90 90
  4. 水平移动到 10 90
  5. 移动到 10 20
  6. 移动到起笔位置

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_6.jpg)

*d3.js 提供了很多接口, 因此一般不需要自己来绘制Path*

### 3.2 D3 Path接口介绍

* `d3.line().x(..).y(..)` 用于将**多个点依次连线** *折线图*
* `d3.arc().innerRadius(..).outerRadius(..)` **绘制弧** *饼图*
* `d3.geoPath().projection()` 用于**地理、地形**数据
* `d3.area()` **区域**的`d`属性 *主题河流*

### 3.3 d3.line()

*多点连线*

**语法**

* `const path = d3.line().x(..).y(..)` 返回值为一个**函数**, 这个**函数**赋予**数据数组**之后设置到`<Path>`的`d`属性 (`.attr('d', path(arr))`)
* `x, y`的参数为`函数`， 代表着横纵坐标如何取值
* 如 `.x(d => d.age * 100)` 这里的形参`d`表示着**返回的path函数未来的参数arr中一个数据**
* `path(arr)` 会生成 `d`属性的一个对应代码, 直接赋到`.attr`

**连线插值**

* `d3.line().x(..).y(..).curve(d3Curve)`

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_7.jpg)

### 3.4 d3.arc()

*根据提供角度勾勒圆弧*

**语法**

* `const path = d3.arc().innerRadius(100).outerRadius(200)`, 同样返回**函数**， 这个**函数**的输入为一个对象 `{'startAngle': 3.0, 'endAngle': 4.34}` 这**两个字段为规则** **弧度制**
* `.innerRadius(100)` 表示圆弧的**内半径** *缺失的部分*
* `.outerRadius(200)` 表示圆弧的**外半径**
* `.padAngle(0.1)` 弧两侧预留`0.1`倍的圆弧角度

### 3.5 时间的处理

**日期对象**

* JS提供**日期处理的对象**
* **输入为日期字符串, 输出为字符对象**
* `let myData = new Data("2023-1-28")`

**D3的日期比例尺**

* *D3的日期(时间)比例尺 `scaleTime`* 支持把**日期**映射为**像素**
* `const xScale = d3.scaleTime()`
* `xScale.domain(d3.extent(data.map(d => d.day))).range([0,1600])` *类似于线性比例尺*

**D3的日期格式化**

* `const timeFormat = d3.timeFormat('%b-%d')` 返回一个**函数** 把输入的日期整理成相应格式
* `const xAxis = d3.axisBottom(xScale).tickFormat(timeFormat)` 对一个**坐标轴应用某一格式**

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_8.jpg)

### 3.6 selection.datum() 绑定单一图元

*对于如折线图, 是单一的一个`<path>`图元绑定一批数据， 而非如柱状图一批图元绑定一批数据*

* 用于给**单一的图元绑定单一数据**
* 语法类似于`data-join`
* `path.datum(data).attr('d', line)` `line`是`d3.line()`生成的函数, 因此这里采用`attr` `函数`的形式, 而非`属性值`
* **`path`的`fill`要为`none`**

### 3.7 d3.pie() 转换弧度

*把数据中的某一条自动换算比例到弧度区间*

**语法**

* `const pie = d3.pie().value(..)` 返回**函数** `.value`表示 对于返回的**函数**来说, 其**传入的参数中的哪一部分**是**要计算的值**, 如 `d => d.population`
* `const arcData = pie(data)`

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_9.jpg)

*映射后每个数据仍有`.data`接口保留原始对象*


### 3.8 离散比例尺 scaleOrdinal 着色

* `.domain(['sun', 'shi', 'bo']).range(['a', 'b', 'c'])`
* 常用于**着色** 结合`data-join`
* *保证颜色够即可, 如果过多会自动处理*

### 3.9 饼图的文字标签 centroid

*饼图的中心点坐标*

**语法**

* `const arcOuter = d3.arc().innerRadius(..).outerRadius(..)` 定义一个饼图d属性函数
* `arcOuter.centroid({'startAngle':..,'endAngle':..})`参数为**饼图的起始终止位置对象**, 返回值为**圆弧的中心点坐标**， **配合`translate`, 绑定`text`**


## 肆 地图和地理

### 4.1 JSON 数据读取

* *JS中对象的文本版, 软件开发的常用格式*
* 本质是**纯文本，与编程语言无关**

**格式**

* `'属性名': '属性值'`
* 属性值可以为**字符串, 整数, 浮点数, 数组, 对象, 对象数组**

**读取**

* `d3.json(..).then(func)`

### 4.2 地理数据 geoJson

*基于JSON, 有自己的规则和命名, 记载经纬度信息*

**内容**

* `'type' : 'FeatureCollection'` 
  * `'feature'`数组 **包含数个下面含有这些属性的对象**
    * `'type' : 'feature'`
    * `'geometry' : 几何信息`
    * `'properties' : 属性, 包含人口, 气候, 邮政编码, 名称等`

**不可缺少的内容(构造方式)**

```js
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        // 点
        "type": "Point",
        "coordinates": [92.23, 42.13]
      }
    },
    {},{}...
  ]
}
```

*该实例为点的geoJson, 如需其他类型请自行查找*

**注意**

* 当原始数据不是`geoJson`的类型, 由于生成`proj`投影函数和z最终绘制时`d3.geoPath`生成函数的参数要为`geoJson.features`，可以把原始数据构造成`geoJson`的形式
* 但另一种解决方案为**当已经用其余geoJson数据生成了投影比例尺`proj`和d函数后**, 直接用投影比例尺`proj`把其余格式数据**投影到像素空间, 直接画出**

### 4.3 投影函数 geoNaturalEarth1()

*需要额外的js文件*

**语法**

* `let proj = d3.geoNaturalEarth1()` 返回一个**投影函数**, 比例尺
* `proj`函数的**输入`geoJson`的一个点(含经纬度), 输出画布上的一个点(含横纵坐标)** *点到点*
* 画在**同一位置的多组数据要用同一比例尺**`proj`(同一`d`函数)

*各种投影方式*

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_10.jpg)
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_11.jpg)
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_12.jpg)
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_13.jpg)

### 4.4 调整投影的大小 proj.fitSize()

*地图要画在多大的画布上*

**语法**

* `proj.fitSize([width, height], geoJson)`

### 4.5 地图绘制中`<path>` d3.groPath() path.projection(..)

**语法**

* `d3.geoPath()` 返回**函数**, 这个**函数**输入为`geoJson`的一个`Feature`, 输出为`d`属性(结合`.projection`)
* `let path = d3.geoPath()`
* `path.projection(..)`设置**经纬度到画布的投影方式**
* `let path = d3.geoPath().projection(proj)` 得到`d`属性

*地理暂时学到 7 19:55 后续地形等待补充*

### 星巴克全球分布可视化
```js
// 作用是找到 transform属性中的 scale 数值
// 注意, 只针对等比例缩放, 即scale只有一个参数
// 要求有scale属性值
// 传入参数是transform的属性值
// 返回值为 scale数值
function getTransformS(attrStr){
    let pos = attrStr.indexOf('scale(') + 6
    let attr = ''
    for(; pos < attrStr.length; pos++){
        if(attrStr[pos] === ',') break
        attr += attrStr[pos]
    }
    return +attr
}

// 作用是找到 transform属性中的 translate 数值
// 要求有translate属性值
// 传入参数是transform的属性值
// 返回值为 一个对象 x: translate的x值, y: translate的y值
function getTransformT(attrStr){
    let pos = attrStr.indexOf('translate(') + 10
    let attrX = ''
    let attrY = ''
    for(; pos < attrStr.length; pos++){
        if(attrStr[pos] === ',') break
        attrX += attrStr[pos]
    }
    for(pos ++; pos < attrStr.length; pos++){
        if(attrStr[pos] === ')') break
        attrY += attrStr[pos]
    }
    return {
        'x': +attrX,
        'y': +attrY
    }
}


// 全局
const mainSvg = d3.select('.mainsvg')
const width = mainSvg.attr('width')
const height = mainSvg.attr('height')

const mainGroup = mainSvg.append('g')


// 读取数据
d3.csv('All_Starbucks_Locations_in_the_World_-_Heat_Map.csv').then(datas => {

    d3.json('countries.geo.json').then(data => {
        // 得到 投影比例尺
        const proj = d3.geoMercator().fitSize([width, height], data)
        
        // 得到 d 函数
        const path = d3.geoPath().projection(proj)

        // 绘制 path map
        mainGroup.selectAll('path').data(data.features).join('path')
        .attr('stroke', 'black')
        .attr('fill', '#0f1a58')
        .attr('d', path)
        .attr('class', 'map')

        // 绘制 path point
        mainGroup.selectAll('.point').data(datas).join('circle')
        .attr('cx', d =>  proj([+d.Longitude, +d.Latitude])[0])
        .attr('cy', d =>  proj([+d.Longitude, +d.Latitude])[1])
        .attr('r', '0.05')
        .attr('fill', '#fff')
        .attr('class', 'point')
        
        mainSvg.on('dblclick', (e, d) => {
            let scale = getTransformS(mainSvg.attr('transform'))
            const oldScale = scale
            if(scale >= 1 && scale < 4) scale = 4
            else if(scale >= 4 && scale < 10) scale = 10
            else if(scale >= 10 && scale < 50) scale = 50
            else scale = 1
            const transform = mainSvg.attr('transform')
            .replace(`scale(${oldScale},${oldScale})`, `scale(${scale},${scale})`)
            const transition = d3.transition().duration(1000)
            mainSvg.transition(transition).attr("transform-origin", `${e.offsetX} ${e.offsetY}`).attr('transform', transform)
        })
        mainSvg.on('wheel',async (e, d) => {
            e.preventDefault();
            let scale = getTransformS(mainSvg.attr('transform'))
            const oldScale = scale
            if(e.deltaY < 0) scale *= 2
            else scale /= 2
            if(scale < 1) scale = 1 
            const transform = mainSvg.attr('transform')
            .replace(`scale(${oldScale},${oldScale})`, `scale(${scale},${scale})`)
            const transition = d3.transition().duration(1000)
            mainSvg.transition(transition).attr("transform-origin", `${e.offsetX} ${e.offsetY}`).attr('transform', transform)
        })

        mainSvg.on('drag', (e, d) => {
            //console.log(e.dataTransfer)
        })
    })
})

```

## 伍 交互

---

### 5.1 基础语法

**语法**

* `selection.on('eventName', (event, d) => {触发动作})`
* `event` **事件对象, 包含这个事件的信息**， 如鼠标触发事件的位置, 对应的图元等
* `event.currentTarget` 得到被事件触发的图元(**HTML形式, 可以直接传入**`d3.select()`)
* `d3.select(event.currentTarget)` 得到该图元(**JS**)
* `d` 当前图元**绑定的数据**

### 5.2 事件event

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_14.jpg)

https://developer.mozilla.org/zh-CN/docs/Web/Events

### 5.3 标签的标注 d3.tip

*需要额外的js文件*

**语法**

* `const tip = d3.tip().html((event, d) = > d.properties.name)` 告知`tip`如何**根据数据显示标签**
* `svg.call(tip)` 把`tip`加载到`svg` 类似坐标轴的添加
* `tip.show(event, d)` 基于**事件和绑定的数据** 显示`tip` *通常直接放在事件监听* 
* `tip.hidw(event, d)` 隐藏`tip`

### 全球一百人
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galaxy</title>
    <script src="./d3.min.js"></script>
    <script src="./d3-geo-projection.min.js"></script>
    <style>
        body{
            background-color: #fff;
        }
        span{
            position: fixed;
            display: block;
        }
        .title{
            top: 36%;
            right: 17%;
            font-size: 30px;
            font-weight: 700;
        }
        .show{
            top: 46%;
            right: 19%;
            font-size: 20px;
            font-weight: 700;
        }

        
    </style>
</head>
<body>
    <svg class="mainsvg" width="1700" height="800" transform="translate(0,0), scale(1,1)" ></svg>
    <span class="title">全球100人</span>
    <span class="show">展示类型</span>
    <script>
        // 闭
        function getRandomInt(start, end) {
            return Math.floor(start + (end - start + 1) * Math.random());
        }

        // 全局
        const width = Math.floor(document.body.offsetWidth) - 800
        const height = Math.floor(document.body.offsetHeight)
        const mainSvg = d3.select('.mainsvg')
        .attr('width', `${width + 800}`)
        .attr('height', `${height}`)


        // 位置数组按照以下格式
        // [{"x":.., "y":..},{},{}...]
        const posArr = []
        let duration = 10000;
        // 混沌状态 0 非混沌 1
        let flag = 0
        let buttonFlag = 0;

        // 数据的处理 处理为 一个数组, 每个元素表示 和标签顺序对应的一个界面, 也是数组, 这个子数组的每一个元素表示一个容器, 由对象表示, name属性表示描述, value属性表示值
        const dataArr = []
        d3.csv('100 People.csv').then(async data => {
            console.log(data)
            let tmp = data[0].Category
            let tmpArr = []
            for(let i = 0; i< data.length; i++){
                if(data[i].Category === ''){
                    dataArr.push(tmpArr)
                    break
                } 
                if(tmp !== data[i].Category){
                    tmp = data[i].Category
                    dataArr.push(tmpArr)
                    tmpArr = []
                }
                tmpArr.push({
                    "name": data[i].Subcategory,
                    "value": data[i].Value
                })
            }
        })

        // 更新posArr为随机的100个值 -3 - 3 范围
        // 返回posArr
        function ranUpPosArr(){
            for(let i = 0; i < 100; i++){
                let x = getRandomInt(-300, 300) * 100 + posArr[i].x
                let y = getRandomInt(-300, 300) * 100 + posArr[i].y
                if(x < 0) x = getRandomInt(0, 100) + posArr[i].x
                else if(x > width) x = posArr[i].x + getRandomInt(-100, 0)
                if(y < 0) y = getRandomInt(0, 100) + posArr[i].y
                else if(y > height) y = posArr[i].y + getRandomInt(-100, 0)
                posArr[i] = {"x": x, "y": y}
            }
            return posArr
        }


        // 使得posArr为随机的100个值   
        // 返回posArr
        function ranPosArr(){
            for(let i = 0; i < 100; i++){
                const x = getRandomInt(0, width)
                const y = getRandomInt(0, height)
                posArr[i] = {"x": x, "y": y}
            }
            return posArr
        }

        // 绘制饼图
        const path = d3.arc().innerRadius(150).outerRadius(300)
        const textArr = ['无序', '大洲', '性别', '年龄', '宗教', '读写能力', '学历', '网络', '手机', '饮用水', '贫穷状况', '营养状况', '住房', '母语', '城乡']
        const pie = d3.pie().value(textArr => 1)
        mainSvg.selectAll('path').data(pie(textArr)).join('path')
        .attr('d', path)
        .attr('transform', 'translate(1500, 400)')
        .attr('fill', (d, i) => d3.schemePastel2[i % 8])
        .attr('stroke', '#fff')
        .attr('stroke-width', '5')
        .attr('cursor', 'pointer')

        // 标注文字
        mainSvg.selectAll('.dsctext').data(textArr).join('text')
        .attr('class',(d, i) => 'dsctext' + i)
        .text(d => d)
        .attr('transform', (d, i) => `translate(${path.centroid(pie(textArr)[i])[0] + 1480}, ${path.centroid(pie(textArr)[i])[1] + 400})`)
        .attr('cursor', 'pointer')

        d3.select('path').attr('fill', '#FFD700')
        mainSvg.select('.dsctext0').attr('fill', '#fff')


        // 监听点击
        mainSvg.selectAll('path').on('click',async (event, d) => {
            // 得到点击的结点索引 i
            let i = d.index
            if(i === buttonFlag) return
            

            //清除
            mainSvg.selectAll('path')
            .attr('fill', (d, i) => d3.schemePastel2[i % 8])
            console.log(mainSvg.select('.dsctext' + buttonFlag).attr('fill', '#000'))
            buttonFlag = i

            //设置当前
            d3.select(event.currentTarget).attr('fill', '#FFD700')
            mainSvg.select('.dsctext' + d.index).attr('fill', '#fff')

            mainSvg.selectAll('.redtext').remove()
            mainSvg.selectAll('rect').remove()

            // 点击 无序状态
            if(i === 0){
                duration = 10000
                flag = 0
                while(true){
                await action()
            }
                return
            } 

            flag = 1

            duration = 1000

            const nowDataArr = dataArr[i - 1]
            
            const lineWidth = 700 / nowDataArr.length

            // 容器的处理
            mainSvg.selectAll('rect').data(nowDataArr).join('rect')
            .attr('height', '5')
            .attr('width', lineWidth)
            .attr('y', height / 2 + 100)
            .attr('fill', 'red')
            .attr('x',(d, i) =>(i + 1) * width / (nowDataArr.length + 1) - lineWidth / 2 )

            // 文字的处理
            mainSvg.selectAll('.redtext').data(nowDataArr).join('text')
            .attr('class', 'redtext')
            .attr('font-size', '18')
            .attr('fill', 'red')
            .attr('y', height / 2 + 130)
            .attr('x', (d, i) => (i + 1) * width / (nowDataArr.length + 1) - 18 * d.name.length / 2)
            .text(d => d.name)


            // posArr 的处理
            let count = 0
            // 外层循环控制的是每一堆
            for(let i = 0; i < nowDataArr.length; i++){
                let ballHeight = 1
                // 每一个球
                for(let j = 0; j < nowDataArr[i].value; j++){
                    // 排满十个球后, 增加高度
                    if(j % 10 === 0) ballHeight += 14
                    posArr[count] = {
                        "x": (i + 1) * width / (nowDataArr.length + 1) - 59 + (j % 10) * 11,
                        "y": height / 2 + 100 - ballHeight
                    }
                    count++;
                }
            }
            posArr.sort(function() {
                return (0.5-Math.random());
            })
            await action()
        })

        // 函数使 图元根据当前的duration和当前的posArr进行动画移动
        const action = async function(){
            // 混沌状态
            if(flag === 0) ranPosArr()
            const transition = d3.transition().duration(duration).ease(d3.easeLinear)
            mainSvg.selectAll('.point').data(posArr).join('circle')
            .attr('class', 'point')
            .attr('r', '5')
            .attr('fill', 'pink')
            .transition(transition)
            .attr('cx', d => d.x )
            .attr('cy', d => d.y)
            await transition.end()
        }

        // 初始化
        mainSvg.selectAll('.point').data(ranPosArr()).join('circle')
            .attr('class', 'point')
            .attr('r', '5')
            .attr('fill', 'pink')
            .attr('cx', d => d.x)
            .attr('cy', d => d.y);

        (async () => {
            while(true){
                await action()
            }
        })()
    </script>
</body>
</html>
```

### 时间题-top10经济
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dome</title>
    <script src="./d3.min.js"></script>
    <script src="./d3-geo-projection.min.js"></script>
    <style>
        

        
    </style>
</head>
<body>
    <svg class="mainsvg" width="1700" height="800" transform="translate(0,0), scale(1,1)" >
        <g class="maingroup">
            <g class="x"></g>
            <g class="y"></g>
        </g>
    </svg>
    <script>
    // 全局
    const mainSvg = d3.select('.mainsvg')
    const width = mainSvg.attr('width')
    const height = mainSvg.attr('height')

    const margin = {
        "top": 50,
        "right": 600,
        "bottom": 150,
        "left": 100
    }
    const innerHeight = height - margin.top - margin.bottom
    const innerWidth = width - margin.left - margin.right
    const mainGroup = mainSvg.select('.maingroup')
    .attr('transform', `translate(${margin.left}, ${margin.top})`)

    const xScale = d3.scaleLinear()
    const yScale = d3.scaleBand()

    const lastShowArr = []
    const lastArr = []

    // 函数 
    //参数 目标数组 原数组
    function copyArr(target, data){
        for(let i = 0; i < data.length; i++){
            target[i] = data[i]
        }
    }

    // 找到当前轮淘汰的国家名
    // 参数 本轮的showArr
    // 返回数个国家数组
    function findOutCountry(nowShowArr){
        const res = []
        const now = nowShowArr.map(d => d.name)
        const last = lastShowArr.map(d => d.name)
        for(let i = 0; i < last.length; i++){
            if(!now.includes(last[i])) res.push(lastShowArr[i])
        }
        return res
    }

    // 找到当前轮的新晋国家名
    // 参数 本轮的showArr
    function findInCountry(nowShowArr){
        const res = []
        const now = nowShowArr.map(d => d.name)
        const last = lastShowArr.map(d => d.name)
        for(let i = 0; i < now.length; i++){
            if(!last.includes(now[i])) res.push(nowShowArr[i])
        }
        return res
    }

    // 找到当前轮仍在榜国家名
    // 参数 本轮的showArr
    function findRemainCountry(nowShowArr){
        const res = []
        const now = nowShowArr.map(d => d.name)
        const inC = findInCountry(nowShowArr)
        for(let i = 0; i < now.length; i++){
            if(!inC.includes(now[i])) res.push(nowShowArr[i])
        }
        return res
    }


    // 根据name属性找到对象数组中相应值
    function nameToValue(name, arr){
        for(let i = 0; i < arr.length; i++){
            const obj = arr[i]
            if(obj.name === name){
                if(obj.value === '') obj.value = 0
                return obj.value
            } 
        }
        return 0
    }

    const text = mainSvg.append('text')
    .attr('x', 300)
    .attr('y', 500)
    .attr('font-size', 300)
    .attr('fill', '#f6dcbb')

    d3.csv('gdp_data_source.csv').then(async datas => {
        // 改
        for(let i = 0; i < datas.length; i++){
            text.text(i + 1960)
            // 本年数据
            const data = datas[i]
            // 数据数组 包含本年数据 从大到小顺序
            // [{"name": .., "value": ..}...]
            const arr = []
            for(let k in data){
                if(k === "year") continue
                if(data[k]) arr.push({"name": k,"value": +data[k].valueOf()})
            }
            arr.sort((a, b) => b.value - a.value)
            console.log(arr)
            // 前十数据
            const showArr = arr.slice(0, 10)

            const outCountry = findOutCountry(showArr)
            const inCountry = findInCountry(showArr)
            const remainCountry = findRemainCountry(showArr)

            const transition = d3.transition().duration(2000).ease(d3.easeLinear)
            

            // 坐标轴
            xScale.domain([0 ,showArr[0].value]).range([0, innerWidth])
            yScale.domain(showArr.map(d => d.name)).range([0, innerHeight]).padding(0.4)
            const xAxis = d3.axisBottom(xScale)
            const yAxis = d3.axisLeft(yScale)
            const yAxisGroup = mainGroup.select('.y')
            .call(yAxis)
            yAxisGroup.selectAll('.tick').remove()




            // 新晋国家的处理

            // 获取上一年的数据
            const inCountryLastValue = []
            for(let i = 0; i < inCountry.length; i++){
                inCountryLastValue[i] = 0
            }
            for(let i = 0; i < inCountry.length; i++){
                const name  = inCountry[i].name
                for(let j = 0; j < lastArr.length; j++){
                    if(name === lastArr[j].name) {
                        if(!lastArr[j].value) lastArr[j].value = 0
                        inCountryLastValue[i] = (lastArr[j].value)
                        break
                    }
                }
            }
            // 设置矩形
            mainGroup.selectAll('.null').data(inCountry).join('rect')
            .attr('fill', 'green')
            .attr('class', 'inrect')
            .attr('id', d => 'r' + d.name)
            .attr('height', yScale.bandwidth)
            .attr('y', innerHeight)
            .attr('opacity', 0)
            .attr('width', (d, i) => xScale(inCountryLastValue[i]))
            .transition(transition)
            .attr('width', d => xScale(d.value))
            .attr('y', d => yScale(d.name))
            .attr('opacity', 1)
            .attr('fill', 'black')
            // 设置名字
            mainGroup.selectAll('.null').data(inCountry).join('text')
            .text(d => d.name)
            .attr('class', 'inname')
            .attr('id', d => 't' + d.name)
            .attr('y', innerHeight)
            .attr('x', -70)
            .attr('opacity', 0)
            .transition(transition)
            .attr('y', d => yScale(d.name) + 20)
            .attr('opacity', 1)
            // 设置数字
            const num = mainGroup.selectAll('.null').data(inCountry).join('text')
            .text((d) => {console.log(Math.floor((nameToValue(d.name, lastArr) / 100000000)) + '亿')
                return Math.floor((nameToValue(d.name, lastArr) / 100000000)) + '亿'})
            .attr('class', 'innum')
            .attr('id', d => 'n' + d.name)
            .attr('y', innerHeight)
            .attr('x', (d, i) => xScale(inCountryLastValue[i]))
            .attr('opacity', 0)
            num.transition(transition)
            .tween('text', d => {
                return e => {
                    num.text((d, i) => Math.floor(Math.floor(inCountryLastValue[i] / 100000000) + Math.floor((d.value - inCountryLastValue[i]) / 100000000) * e) + '亿')
                }
            })
            .attr('y', d => yScale(d.name) + 20)
            .attr('x', (d, i) => xScale(d.value))
            .attr('opacity', 1)

            // 淘汰国家的处理
            for(let i = 0; i < outCountry.length; i++){
                mainGroup.select('#r' + outCountry[i].name)
                .transition(transition)
                .attr('fill', 'red')
                .attr('y', innerHeight)
                .attr('opacity', 0)
                mainGroup.select('#t' + outCountry[i].name)
                .transition(transition)
                .attr('y', innerHeight)
                .attr('opacity', 0)
                const num = mainGroup.select('#n' + outCountry[i].name)
                num.transition(transition)
                .tween('text', d => {
                    return e => {
                        num.text((d, i) => Math.floor(Math.floor(inCountryLastValue[i] / 100000000) + Math.floor((d.value - inCountryLastValue[i]) / 100000000) * e) + '亿')
                    }
                })
                .attr('x', (d, i) => xScale(d.value))
                .attr('y', innerHeight)
                .attr('opacity', 0)
            }

            // 保留国家的处理
            for(let i = 0; i < remainCountry.length; i++){
                mainGroup.select('#r' + remainCountry[i].name)
                .transition(transition)
                .attr('y', yScale(remainCountry[i].name))
                .attr('width', xScale(remainCountry[i].value))
                mainGroup.select('#t' + remainCountry[i].name)
                .transition(transition)
                .attr('y', yScale(remainCountry[i].name) + 20)
                const num = mainGroup.select('#n' + remainCountry[i].name)
                num.transition(transition)
                .tween('text', d => {
                    return e => {
                        num.text(Math.floor(nameToValue(d.name, lastArr) / 100000000 + (remainCountry[i].value - nameToValue(d.name, lastArr)) / 100000000 * e) + '亿')
                    }
                })
                .attr('y', yScale(remainCountry[i].name) + 20)
                .attr('x', xScale(remainCountry[i].value))
            }
            await transition.end()
            // 删除淘汰国家
            for(let i = 0; i < outCountry.length; i++){
                mainGroup.select('#r' + outCountry[i].name).remove()
                mainGroup.select('#t' + outCountry[i].name).remove()
                mainGroup.select('#n' + outCountry[i].name).remove()
            }
            copyArr(lastShowArr, showArr)
            copyArr(lastArr, arr)
        }
        
    })
    </script>
</body>
</html>
```

### 文本分析题

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <style>
        body{
            background-color: #000;
        }
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <script >// ctrls
        const groupsArr = [
            ["鸟", "龙", "马", "雁", "蝉", "莺"],
            ["树", "草", "松", "竹", "柳", "叶", "苔", "梅", "菊"],
            ["春", "夏", "秋", "冬"],
            ["长安", "江南", "洛阳", "南山", "洞庭"],
            ["今日", "曾", "年", "昏", "明", "时", "晨", "夜",  "今朝"],
            ["丹", "朱", "黄", "绿", "青", "碧", "紫"],
            ["李白", "杜甫", "白居易", "韩愈", "刘长卿", "韦应物", "刘禹锡", "孟郊"],
            ["相公", "主人", "员外", "将军",  "故人", "郎中"]
        ];
        
        const buttonsArr = ["动物", "植物", "四季", "美景", "良辰", "色彩", "名家", "称呼"];
        
        const width = window.innerWidth;
        const height = window.innerHeight;
        
        const svg = d3.select(".mainsvg")
        .attr("width", width)
        .attr("height", height);
        
        const margin = {
            "top": 50,
            "right": 200,
            "bottom": 50,
            "left": 200
        };
        
        // inner
        const innerHeight = height - margin.top - margin.bottom;
        const innerWidth = width - margin.left - margin.right;
        
        // mainGroup
        const mainGroup  =  svg.append("g")
        .attr("class", "maingroup")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);
        
        // leftGroup
        const leftWidth = innerWidth / 2; // 调整左右相对大小修改此处
        const leftGroup = mainGroup.append("g")
        .attr("class", "leftgroup");
        
        // rightGroup
        const rightWidth = innerWidth - leftWidth;
        const rightGroup = mainGroup.append("g")
        .attr("class", "rightgroup")
        .attr("transform", `translate(${leftWidth}, 0)`);
        
        // 饼图
        const innerRadius = 150;
        const outerRadius = 200;
        const arcsPath = d3.arc()
        .innerRadius(innerRadius)
        .outerRadius(outerRadius)
        .padAngle(0.1);
        const pie = d3.pie()
        .value(d => 1);
        // linePath([[x1, y1], [x2, y2]])
        const linePath = d3.line()
        .x(d => d[0]).y(d => d[1])
        
        // 虚拟饼图
        const virArcsPath = d3.arc()
        .innerRadius(innerRadius - 10)
        .outerRadius(innerRadius - 10)
        .padAngle(0.1);
        
        // 坐标系
        const yScale = d3.scaleLinear()
        const xScale = d3.scaleBand()
        
        
        // init
        const arcBackGround = leftGroup.append("circle")
        .attr("cx", leftWidth / 2)
        .attr("cy", innerHeight / 2)
        .attr("r", innerRadius + 20)
        .attr("fill", "#419eb5")
        
        const arcs = leftGroup.selectAll(".null")
        .data(pie(buttonsArr))
        .join("path")
        .attr("class", "arc")
        .attr("d", arcsPath)
        .attr("transform", `translate(${leftWidth / 2}, ${innerHeight / 2})`)
        .attr("fill", "#354f66")
        .attr('cursor', 'pointer');
        
        const virArcs = leftGroup.selectAll(".null")
        .data(pie(buttonsArr))
        .join("path")
        .attr("class", "virarc")
        .attr("d", virArcsPath)
        .attr("transform", `translate(${leftWidth / 2}, ${innerHeight / 2})`)
        .attr("fill", "#ffffff00");
        
        let sourceAngle = (pie(buttonsArr)[0].endAngle + pie(buttonsArr)[0].startAngle) / 2;
        
        const arcPoint = leftGroup.append("path")
        .attr("d", linePath([[leftWidth / 2, innerHeight / 2], [virArcsPath.centroid(pie(buttonsArr)[0])[0] + leftWidth / 2, virArcsPath.centroid(pie(buttonsArr)[0])[1] + innerHeight / 2]]))
        .attr("stroke-width", 10)
        .attr("stroke", "#f6f3cf");
        
        const arcPointCicle = leftGroup.append("circle")
        .attr("cx", leftWidth / 2)
        .attr("cy", innerHeight / 2)
        .attr("r", 8)
        .attr("fill", "#000");
        
        const arcTexts = leftGroup.selectAll(".null")
        .data(pie(buttonsArr))
        .join("text")
        .attr("class", "arctext")
        .text(d => d.data)
        .attr("transform", d =>
        `translate(${arcsPath.centroid(d)[0] + leftWidth / 2 - 15}, ${arcsPath.centroid(d)[1] + innerHeight / 2})`)
        .attr("fill", "#fcf5cd")
        .attr('cursor', 'pointer');
        
        let xWidth = 600;
        xScale.domain(groupsArr[0])
        .range([0, xWidth])
        .padding(0.5);
        
        d3.csv("./唐诗 top1000.csv").then(data => {
            // 处理data为  name-num的性质
            const tmp = {};
            for(let i = 0; i < data.length; i++){
                tmp[data[i].name] = data[i].num
            }
        
            data = tmp;
            const yHeight = 600;
            yScale.domain([0, d3.max(groupsArr[0].map(d => +data[d]))])
            .range([0, yHeight]);
        
            let xAxis = d3.axisBottom(xScale);
            let yAxis = d3.axisTop(yScale);
        
            let oMarginLeft = (rightWidth - xWidth) / 2;
        
            const xAxisGroup = rightGroup.append('g')
            .call(xAxis)
            .attr('transform', `translate(${oMarginLeft}, ${yHeight})`);
        
        
            const yAxisGroup = rightGroup.append('g')
            .call(yAxis)
            .attr('transform', `translate(${oMarginLeft}, ${yHeight}),rotate(-90)`);
            
            const rects = rightGroup.selectAll('.null')
            .data(groupsArr[0])
            .join('rect')
            .attr("class", (d, i) => "rect" + i)
            .attr("x",d => xScale(d) + oMarginLeft)
            .attr("y",d => yHeight - yScale(data[d]))
            .attr("height", d => yScale(data[d]))
            .attr("width", xScale.bandwidth)
            .attr("fill", "#419eb5");
        
            const dLength = xScale.bandwidth();
        
            let xLastWidth = xWidth;
            let oLastMarginLeft = oMarginLeft;
            let lastI = 0;
        
            xAxisGroup.selectAll("text")
            .attr('font-size', '16px');
        
            rightGroup.selectAll("text")
            .attr("fill", "#fcf5cd")
        
            xAxisGroup.select('path')
            .attr("stroke", "#419eb5")
            yAxisGroup.select('path')
            .attr("stroke", "#419eb5")
            yAxisGroup.selectAll('line')
            .attr("stroke", "#419eb5")
            // listen
            svg.selectAll('.arc').on('click',async (event, d) => {
                
                const i = d.index;
                
                const transition = d3.transition()
                .duration(500).ease(d3.easeLinear);
                const targetAngle = (d.endAngle + d.startAngle) / 2;
        
                xWidth = (2 * groupsArr[i].length + 1) * dLength;
                oMarginLeft = (rightWidth - xWidth) / 2;
        
                // 把本次数组分为两部分 {source:4, change:-2}
                
                const change = {"source": d3.min([groupsArr[lastI].length, groupsArr[i].length]), "change": groupsArr[i].length - groupsArr[lastI].length};
        
        
                // point
                arcPoint.transition(transition)
                .tween("d", d => {
                    
                    return e => {
                        const nowAngle = (targetAngle - sourceAngle) * e + sourceAngle;
                        arcPoint.attr("d", linePath([[leftWidth / 2, innerHeight / 2], [virArcsPath.centroid({"startAngle": nowAngle, "endAngle":nowAngle})[0] + leftWidth / 2, virArcsPath.centroid({"startAngle": nowAngle, "endAngle":nowAngle})[1] + innerHeight / 2]]))
                }})
        
                // axis
                yScale.domain([0, d3.max(groupsArr[i].map(d => +data[d]))])
                .range([0, yHeight]);
        
                yAxis = d3.axisTop(yScale);
        
                yAxisGroup.call(yAxis)
                .transition(transition)
                .attr('transform', `translate(${oMarginLeft}, ${yHeight}),rotate(-90)`)
        
                // 新增部分
                if(change.change > 0){
                    var add = rightGroup.selectAll(".null")
                    .data(groupsArr[i].slice(change.source))
                    .join("rect")
                    .attr("class", (d,i) => "rect" + (change.source + i))
                    .attr("y",yHeight)
                    .attr("fill", "#419eb5")
                    .attr("width", dLength);
                    add.transition(transition)
                    .attr("y",d => yHeight - yScale(data[d]))
                    .attr("height", d => yScale(data[d]))
                }
        
               
        
                xAxisGroup.transition(transition)
                .tween("call", d => {
                    return e => {
                        xScale.domain(groupsArr[i])
                        .range([0, (xWidth - xLastWidth) * e + xLastWidth])
                        .padding(0.5);
        
                        xAxis = d3.axisBottom(xScale);
        
                        xAxisGroup.call(xAxis)
                        .attr('transform', `translate(${(oMarginLeft - oLastMarginLeft) * e + oLastMarginLeft} , ${yHeight})`);
        
                        for(let j = 0; j < change.source; j++){
                            rightGroup.select(".rect" + j)
                            .attr("x", xScale(groupsArr[i][j]) + (oMarginLeft - oLastMarginLeft) * e + oLastMarginLeft)
                        }
                        if(change.change > 0) add.attr("x", (d, j) => xScale(groupsArr[i][change.source + j]) +(oMarginLeft - oLastMarginLeft) * e + oLastMarginLeft);
                        xAxisGroup.selectAll("text")
                        .attr('font-size', '16px');
                        rightGroup.selectAll("text")
                        .attr("fill", "#fcf5cd")
                        xAxisGroup.select('path')
                        .attr("stroke", "#419eb5")
                        yAxisGroup.select('path')
                        .attr("stroke", "#419eb5")
                        yAxisGroup.selectAll('line')
                        .attr("stroke", "#419eb5")
                    }
                })
        
                // rects
                // 没有新增减少的部分
                for(let j = 0; j < change.source; j++){
                    rightGroup.select(".rect" + j)
                    .transition(transition)
                    .attr("height", yScale(data[groupsArr[i][j]]))
                    .attr("y", yHeight - yScale(data[groupsArr[i][j]]))
                    
                }
        
                // 删除部分
                if(change.change < 0){
                    for(let j = 0; j < 0 - change.change; j++){
                        rightGroup.select(".rect" + (change.source + j))
                        .transition(transition)
                        .attr("height", 0)
                        .attr("y", yHeight)
                        .attr("fill", "#419eb500")
                    }
                }
                
        
                await transition.end();
                sourceAngle = targetAngle;
                xLastWidth = xWidth;
                oLastMarginLeft = oMarginLeft;
                lastI = i;
                if(change.change < 0){
                    for(let j = 0; j < 0 - change.change; j++){
                        rightGroup.select(".rect" + (change.source + j))
                        .remove();
                    }
                }
            });
        })
    </script>
</body>
</html>
```

## 陆 堆叠

---

### 6.1 概览

**接口**

* `stack`接口, 把数据堆叠起来, 映射到画图空间
* `let stack = d3.stack()` 返回一个堆叠函数, 用于将输入(对象)数据堆叠
* 对数据堆叠`let stackedData = stack(nativeData)`
* 返回结果`stackedData`以属性为单位, 将数据分堆 **三重数组**
* 每一**列为一个柱状图从下到上的坐标**

*堆叠前*
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_15.jpg)


*堆叠后*
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_17.jpg)

*堆叠效果*
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_16.jpg)


### 6.2 堆叠数据中的特定属性

* 通过`d3.stack()`返回的`stack`函数中的`keys()`函数
* `stack.keys(keysArr)`
* 传入参数为包含要堆叠属性的数据 `e.g. ["apples", "bananas"]`

### 6.3 堆叠数据中的顺序

*默认跟随keysArr中的顺序*

**语法**

* `stack.orders(顺序函数)`
* e.g. `d3.stackOrderNone` 默认, 随Key的顺序
* e.g. `d3.stackOrderAscending` 按照堆叠值升序


*顺序函数*
https://github.com/d3/d3-shape/blob/v2.1.0/README.md#stack-orders

### 6.4 data-join连续调用

* `selection.data(data)` 传入的是数组, 实则把其中的**各个元素取出**进行图元绑定
* `selection.data(data).attr('fill', d -> color(d.key)).data(d -> d)` 前一次`data`拆分了最外数组, 绑定其中的各个小数组, 第二次`data`中的`d`和前面`attr`中的`d`含义相同, 指的是**绑定的各个小数组**, 因此**第二次拆分的是各个小数组**, 绑定**小数组中的元素**
* data的连续链式调用起到了*拆分多重数组的作用*

*data-join连续调用实例*
![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_18.jpg)


### 6.5 主题河流的实现

* 本质为随x横坐标变化, 上y0和下y1分别插值, 所以**需要以数组形式给出x, y0, y1**

**d3.area**

* `let path = d3.area()` 这个path函数输入为数组, 输出为d函数
* `path.x(d => xScale(d.data.ym))`这里的d即为日后传给path的数组的一个数据
* `path.y1(..)`上界
* `path.y0`下界
* `path.curve()` 插值方式

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_19.jpg)

### 6.6 d3.bin数据拆分

**语法**

* `let histogram = d3.bin();` 返回函数用于**将输入数据分区存放** *根据数据的某一些特征进行划分*
* `d3.bin().value(d => d.occur);`对于每个对象参考其`occur`属性决定划分到哪一堆
* `d3.bin().value().threshold([x1,x2,x3,..xn])`一些阈值来分堆
* 基于比例尺分堆`.threshold(xScale.ticks(20))` 在比例尺的范围内进行20个隔断来分堆 `(scaleLinear)`


### gdp堆叠图
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <script src="./d3-geo-projection.min.js"></script>
    <style>
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <script>
        // 闭
function getRandomInt(start, end) {
    return Math.floor(start + (end - start + 1) * Math.random());
}
// 随机颜色
function randomColor(){
    const colorArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
    let res = "#";
    for(let i = 0; i < 6; i++){
        res += colorArr[getRandomInt(0, 15)];
    }
    return res;
}

// 全局

const width = window.innerWidth;
const height = window.innerHeight;

const mainSvg = d3.select('.mainsvg')
.attr('width', width)
.attr('height', height);

const margin = {
    "top": 100,
    "right": 100,
    "bottom": 100,
    "left": 100
};

const mainGroup = mainSvg.append('g')
.attr('transform', `translate(${margin.left}, ${margin.top})`);

const innerHeight = height - margin.top - margin.bottom;
const innerWidth = width - margin.left - margin.right;

// 读取数据
d3.csv('gdp_data_source.csv').then(data => {
    // text
    let tmp = [];
    for(k in data[57]){
        tmp.push({"name": k, "num": data[57][k]});
    }
    tmp.sort((d1, d2) => d2.num - d1.num);
    const text = tmp.map(d => d.name).slice(0, 15);
;
    const keys = []
    for(k in data[0]){
        if(k !== "year") keys.push(k);
    }
    
    // stack & sort
    let stackedData = d3.stack()
    .keys(keys)
    .order(d3.stackOrderAscending)([data[0]]);

    let data2017 = d3.stack()
    .keys(keys)
    .order(d3.stackOrderAscending)([data[57]])
    
    for(let i = 1; i < data.length; i++){
        const  tmpData = d3.stack()
        .keys(keys)
        .order(d3.stackOrderAscending)([data[i]]);
        // 合并到stackedData
        for(let j = 0; j < stackedData.length; j++){
            stackedData[j].push(tmpData[j][0]);
        }
    }
    

    // axis
    const textwidth = 150; // 文字预留宽度
    const xScale = d3.scaleLinear()
    .domain([1960, 2017]).range([0, innerWidth - textwidth]);
    const yScale = d3.scaleLinear()
    .domain([0, data[57]["美国"] * 3/ 1e12 + 21]).range([0, innerHeight]);
    const yAxis = d3.axisTop(yScale);
    const xAxis = d3.axisBottom(xScale);
    const yAxisGroup = mainGroup.append('g')
    .call(yAxis)
    .attr('transform', `translate(0, ${innerHeight}),rotate(-90)`);

    yAxisGroup.append("text")
    .text("万亿(美元)")
    .attr("transform", `translate(${innerHeight}, ${50}), rotate(90)`)
    .attr("fill", "#000")
    .attr("font-size", 18)

    const xAxisGroup = mainGroup.append('g')
    .call(xAxis)
    .attr('transform', `translate(0, ${innerHeight})`)

   // area
    const path = d3.area()
    .x(d => xScale(d.data.year))
    .y1(d =>innerHeight - yScale(d[1] / 1e12))
    .y0(d =>innerHeight - yScale(d[0] / 1e12))
    .curve(d3.curveCardinal.tension(0.5))

    const areas = mainGroup.selectAll('.null')
    .data(stackedData)
    .join("path")
    .attr("class", "river")
    .attr('d', path)
    .attr('fill', (d, i) => d3.schemeSet3[i % 12]);


    // 标注
    let tmpObj = {};
    for(let i = 0; i < data2017.length; i++){
        tmpObj[data2017[i].key] = (data2017[i][0][0] + data2017[i][0][1]) / 2 / 1e12;
    }
    const data2017Obj = tmpObj;

    mainGroup.selectAll(".null")
    .data(text)
    .join("text")
    .attr("class", "text")
    .attr("transform",d => `translate(${innerWidth - textwidth}, ${innerHeight - yScale(data2017Obj[d])})`)
    .text(d => d)
    .attr("id", d => d)
    .attr("font-size", 14)
    let timer = null;

    // 交互
    d3.selectAll(".river").on("mouseover", (event, d)=>{
        if(timer !== null){
            clearTimeout(timer);
        }
        d3.selectAll(".river")
        .attr("opacity", 0.4)
        .attr("fill", "#bbbbbb");
        d3.selectAll(".text")
        .attr("opacity", 0);
        d3.select("#" + d.key)
        .attr("opacity", 1);
        d3.select(event.currentTarget)
        .attr("opacity", 1)
        .attr("fill", "#ffff00");
    });
    d3.selectAll(".river").on("mouseout", (event, d)=>{
        // 消抖 如果触发mouseout的回调函数后，短时间内又触发了over的回调函数, 则取消out的执行
        // 只有一段时间内没有触发over， 才能执行out
        timer = null;
        timer = setTimeout(()=>{
            d3.selectAll(".river")
            .attr("opacity", 1)
            .attr("fill", (d, i) => d3.schemeSet3[i % 12]);
            d3.selectAll(".text")
            .attr("opacity", 1);
        },300)
    });

});
    </script>
</body>
</html>
```

### 水浒人物出场统计

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <script>
        // 基本尺寸
        const width = window.innerWidth;
        const height = window.innerHeight;

        const mainSvg = d3.select('.mainsvg')
        .attr('width', width)
        .attr('height', height);

        const margin = {
            "top": 50,
            "right": 100,
            "bottom": 100,
            "left": 100
        };

        const mainGroup = mainSvg.append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);

        const innerHeight = height - margin.top - margin.bottom;
        const innerWidth = width - margin.left - margin.right;

        const stackWidth = 1370;
        const stackHeight = 600;

        const stackGroup = mainGroup.append("g")
        const timeGroup = mainGroup.append("g")
        .attr("transform", `translate(0, ${stackHeight + 30})`);
        const personGroup = mainGroup.append("g")
        .attr("transform", `translate(${stackWidth + 20}, 0)`);

        d3.csv("水浒各章节人物出场次数.csv").then(data => {
            
            // persons
            const persons = [];
            for(let k in data[0]){
                if(k === "chapter") continue;
                persons.push(k);
            }
            
            // color
            const num2Color = d3.scaleSequential()
            .domain([0, persons.length])
            .interpolator(d3.interpolateRgbBasis(d3.schemePaired.slice(0, 8)));
            const tmp  = [];
            for(let i = 0; i < 7; i++){
                for(let j = 0;j < 19; j++){
                    tmp.push(persons[i + j * 7]);
                }
            }
            const person2Num = d3.scaleBand()
            .domain(tmp)
            .range([0, persons.length]);
            const color = person => num2Color(person2Num(person));
            
            // stack
            const stackedData = d3.stack()
            .keys(persons)(data);

            // personrect
            personGroup.selectAll(".null")
            .data(stackedData)
            .join("rect")
            .attr("class", "personrect")
            .attr("id",d => "rect" + d.key)
            .attr("width", 20)
            .attr("height", 20)
            .attr("cursor", "pointer")
            .attr("transform", (d, i) => `translate(${i % 7 * 110  + 18}, ${(i - i % 7) / 7 * 30 + 50})`);

            // persontext
            personGroup.selectAll(".null")
            .data(stackedData)
            .join("text")
            .attr("class", "persontext")
            .attr("id",d => "text" + d.key)
            .attr("width", 40)
            .attr("height", 20)
            .attr("fill", "#000")
            .attr("cursor", "pointer")
            .text(d => d.key)
            .attr("transform", (d, i) => `translate(${i % 7 * 110 + 40}, ${(i - i % 7) / 7 * 30 + 15 + 50})`);

            
            // init
            // init personrect
            personGroup.selectAll(".personrect")
            .attr("fill", (d, i) => i > 9 ? "gray" : color(d.key))
            .attr("opacity", (d, i) => i > 9 ? 0.4 : 1);

            // init persontext
            personGroup.selectAll(".persontext")
            .attr("opacity", (d, i) => i > 9 ? 0.4 : 1);

            // init stackAxis
            let chooseTime = [0, 120];
            let choosePersons = persons.slice(0, 10)
            let chooseStackedData = d3.stack()
            .keys(choosePersons)(data);
            
            const stackXScale = d3.scaleLinear()
            .domain(chooseTime)
            .range([0, stackWidth]);
            const stackYScale = d3.scaleLinear()
            .domain([0, 1.2 * d3.max(chooseStackedData, d => d3.max(d, d1 => d1[1]))]).range([0, stackHeight]);

            let stackXAxis = d3.axisBottom(stackXScale)
            .ticks(20);
            let stackYAxis = d3.axisTop(stackYScale);

            const stackXAxisGroup = stackGroup.append("g")
            .call(stackXAxis)
            .attr("transform", `translate(0, ${stackHeight})`);
            const stackYAxisGroup = stackGroup.append("g")
            .call(stackYAxis)
            .attr("transform", `translate(0, ${stackHeight + 1}),rotate(-90)`);

            stackYAxisGroup.selectAll("line")
            .attr("y1", stackWidth)

            stackYAxisGroup.append("text")
            .text("出场次数")
            .attr("font-size", 20)
            .attr("transform", `translate(${stackHeight - 10}, 45), rotate(90)`)
            .attr("fill", "#000")
            stackXAxisGroup.append("text")
            .text("回")
            .attr("font-size", 20)
            .attr("transform", `translate(${stackWidth + 10}, -5), rotate(90)`)
            .attr("fill", "#000")
            stackXAxisGroup.append("text")
            .text("选中人物出场次数层叠分布")
            .attr("font-size", 30)
            .attr("font-weight", 700)
            .attr("transform", `translate(${stackWidth / 2 - 10}, ${-stackHeight}) `)
            .attr("fill", "#000")

            // init area
            let areaPath = d3.area()
            .x(d => stackXScale(+d.data.chapter))
            .y0(d => stackHeight - stackYScale(d[0]))
            .y1(d => stackHeight - stackYScale(d[1]))
            .curve(d3.curveCardinal.tension(0.5));
            const areaSvg = stackGroup.append("svg")
            .attr("width", stackWidth)
            .attr("height", stackHeight);
            const area = areaSvg.selectAll(".null")
            .data(chooseStackedData)
            .join("path")
            .attr("class", "stackarea")
            .attr("d", areaPath)
            .attr("fill", d => color(d.key));

            // init timeaxis
            let allPersons = []
            for(let i = 0; i < 120; i++){
                cnt = 0
                for(let k in data[i]){
                    if(k === "chapter") continue;
                    for(let j = 0;j < choosePersons.length; j++){
                        if(choosePersons[j] === k) cnt += +data[i][k];
                    }
                }
                allPersons.push(cnt)
            }

            const timeWidth = innerWidth;
            const timeHeight = innerHeight - stackHeight - 20;
            const timeXScale = d3.scaleLinear()
            .domain([0, 120])
            .range([0, timeWidth]);
            const timeYScale = d3.scaleLinear()
            .domain([0, d3.max(allPersons)]).range([0, timeHeight]);

            const timeXAxis = d3.axisBottom(timeXScale)
            .ticks(60);
            let timeYAxis = d3.axisTop(timeYScale)
            .ticks(6);

            const timeXAxisGroup = timeGroup.append("g")
            .call(timeXAxis)
            .attr("transform", `translate(0, ${timeHeight})`);
            const timeYAxisGroup = timeGroup.append("g")
            .call(timeYAxis)
            .attr("transform", `translate(0, ${timeHeight}),rotate(-90)`);

            timeYAxisGroup.append("text")
            .text("出场次数")
            .attr("font-size", 20)
            .attr("transform", `translate(${timeHeight - 10}, 45), rotate(90)`)
            .attr("fill", "#000")
            timeXAxisGroup.append("text")
            .text("回")
            .attr("font-size", 20)
            .attr("transform", `translate(${timeWidth - 10}, -15)`)
            .attr("fill", "#000")
            timeXAxisGroup.append("text")
            .text("选中人物总出场次数分布")
            .attr("font-size", 30)
            .attr("font-weight", 700)
            .attr("transform", `translate(${timeWidth / 2 - 10}, 50) `)
            .attr("fill", "#000")
            
            // init time line
            let timeLinePath = d3.line()
            .x((d,i) => timeXScale(i + 1))
            .y(d => timeHeight - timeYScale(d));

            const timeLine = timeGroup.append("path")
            .datum(allPersons)
            .attr("d", timeLinePath)
            .attr("fill", "none")
            .attr("stroke", "#0769b4")
            
            var timer1 = null;
            // areasvg 堆叠图悬浮鼠标交互
            areaSvg.on("mousemove", (event, d) => {
                // 消抖
                if(timer1 !== null){
                    clearTimeout(timer1);
                }
                timer1 = setTimeout(()=>{
                    const areaMoveScale  = d3.scaleLinear()
                    .domain([margin.left, margin.left + stackWidth])
                    .range(chooseTime);
                    // title
                    const titleArr = [
                        "一",
                        "二",
                        "三",
                        "四",
                        "五",
                        "六",
                        "七",
                        "八",
                        "九",
                        "十",
                        "十一",
                        "十二",
                        "十三",
                        "十四",
                        "十五",
                        "十六",
                        "十七",
                        "十八",
                        "十九",
                        "二十",
                        "二十一",
                        "二十二",
                        "二十三",
                        "二十四",
                        "二十五",
                        "二十六",
                        "二十七",
                        "二十八",
                        "二十九",
                        "三十",
                        "三十一",
                        "三十二",
                        "三十三",
                        "三十四",
                        "三十五",
                        "三十六",
                        "三十七",
                        "三十八",
                        "三十九",
                        "四十",
                        "四十一",
                        "四十二",
                        "四十三",
                        "四十四",
                        "四十五",
                        "四十六",
                        "四十七",
                        "四十八",
                        "四十九",
                        "五十",
                        "五十一",
                        "五十二",
                        "五十三",
                        "五十四",
                        "五十五",
                        "五十六",
                        "五十七",
                        "五十八",
                        "五十九",
                        "六十",
                        "六十一",
                        "六十二",
                        "六十三",
                        "六十四",
                        "六十五",
                        "六十六",
                        "六十七",
                        "六十八",
                        "六十九",
                        "七十",
                        "七十一",
                        "七十二",
                        "七十三",
                        "七十四",
                        "七十五",
                        "七十六",
                        "七十七",
                        "七十八",
                        "七十九",
                        "八十",
                        "八十一",
                        "八十二",
                        "八十三",
                        "八十四",
                        "八十五",
                        "八十六",
                        "八十七",
                        "八十八",
                        "八十九",
                        "九十",
                        "九十一",
                        "九十二",
                        "九十三",
                        "九十四",
                        "九十五",
                        "九十六",
                        "九十七",
                        "九十八",
                        "九十九",
                        "一百",
                        "一百零一",
                        "一百零二",
                        "一百零三",
                        "一百零四",
                        "一百零五",
                        "一百零六",
                        "一百零七",
                        "一百零八",
                        "一百零九",
                        "一百一十",
                        "一百一十一",
                        "一百一十二",
                        "一百一十三",
                        "一百一十四",
                        "一百一十五",
                        "一百一十六",
                        "一百一十七",
                        "一百一十八",
                        "一百一十九",
                        "一百二十",
                    ]
                    const index = Math.round(areaMoveScale(event.clientX)) - 1;
                    personGroup.selectAll(".title").remove();
                    personGroup.selectAll(".personnum").remove();
                    const titleText = personGroup.append("text")
                    .attr("class", "title")
                    .text("第" + titleArr[index] + "回")
                    .attr("font-size", 30)
                    .attr("transform", "translate(220, 20)")
                    const timesArr = []
                    for(k in data[index]){
                        if(k === "chapter") continue;
                        timesArr.push({
                            "name": k,
                            "value":data[index][k]
                        });
                    }
                    // 人物出场次数显示
                    personGroup.selectAll(".null")
                    .data(timesArr)
                    .join("text")
                    .text(d => d.value)
                    .attr("class", "personnum")
                    .attr("id",d => "num" + d.name)
                    .attr("height", 20)
                    .attr("fill", "#000")
                    .attr("transform", (d, i) => `translate(${i % 7 * 110 - 5}, ${(i - i % 7) / 7 * 30 + 15 + 50})`)
                    .attr("opacity", 0)
                    for(let i = 0; i < choosePersons.length; i++){
                        personGroup.select("#num" + choosePersons[i])
                        .attr("opacity", 1)
                    }
                },100)
            })
            // 鼠标移出堆叠图
            var timer2 = null;
            areaSvg.on("mouseout", (event, d) => {
                console.log(1)
                if(timer2 !== null){
                    clearTimeout(timer2);
                }
                timer1 = setTimeout(()=>{
                    personGroup.selectAll(".title").remove();
                    personGroup.selectAll(".personnum").remove();
                }, 100)
                
            })
            var timer = null;
            //  brush时间轴交互
            const brush = d3.brushX().extent([[0, 0], [timeWidth,timeHeight]]).on("brush", d =>{
                // 消抖
                if(timer !== null){
                    clearTimeout(timer);
                }
                timer = setTimeout(()=>{
                    const brushScale = d3.scaleLinear()
                    .domain([0, timeWidth])
                    .range([0, 120]);
                    chooseTime = [Math.ceil(brushScale(d.selection[0])), Math.floor(brushScale(d.selection[1]))];
                    console.log(chooseTime)
                    // 重新堆叠
                    chooseStackedData = d3.stack()
                    .keys(choosePersons)(data);
                    // 绘制坐标轴
                    stackXScale.domain(chooseTime)
                    .range([0, stackWidth]);
                    stackYScale.domain([0, 1.2 * d3.max(chooseStackedData, d => d3.max(d, d1 => d1[1]))]).range([0, stackHeight]);

                    stackXAxis = d3.axisBottom(stackXScale)
                    .ticks(20);
                    stackYAxis = d3.axisTop(stackYScale);

                    stackXAxisGroup.call(stackXAxis);
                    
                    stackYAxisGroup.call(stackYAxis);
                    // 绘制 堆叠图
                    areaPath = d3.area()
                    .x(d => stackXScale(+d.data.chapter))
                    .y0(d => stackHeight - stackYScale(d[0]))
                    .y1(d => stackHeight - stackYScale(d[1]))
                    .curve(d3.curveCardinal.tension(0.5));
                    areaSvg.selectAll(".stackarea").remove();
                    
                    const area = areaSvg.selectAll(".null")
                    .data(chooseStackedData)
                    .join("path")
                    .attr("class", "stackarea")
                    .attr("d", areaPath)
                    .attr("fill", d => color(d.key));

                },100)
                
            })
            timeGroup.call(brush);


            // 点击删除人物交互
            function personClick(event, d){
                
                // 按钮的显示
                let flag = 1;
                for(let i = 0 ;i < chooseStackedData.length; i++){
                    if(chooseStackedData[i].key === d.key){
                        flag = 0;
                        choosePersons.splice(i, 1);
                        break;
                    }
                }
                if(flag){
                    choosePersons.push(d.key);
                    personGroup.select("#rect" + d.key)
                    .attr("fill", color(d.key))
                    .attr("opacity", 1);
                    personGroup.select("#text" + d.key)
                    .attr("opacity", 1);
                }
                else{
                    personGroup.select("#rect" + d.key)
                    .attr("fill", "gray")
                    .attr("opacity", 0.4);
                    personGroup.select("#text" + d.key)
                    .attr("opacity", 0.4);
                }
                // 重新堆叠
                chooseStackedData = d3.stack()
                .keys(choosePersons)(data);
                // 绘制坐标轴
                stackYScale.domain([0, 1.2 * d3.max(chooseStackedData, d => d3.max(d, d1 => d1[1]))]).range([0, stackHeight]);
                stackYAxis = d3.axisTop(stackYScale);
                stackYAxisGroup.call(stackYAxis);

                stackYAxisGroup.selectAll("line")
                .attr("y1", stackWidth)


                // 绘制堆叠图
                areaSvg.selectAll(".stackarea").remove();
                const area = areaSvg.selectAll(".null")
                .data(chooseStackedData)
                .join("path")
                .attr("class", "stackarea")
                .attr("d", areaPath)
                .attr("fill", d => color(d.key));

                // 绘制时间轴
                let allPersons = []
                for(let i = 0; i < 120; i++){
                    cnt = 0
                    for(let k in data[i]){
                        if(k === "chapter") continue;
                        for(let j = 0;j < choosePersons.length; j++){
                            if(choosePersons[j] === k) cnt += +data[i][k];
                        }
                    }
                    allPersons.push(cnt)
                }
                

                timeYScale.domain([0, d3.max(allPersons)]).range([0, timeHeight]);

                let timeYAxis = d3.axisTop(timeYScale)
                .ticks(6);


                timeYAxisGroup.call(timeYAxis)
                .attr("transform", `translate(0, ${timeHeight}),rotate(-90)`);

                
                let timeLinePath = d3.line()
                .x((d,i) => timeXScale(i + 1))
                .y(d => timeHeight - timeYScale(d));

                timeLine.datum(allPersons)
                .attr("d", timeLinePath)
                .attr("fill", "none")
                .attr("stroke", "#0769b4")
            }

            
            personGroup.selectAll(".personrect")
            .on("click", personClick)
            personGroup.selectAll(".persontext")
            .on("click", personClick)
        });
    </script>
</body>
</html>
```


### 哈夫曼树可视化
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <script>
        
let width = window.innerWidth;
let height = window.innerHeight;

const mainSvg = d3.select('.mainsvg')
.attr('width', width)
.attr('height', height);

const margin = {
    "top": 50,
    "right": 0,
    "bottom": 250,
    "left": 100
}
height = height - margin.top - margin.bottom
width = width - margin.left - margin.right
const mainGroup = mainSvg.append("g")
.attr("class", 'maingroup')
.attr('transform', `translate(${margin.left}, ${margin.top})`)

const circleWidth = 10;

// 生成节点数组
let nodeIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
function creatLine(height){
    if(height === 11) return null;
    const leftChild = creatLine(height + 1);
    const rightChild = creatLine(height + 1);
    const bandWidth = height > 0 ? width / (2 ** (height - 1) + 1) : width / 2;
    const nodeX = height > 0 ? nodeIndex[height] % 2 === 0 ? parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth - 45: 
    parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth + 45 : bandWidth;
    const nodeY = 70 * height + 50;
    // node 
    mainGroup.append('circle')
    .attr('id', 'o' + (nodeIndex[height] + 2 ** height - 1))
    .attr('cy', nodeY)
    .attr('cx', nodeX)
    .attr("opacity", 0)
    .attr('r', circleWidth);
    //line
    const path = d3.line()
    .x(d => d[0])
    .y(d => d[1]);
    const me = {
        "index" : (nodeIndex[height] + 2 ** height - 1),
        "leftChild" : leftChild,
        "rightChild" : rightChild
    };
    if(me.leftChild !== null){
        const leftChildX = +mainGroup.select('#o' + leftChild.index).attr("cx");
        const leftChildY = +mainGroup.select('#o' + leftChild.index).attr("cy");
        mainGroup.append("path")
        .attr("id", "l" + me.index + "a" + leftChild.index)
        .attr("opacity", 0)
        .attr("d", path([[nodeX, nodeY], [leftChildX, leftChildY] ]))
        .attr('stroke', '#fff');
    }
    if(me.rightChild !== null){
        const rightChildX = +mainGroup.select('#o' + rightChild.index).attr("cx");
        const rightChildY = +mainGroup.select('#o' + rightChild.index).attr("cy");
        mainGroup.append("path")
        .attr("id", "l" + me.index + "a" + rightChild.index)
        .attr("opacity", 0)
        .attr("d", path([[nodeX, nodeY], [rightChildX, rightChildY]]))
        .attr('stroke', '#fff');
    }
    nodeIndex[height]++;
    if(height === 0){
        nodeIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        creatNode(0);
    } 
    return me;
}
function creatNode(height){
    if(height === 11) return null;
    const leftChild = creatNode(height + 1);
    const rightChild = creatNode(height + 1);
    const bandWidth = height > 0 ? width / (2 ** (height - 1) + 1) : width / 2;
    const nodeX = height > 0 ? nodeIndex[height] % 2 === 0 ? parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth - 45: 
    parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth + 45 : bandWidth;
    const nodeY = 70 * height + 50;
    //line
    const path = d3.line()
    .x(d => d[0])
    .y(d => d[1]);
    const me = {
        "index" : (nodeIndex[height] + 2 ** height - 1),
        "leftChild" : leftChild,
        "rightChild" : rightChild
    };
    // node 
    mainGroup.append('circle')
    .attr('id', 'c' + (nodeIndex[height] + 2 ** height - 1))
    .attr('cy', nodeY)
    .attr('cx', nodeX)
    .attr("opacity", 0)
    .attr('r', circleWidth);
    // text
    mainGroup.append('text')
    .attr('id', 't' + (nodeIndex[height] + 2 ** height - 1))
    .attr('fill', '#000')
    .attr('y',70 * height + 55)
    .attr('x',height > 0 ? nodeIndex[height] % 2 === 0 ? parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth - 50: 
    parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth + 40 : bandWidth - 5);
    // weight text
    mainGroup.append('text')
    .attr('id', 'tw' + (nodeIndex[height] + 2 ** height - 1))
    .attr('fill', '#000')
    .attr('y',70 * height + 40)
    .attr('font-size', 12)
    .attr('fill', 'rgb(224,16,16)')
    .attr('x',height > 0 ? nodeIndex[height] % 2 === 0 ? parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth - 50: 
    parseInt(nodeIndex[height] / 2) * bandWidth + bandWidth + 40 : bandWidth - 5);


    // line linetext
    if(me.leftChild !== null){ 
        mainGroup.append("text")
        .attr("id", "lt" + me.index + "a" + leftChild.index)
        .attr("opacity", 0)
        .attr('fill', '#000')
        .text("1")
        .attr("x", (+(mainGroup.select('#c' + me.index).attr('cx')) + +(mainGroup.select('#c' + leftChild.index).attr('cx'))) / 2)
        .attr("y", (+(mainGroup.select('#c' + me.index).attr('cy')) + +(mainGroup.select('#c' + leftChild.index).attr('cy'))) / 2);
    }
    if(me.rightChild !== null){ 
        mainGroup.append("text")
        .attr("id", "lt" + me.index + "a" + rightChild.index)
        .attr("opacity", 0)
        .attr('fill', '#000')
        .text("0")
        .attr("x", (+(mainGroup.select('#c' + me.index).attr('cx')) + +(mainGroup.select('#c' + rightChild.index).attr('cx'))) / 2)
        .attr("y", (+(mainGroup.select('#c' + me.index).attr('cy')) + +(mainGroup.select('#c' + rightChild.index).attr('cy'))) / 2);
    }
    nodeIndex[height]++;
    return me;
}

const root = creatLine(0);

// 通过 "A10101" , [1, 0.2, 0.3, 0.1, 0.05, 0.001] 点亮相应节点和通路
function light(str, arr){
    const ch = str[0];
    let point = root;
    mainGroup.select('#c' + 0)
    .attr("opacity", 1)
    .attr('fill', '#5897cf');
    for(let i = 1; i < str.length; i++){
        // 显示权重
        mainGroup.select('#tw' + point.index)
        .text(arr[i - 1])
        if(str[i] === "1"){
            // 左子节点变亮
            mainGroup.select('#c' + point.leftChild.index)
            .attr("opacity", 1)
            .attr('fill', '#5897cf');
            // 左通路
            mainGroup.select('#l' + point.index + "a" + point.leftChild.index)
            .attr("opacity", 1)
            .attr('stroke', 'skyblue');
            mainGroup.select('#lt' + point.index + "a" + point.leftChild.index)
            .attr("opacity", 1);
            point = point.leftChild;
        }
        else{
            // 右子节点变亮
            mainGroup.select('#c' + point.rightChild.index)
            .attr("opacity", 1)
            .attr('fill', '#5897cf');
            // 右通路
            mainGroup.select('#l' + point.index + "a" + point.rightChild.index)
            .attr("opacity", 1)
            .attr('stroke', 'skyblue');
            mainGroup.select('#lt' + point.index + "a" + point.rightChild.index)
            .attr("opacity", 1);
            point = point.rightChild;
        }
    }
    mainGroup.select('#tw' + point.index)
    .text(arr[arr.length - 1])
    mainGroup.select('#c' + point.index)
    .attr('fill', '#70ad47');
    mainGroup.select('#t' + point.index)
    .attr("fill", "#fff")
    .text(ch);
}
const data = {
    "J1111111" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0202, 0.0093, 0.0041,],
    "X11111101" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0202, 0.0093, 0.0052, 0.0021,],
    "K111111001" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0202, 0.0093, 0.0052, 0.0031, 0.0014,],
    "Z1111110001" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0202, 0.0093, 0.0052, 0.0031, 0.0017, 0.0008,],
    "Q1111110000" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0202, 0.0093, 0.0052, 0.0031, 0.0017, 0.0009,],
    "V111110" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0202, 0.0109,],
    "F11110" : [ 1, 0.4233, 0.1826, 0.0885, 0.0428, 0.0226,],
    "H1110" : [ 1, 0.4233, 0.1826, 0.0885, 0.0457,],
    "T110" : [ 1, 0.4233, 0.1826, 0.0941,],
    "U10111" : [ 1, 0.4233, 0.2407, 0.1182, 0.0547, 0.0258,],
    "P10110" : [ 1, 0.4233, 0.2407, 0.1182, 0.0547, 0.0289,],
    "B101011" : [ 1, 0.4233, 0.2407, 0.1182, 0.0635, 0.0305, 0.0147,],
    "Y101010" : [ 1, 0.4233, 0.2407, 0.1182, 0.0635, 0.0305, 0.0158,],
    "W101001" : [ 1, 0.4233, 0.2407, 0.1182, 0.0635, 0.033, 0.0159,],
    "G101000" : [ 1, 0.4233, 0.2407, 0.1182, 0.0635, 0.033, 0.0171,],
    "E100" : [ 1, 0.4233, 0.2407, 0.1225,],
    "S0111" : [ 1, 0.5767, 0.2737, 0.1321, 0.0636,],
    "R0110" : [ 1, 0.5767, 0.2737, 0.1321, 0.0685,],
    "N0101" : [ 1, 0.5767, 0.2737, 0.1416, 0.0706,],
    "I0100" : [ 1, 0.5767, 0.2737, 0.1416, 0.071,],
    "M00111" : [ 1, 0.5767, 0.303, 0.1437, 0.0711, 0.0334,],
    "L00110" : [ 1, 0.5767, 0.303, 0.1437, 0.0711, 0.0377,],
    "O0010" : [ 1, 0.5767, 0.303, 0.1437, 0.0726,],
    "C00011" : [ 1, 0.5767, 0.303, 0.1593, 0.0774, 0.0383,],
    "D00010" : [ 1, 0.5767, 0.303, 0.1593, 0.0774, 0.0391,],
    "A0000" : [ 1, 0.5767, 0.303, 0.1593, 0.0819,],
};

// 微调
mainGroup.select("#tw85")
.attr("y", +mainGroup.select("#tw85").attr("y") + 30)
.attr("x", +mainGroup.select("#tw85").attr("x") - 20);

mainGroup.select("#tw40")
.attr("y", +mainGroup.select("#tw40").attr("y") + 25)
.attr("x", +mainGroup.select("#tw40").attr("x") - 40);

for(k in data){
    light(k, data[k]);
}
    </script>
</body>
</html>
```

### BFS迷宫路径可视化

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <script>
        
let width = window.innerWidth;
let height = window.innerHeight;

const mainSvg = d3.select('.mainsvg')
.attr('width', width)
.attr('height', height);

const margin = {
    "top": 50,
    "right": 0,
    "bottom": 250,
    "left": 100
}
height = height - margin.top - margin.bottom
width = width - margin.left - margin.right
const mainGroup = mainSvg.append("g")
.attr("class", 'maingroup')
.attr('transform', `translate(${margin.left}, ${margin.top})`)

const data = [
    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 3, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 3, 1, 0, 1, 1, 1, 0, 1, ],
    [1, 0, 0, 0, 1, 3, 1, 0, 0, 0, 1, 0, 1, ],
    [1, 0, 1, 1, 1, 3, 1, 1, 1, 0, 1, 1, 1, ],
    [1, 3, 3, 3, 1, 3, 3, 3, 1, 0, 0, 0, 1, ],
    [1, 3, 1, 3, 1, 1, 1, 3, 1, 0, 1, 0, 1, ],
    [1, 3, 1, 3, 1, 3, 3, 3, 0, 0, 1, 0, 1, ],
    [1, 3, 1, 3, 1, 3, 1, 0, 1, 1, 1, 0, 1, ],
    [1, 3, 1, 3, 3, 3, 1, 0, 1, 3, 3, 3, 1, ],
    [1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 3, 1, ],
    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
];

const rectLength = 50;
mainGroup.selectAll(".null")
.data(data)
.join("g")
.attr("id", (d, i) => "g" + i)
.attr("transform", (d, i) => `translate(0, ${i * rectLength})`)

function color(num){
    if(num == 0) return "#fff";
    if(num == 1) return "#585858";
    if(num == 3) return "#00FF7F";
}

for(let i = 0; i < data.length; i++){
    mainGroup.select("#g" + i).selectAll(".null")
    .data(data[i])
    .join("rect")
    .attr("width", rectLength)
    .attr("height", rectLength)
    .attr("x", (d, i) => i * rectLength)
    .attr("fill", color)
    .attr("stroke", "#000")
}
    </script>
</body>
</html>
```

## 柒 网络

...后续补充

### 力模拟 d3.force()

*与transition data-join等是不同的体系*

**定义力模拟环境** 

* `let nodes = [{}, {}, {}, ...] // 节点列表`
* `let simulation = d3.forceSimulation(nodes)`提供环境
* 提供的结点列表是空, `d3.dorceSimulation`后, 会给`node`初始化位置和速度, 也可以提供

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_20.png)

* 环境定义后开始模拟运动 *粒子质量为1*

**力的相互作用**

* `d3.forceManyBody().strength(value)`
  * 粒子间两两的作用力, **类似于万有引力/斥力**
  * `.strength(value)`设置**力的大小**, `value`为**正相互吸引,为负相互排斥**
* `d3.forceCenter(w, h).strength(value)`
  * 指向某个中心的力, 尽可能让粒子向中心靠近/原理
  * `.strength()`同理
  * `w`,`h`为中心位置
* `d3.forceLink(links).strength(strength).distance(distance)`
  * 部分粒子之间的两两作用力, **每个节点仅会和一部分节点有力的作用**
  * `.distance`为**预期距离**, 如何当前距离为预期, 两个节点间力为0, 如果小于预期, 两节点间有斥力, 否则有引力, **靠近排斥, 靠近吸引**
  * `links`表示边的数组, 由特定格式, 每条边由`source`和`target`组成

![图床异常](https://gitee.com/sun-shiboxy/my_study/raw/markdown/MDImgs/d3_js_21.jpg)

*要预先设置好相应的图元, 再把这些图元交给力模拟*

**力和环境绑定**

* `simulation.force('link/center/manyBody', 相应力).on('tick', ticked);` tick用于每隔很短的时间更新位置
* `ticked`函数
```js
function ticked(){
    lines
    .attr('x1', d => d.source.x)
    .attr('y1', d => d.source.y)
    .attr('x2', d => d.target.x)
    .attr('y2', d => d.target.y);
    circles
    .attr('cx', d => d.x)
    .attr('cy', d => d.y);
}
```

### k-core分解

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <style>
        *{
            margin: 0;
            padding: 0;
            user-select:none;
        }
        .mainsvg{
            display: block;
            margin: auto;
        }
        button{
            border: 1px solid #00ff01;
            border-radius: 20px;
            width: 100px;
            height: 40px;
            position: fixed;
            left: 100px;
            font-size: 18px;
            background-color: #0da1ff;
            color: #fff;
            cursor: pointer;
        }
        button:nth-child(2){
            top: 100px;
        }
        button:nth-child(3){
            top: 180px;
        }
        button:nth-child(4){
            top: 260px;
        }
        button:hover{
            border: 1px solid #ffcc10;
            background-color: #ffcc10;
        }
        button.active{
            border: 1px solid #0da1ff;
            background-color: #00ff01;
        }
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <button class="one">1</button>
    <button class="two">2</button>
    <button class="clear">clear</button>
    <script>
        
let width = window.innerWidth;
let height = window.innerHeight;

const mainSvg = d3.select('.mainsvg')
.attr('width', width)
.attr('height', height);




d3.text("./案例数据1.txt").then(data => {
    // 处理为临接矩阵
    const graph = [];
    for(let i = 0; i < data.length; i++){
        if(data[i] !== " " && data[i] != "\n") graph.push(+data[i]);
    }

    // 找到边
    const links = [];
    // 循环每个节点
    for(let i = 0; i < 10; i++){
        // 循环找到每个结点相连的边
        for(let j = 0; j < i; j++){
            if(graph[i * 10 + j] === 1) links.push({
                "source": i,
                "target": j
            });
        }
    }
    
    // 得到点
    const nodes = []
    for(let i = 0; i < 10; i++){
        nodes.push({"index": i, "x": width / 2, "y": height / 2});
    }

    function ticked(){
        lines
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);
        circles
        .attr('cx', d => d.x)
        .attr('cy', d => d.y);
        texts
        .attr('x', d => d.x - 5)
        .attr('y', d => d.y + 7);
    }

    // 绘制circle, line, text
    const lines = mainSvg
    .selectAll(".null")
    .data(links)
    .join("line")
    .attr('stroke', 'black')
    .attr('opacity', 0.8)
    .attr('stroke-width', .5);

    const circles = mainSvg
    .selectAll(".null")
    .data(nodes)
    .join("circle")
    .attr("id", (d, i) => "c" + i)
    .attr('r', 15)
    .attr('fill', "rgb(13, 161, 255)");

    const texts = mainSvg
    .selectAll(".null")
    .data(nodes)
    .join("text")
    .text(d => d.index)
    .attr("font-size", 18)
    .attr("cursor", "default")
    .attr('fill', "#fff");

    // 绘制力导向
    const simulation = d3.forceSimulation(nodes)
    .force('manyBody', d3.forceManyBody().strength(-30))
    .force('link', d3.forceLink(links).strength(1).distance(links => Math.random() * 300 + 100))
    .on('tick', ticked)

    // 添加拖拽
    circles.call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

    texts.call(d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended));

    // Reheat the simulation when drag starts, and fix the subject position.
    function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.05).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }

  // Update the subject (dragged node) position during drag.
    function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }

  // Restore the target alpha so the simulation cools after dragging ends.
  // Unfix the subject position now that it’s no longer being dragged.
    function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }

    // k-核分解算法 使对应节点变色
    function k_core(k) {
        const tmpGraph = graph.concat() //拷贝 
        // 节点颜色初始化
        circles.attr("fill", "rgb(13, 161, 255)")
        let greenCnt = 1; // 本次变绿的结点个数
        const nodesEachArr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; // 决定是否遍历的数组
        while(greenCnt){
            greenCnt = 0;
            // 遍历一遍节点, 使节点连接个数比k小的变色, 同时"去掉"节点, 即使断开边
            for(let i = 0; i < 10; i++){
                if(nodesEachArr[i] === 0) continue;
                // 记录下连接的结点
                const linkNodes = [];
                let cnt = 0;
                for(let j = 0; j < 10; j++){
                    if(tmpGraph[i * 10 + j] === 1){
                        cnt++;
                        linkNodes.push(j);
                    }
                }
                // 满足 连接边数 < k
                if(cnt <= k){
                    greenCnt++;
                    nodesEachArr[i] = 0;
                    // 变色
                    mainSvg.select("#c" + i)
                    .attr("fill", "rgb(0, 255, 1)")
                    // 断开连接
                    for(let j = 0; j < linkNodes.length; j++){
                        tmpGraph[linkNodes[j] * 10 + i] = 0;
                    }
                }
            }
        }
        
    }
    const buttonOne  = document.querySelector(".one");
    const buttonTwo  = document.querySelector(".two");
    const buttonClear  = document.querySelector(".clear");
    
    buttonOne.addEventListener("click", ()=>{
        // 设置按钮颜色
        buttonOne.classList.add("active")
        buttonTwo.classList.remove("active")
        buttonClear.classList.remove("active")
        k_core(1);
    })
    buttonTwo.addEventListener("click", ()=>{
        // 设置按钮颜色
        buttonTwo.classList.add("active")
        buttonOne.classList.remove("active")
        buttonClear.classList.remove("active")
        k_core(2);
    })
    buttonClear.addEventListener("click", ()=>{
        // 设置按钮颜色
        buttonTwo.classList.remove("active")
        buttonOne.classList.remove("active")
        // 节点颜色初始化
        circles.attr("fill", "rgb(13, 161, 255)")
    })
})
    </script>
</body>
</html>
```

### 中心性

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="./d3.min.js"></script>
    <style>
        *{
            margin: 0;
            padding: 0;
            user-select:none;
            overflow: hidden;
        }
        .mainsvg{
            display: block;
            margin: auto;
        }
        button{
            border: 1px solid #00ff01;
            border-radius: 20px;
            width: 100px;
            height: 40px;
            position: fixed;
            left: 100px;
            font-size: 18px;
            background-color: #0da1ff;
            color: #fff;
            cursor: pointer;
        }
        button:nth-child(2){
            top: 100px;
        }
        button:nth-child(3){
            top: 180px;
        }
        button:nth-child(4){
            top: 260px;
        }
        button:hover{
            border: 1px solid #ffcc10;
            background-color: #ffcc10;
        }
        button.active{
            border: 1px solid #0da1ff;
            background-color: #00ff01;
        }
    </style>
</head>
<body>
    <svg class="mainsvg"></svg>
    <button class="one">度中心性</button>
    <button class="two">接近中心性</button>
    <button class="clear">介数中心性</button>
    <script>
        const degree = {
    "1": 0.013623978201634877,
    "2": 0.010899182561307902,
    "3": 0.013623978201634877,
    "4": 0.15258855585831063,
    "5": 0.16348773841961853,
    "6": 0.15258855585831063,
    "7": 0.0027247956403269754,
    "8": 0.0027247956403269754,
    "9": 0.013623978201634877,
    "10": 0.013623978201634877,
    "11": 0.005449591280653951,
    "12": 0.013623978201634877,
    "13": 0.005449591280653951,
    "14": 0.013623978201634877,
    "15": 0.013623978201634877,
    "16": 0.005449591280653951,
    "17": 0.013623978201634877,
    "18": 0.013623978201634877,
    "19": 0.013623978201634877,
    "20": 0.013623978201634877,
    "21": 0.013623978201634877,
    "22": 0.013623978201634877,
    "23": 0.013623978201634877,
    "24": 0.013623978201634877,
    "25": 0.013623978201634877,
    "26": 0.013623978201634877,
    "27": 0.013623978201634877,
    "28": 0.013623978201634877,
    "29": 0.013623978201634877,
    "30": 0.005449591280653951,
    "31": 0.005449591280653951,
    "32": 0.005449591280653951,
    "33": 0.005449591280653951,
    "34": 0.005449591280653951,
    "35": 0.005449591280653951,
    "36": 0.013623978201634877,
    "37": 0.005449591280653951,
    "38": 0.013623978201634877,
    "39": 0.013623978201634877,
    "40": 0.005449591280653951,
    "41": 0.013623978201634877,
    "42": 0.013623978201634877,
    "43": 0.013623978201634877,
    "44": 0.005449591280653951,
    "45": 0.013623978201634877,
    "46": 0.005449591280653951,
    "47": 0.013623978201634877,
    "48": 0.013623978201634877,
    "49": 0.005449591280653951,
    "50": 0.013623978201634877,
    "51": 0.013623978201634877,
    "52": 0.005449591280653951,
    "53": 0.013623978201634877,
    "54": 0.01907356948228883,
    "55": 0.01907356948228883,
    "56": 0.013623978201634877,
    "57": 0.013623978201634877,
    "58": 0.013623978201634877,
    "59": 0.013623978201634877,
    "60": 0.013623978201634877,
    "61": 0.013623978201634877,
    "62": 0.013623978201634877,
    "63": 0.013623978201634877,
    "64": 0.013623978201634877,
    "65": 0.013623978201634877,
    "66": 0.005449591280653951,
    "67": 0.013623978201634877,
    "68": 0.013623978201634877,
    "69": 0.013623978201634877,
    "70": 0.005449591280653951,
    "71": 0.013623978201634877,
    "72": 0.013623978201634877,
    "73": 0.013623978201634877,
    "74": 0.005449591280653951,
    "75": 0.01907356948228883,
    "76": 0.01907356948228883,
    "77": 0.008174386920980926,
    "78": 0.01634877384196185,
    "79": 0.005449591280653951,
    "80": 0.013623978201634877,
    "81": 0.013623978201634877,
    "82": 0.013623978201634877,
    "83": 0.01634877384196185,
    "84": 0.013623978201634877,
    "85": 0.005449591280653951,
    "86": 0.01634877384196185,
    "87": 0.01634877384196185,
    "88": 0.0653950953678474,
    "89": 0.021798365122615803,
    "90": 0.010899182561307902,
    "91": 0.31335149863760214,
    "92": 0.010899182561307902,
    "93": 0.005449591280653951,
    "94": 0.005449591280653951,
    "95": 0.005449591280653951,
    "96": 0.005449591280653951,
    "97": 0.005449591280653951,
    "98": 0.02997275204359673,
    "99": 0.01634877384196185,
    "100": 0.005449591280653951,
    "101": 0.07629427792915532,
    "102": 0.005449591280653951,
    "103": 0.005449591280653951,
    "104": 0.0027247956403269754,
    "105": 0.0027247956403269754,
    "106": 0.0027247956403269754,
    "107": 0.0027247956403269754,
    "108": 0.0027247956403269754,
    "109": 0.005449591280653951,
    "110": 0.0027247956403269754,
    "111": 0.005449591280653951,
    "112": 0.008174386920980926,
    "113": 0.0027247956403269754,
    "114": 0.0027247956403269754,
    "115": 0.005449591280653951,
    "116": 0.008174386920980926,
    "117": 0.01634877384196185,
    "118": 0.01634877384196185,
    "119": 0.008174386920980926,
    "120": 0.005449591280653951,
    "121": 0.01634877384196185,
    "122": 0.01634877384196185,
    "123": 0.01634877384196185,
    "124": 0.01634877384196185,
    "125": 0.021798365122615803,
    "126": 0.021798365122615803,
    "127": 0.008174386920980926,
    "128": 0.008174386920980926,
    "129": 0.008174386920980926,
    "130": 0.008174386920980926,
    "131": 0.008174386920980926,
    "132": 0.008174386920980926,
    "133": 0.008174386920980926,
    "134": 0.008174386920980926,
    "135": 0.008174386920980926,
    "136": 0.008174386920980926,
    "137": 0.008174386920980926,
    "138": 0.008174386920980926,
    "139": 0.005449591280653951,
    "140": 0.005449591280653951,
    "141": 0.005449591280653951,
    "142": 0.0027247956403269754,
    "143": 0.005449591280653951,
    "144": 0.005449591280653951,
    "145": 0.005449591280653951,
    "146": 0.0027247956403269754,
    "147": 0.010899182561307902,
    "148": 0.005449591280653951,
    "149": 0.010899182561307902,
    "150": 0.005449591280653951,
    "151": 0.005449591280653951,
    "152": 0.005449591280653951,
    "153": 0.005449591280653951,
    "154": 0.005449591280653951,
    "155": 0.0027247956403269754,
    "156": 0.0027247956403269754,
    "157": 0.0027247956403269754,
    "158": 0.005449591280653951,
    "159": 0.0027247956403269754,
    "160": 0.005449591280653951,
    "161": 0.0027247956403269754,
    "162": 0.005449591280653951,
    "163": 0.0027247956403269754,
    "164": 0.005449591280653951,
    "165": 0.0027247956403269754,
    "166": 0.005449591280653951,
    "167": 0.0027247956403269754,
    "168": 0.005449591280653951,
    "169": 0.0027247956403269754,
    "170": 0.005449591280653951,
    "171": 0.0027247956403269754,
    "172": 0.005449591280653951,
    "173": 0.0027247956403269754,
    "174": 0.005449591280653951,
    "175": 0.0027247956403269754,
    "176": 0.005449591280653951,
    "177": 0.0027247956403269754,
    "178": 0.005449591280653951,
    "179": 0.0027247956403269754,
    "180": 0.005449591280653951,
    "181": 0.005449591280653951,
    "182": 0.005449591280653951,
    "183": 0.0027247956403269754,
    "184": 0.005449591280653951,
    "185": 0.0027247956403269754,
    "186": 0.005449591280653951,
    "187": 0.0027247956403269754,
    "188": 0.010899182561307902,
    "189": 0.005449591280653951,
    "190": 0.0027247956403269754,
    "191": 0.005449591280653951,
    "192": 0.0027247956403269754,
    "193": 0.005449591280653951,
    "194": 0.0027247956403269754,
    "195": 0.005449591280653951,
    "196": 0.0027247956403269754,
    "197": 0.005449591280653951,
    "198": 0.0027247956403269754,
    "199": 0.005449591280653951,
    "200": 0.0027247956403269754,
    "201": 0.005449591280653951,
    "202": 0.0027247956403269754,
    "203": 0.005449591280653951,
    "204": 0.0027247956403269754,
    "205": 0.005449591280653951,
    "206": 0.0027247956403269754,
    "207": 0.005449591280653951,
    "208": 0.005449591280653951,
    "209": 0.005449591280653951,
    "210": 0.005449591280653951,
    "211": 0.0027247956403269754,
    "212": 0.05994550408719346,
    "213": 0.0027247956403269754,
    "214": 0.005449591280653951,
    "215": 0.0027247956403269754,
    "216": 0.005449591280653951,
    "217": 0.0027247956403269754,
    "218": 0.0027247956403269754,
    "219": 0.0027247956403269754,
    "220": 0.0027247956403269754,
    "221": 0.0027247956403269754,
    "222": 0.0027247956403269754,
    "223": 0.0027247956403269754,
    "224": 0.0027247956403269754,
    "225": 0.0027247956403269754,
    "226": 0.0027247956403269754,
    "227": 0.0027247956403269754,
    "228": 0.0027247956403269754,
    "229": 0.0027247956403269754,
    "230": 0.0027247956403269754,
    "231": 0.0027247956403269754,
    "232": 0.0027247956403269754,
    "233": 0.0027247956403269754,
    "234": 0.005449591280653951,
    "235": 0.0027247956403269754,
    "236": 0.005449591280653951,
    "237": 0.0027247956403269754,
    "238": 0.005449591280653951,
    "239": 0.0027247956403269754,
    "240": 0.005449591280653951,
    "241": 0.0027247956403269754,
    "242": 0.005449591280653951,
    "243": 0.0027247956403269754,
    "244": 0.005449591280653951,
    "245": 0.0027247956403269754,
    "246": 0.005449591280653951,
    "247": 0.005449591280653951,
    "248": 0.005449591280653951,
    "249": 0.005449591280653951,
    "250": 0.0027247956403269754,
    "251": 0.005449591280653951,
    "252": 0.005449591280653951,
    "253": 0.0027247956403269754,
    "254": 0.005449591280653951,
    "255": 0.0027247956403269754,
    "256": 0.005449591280653951,
    "257": 0.0027247956403269754,
    "258": 0.005449591280653951,
    "259": 0.0027247956403269754,
    "260": 0.005449591280653951,
    "261": 0.0027247956403269754,
    "262": 0.005449591280653951,
    "263": 0.0027247956403269754,
    "264": 0.005449591280653951,
    "265": 0.0027247956403269754,
    "266": 0.005449591280653951,
    "267": 0.0027247956403269754,
    "268": 0.005449591280653951,
    "269": 0.0027247956403269754,
    "270": 0.005449591280653951,
    "271": 0.0027247956403269754,
    "272": 0.005449591280653951,
    "273": 0.008174386920980926,
    "274": 0.005449591280653951,
    "275": 0.0027247956403269754,
    "276": 0.005449591280653951,
    "277": 0.0027247956403269754,
    "278": 0.005449591280653951,
    "279": 0.0027247956403269754,
    "280": 0.005449591280653951,
    "281": 0.0027247956403269754,
    "282": 0.005449591280653951,
    "283": 0.0027247956403269754,
    "284": 0.005449591280653951,
    "285": 0.0027247956403269754,
    "286": 0.005449591280653951,
    "287": 0.0027247956403269754,
    "288": 0.005449591280653951,
    "289": 0.0027247956403269754,
    "290": 0.005449591280653951,
    "291": 0.0027247956403269754,
    "292": 0.008174386920980926,
    "293": 0.0027247956403269754,
    "294": 0.005449591280653951,
    "295": 0.0027247956403269754,
    "296": 0.005449591280653951,
    "297": 0.0027247956403269754,
    "298": 0.005449591280653951,
    "299": 0.0027247956403269754,
    "300": 0.005449591280653951,
    "301": 0.0027247956403269754,
    "302": 0.005449591280653951,
    "303": 0.005449591280653951,
    "304": 0.005449591280653951,
    "305": 0.0027247956403269754,
    "306": 0.005449591280653951,
    "307": 0.0027247956403269754,
    "308": 0.005449591280653951,
    "309": 0.0027247956403269754,
    "310": 0.005449591280653951,
    "311": 0.0027247956403269754,
    "312": 0.005449591280653951,
    "313": 0.0027247956403269754,
    "314": 0.0027247956403269754,
    "315": 0.0027247956403269754,
    "316": 0.0027247956403269754,
    "317": 0.0027247956403269754,
    "318": 0.0027247956403269754,
    "319": 0.005449591280653951,
    "320": 0.0027247956403269754,
    "321": 0.0027247956403269754,
    "322": 0.0027247956403269754,
    "323": 0.0027247956403269754,
    "324": 0.005449591280653951,
    "325": 0.005449591280653951,
    "326": 0.005449591280653951,
    "327": 0.0027247956403269754,
    "328": 0.0027247956403269754,
    "329": 0.005449591280653951,
    "330": 0.0027247956403269754,
    "331": 0.005449591280653951,
    "332": 0.005449591280653951,
    "333": 0.0027247956403269754,
    "334": 0.005449591280653951,
    "335": 0.0027247956403269754,
    "336": 0.0027247956403269754,
    "337": 0.0027247956403269754,
    "338": 0.005449591280653951,
    "339": 0.0027247956403269754,
    "340": 0.005449591280653951,
    "341": 0.005449591280653951,
    "342": 0.0027247956403269754,
    "343": 0.005449591280653951,
    "344": 0.0027247956403269754,
    "345": 0.010899182561307902,
    "346": 0.0027247956403269754,
    "347": 0.005449591280653951,
    "348": 0.0027247956403269754,
    "349": 0.005449591280653951,
    "350": 0.005449591280653951,
    "351": 0.0027247956403269754,
    "352": 0.005449591280653951,
    "353": 0.0027247956403269754,
    "354": 0.0027247956403269754,
    "355": 0.005449591280653951,
    "356": 0.0027247956403269754,
    "357": 0.0027247956403269754,
    "358": 0.0027247956403269754,
    "359": 0.005449591280653951,
    "360": 0.0027247956403269754,
    "361": 0.005449591280653951,
    "362": 0.0027247956403269754,
    "363": 0.005449591280653951,
    "364": 0.0027247956403269754,
    "365": 0.0027247956403269754,
    "366": 0.0027247956403269754,
    "367": 0.0027247956403269754,
    "368": 0.0027247956403269754
};
const closeness = {
    "1": 0.260099220411056,
    "2": 0.20711060948081264,
    "3": 0.260099220411056,
    "4": 0.3177489177489177,
    "5": 0.3475378787878788,
    "6": 0.3177489177489177,
    "7": 0.1716557530402245,
    "8": 0.1716557530402245,
    "9": 0.2593639575971731,
    "10": 0.2593639575971731,
    "11": 0.20617977528089887,
    "12": 0.2593639575971731,
    "13": 0.20617977528089887,
    "14": 0.2593639575971731,
    "15": 0.2593639575971731,
    "16": 0.20617977528089887,
    "17": 0.2593639575971731,
    "18": 0.2593639575971731,
    "19": 0.2593639575971731,
    "20": 0.2593639575971731,
    "21": 0.2593639575971731,
    "22": 0.2593639575971731,
    "23": 0.2593639575971731,
    "24": 0.2593639575971731,
    "25": 0.2593639575971731,
    "26": 0.2593639575971731,
    "27": 0.2593639575971731,
    "28": 0.2593639575971731,
    "29": 0.2593639575971731,
    "30": 0.20617977528089887,
    "31": 0.20617977528089887,
    "32": 0.20617977528089887,
    "33": 0.20617977528089887,
    "34": 0.20617977528089887,
    "35": 0.20617977528089887,
    "36": 0.2593639575971731,
    "37": 0.20617977528089887,
    "38": 0.2593639575971731,
    "39": 0.2593639575971731,
    "40": 0.20617977528089887,
    "41": 0.2593639575971731,
    "42": 0.2593639575971731,
    "43": 0.2593639575971731,
    "44": 0.20617977528089887,
    "45": 0.2593639575971731,
    "46": 0.20617977528089887,
    "47": 0.2593639575971731,
    "48": 0.2593639575971731,
    "49": 0.20617977528089887,
    "50": 0.2593639575971731,
    "51": 0.2593639575971731,
    "52": 0.20617977528089887,
    "53": 0.2593639575971731,
    "54": 0.37410805300713557,
    "55": 0.37410805300713557,
    "56": 0.2593639575971731,
    "57": 0.2593639575971731,
    "58": 0.2593639575971731,
    "59": 0.2593639575971731,
    "60": 0.2593639575971731,
    "61": 0.2593639575971731,
    "62": 0.2593639575971731,
    "63": 0.2593639575971731,
    "64": 0.2593639575971731,
    "65": 0.2593639575971731,
    "66": 0.20617977528089887,
    "67": 0.2593639575971731,
    "68": 0.2593639575971731,
    "69": 0.2593639575971731,
    "70": 0.20617977528089887,
    "71": 0.2593639575971731,
    "72": 0.2593639575971731,
    "73": 0.2593639575971731,
    "74": 0.20617977528089887,
    "75": 0.26440922190201727,
    "76": 0.26440922190201727,
    "77": 0.21104082806210467,
    "78": 0.2597310686482661,
    "79": 0.2064116985376828,
    "80": 0.2593639575971731,
    "81": 0.2593639575971731,
    "82": 0.2593639575971731,
    "83": 0.2597310686482661,
    "84": 0.2593639575971731,
    "85": 0.2064116985376828,
    "86": 0.2765636774679729,
    "87": 0.2765636774679729,
    "88": 0.22809198259788688,
    "89": 0.32622222222222225,
    "90": 0.27408513816280805,
    "91": 0.39934711643090315,
    "92": 0.20664414414414414,
    "93": 0.20617977528089887,
    "94": 0.20617977528089887,
    "95": 0.20617977528089887,
    "96": 0.20617977528089887,
    "97": 0.20617977528089887,
    "98": 0.21767497034400948,
    "99": 0.21626399528579845,
    "100": 0.20617977528089887,
    "101": 0.2299498746867168,
    "102": 0.21690307328605202,
    "103": 0.21690307328605202,
    "104": 0.2461435278336687,
    "105": 0.2461435278336687,
    "106": 0.2461435278336687,
    "107": 0.2461435278336687,
    "108": 0.17884990253411306,
    "109": 0.1791117618350415,
    "110": 0.17884990253411306,
    "111": 0.1791117618350415,
    "112": 0.1871494135645079,
    "113": 0.17884990253411306,
    "114": 0.17884990253411306,
    "115": 0.18554095045500504,
    "116": 0.1874361593462717,
    "117": 0.18791602662570406,
    "118": 0.18791602662570406,
    "119": 0.1874361593462717,
    "120": 0.1871494135645079,
    "121": 0.18791602662570406,
    "122": 0.18791602662570406,
    "123": 0.18791602662570406,
    "124": 0.18791602662570406,
    "125": 0.19035269709543567,
    "126": 0.19035269709543567,
    "127": 0.1874361593462717,
    "128": 0.18734047983665136,
    "129": 0.18734047983665136,
    "130": 0.18734047983665136,
    "131": 0.18734047983665136,
    "132": 0.18734047983665136,
    "133": 0.18734047983665136,
    "134": 0.18734047983665136,
    "135": 0.18734047983665136,
    "136": 0.18734047983665136,
    "137": 0.18734047983665136,
    "138": 0.1874361593462717,
    "139": 0.18724489795918367,
    "140": 0.1871494135645079,
    "141": 0.18878600823045266,
    "142": 0.1579173838209983,
    "143": 0.15832614322691976,
    "144": 0.15832614322691976,
    "145": 0.15832614322691976,
    "146": 0.1579173838209983,
    "147": 0.15873702422145328,
    "148": 0.15832614322691976,
    "149": 0.15873702422145328,
    "150": 0.15832614322691976,
    "151": 0.16005233318796336,
    "152": 0.16005233318796336,
    "153": 0.16005233318796336,
    "154": 0.16005233318796336,
    "155": 0.1579173838209983,
    "156": 0.1579173838209983,
    "157": 0.15778159931212382,
    "158": 0.2860483242400624,
    "159": 0.22255912674348088,
    "160": 0.2860483242400624,
    "161": 0.22255912674348088,
    "162": 0.2860483242400624,
    "163": 0.22255912674348088,
    "164": 0.2860483242400624,
    "165": 0.22255912674348088,
    "166": 0.2860483242400624,
    "167": 0.22255912674348088,
    "168": 0.2860483242400624,
    "169": 0.22255912674348088,
    "170": 0.2860483242400624,
    "171": 0.22255912674348088,
    "172": 0.2860483242400624,
    "173": 0.22255912674348088,
    "174": 0.2860483242400624,
    "175": 0.22255912674348088,
    "176": 0.2860483242400624,
    "177": 0.22255912674348088,
    "178": 0.2860483242400624,
    "179": 0.22255912674348088,
    "180": 0.2860483242400624,
    "181": 0.22337188070602557,
    "182": 0.2860483242400624,
    "183": 0.22255912674348088,
    "184": 0.2860483242400624,
    "185": 0.22255912674348088,
    "186": 0.2860483242400624,
    "187": 0.22255912674348088,
    "188": 0.2869429241594996,
    "189": 0.2860483242400624,
    "190": 0.22255912674348088,
    "191": 0.2860483242400624,
    "192": 0.22255912674348088,
    "193": 0.2860483242400624,
    "194": 0.22255912674348088,
    "195": 0.2860483242400624,
    "196": 0.22255912674348088,
    "197": 0.2860483242400624,
    "198": 0.22255912674348088,
    "199": 0.2860483242400624,
    "200": 0.22255912674348088,
    "201": 0.2860483242400624,
    "202": 0.22255912674348088,
    "203": 0.2860483242400624,
    "204": 0.22255912674348088,
    "205": 0.2860483242400624,
    "206": 0.22255912674348088,
    "207": 0.2860483242400624,
    "208": 0.222829386763813,
    "209": 0.2860483242400624,
    "210": 0.2860483242400624,
    "211": 0.22255912674348088,
    "212": 0.29477911646586347,
    "213": 0.22780881440099318,
    "214": 0.2901185770750988,
    "215": 0.22780881440099318,
    "216": 0.2901185770750988,
    "217": 0.22780881440099318,
    "218": 0.22780881440099318,
    "219": 0.22780881440099318,
    "220": 0.22780881440099318,
    "221": 0.22780881440099318,
    "222": 0.22780881440099318,
    "223": 0.22780881440099318,
    "224": 0.22780881440099318,
    "225": 0.22780881440099318,
    "226": 0.22780881440099318,
    "227": 0.22780881440099318,
    "228": 0.22780881440099318,
    "229": 0.22780881440099318,
    "230": 0.22780881440099318,
    "231": 0.22780881440099318,
    "232": 0.22780881440099318,
    "233": 0.22780881440099318,
    "234": 0.2860483242400624,
    "235": 0.22255912674348088,
    "236": 0.2860483242400624,
    "237": 0.22255912674348088,
    "238": 0.2860483242400624,
    "239": 0.22255912674348088,
    "240": 0.2860483242400624,
    "241": 0.22255912674348088,
    "242": 0.2860483242400624,
    "243": 0.22255912674348088,
    "244": 0.2860483242400624,
    "245": 0.22255912674348088,
    "246": 0.2860483242400624,
    "247": 0.222829386763813,
    "248": 0.2860483242400624,
    "249": 0.2860483242400624,
    "250": 0.22255912674348088,
    "251": 0.2860483242400624,
    "252": 0.2860483242400624,
    "253": 0.22255912674348088,
    "254": 0.2860483242400624,
    "255": 0.22255912674348088,
    "256": 0.2860483242400624,
    "257": 0.22255912674348088,
    "258": 0.2860483242400624,
    "259": 0.22255912674348088,
    "260": 0.2860483242400624,
    "261": 0.22255912674348088,
    "262": 0.2860483242400624,
    "263": 0.22255912674348088,
    "264": 0.2860483242400624,
    "265": 0.22255912674348088,
    "266": 0.2860483242400624,
    "267": 0.22255912674348088,
    "268": 0.2860483242400624,
    "269": 0.22255912674348088,
    "270": 0.2860483242400624,
    "271": 0.22255912674348088,
    "272": 0.2860483242400624,
    "273": 0.2231003039513678,
    "274": 0.2860483242400624,
    "275": 0.22255912674348088,
    "276": 0.2860483242400624,
    "277": 0.22255912674348088,
    "278": 0.2860483242400624,
    "279": 0.22255912674348088,
    "280": 0.2860483242400624,
    "281": 0.22255912674348088,
    "282": 0.2860483242400624,
    "283": 0.22255912674348088,
    "284": 0.2860483242400624,
    "285": 0.22255912674348088,
    "286": 0.2860483242400624,
    "287": 0.22255912674348088,
    "288": 0.2860483242400624,
    "289": 0.22255912674348088,
    "290": 0.2860483242400624,
    "291": 0.22255912674348088,
    "292": 0.2864949258391881,
    "293": 0.222829386763813,
    "294": 0.2860483242400624,
    "295": 0.222829386763813,
    "296": 0.2860483242400624,
    "297": 0.22255912674348088,
    "298": 0.2860483242400624,
    "299": 0.22255912674348088,
    "300": 0.2860483242400624,
    "301": 0.22255912674348088,
    "302": 0.2860483242400624,
    "303": 0.222829386763813,
    "304": 0.2860483242400624,
    "305": 0.22255912674348088,
    "306": 0.2860483242400624,
    "307": 0.22255912674348088,
    "308": 0.2860483242400624,
    "309": 0.22255912674348088,
    "310": 0.2860483242400624,
    "311": 0.22255912674348088,
    "312": 0.2860483242400624,
    "313": 0.22255912674348088,
    "314": 0.2231003039513678,
    "315": 0.2231003039513678,
    "316": 0.2856031128404669,
    "317": 0.2856031128404669,
    "318": 0.2856031128404669,
    "319": 0.2860483242400624,
    "320": 0.22255912674348088,
    "321": 0.2856031128404669,
    "322": 0.2856031128404669,
    "323": 0.2856031128404669,
    "324": 0.2860483242400624,
    "325": 0.222829386763813,
    "326": 0.2860483242400624,
    "327": 0.22255912674348088,
    "328": 0.2856031128404669,
    "329": 0.2860483242400624,
    "330": 0.2856031128404669,
    "331": 0.2860483242400624,
    "332": 0.2860483242400624,
    "333": 0.22255912674348088,
    "334": 0.2860483242400624,
    "335": 0.22255912674348088,
    "336": 0.2856031128404669,
    "337": 0.2856031128404669,
    "338": 0.2860483242400624,
    "339": 0.22255912674348088,
    "340": 0.2860483242400624,
    "341": 0.222829386763813,
    "342": 0.2856031128404669,
    "343": 0.2860483242400624,
    "344": 0.2856031128404669,
    "345": 0.2864949258391881,
    "346": 0.222829386763813,
    "347": 0.2860483242400624,
    "348": 0.22255912674348088,
    "349": 0.2860483242400624,
    "350": 0.2860483242400624,
    "351": 0.22255912674348088,
    "352": 0.2860483242400624,
    "353": 0.2856031128404669,
    "354": 0.2856031128404669,
    "355": 0.2860483242400624,
    "356": 0.2856031128404669,
    "357": 0.2856031128404669,
    "358": 0.2856031128404669,
    "359": 0.2860483242400624,
    "360": 0.22255912674348088,
    "361": 0.2860483242400624,
    "362": 0.22255912674348088,
    "363": 0.2860483242400624,
    "364": 0.22255912674348088,
    "365": 0.2856031128404669,
    "366": 0.2856031128404669,
    "367": 0.2856031128404669,
    "368": 0.2856031128404669
};
const betweenness = {
    "1": 0.008132642881604348,
    "2": 0.010884292967644912,
    "3": 0.008132642881604348,
    "4": 0.12039335470344438,
    "5": 0.3643940892567299,
    "6": 0.12039335470344438,
    "7": 0.0,
    "8": 0.0,
    "9": 0.0027426099756023346,
    "10": 0.0027426099756023346,
    "11": 0.0,
    "12": 0.0027426099756023346,
    "13": 0.0,
    "14": 0.0027426099756023346,
    "15": 0.0027426099756023346,
    "16": 0.0,
    "17": 0.0027426099756023346,
    "18": 0.0027426099756023346,
    "19": 0.0027426099756023346,
    "20": 0.0027426099756023346,
    "21": 0.0027426099756023346,
    "22": 0.0027426099756023346,
    "23": 0.0027426099756023346,
    "24": 0.0027426099756023346,
    "25": 0.0027426099756023346,
    "26": 0.0027426099756023346,
    "27": 0.0027426099756023346,
    "28": 0.0027426099756023346,
    "29": 0.0027426099756023346,
    "30": 0.0,
    "31": 0.0,
    "32": 0.0,
    "33": 0.0,
    "34": 0.0,
    "35": 0.0,
    "36": 0.0027426099756023346,
    "37": 0.0,
    "38": 0.0027426099756023346,
    "39": 0.0027426099756023346,
    "40": 0.0,
    "41": 0.0027426099756023346,
    "42": 0.0027426099756023346,
    "43": 0.0027426099756023346,
    "44": 0.0,
    "45": 0.0027426099756023346,
    "46": 0.0,
    "47": 0.0027426099756023346,
    "48": 0.0027426099756023346,
    "49": 0.0,
    "50": 0.0027426099756023346,
    "51": 0.0027426099756023346,
    "52": 0.0,
    "53": 0.0027426099756023346,
    "54": 0.24100961016916692,
    "55": 0.24100961016916692,
    "56": 0.001376489757023103,
    "57": 0.001376489757023103,
    "58": 0.002742609975602335,
    "59": 0.002742609975602335,
    "60": 0.001376489757023103,
    "61": 0.001376489757023103,
    "62": 0.008129718139991957,
    "63": 0.008129718139991957,
    "64": 0.0027426099756023346,
    "65": 0.0027426099756023346,
    "66": 0.0,
    "67": 0.002742609975602335,
    "68": 0.002742609975602335,
    "69": 0.0027426099756023346,
    "70": 0.0,
    "71": 0.0027426099756023346,
    "72": 0.0027426099756023346,
    "73": 0.0027426099756023346,
    "74": 0.0,
    "75": 0.02574206898703261,
    "76": 0.02574206898703261,
    "77": 0.0,
    "78": 0.0027644125948945684,
    "79": 0.0,
    "80": 0.0027266568395348466,
    "81": 0.002742609975602335,
    "82": 0.002742609975602335,
    "83": 0.0027644125948945684,
    "84": 0.0027266568395348466,
    "85": 0.0,
    "86": 0.10663120461775927,
    "87": 0.10663120461775927,
    "88": 0.09258423787614836,
    "89": 0.022494453626360537,
    "90": 0.0011539435088816427,
    "91": 0.8138651896189752,
    "92": 1.4889593662988937e-05,
    "93": 0.0,
    "94": 0.0,
    "95": 0.0,
    "96": 0.0,
    "97": 0.0,
    "98": 0.03286778537147055,
    "99": 0.009815716462431068,
    "100": 0.0,
    "101": 0.12071663614299968,
    "102": 0.0,
    "103": 0.0,
    "104": 0.0,
    "105": 0.0,
    "106": 0.0,
    "107": 0.0,
    "108": 0.0,
    "109": 0.0,
    "110": 0.0,
    "111": 0.0,
    "112": 0.004972131643860767,
    "113": 0.0,
    "114": 0.0,
    "115": 0.0009638530297841518,
    "116": 0.0054539340788056535,
    "117": 0.008134060938143662,
    "118": 0.008134060938143662,
    "119": 0.0054539340788056535,
    "120": 0.0,
    "121": 0.00540554289940094,
    "122": 0.00540554289940094,
    "123": 0.00540554289940094,
    "124": 0.00540554289940094,
    "125": 0.013047130527141246,
    "126": 0.013047130527141246,
    "127": 0.0054539340788056535,
    "128": 4.3427981517051066e-06,
    "129": 4.3427981517051066e-06,
    "130": 4.3427981517051066e-06,
    "131": 4.3427981517051066e-06,
    "132": 4.3427981517051066e-06,
    "133": 4.3427981517051066e-06,
    "134": 4.3427981517051066e-06,
    "135": 4.3427981517051066e-06,
    "136": 4.3427981517051066e-06,
    "137": 4.3427981517051066e-06,
    "138": 0.0054539340788056535,
    "139": 0.005449591280653948,
    "140": 0.0,
    "141": 0.0014700992143257753,
    "142": 0.0,
    "143": 0.0,
    "144": 0.0,
    "145": 0.0,
    "146": 0.0,
    "147": 3.3501585741725105e-05,
    "148": 0.0,
    "149": 3.3501585741725105e-05,
    "150": 0.0,
    "151": 0.0,
    "152": 0.0,
    "153": 0.0,
    "154": 0.0,
    "155": 0.0,
    "156": 0.0,
    "157": 0.0,
    "158": 0.005449591280653951,
    "159": 0.0,
    "160": 0.005449591280653951,
    "161": 0.0,
    "162": 0.005449591280653951,
    "163": 0.0,
    "164": 0.005449591280653951,
    "165": 0.0,
    "166": 0.005449591280653951,
    "167": 0.0,
    "168": 0.005449591280653951,
    "169": 0.0,
    "170": 0.005449591280653951,
    "171": 0.0,
    "172": 0.005449591280653951,
    "173": 0.0,
    "174": 0.005449591280653951,
    "175": 0.0,
    "176": 0.005449591280653951,
    "177": 0.0,
    "178": 0.005449591280653951,
    "179": 0.0,
    "180": 0.002702461249832492,
    "181": 2.2334390494483405e-05,
    "182": 0.005449591280653951,
    "183": 0.0,
    "184": 0.005449591280653951,
    "185": 0.0,
    "186": 0.005449591280653951,
    "187": 0.0,
    "188": 0.013586754217477405,
    "189": 0.005449591280653951,
    "190": 0.0,
    "191": 0.005449591280653951,
    "192": 0.0,
    "193": 0.005449591280653951,
    "194": 0.0,
    "195": 0.005449591280653951,
    "196": 0.0,
    "197": 0.005449591280653951,
    "198": 0.0,
    "199": 0.005449591280653951,
    "200": 0.0,
    "201": 0.005449591280653951,
    "202": 0.0,
    "203": 0.005449591280653951,
    "204": 0.0,
    "205": 0.005449591280653951,
    "206": 0.0,
    "207": 0.002717350843495481,
    "208": 7.4447968314944685e-06,
    "209": 0.0007854260657226664,
    "210": 0.005449591280653951,
    "211": 0.0,
    "212": 0.10100355861288546,
    "213": 0.0,
    "214": 0.0,
    "215": 0.0,
    "216": 0.0,
    "217": 0.0,
    "218": 0.0,
    "219": 0.0,
    "220": 0.0,
    "221": 0.0,
    "222": 0.0,
    "223": 0.0,
    "224": 0.0,
    "225": 0.0,
    "226": 0.0,
    "227": 0.0,
    "228": 0.0,
    "229": 0.0,
    "230": 0.0,
    "231": 0.0,
    "232": 0.0,
    "233": 0.0,
    "234": 0.005449591280653951,
    "235": 0.0,
    "236": 0.005449591280653951,
    "237": 0.0,
    "238": 0.005449591280653951,
    "239": 0.0,
    "240": 0.005449591280653951,
    "241": 0.0,
    "242": 0.005449591280653951,
    "243": 0.0,
    "244": 0.005449591280653951,
    "245": 0.0,
    "246": 0.002717350843495481,
    "247": 7.4447968314944685e-06,
    "248": 0.002717350843495481,
    "249": 0.005449591280653951,
    "250": 0.0,
    "251": 0.002717350843495481,
    "252": 0.005449591280653951,
    "253": 0.0,
    "254": 0.005449591280653951,
    "255": 0.0,
    "256": 0.005449591280653951,
    "257": 0.0,
    "258": 0.005449591280653951,
    "259": 0.0,
    "260": 0.005449591280653951,
    "261": 0.0,
    "262": 0.005449591280653951,
    "263": 0.0,
    "264": 0.005449591280653951,
    "265": 0.0,
    "266": 0.005449591280653951,
    "267": 0.0,
    "268": 0.005449591280653951,
    "269": 0.0,
    "270": 0.005449591280653951,
    "271": 0.0,
    "272": 0.0018066040311093294,
    "273": 2.2334390494483405e-05,
    "274": 0.005449591280653951,
    "275": 0.0,
    "276": 0.005449591280653951,
    "277": 0.0,
    "278": 0.005449591280653951,
    "279": 0.0,
    "280": 0.005449591280653951,
    "281": 0.0,
    "282": 0.005449591280653951,
    "283": 0.0,
    "284": 0.005449591280653951,
    "285": 0.0,
    "286": 0.005449591280653951,
    "287": 0.0,
    "288": 0.005449591280653951,
    "289": 0.0,
    "290": 0.005449591280653951,
    "291": 0.0,
    "292": 0.010884292967644912,
    "293": 0.0,
    "294": 0.0018066040311093294,
    "295": 0.0,
    "296": 0.005449591280653951,
    "297": 0.0,
    "298": 0.005449591280653951,
    "299": 0.0,
    "300": 0.005449591280653951,
    "301": 0.0,
    "302": 0.002717350843495481,
    "303": 7.4447968314944685e-06,
    "304": 0.005449591280653951,
    "305": 0.0,
    "306": 0.005449591280653951,
    "307": 0.0,
    "308": 0.005449591280653951,
    "309": 0.0,
    "310": 0.005449591280653951,
    "311": 0.0,
    "312": 0.005449591280653951,
    "313": 0.0,
    "314": 0.0,
    "315": 0.0,
    "316": 0.0,
    "317": 0.0,
    "318": 0.0,
    "319": 0.005449591280653951,
    "320": 0.0,
    "321": 0.0,
    "322": 0.0,
    "323": 0.0,
    "324": 0.002717350843495481,
    "325": 7.4447968314944685e-06,
    "326": 0.005449591280653951,
    "327": 0.0,
    "328": 0.0,
    "329": 0.002717350843495481,
    "330": 0.0,
    "331": 0.0018066040311093294,
    "332": 0.005449591280653951,
    "333": 0.0,
    "334": 0.005449591280653951,
    "335": 0.0,
    "336": 0.0,
    "337": 0.0,
    "338": 0.005449591280653951,
    "339": 0.0,
    "340": 0.002717350843495481,
    "341": 7.4447968314944685e-06,
    "342": 0.0,
    "343": 0.002717350843495481,
    "344": 0.0,
    "345": 0.005457036077485445,
    "346": 0.0,
    "347": 0.005449591280653951,
    "348": 0.0,
    "349": 0.0,
    "350": 0.005449591280653951,
    "351": 0.0,
    "352": 0.0,
    "353": 0.0,
    "354": 0.0,
    "355": 0.002717350843495481,
    "356": 0.0,
    "357": 0.0,
    "358": 0.0,
    "359": 0.005449591280653951,
    "360": 0.0,
    "361": 0.005449591280653951,
    "362": 0.0,
    "363": 0.005449591280653951,
    "364": 0.0,
    "365": 0.0,
    "366": 0.0,
    "367": 0.0,
    "368": 0.0
};

let fun = 1; // 1度中心性 2接近中心线 3介数中心性

const centrality = str => {
    if(fun === 1) return (degree[str] - d3.min(Object.values(degree))) / (d3.max(Object.values(degree)) - d3.min(Object.values(degree)));
    if(fun === 2) return (closeness[str] - d3.min(Object.values(closeness))) / (d3.max(Object.values(closeness)) - d3.min(Object.values(closeness)));
    if(fun === 3) return (betweenness[str] - d3.min(Object.values(betweenness))) / (d3.max(Object.values(betweenness)) - d3.min(Object.values(betweenness)));
}

let width = window.innerWidth;
let height = window.innerHeight ;

const mainSvg = d3.select('.mainsvg')
.attr('width', width)
.attr('height', height);

const relation2Weights = {
    "r_dns_a": 80,
    "r_dns_cname": 80,
    "r_cert": 80,
    "r_certchain": 70,
    "r_request_jump": 35,
    "r_subdomain": 30,
    "r_asn": 30,
    "r_cidr": 25,
    "r_whois_phone": 25,
    "r_whois_name": 10,
    "r_whois_email":10
};


d3.json("./案例数据2.json").then(data => {
    // 找到结点
    const nodes = data['nodes'].map(d => ({
        "index": +d.name,
        "x": -1000 ,
        "y": 0
    }));

    // 找到边
    const links = data['links'].map(d => ({
        "weight": relation2Weights[d.relation],
        "source": +d.source - 1, 
        "target": +d.target - 1
    }));


    
    function ticked(){
        lines
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);
        circles
        .attr("r", (d, i) => 5 + centrality(""+(i+1)) * 20)
        .attr("fill", (d, i) => d3.interpolate("#0da1ff", "#00ff01")(centrality(""+(i+1))))
        .attr('cx', d => d.x = Math.max(5 + centrality(""+(d.index+1)) * 50, Math.min(width - (5 + centrality(""+(d.index+1)) * 50), d.x)))
        .attr('cy', d => d.y = Math.max(5 + centrality(""+(d.index+1)) * 50, Math.min(height - (5 + centrality(""+(d.index+1)) * 50), d.y)));
    }

    

    // 绘制circle, line, text
    const lines = mainSvg
    .selectAll(".null")
    .data(links)
    .join("line")
    .attr('stroke', '#33333370')
    .attr('opacity', 0.8)
    .attr('stroke-width', .4);

    const circles = mainSvg
    .selectAll(".null")
    .data(nodes)
    .join("circle")
    .attr("id", (d, i) => "c" + i)
    .attr('r', (d, i) => 5 + centrality(""+(i+1)) * 50)
    .attr('stroke', '#000')
    .attr('fill', (d, i) => d3.interpolate("#0da1ff", "#00ff01")(5 * centrality(""+(i+1))));


    // 绘制力导向
    const simulation = d3.forceSimulation(nodes)
    .force('manyBody', d3.forceManyBody().strength(node => centrality(""+(node.index+1)) * -30 - 100))
    .force('link', d3.forceLink(links).strength(1).distance(link => (link.weight + 30)))
    .force("collide", d3.forceCollide().radius(function(d) {
        return 5 + centrality(""+(d.index+1)) * 50; // 为节点添加半径
    }))
    .on('tick', ticked)

    // 添加拖拽
    circles.call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));


    // Reheat the simulation when drag starts, and fix the subject position.
    function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.05).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }

  // Update the subject (dragged node) position during drag.
    function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }

  // Restore the target alpha so the simulation cools after dragging ends.
  // Unfix the subject position now that it’s no longer being dragged.
    function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }

    
    const buttonOne  = document.querySelector(".one");
    const buttonTwo  = document.querySelector(".two");
    const buttonClear  = document.querySelector(".clear");
    
    buttonOne.addEventListener("click", ()=>{
        // 设置按钮颜色
        buttonOne.classList.add("active")
        buttonTwo.classList.remove("active")
        buttonClear.classList.remove("active")
        fun = 1;
        ticked();
    })
    buttonTwo.addEventListener("click", ()=>{
        // 设置按钮颜色
        buttonTwo.classList.add("active")
        buttonOne.classList.remove("active")
        buttonClear.classList.remove("active")
        fun = 2;
        ticked();
    })
    buttonClear.addEventListener("click", ()=>{
        // 设置按钮颜色
        buttonClear.classList.add("active")
        buttonTwo.classList.remove("active")
        buttonOne.classList.remove("active")
        // 节点颜色初始化
        fun = 3
        ticked();
    })
})
    </script>
</body>
</html>
```