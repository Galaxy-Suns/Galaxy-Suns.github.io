# _贰__WebAPIs
 
* [2.1_声明变量优先使用`const`](#2.1_声明变量优先使用`const`)
* [2.2_DOM_初识](#2.2_DOM_初识)
* [2.3_获取_DOM_元素](#2.3_获取_DOM_元素)
* [2.4_操作元素内容](#2.4_操作元素内容)
* [2.5_操作元素属性](#2.5_操作元素属性)
  * [2.5.1_操作元素常用属性](#2.5.1_操作元素常用属性)
  * [2.5.2_操作元素的样式属性](#2.5.2_操作元素的样式属性)
  * [2.5.3_操作表单元素的属性](#2.5.3_操作表单元素的属性)
  * [2.5.4_自定义属性](#2.5.4_自定义属性)
* [2.6_定时器_间歇函数](#2.6_定时器_间歇函数)
* [2.7_事件监听](#2.7_事件监听)
* [2.8_事件监听版本](#2.8_事件监听版本)
* [2.9_鼠标事件](#2.9_鼠标事件)
* [2.10_焦点事件](#2.10_焦点事件)
* [2.11_键盘事件和用户输入事件](#2.11_键盘事件和用户输入事件)
* [2.12_事件对象](#2.12_事件对象)
* [2.13_环境对象](#2.13_环境对象)
* [2.14_回调函数](#2.14_回调函数)
* [2.15_事件流](#2.15_事件流)
* [2.16_解绑事件](#2.16_解绑事件)
* [2.17_鼠标经过事件](#2.17_鼠标经过事件)
* [2.18_事件委托](#2.18_事件委托)
* [2.19_阻止元素的默认行为](#2.19_阻止元素的默认行为)
* [2.20_其它事件](#2.20_其它事件)
  * [2.20.1_页面加载事件_load](#2.20.1_页面加载事件_load)
  * [2.20.2_DOMContentLoaded](#2.20.2_DOMContentLoaded)
  * [2.20.3_元素滚动事件_scroll](#2.20.3_元素滚动事件_scroll)
  * [2.20.4_页面尺寸事件_resize](#2.20.4_页面尺寸事件_resize)
* [2.21_元素尺寸与位置](#2.21_元素尺寸与位置)
  * [2.21.1_元素尺寸与位置_尺寸_offsetWidth](#2.21.1_元素尺寸与位置_尺寸_offsetWidth)
  * [2.21.2_元素尺寸与位置_位置_offsetTop](#2.21.2_元素尺寸与位置_位置_offsetTop)
  * [2.21.3_元素尺寸与位置_getBoundingClientRect()](#2.21.3_元素尺寸与位置_getBoundingClientRect())
* [2.22_日期对象的使用](#2.22_日期对象的使用)
  * [2.22.1_日期对象实例化](#2.22.1_日期对象实例化)
  * [2.22.2_日期对象方法](#2.22.2_日期对象方法)
  * [2.22.3_时间戳的使用](#2.22.3_时间戳的使用)
* [2.23_节点操作](#2.23_节点操作)
  * [2.23.1_查找DOM节点](#2.23.1_查找DOM节点)
  * [2.23.2_增加节点](#2.23.2_增加节点)
  * [2.23.3_删除节点](#2.23.3_删除节点)
* [2.24_M端事件](#2.24_M端事件)
* [2.25_swiper插件](#2.25_swiper插件)
* [2.25_BOM和延迟函数setTimeout](#2.25_BOM和延迟函数setTimeout)
* [2.26_事件循环eventloop](#2.26_事件循环eventloop)
* [2.27_location对象](#2.27_location对象)
* [2.28_navigator对象和history对象](#2.28_navigator对象和history对象)
* [2.29_本地存储](#2.29_本地存储)
* [2.30_本地存储处理复杂数据类型](#2.30_本地存储处理复杂数据类型)
* [2.31_数组映射方法_map()](#2.31_数组映射方法_map())
* [2.32_数组拼接字符串方法_join()](#2.32_数组拼接字符串方法_join())
* [2.33_对话判断框confirm](#2.33_对话判断框confirm)
* [2.34_正则表达式](#2.34_正则表达式)
  * [2.34.1_正则表达式及其使用](#2.34.1_正则表达式及其使用)
  * [2.34.2_元字符-边界符](#2.34.2_元字符-边界符)
  * [2.34.2_元字符-量词](#2.34.2_元字符-量词)
  * [2.34.3_元字符-字符类](#2.34.3_元字符-字符类)
  * [2.34.4_预定义类](#2.34.4_预定义类)
  * [2.34.5_修饰符](#2.34.5_修饰符)
* [表单change事件](#表单change事件)

_API 通过 js 操作 html 和浏览器_

_分为 DOM 文档对象模型,BOM 浏览器对象模型_

## 2.1_声明变量优先使用`const`

_能用`const`就用`const`_

**步骤**

1. 变量全部`const`
2. 后续需要修改再改为`let`

**注意**

_对于复杂数据类型`object` `data` `array`等，由于直接存储的是"栈区"的地址，`const`保证这个地址不会改变，而改变"栈区"存储地址指向的"堆区"存储内容是被允许的，因而`const`修饰的复杂数据类型可以更改内容(地址变化除外)_

```js
const arr = ["red", "pink"];
arr.push("blue");
console.log(arr); // 允许

/* const arr1 = ['yellow']
arr = arr1 修改了地址 报错
console.log(arr) */
```

## 2.2_DOM_初识

**简介**

_文档对象模型 浏览器提供的一套专门**操作网页内容**的功能 标签等_

_开发网页特效 实现用户交互_

**DOM 树**

_将 html 文档**以树状结构直观表现**出来，我们称之为文档数或 DOM 树_

**_直观体现标签与标签的关系_**

**DOM 对象**

_浏览器根据每一个 html 标签都会生成一个对应的 js 对象_

\*所有的标签**属性都可以在这个对象上找到\***

\*修改这个对象的**属性会自动映射到标签\***

**html 里的标签，在 js 里叫对象**

**DOM 的核心** 把网页内容**当作对象处理**

**document 对象**

- 是 DOM 中的最大对象
- 它提供的方法和属性用来**访问和操作网页内容** _document.write()_
- 网页所有的内容都在 document 里

.html

```html
<body>
  <div>123</div>
  <script src="./try.js"></script>
</body>
```

.js

```js
// DOM对象
const div = document.querySelector("div");
// 打印对象
console.dir(div); // dom 对象
```

## 2.3_获取_DOM_元素

_推荐通过 CSS 选择器获取 DOM 元素_

**通过 CSS 选择器获取 DOM 元素**

- `decument.querySelector('css选择器')`选择**匹配的第一个元素**,返回**对象**,没有匹配到，返回`null`
- `decument.querySelectorAll('css选择器')`,返回**对象数组** <br> 返回的是一个**伪数组**(哪怕只有一个元素),具有长度和索引号，但没有 pop(),push()等数组方法，可以正常遍历

.html

```html
<body>
  <div class="box">123</div>
  <div class="box">abc</div>
  <p id="nav">导航栏</p>
  <ul>
    <li>测试1</li>
    <li>测试2</li>
    <li>测试3</li>
  </ul>
  <script src="./try.js"></script>
</body>
```

.js

```js
// 获取匹配的第一个元素
// const box = document.querySelector('div')
const box = document.querySelector(".box");
console.dir(box);
const nav = document.querySelector("#nav");
console.dir(nav);
nav.style.color = "red";
// 获取第二个小li
const li = document.querySelector("ul li:nth-child(2)");
console.dir(li);
// 获取所有小li
const Lis = document.querySelectorAll("ul li");
console.dir(Lis);
```

## 2.4_操作元素内容

_DOM 对象都是通过标签生成的，操作标签，本质上就是操作 DOM 对象，反过来也一样_

**修改标签内容**

- `对象.innerText`属性 <br> 将文本内容添加/更新，显示纯文本，**不解析标签**
- `对象.innerHTML`属性 <br> 识别文本，**会解析标签** **常用**

```js
const obj = {
  uname: "pink老师",
};
console.log(obj.uname);
obj.uname = "red老师";

// 获取元素
const box = document.querySelector(".box");

// 修改文字内容 对象.innerText属性
console.log(box.innerText); // 获取文字内容
box.innerText = "<strong>我是一个盒子</strong>";

// 修改内容 解析标签
console.log(box.innerHTML);
box.innerHTML = "<strong>我要更换</strong>";
console.log(box.innerHTML);
```

## 2.5_操作元素属性

### 2.5.1_操作元素常用属性

_可以通过 js 设置/修改标签元素属性,比如通过 src 更换图片_

_href,title,src 等_

**语法**

- `对象.属性 = 值`
- 值为字符串

.html

```html
<body>
  <img
    src="./1.2023新版前端JavaScript/2.web APIs/资料/web APIs第一天/06-素材/images/1.webp"
    alt=""
  />
  <script src="./try.js"></script>
</body>
```

.css

```css
img {
  width: 600px;
}
```

.js

```js
function getRandomInt(start, end) {
  return Math.floor(start + (end - start + 1) * Math.random());
}

const img = document.querySelector("img");
img.src = `./1.2023新版前端JavaScript/2.web APIs/资料/web APIs第一天/06-素材/images/${getRandomInt(
  1,
  6
)}.webp`;
```

### 2.5.2_操作元素的样式属性

**通过 style 属性修改 CSS**

- `对象.style.样式属性 = 值`
- 值为字符串
- 出现含`-`的属性，使用小驼峰命名法即可
- 生成的样式是行内样式表，权重较高

```js
// 获取元素
const box = document.querySelector(".box");
// 修改样式属性
box.style.width = "300px";
box.style.backgroundColor = "hotpink";
box.style.border = "1px solid #000";
box.style.borderTop = "1px solid blue";
```

_获取 body 标签的方法_ `document.body`

_body 的属性_ `document.body.属性`

**通过类名操作 CSS**

- `对象.className = '新增类名'`
- 适用于改变元素较多的情况，事先在 css 创建好，要变化的类，在 js 中只添加类名就能完成大规模的改变样式

.html

```html
<body>
  <div class="nav">123</div>
  <script src="./try.js"></script>
</body>
```

.css

```css
div {
  width: 200px;
  height: 200px;
  background-color: pink;
}

.nav {
  color: red;
}

.box {
  width: 300px;
  height: 300px;
  background-color: skyblue;
  margin: 100px auto;
  padding: 10px;
  border: 1px solid #000;
}
```

```js
// 获取元素
const div = document.querySelector("div");
div.className += " box"; // 保留了nav
```

**通过 classList 控制 CSS** _常用_

_为了解决 className 容易覆盖以前类名，通过 classList 方式**追加和删除**类名_

- `元素.classList.add('类名')`追加一个类名
- `元素.classList.remove('类名')`删除一个类名
- `元素.classList.toggle('类名')`切换一个类名 _有就删，没有就加_

```js
// 获取元素
const box = document.querySelector(".box");
// 修改样式 类名不加.,且为字符型
box.classList.add("active");
// 移除类
box.classList.remove("box");
// 切换类 右就删，没有就加
box.classList.toggle("box");
box.classList.toggle("active");
```

### 2.5.3_操作表单元素的属性

**获取表单的内容**

- `表单.value`
- inner..获取不到

**改变表单的类型**

_如文本框转密码框实现密码的隐藏显示_

- `表单.type`

**表单选中属性等**

_这种添加属性生效，移除失效的**采用布尔值表示**，true 生效 false 失效_

_disabled,checked,selected 等_

- `表单.属性 = true/false`
- 注意要用布尔值，而非字符串(字符串除了空字符串都是`true`)

```js
// 获取元素
const uname = document.querySelector(".text");

// 获取值 获取表单里面的值 用的 表单.value
console.log(uname.value); // 电脑
console.log(uname.innerHTML);

// 设置表单内容的值
uname.value = "我要买电脑";
console.log(uname.type);
uname.type = "password";

// 获取
const ipt = document.querySelector(".checkbox");

console.log(ipt.checked); // false

ipt.checked = true;

const button = document.querySelector("button");
button.disabled = true; // disabled 禁用点击
```

### 2.5.4_自定义属性

_开发者自己定义的属性_

_标签上以 data-开头_

_以 dataset 对象形式获取_

**获取自定义属性**

`对象.dataset.属性(不含data-)`

.html

```html
<body>
  <div data-id="1" data-spm="不知道">1</div>
  <div data-id="2">2</div>
  <div data-id="3">3</div>
  <div data-id="4">4</div>
  <div data-id="5">5</div>
  <script src="./try.js"></script>
</body>
```

.js

```js
const one = document.querySelector("div");
console.log(one.dataset);

console.log(one.dataset.id);
console.log(one.dataset.spm);
```

## 2.6_定时器_间歇函数

_每隔一段时间，自动执行一段代码_

**开启定时器**

- `setInterval(函数, 间隔时间)`
- 每间隔一段时间，调用一次这个函数
- 间隔时间的单位为毫秒
- 第一次执行也会间隔
- 返回值是这个定时器的序号
- **返回用 let 声明变量** （后续开关可能会变）

**关闭定时器**

- `clearInterval(定时器编号)`

```js
// setInterval(函数,间隔时间)
let n = setInterval(function () {
  console.log("hi");
}, 1000);

function fn() {
  console.log("调用");
}

let m = setInterval(fn, 1000);

console.log(n);
console.log(m);

clearInterval(m);
```

## 2.7_事件监听

_事件 编程期间内系统内发生的动作_

_事件监听 有事件发生后，立即调用一个函数做出响应 也叫绑定事件/注册事件_

**语法**

- `元素对象.addEventListener('事件类型',要执行的函数)`

**三要素**

- 事件源:那个 dom 元素被事件触发
- 事件类型:用什么方式触发，如鼠标点击`click`或鼠标经过`mouseover`等
- 事件调用的函数:要做什么

```js
document.querySelector("button").addEventListene("click", function () {
  alert("你好");
});
```

## 2.8_事件监听版本

- 早期版本 DOML0 `事件源.on事件 = function(){}`
- DOML2 `事件源.addEventListener('事件',要处理函数)` 当今的 L3 也采用这种版本

_早期采取赋值的形式，会使新注册的事件覆盖掉之前注册的 只可以冒泡_

_当今版本的方式，不会出现覆盖的情况，新注册的监听保留之前注册的(add) 可以冒泡，捕获_

```js
const btn = document.querySelector("button");
/* btn.onclick = function(){
  alert('hi')
}

btn.onclick = function(){
  alert('22')
} */

btn.addEventListener("click", function () {
  alert(11);
});

btn.addEventListener("click", function () {
  alert(22);
});
```

## 2.9_鼠标事件

- 鼠标点击 `click`
- 鼠标经过 `mouseenter`
- 鼠标离开 `mouseleave`

```js
// 鼠标经过和离开

const div = document.querySelector("div");

// 鼠标经过
div.addEventListener("mouseenter", function () {
  console.log("轻轻的我来了");
});

// 鼠标离开
div.addEventListener("mouseleave", function () {
  console.log("轻轻的我走了，正如我轻轻的来");
});
```

## 2.10_焦点事件

_焦点是指一些元素，如文本框，在获取到光标(即其中不断闪烁的小杠杠)_

- 获得焦点 `focus`
- 失去焦点 `blur`

```js
// 焦点事件
const text = document.querySelector("input");

// 获得焦点
text.addEventListener("focus", function () {
  console.log("我得到了焦点");
});

// 失去焦点
text.addEventListener("blur", function () {
  console.log("我失去了焦点");
});
```

## 2.11_键盘事件和用户输入事件

**键盘事件** _用户按下抬起任意键盘触发_

- 键盘按下触发 `keydown`
- 键盘抬起触发 `Keyup`

**用户输入文本事件** _用户输入任意内容触发_

- `input`

```js
// 键盘事件
const input = document.querySelector("input");
/* input.addEventListener('keydown', function(){
  console.log('键盘按下了')
})
input.addEventListener('keyup', function(){
  console.log('键盘抬起了')
}) */

// 文本事件
input.addEventListener("input", function () {
  // 获取到用户输入内容
  console.log(input.value);
});
```

## 2.12_事件对象

_是一个对象，这个对象中存有事件触发时的相关信息_

_比如鼠标点击事件中，事件对象存有鼠标在哪个位置等信息_

_判断按下哪个键，判断按下哪个元素_

**语法**

_在事件绑定的回调函数中，第一个参数就是事件对象_

- 一般命名为`event` `ev` `e`
- `元素对象.addEventListener('事件类型',function(e){})`

**事件对象的常用属性**

- `type`获取事件类型
- `clientX/clientY`获取鼠标相对浏览器左上角的位置
- `offsetX/offsetY`获取鼠标相对于当前 DOM 元素左上的位置
- `key`用户按下的键盘的值

```js
/* const btn = document.querySelector('button')
btn.addEventListener('click',function(e){
  console.log(e)
}) */
document.querySelector("input").addEventListener("keydown", function (e) {
  console.log(e.key);
});
```

_字符串的 trim()方法可以去掉两边的空格_

## 2.13_环境对象

- 函数内部特殊的变量对象`this`，代表当前函数运行的环境

_函数在哪个对象内声明，其内的 this 就代表包裹它的最内层对象_

_全局函数视为在 window 对象内声明_

**在绑定事件时，回调函数内 this 为绑定的元素**

```js
// 每个函数里面都有this环境对象
function fn() {
  console.log(this);
}
fn();
// 在哪个对象内声明，就是指向谁，全局函数在window声明，调用时完整写法
// window.fn()

const btn = document.querySelector("button");
btn.addEventListener("click", function () {
  console.log(this);
  this.style.color = "red";
});

const obj = {
  uname: "pink",
  age: 18,
  fun: function () {
    fn();
  },
};

obj.fun();
```

## 2.14_回调函数

_将某一函数作为参数传给另一函数，前者为回调函数_

- `setInterval(fn , 1000)`
- `addEventListener('click',fn)`
- `arr.sort(fn)`

_css 伪类型 checkbox:checked 选择选中的 checkbox 复选框_

## 2.15_事件流

_事件完整执行过程中的流动路径_

**两个阶段**

- 捕获 _大到小 document html body div_
- 冒泡 _小到大 div dody html document_

_项目中以冒泡为主_

**事件捕获**

- 从`DOM`的根元素开始执行对应事件(从外到里)
- `DOM.addEventListener(事件类型, 事件处理函数, 是否使用捕获机制)`
- `false`默认，冒泡。`true`捕获
- L0 无捕获

```js
const fa = document.querySelector(".father");
const son = document.querySelector(".son");

document.addEventListener(
  "click",
  function () {
    alert("我是爷爷");
  },
  true
);
fa.addEventListener(
  "click",
  function () {
    alert("我是爸爸");
  },
  true
);
son.addEventListener(
  "click",
  function () {
    alert("我是儿子");
  },
  true
);
```

**事件冒泡**

_当一个元素的事件触发时，其祖先元素由于绑定了**同样事件**，会从内到外依次触发事件_

**阻止冒泡**

_子元素触发事件后，绑定了同一事件的祖先元素不再冒泡_

- `事件对象e.stopPropagation()`
- 阻止传播(冒泡和捕获)
- 写在子元素，阻止其向父元素传播

```js
const fa = document.querySelector(".father");
const son = document.querySelector(".son");

document.addEventListener("click", function () {
  alert("我是爷爷");
});
fa.addEventListener("click", function () {
  alert("我是爸爸");
});
son.addEventListener("click", function (e) {
  alert("我是儿子");
  // 阻止流动传播
  e.stopPropagation();
});
```

## 2.16_解绑事件

_对于 on 绑定事件，使其赋为 null 即可解绑_

**addEventListener()解绑方法**

- `DOM.removeEventListener(事件类型, 事件处理函数[, 捕获或冒泡阶段])`
- add 时采取匿名函数，无法解绑

```js
const btn = document.querySelector("button");

// L0事件移除
btn.onclick = function () {
  alert("点击了");
};
// 事件解绑
btn.onclick = null;

// L2事件移除
function fn() {
  alert("点击了");
}

btn.addEventListener("click", fn);

btn.removeEventListener("click", fn);
```

## 2.17_鼠标经过事件

_mouseover 和 mouseout_ 有冒泡效果
_mouseenter 和 mouseleave_ 无冒泡效果，**推荐**

```js
const dad = document.querySelector(".dad");
const baby = document.querySelector(".baby");

dad.addEventListener("mouseenter", function () {
  console.log("鼠标经过");
});
dad.addEventListener("mouseleave", function () {
  console.log("鼠标离开");
});
```

## 2.18_事件委托

_同时给兄弟关系的一系列元素绑定事件,可以委托给它们的父元素 利用了事件冒泡_

**好处**

- 减少了事件绑定次数，提高了程序性能

**步骤**

- 给**父元素注册事件**，触发子元素时，直接冒泡给父元素，从而触发到父元素的事件
- 父元素冒泡触发事件，获取真正触发的元素`e.target`对象
- 找到真正触发元素的标签名`e.target.tagName`

```js
// 点击每个小li当前li文字变为红色
// 点击li，冒泡到父元素绑定事件
document.querySelector("ul").addEventListener("click", function (e) {
  // 通过事件对象.target获取到点击的真正对象
  if (e.target.tagName === "LI") {
    // 需求 : 点击p不变色 可以用tagName限制变色的标签
    e.target.style.color = "red";
  }
});
```

## 2.19_阻止元素的默认行为

_阻止连接的调整,表单域的跳转_

**语法**

- `e.preventDefault`

```js
const form = document.querySelector("form");
form.addEventListener("submit", function (e) {
  // 阻止默认行为，提交
  e.preventDefault();
});

const a = document.querySelector("a");
a.addEventListener("click", function (e) {
  // 阻止默认行为 点击
  e.preventDefault();
});
```

## 2.20_其它事件

### 2.20.1_页面加载事件_load

_页面加载事件_

_加载外部资源 图片 外联 CSS Js 等 加载完毕时触发的事件_

_页面资源处理完了再做一些事情_

**语法**

- 事件名`load`
- 监听页面所有资源加载完毕 给`window`(大于`document`)添加`load`

**用途**

- 当`script`写在 head，作为入口函数
- 图片加载完后，再执行相应代码

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>页面加载事件</title>
    <link rel="stylesheet" href="./try.css" />
    <script>
      // 等待页面所有资源加载完毕，就会去执行回调函数
      window.addEventListener("load", function () {
        const btn = document.querySelector("button");
        btn.addEventListener("click", function () {
          alert("中");
        });
      });
      // 等待图片加载完毕再执行里面代码
      img.addEventListener("load", function () {});
    </script>
  </head>
  <body>
    <button>点击</button>
    <script src="./try.js"></script>
  </body>
</html>
```

### 2.20.2_DOMContentLoaded

_当**初始的 HTML 文档**被完全加载和解析完成之后，DOMContentLoaded 事件被触发，而无需等待样式表，图像等完全加载_

_相比于 load，需要等待的时间更短_

**语法**

- 给`document`添加`DOMContentLoaded`事件
- 适用于当`script`写在 `head`，作为入口函数

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>页面加载事件</title>
    <link rel="stylesheet" href="./try.css" />
    <script>
      document.addEventListener("DOMContentLoaded", function () {
        document.querySelector("button").addEventListener("click", function () {
          alert("中");
        });
      });
    </script>
  </head>
  <body>
    <button>点击</button>
    <script src="./try.js"></script>
  </body>
</html>
```

### 2.20.3_元素滚动事件_scroll

_滚动条在滚动的时候持续触发的事件_

_检测到用户滚动到某区域， 做一些操作_

**语法**

- 事件名 `scroll`
- 监听整个页面滚动 给`window`添加
- 监听元素的滚动 给元素添加事件
- 获取滚动位置 元素属性 `scrollLeft`被“卷去”的左侧 `scrollTop`被“卷去”的头部 _数字型，不带单位_ **可读写**，实现返回顶部等操作

```html
<body>
  <div>
    我里面有很多很多的文字 我里面有很多很多的文字 我里面有很多很多的文字
    我里面有很多很多的文字 我里面有很多很多的文字 我里面有很多很多的文字
    我里面有很多很多的文字 我里面有很多很多的文字 我里面有很多很多的文字
    我里面有很多很多的文字 我里面有很多很多的文字 我里面有很多很多的文字
    我里面有很多很多的文字 我里面有很多很多的文字
  </div>
  <script src="./try.js"></script>
</body>
```

```css
body {
  padding-top: 100px;
  height: 1000px;
}

div {
  display: none;
  margin: 100px;
  height: 200px;
  width: 200px;
  border: 1px solid #000;
  overflow: scroll;
}
```

```js
const div = document.querySelector("div");
// 页面滚动事件
window.addEventListener("scroll", function () {
  // 我想知道页面到底滚动了多少像素 被卷去了多少 scrollTop
  // 对于 html 添加属性 document.documentElement -> 获取html标签
  // console.log(document.documentElement.scrollTop)
  const n = document.documentElement.scrollTop;
  if (n >= 100) {
    div.style.display = "block";
  } else div.style.display = "none";
  // console.log('我滚了')
});

div.addEventListener("scroll", function () {
  // scrollTop 滚动卷去的头部
  // console.log(div.scrollTop)
});
```

### 2.20.4_页面尺寸事件_resize

_窗口尺寸改变时触发事件_

**语法**

- 事件名 `resize`
- 添加给`window`, 在窗口改变时触发

**获取元素的可见部分宽高**

- 不含边框，margin,滚动条等
- `clientWidth`和`clientHeight`**属性**
- **只读**

```html
<body>
  <div>123123123123231543321</div>
  <script src="./try.js"></script>
</body>
```

```css
div {
  display: inline-block;
  border: 10px solid red;
  padding: 10px;
  /* width: 200px; */
  height: 200px;
  background-color: pink;
}
```

```js
// resize 浏览器窗口大小发生变化的时候触发的事件
window.addEventListener("resize", function () {
  console.log(1);
});

// 获取元素的可见部分宽高 padding content
const div = document.querySelector("div");
console.log(div.clientWidth);
```

## 2.21_元素尺寸与位置

_获取页面滚动到某个元素的位置，就去做某个元素_

_而不是去实际测量测量 省去计算_

_通过 js 获取元素在页面的位置_

### 2.21.1_元素尺寸与位置_尺寸_offsetWidth

- `offsetWidth`和`offsetHeight`**属性**
- 获取元素自身宽高，包含元素自身设置的宽高，`padding`,`border`,滚动条 与`client`系列区别于`border`，滚动条
- 可视宽高，`display: none`获取的是`0`

### 2.21.2_元素尺寸与位置_位置_offsetTop

- **只读属性**
- 获取元素**距离自己定位父级(祖先)**元素的左，上距离

```html
<body>
  <div>
    <p></p>
  </div>
  <script src="./try.js"></script>
</body>
```

```css
div {
  position: relative;
  margin: 100px;
  width: 200px;
  height: 200px;
  background-color: pink;
  overflow: hidden;
}

p {
  width: 100px;
  height: 100px;
  background-color: purple;
  margin: 50px;
}
```

```js
const div = document.querySelector("div");
const p = document.querySelector("p");
// 检测盒子的位置， 最近一级带有定位的祖先元素
console.log(div.offsetLeft);
console.log(p.offsetLeft);
```

### 2.21.3_元素尺寸与位置_getBoundingClientRect()

_获取元素大小以及相对于视口的位置_

**语法**

- `元素.getBoundingClientRect()` 注意`getBoundingClientRect()`是元素的方法，要加`()`
- 相对于**当前视口**的位置，与 offset 相对于定位的祖先不同，滚动页面也会改变 top 值,(_因为元素在视口中位置变了_)
- 返回的是一个对象

---

```css
html {
  scroll-behavior: smooth;
}
```

可以为滚动条添加**滑动效果**,改变滚动条位置后，有过渡效果

---

## 2.22_日期对象的使用

_让网页显示 日期，时间_

_用来表示时间的对象_

_可以得到当前系统时间_

### 2.22.1_日期对象实例化

**实例化语法**

- `new`关键字
- `new 类名()` _通过无参构造出一个匿名的类对象，new 赋值给名字_

**创建时间对象 获取时间**

- 获取当前时间 `new Data()`
- 返回指定时间 `new Data('2023-11-11')` _有参构造_

```js
// 实例化 new
// 1、得到当前时间
const date = new Date();
console.log(date);
// 2、指定时间
const date1 = new Date("2023-11-11 08:30:00");
console.log(date1);
```

### 2.22.2_日期对象方法

**语法**

- `getFullYear()` 获得四位年份
- `getMonth()` 获得月份 取值`0-11`!!
- `getDate()` 获得天 根据月份取值不同而不同
- `getHours() getMinutes() getSecond()` 时分秒

```js
// 获得日期对象
const date = new Date();
// 使用方法
console.log(date.getFullYear());
console.log(date.getMonth() + 1);
console.log(date.getDate());
console.log(date.getDay()); // 星期 0-6 星期日:0
console.log(date.getHours());
console.log(date.getMinutes());
console.log(date.getSeconds());
```

_`toLocaleString`返回一个初步格式化时间字符串_

### 2.22.3_时间戳的使用

_1970-01-01 00:00:00 到现在的毫秒数_

_用于计算时间 日期等_

**获取时间戳**

- `getTime()`方法
- `+new Data()`得到匿名 Data 对象后，隐式转换为 Number
- `Data.now()` 静态方法

```js
// 得到时间戳 getTime方法
const date = new Date();
console.log(date.getTime());
// +new Date()
console.log(+new Date());
// Date.now() 只能当前
console.log(Date.now());

console.log(+new Date("2023-11-11 08:35"));
```

## 2.23_节点操作

*对页面元素进行增删改查*

*DOM树的每一个内容都称为结点*

**元素节点***主要*

* **所有的标签**如`body`, `div`
* `html`是根节点

**属性节点**

* **所有的属性**如`href`

**文本节点**

* 所有的文字

### 2.23.1_查找DOM节点

*区别于qs方法, 站在节点关系的角度查找*

*减少qs*

**语法**

* 元素对象属性`parentNode`，返回**最近一级父节点**，找不到返回`null`

```html
<body>
  <div class="grandfather">
    <div class="dad">
      <div class="baby">x</div>
    </div>
  </div>
  <script src="./try.js"></script>
</body>
```

```js
const baby = document.querySelector('.baby')
console.log(baby)

const father = baby.parentNode
console.log(father)

const grandfather = baby.parentNode.parentNode
console.log(grandfather)
```

* 元素对象方法`childNodes`, 返回所有子节点(*包括文本节点, 空格, 换行, 注释节点等*)
* 元素`children`属性**常用**, 仅获得**所有最近的子元素节点**,返回一个**伪数组** *查找不到length === 0*

```html
<body>
  <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>
  <script src="./try.js"></script>
</body>
```

```js
const ul = document.querySelector('ul') // ul
const lis = ul.children
console.log(lis)

for(let i = 0; i < lis.length; i++){
    lis[i].innerHTML = i + 1;
}
```

* 元素属性`nextElementSibling`属性 返回下一个兄弟节点
* 元素属性`previousElementSibling`属性 返回上一个兄弟节点

```html
<body>
  <ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
  </ul>
  <script src="./try.js"></script>
</body>
```
```js
const li2 = document.querySelector('ul li:nth-child(2)')

const li3 = li2.nextElementSibling
const li4 = li2.nextElementSibling.nextElementSibling

const li1 = li2.previousElementSibling

console.log(li3)
console.log(li4)
console.log(li1)
console.log(li1.previousElementSibling) // null
```

### 2.23.2_增加节点

*在页面中新增元素以完成一定功能*

**步骤**

1. 创建一个节点
2. 把创建的结点放到指定元素内部

**创建节点**

* `document.createElement('标签名')`

**追加结点**

*插入到某个父元素中*

* 元素方法`父元素.appendChild(插入元素)`插入为**父元素的最后一个子元素**
```js
// 创建节点
const div = document.createElement('div')
div.innerHTML = '我是div'
// 插入为最后一个子元素
document.body.appendChild(div)
```
* 元素方法`父元素.insertBefore(插入元素, 在哪个元素前)`插入到父元素中的**某个子元素前面**

```js
const ul = document.querySelector('ul')
const li = document.createElement('li')
li.innerHTML = '0'
ul.insertBefore(li, ul.children[0])
```

**克隆节点**

*复制已有节点到一些区域*

1. 复制一个原有的节点
2. 把复制的节点放入到指定的元素内部

* 元素方法`元素.cloneNode(布尔值)`
* 布尔值`true` 克隆时包含后代节点
* 布尔值`false` 克隆时不包含后代节点
* 默认`false`
* *注 标签内包裹的文字也算为后代*

```js
const ul = document.querySelector('ul')
// 克隆节点
const li = ul.children[0].cloneNode(true)
// 插入节点
ul.appendChild(li)
```

### 2.23.3_删除节点

*在JS原生DOM操作中, 要删除元素必须通过父元素删除*

**语法**

* 元素对象方法`父元素.removeChild(要删除的元素)`
* 如不存在**直接父子关系**则删除不成功
* 不同于`display: none ` `removeChild`真正删掉了节点

```js
const ul = document.querySelector('ul')
sul.removeChild(ul.children[0])
```

## 2.24_M端事件

*待补充*


## 2.25_swiper插件

**插件**

* 其他人封装好的一些代码，可以直接实现对应效果

**swiper插件使用的基本流程**

1. 熟悉官网，了解这个插件可以完成什么需求
2. 看在线演示，找到符合自己需求的demo
3. 查看基本使用流程
4. 查看api文档，配置自己的需求
5. *注意 多个swiper同时使用，类名注意区分*

*待补充*

## 2.25_BOM和延迟函数setTimeout

*BOM 浏览器对象模型*

***BOM中包含着DOM***

*BOM依然可以树状表示*

```
BOM:
window-
-navigator
-location
-document
-history
-screen
```

*window对象是一个**全局对象** 是JS中的**顶级对象***

*`document` `alert` `console.log()`*这些都是window中的**属性与方法***省略了window.*
*我们声明的全局函数和var声明的变量都挂载到window身上, 成为了window的属性和方法*
*window对象的属性和方法在**调用时可以省掉window.***

```js
// document.querySelector()
// window.document.querySelector()
console.log(document === window.document)


function fn(){
    console.log(11)
}
window.fn()

var num = 10
console.log(window.num)
```

**延时函数setTimeout**

*与`setInterval()`的区别 setInterval()执行多次 setTimeout()延时后执行一次终止*
* `setTimeout(function(){}, ms)`ms毫秒后执行回调函数
* 清除延时函数`clearTimeout(Timer)`参数为setTimeout的数字型返回值

```js
setTimeout(function(){
    console.log('没有时间了')
}, 2000)
```

## 2.26_事件循环eventloop

*浏览器的两个引擎 渲染引擎(负责渲染html和css) JS解析器*

***JS是单线程语言**, 同一时间只能做一件事*

*所有任务要排队, 前一个结束, 后一个才执行*

*但是当出现定时器等耗时操作, 不能死板单线程卡在那里*

*于是html5标准, 允许JS创建多个线程， 出现了**同步**和**异步***

**同步**

前一个任务一结束后再执行后一个任务, **程序的执行顺序和任务的排列顺序一致** *耗时任务停下来等待*

**异步**

对于耗时操作，**在(等待)做这件事的同时，可以去做其他事情**

*区别在于执行顺序不同*

**同步任务** 都在**主线程**上执行，形成一个**执行栈**

**异步任务** 

* JS的异步是通过回调函数执行
* 有三种类型**普通事件**, **资源加载**, **定时器**
* 异步任务相关添加到**任务队列中(消息队列)**

**JS执行机制**

1. **先执行执行栈**中的同步任务
2. **已结束异步任务(该执行了) (由支持多线程的浏览器判断异步任务是否结束)** 放入任务队列
3. 当执行栈中所有**同步任务执行完毕**, 系统会**按次序*不断*读取**任务队列中的**异步任务**, 于是**被读取的异步任务**结束等待状态, **进入执行栈, 开始执行**, *事件循环*

```js
console.log(1)
console.log(2)
setTimeout(function(){
    console.log(3)
})
console.log(4)
```

## 2.27_location对象

*`location`对象拆分并保存了url地址的各个组成部分*

**常用属性方法**

* `href`属性 获取**完整的url地址, 对其赋值时用于地址的跳转**

```js
console.log(location)
console.log(window.location)
// 1. href 经常用href 利用js的方法去跳转页面
console.log(location.href)
// location.href = 'http://www.baidu.com'
```

* `search`属性 获取地址中携带的参数, 符号?后面部分 *常用获取表单提交信息*
* `hash`属性 获取地址中的哈希值, 符号#后面部分 *常用于组件化*
* `reload()` 方法 刷新页面, 传入`true`表示强刷新

```html
<body>
  <form action="#">
    <input type="text" name="username">
    <input type="text" name="pwd">
    <button>提交</button>
  </form>
    <a href="#/my">我的</a>
    <a href="#/friend">朋友</a>
    <a href="#/download">下载</a>
    <button class="reload">刷新</button>
  <script src="./try.js"></script>
</body>
```

```js
const reload = document.querySelector('.reload')
reload.addEventListener('click', function(){
    // 刷新页面 f5
    location.reload()
    // 强制刷新 ctrl + f5 从云端拉取数据重新渲染，而非本地
    location.reload(true)
})
```

## 2.28_navigator对象和history对象

**navigator对象**

*记录浏览器的自身相关信息*

*常用属性方法*

* `userAgent`属性 检测浏览器版本及平台

*移动端适配模版代码*

```js
<script>
  !(function () {
    const userAgent = navigator.userAgent
    // 验证是否为Android或iPhone
    const android = userAgent.match(/(Android);?[\s\/]+([\d.]+)?/)
    const iphone = userAgent.match(/(iPhone\sOS)\s([\d_]+)/)
    // 如果是Android或iPhone，则跳转至移动站点
    if (android || iphone) {
      location.href = 'http://m.itcast.cn'
    }
  })();
</script>
```

*粘贴在head*

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>location对象</title>
  <link rel="stylesheet" href="./try.css">
  <script>
    !(function () {
      const userAgent = navigator.userAgent
      // 验证是否为Android或iPhone
      const android = userAgent.match(/(Android);?[\s\/]+([\d.]+)?/)
      const iphone = userAgent.match(/(iPhone\sOS)\s([\d_]+)/)
      // 如果是Android或iPhone，则跳转至移动站点
      if (android || iphone) {
        location.href = 'http://m.itcast.cn'
      }
    })();
  </script>
</head>
<body>
  这是PC端页面
  <script src="./try.js"></script>
</body>
</html>
```

**history对象**

*管理历史记录, 与浏览器按钮前进后退对应*

*常用属性方法*

* `back()`后退
* `forward()`前进功能
* `go()` 参数为1, 前进功能 参数为-1, 后退功能 

```js
const back = document.body.children[0]
const forward = document.body.children[1]
back.addEventListener('click', function(){
    // history.back()
    history.go(-1)
})
forward.addEventListener('click', function(){
    history.forward()
    history.go(1)
})
```

## 2.29_本地存储

*html5针对需要在用户本地存储数据提出解决方案*

*数据存在用户的浏览器*

*设置读取方便,且刷新不丢失*

*容量大, 约5M*

**localstorage**

* 可以**永久性存储**数据到浏览器, 除非**手动删除, 否则关闭页面也存在**
* **同一浏览器**可以**多页面共享**数据
* 以**键值对**形式存储
* **不可跨域**

*存数据,修改数据*

* `localStorage.setItem(key, value)`
* 本地存储只能存储字符串类型, 传入**value无论什么类型,都会隐式转换成字符串**

*取数据*

* `localStorage.getItem(key)`
* 得到value**字符串**

*删除*

* `localStorage.removeItem(key)`

**sessionStorage**

* 生命周期为**关闭浏览器窗口**, 与`localStorage`区别
* 其余与`localStorage`相同

```js
// 要存储一个名字 uname, pink老师
// localStorage.setItem(键, 值)
localStorage.setItem('uname', 'pink老师')

// 获取方式
console.log(localStorage.getItem('uname'))

// 修改方式
localStorage.setItem('uname', 'red老师')

// 删除方式
// localStorage.removeItem('uname')

// 存一个年龄
localStorage.setItem('age', 18)

console.log(localStorage.getItem('age')) // 仍为字符型
```

## 2.30_本地存储处理复杂数据类型

*本地存储只能存字符串，无法直接存储复杂数据类型*

*把整个复杂类型原封不动的按字符串存入*

**语法**

* `JSON.stringify(复杂数据类型)` 将复杂数据类型，转换成JSON字符串
* `JSON.parse(JSON字符串)`得到还原后的复杂数据类型

```js
const obj = {
    uname: 'pink老师',
    age: 18,
    gender: '女'
}

// 存储复杂数据类型, 无法使用
// localStorage.setItem('obj', obj)
// 取 [object Object]
// console.log(localStorage.getItem('obj'))

// 复杂数据类型存储必须转换为JSON字符串存储
localStorage.setItem('obj', JSON.stringify(obj))

// 取 {"uname":"pink老师","age":18,"gender":"女"}
console.log(localStorage.getItem('obj'))

// JSON 对象 属性和值有引号, 而且统一是双引号

// 得到JSON字符串后, 转换为对象
console.log(JSON.parse(localStorage.getItem('obj')))
```

## 2.31_数组映射方法_map()

*可以遍历数组**处理数据**,**并返回新数组***

**语法**

```js
arr.map(function(ele数组元素, index数组索引){
  ele.. 对ele和index的操作均不会影响当前数组
  index..
  return .. -> 将什么东西return到当前元素（在自身数组不改变,在返回的数组改变）
})
```

*映射到返回数组*

```js
const arr = ['red', 'blue', 'pink']
newArr = arr.map(function(ele, index){
    console.log(ele)
    console.log(index)
    ele += '1'
    return ele
})

console.log(arr)
console.log(newArr)
```

*不需要用到`index`可以只有一个`ele`参数*

## 2.32_数组拼接字符串方法_join()

*把数组转换成一个字符串*

**语法**

* `arr.join(拼接字符)`
* 不写拼接字符按','分割
* 数组中若有非字符串元素，发生隐式转换

```js
const arr = [1, 'blue', 'pink']
console.log(arr.join(''))
```

## 2.33_对话判断框confirm

**语法**

* `confirm('提示语')`
* 弹出对话框，用户点击是, 返回`true`,点击否,返回`falses` 

```js
if(confirm('你好吗')) alert('真不错, 要开开心心的')
else alert('我很抱歉, 放松一下吧, 一切都会好起来的')
```

## 2.34_正则表达式

### 2.34.1_正则表达式及其使用

*用以匹配字符串中**特定字符组合**的**一种模式***

*在JS中, 正则表达式也是**对象***

*通常用来**查找, 替换**那些符合正则表达式的文本*

*使用场景, **验证表单合法性**, **过滤敏感词**, **从字符串中提取想要的特定部分**...*

**语法**

*先定义规则, 再按照规则查找返回*

* 定义正则表达式`const 变量名 = /表达式/`
* `/../`正则表达式的字面量
* 判断正则表达式与指定字符串**是否匹配**`正则.test(字符串)`方法 **返回布尔值, 匹配为真**s
* 检索方法`正则.exec(字符串)`方法 **匹配返回一个数组, 否则返回null**

```js
const str = '我们在学习前端, 希望学习前端能高薪毕业'
// 正则表达式使用:
// 1、定义规则
const reg = /前端/
// 2、查找 是否匹配
console.log(reg.test(str))

console.log(reg.exec(str)) // 返回数组, 存有位置
```

### 2.34.2_元字符-边界符

*字符分为**普通字符**和**元字符***

*普通字符只能匹配它本身,(a,b,c,d,前端..)*

**元字符**

*也称为特殊字符*

* 一些具有**特殊含义的字符**, 能极大提高灵活性, 具有**强大的匹配功能**

**边界符**

*表示以什么开头，什么结尾*

* `^谁`表示匹配字符以谁开始
* `谁$`表示匹配字符以谁结束
* `^谁$` 精确匹配,**字符串必须和正则完全相同,可以通过量词影响** **常用**

```js
console.log(/哈/.test('哈')) // true

console.log(/哈/.test('哈哈'))  // true

console.log(/哈/.test('二哈'))  // true

// 元字符 - 边界符

console.log(/^哈/.test('哈')) // true

console.log(/^哈/.test('哈哈'))  // true

console.log(/^哈/.test('二哈')) // false


console.log(/^哈$/.test('哈')) // true

// 精确匹配, 同时出现^和$后, 匹配字符必须和正则完全相同
console.log(/^哈$/.test('哈哈')) // false

console.log(/^哈哈$/.test('哈哈')) // true

console.log(/^哈哈$/.test('哈')) // false
console.log(/^哈哈$/.test('哈哈哈')) // false
```

### 2.34.2_元字符-量词

*用来设定**某个模式**出现的次数*

**语法**

* `*` 允许重复0次及以上
* `+` 允许重复1次及以上
* `?` 允许重复1次或0次
* `{n}` 允许重复n次
* `{n,}` 允许重复n次或更多次

```js
// '*' 出现 0 次及以上
console.log(/^哈*$/.test('哈')) // true
console.log(/^哈*$/.test('哈哈')) // true
console.log(/^哈*$/.test('')) // true
console.log(/^哈*$/.test('哈32')) // false
// 仅对 * 前内容有效
console.log(/^哈一*$/.test('哈一一')) // true
console.log(/^哈一*$/.test('哈一哈一')) // false

// + 出现 1 次及以上
console.log(/^哈+$/.test('哈哈')) // true
console.log(/^哈+$/.test('')) // false

// '?' 0 次或 1 次
console.log(/^哈?$/.test('哈哈')) // false
console.log(/^哈?$/.test('')) // true
console.log(/^哈?$/.test('哈')) // true

// {n} 重复 n 次
console.log(/^哈{3}$/.test('哈哈')) // false
console.log(/^哈{3}$/.test('哈哈哈')) // true
console.log(/^哈{3}$/.test('哈')) // false

// {n,} 重复 n 次或更多
console.log(/^哈{3,}$/.test('哈哈')) // false
console.log(/^哈{3,}$/.test('哈哈哈')) // true
console.log(/^哈{3,}$/.test('哈')) // false
console.log(/^哈{3,}$/.test('哈哈哈哈')) // true

// {n,m} 重复n次到m次 不可有空格！！
console.log(/^哈{3,5}$/.test('哈哈')) // false
console.log(/^哈{3,5}$/.test('哈哈哈')) // true
console.log(/^哈{3,5}$/.test('哈')) // false
console.log(/^哈{3,5}$/.test('哈哈哈哈')) // true
console.log(/^哈{3,5}$/.test('哈哈哈哈哈')) // true
console.log(/^哈{3,5}$/.test('哈哈哈哈哈哈')) // false
```

### 2.34.3_元字符-字符类

**语法**

* `[abc..]`匹配字符集合，包含其中的**任意一个元素**即可 **多选一!!**
* `[]`内连字符`-` `[a-z]` 表示仅可小写字母 `[0-10]` `[A-Z]` `[a-b0-5]` 连字符可直接替换为省略的所有字符
* `[]`**内**取反号`^` `[^a-z]` 表示除了小写字母以外 除了`[]`内以外字符
* `.`**除换行符外**任意字符

```js
console.log(/^[abc]$/.test('abc')) // false
console.log(/^[abc]$/.test('a')) // true
console.log(/^[abc]$/.test('b')) // true

console.log(/^[abc]+$/.test('abc')) // true
console.log(/^[abc]+$/.test('abd')) // false

console.log(/^[a-z]$/.test('A')) // false
console.log(/^[a-z]$/.test('f')) // true

console.log(/^[a-d]$/.test('f')) // false
console.log(/^[a-f]$/.test('f')) // true

console.log(/^[a-z0-9]$/.test('5')) // true
console.log(/^[a-zA-Z]$/.test('B')) // true
```

### 2.34.4_预定义类

*某些常见模式的简写方式*

* `\d`匹配 0 - 9 的任意**一个**数字，相当于`[0-9]` **常用**
* `\D`相当与`[^0-9]`
* `\w`相当于`[a-zA-Z0-9_]` 
* `\W`相当于`[^a-zA-Z0-9_]`
* `\s`相当于`[\t\r\n\v\f]` 匹配空格 包括换行符,制表符,空格符等
* `^\s`相当于`[^\t\r\n\v\f]`

### 2.34.5_修饰符

*约束正则执行的某些细节行为, 如是否区分大小写, 是否支持多行匹配*

* `/../i` ignore, 匹配时字母不区分大小写
* `/../g` global, **全局查找**匹配所有满足正则表达式的结果 在下面的字符串替换中使用

***字符串*的replace()方法**

*找到文本,做替换*

* `字符串.repalce(正则, 替代文本)`
* 这里的正则表达式为要查找内容

**正则的或**

* `/java|JAVA/`

```js
console.log(/^java$/.test('java')) // true
console.log(/^java$/.test('Java')) // false

console.log(/^java$/i.test('JavA')) // true

const str = 'java是一门编程语言, 学完java工资很高'

// 将 java 替换为 前端 i 忽略大小写 g 全局查找
const res = str.replace(/jAva/ig, '前端')

console.log(res)
```

## 表单change事件

*当表单**失去焦点**, 且**内容较得到焦点之前发生改变**时触发*

```js
const input = document.querySelector('input')

input.addEventListener('change', function(){
    console.log(111)
})
``` 

