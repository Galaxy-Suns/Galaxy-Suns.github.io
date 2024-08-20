# _壹__JS_基础语法
 
* [1.1_JS_介绍](#1.1_JS_介绍)
* [1.2_JS_书写位置](#1.2_JS_书写位置)
* [1.3_JS_的注释和结束符](#1.3_JS_的注释和结束符)
* [1.4_输入和输出](#1.4_输入和输出)
* [1.5_变量](#1.5_变量)
  * [1.5.1_变量的声明](#1.5.1_变量的声明)
  * [1.5.2_变量的赋值](#1.5.2_变量的赋值)
  * [1.5.3_更新变量](#1.5.3_更新变量)
  * [1.5.4_变量的本质_命名规则](#1.5.4_变量的本质_命名规则)
* [1.6_数组](#1.6_数组)
* [1.7_常量](#1.7_常量)
* [1.8_基本数据类型](#1.8_基本数据类型)
  * [1.8.1_数字类型`number`](#1.8.1_数字类型`number`)
  * [1.8.2_字符串类型`string`](#1.8.2_字符串类型`string`)
  * [1.8.3_模版字符串](#1.8.3_模版字符串)
  * [1.8.4_其它基本数据类型](#1.8.4_其它基本数据类型)
  * [1.8.5_检测数据类型](#1.8.5_检测数据类型)
* [1.9_类型的转换](#1.9_类型的转换)
  * [1.9.1_隐式转换](#1.9.1_隐式转换)
  * [1.9.2_显示转换](#1.9.2_显示转换)
* [1.10_赋值运算符](#1.10_赋值运算符)
* [1.11_自增运算符](#1.11_自增运算符)
* [1.12_比较运算符](#1.12_比较运算符)
* [1.13_逻辑运算符](#1.13_逻辑运算符)
* [1.14_运算符优先级\*\*](#1.14_运算符优先级\*\*)
* [1.15_分支语句](#1.15_分支语句)
  * [1.15.1_if_单分支](#1.15.1_if_单分支)
  * [1.15.2_if_双分支](#1.15.2_if_双分支)
  * [1.15.3_if_多分支](#1.15.3_if_多分支)
  * [1.15.4_三元运算符](#1.15.4_三元运算符)
  * [1.15.5_switch_分支语句](#1.15.5_switch_分支语句)
* [1.16_循环语句](#1.16_循环语句)
  * [1.16.1_while](#1.16.1_while)
  * [1.16.2_退出循环](#1.16.2_退出循环)
  * [1.16.3_for](#1.16.3_for)
* [1.17_数组](#1.17_数组)
  * [1.17.1_数组的基本使用](#1.17.1_数组的基本使用)
  * [1.17.2_数组的修改](#1.17.2_数组的修改)
  * [1.17.3_数组的新增](#1.17.3_数组的新增)
  * [1.17.4_数组的删除](#1.17.4_数组的删除)
  * [1.17.5_数组的排序](#1.17.5_数组的排序)
* [1.18_函数](#1.18_函数)
  * [1.18.1_函数的使用](#1.18.1_函数的使用)
  * [1.18.2_函数的参数](#1.18.2_函数的参数)
  * [1.18.3_函数的返回值](#1.18.3_函数的返回值)
  * [1.18.4_作用域](#1.18.4_作用域)
  * [1.18.5_匿名函数](#1.18.5_匿名函数)
* [1.19_逻辑中断](#1.19_逻辑中断)
* [1.20_转换为布尔型](#1.20_转换为布尔型)
* [1.21_对象](#1.21_对象)
  * [1.21.1_对象的使用](#1.21.1_对象的使用)
  * [1.21.2_对象的增删改查](#1.21.2_对象的增删改查)
  * [1.21.3_对象的方法](#1.21.3_对象的方法)
  * [1.21.4_遍历对象](#1.21.4_遍历对象)
  * [1.21.5_内置对象](#1.21.5_内置对象)

---

## 1.1_JS_介绍

\*一种运行在**客户端（浏览器）的编程语言**，实现**人机交互效果\***

_CSS 和 html 是标记语言，并不是编程语言。作区分_

**作用实例**

- 网页特效(监听用户行为，让网页做出相应反馈)
- 表单验证（针对表单数据的合法性判断）
- 数据交互（获取后台数据，渲染到前端 ）
- 服务器编程(node.js)

**JS 的组成部分**

- ECMAScript->JavaScript 的语法规范，语言基础
- Web APIs(分为 DOM 页面文档对象模型，BOM 浏览器对象模型)

_mdn_ web 开发权威的查找参考网站

**体验 JS**

- 写在`</body>`上方，用`<script></script>`双标签包裹

.html

```html
<body>
  <button class="pink">按钮1</button>
  <button>按钮2</button>
  <button>按钮3</button>
  <button>按钮4</button>
  <script>
    let bts = document.querySelectorAll("button");
    for (let i = 0; i < bts.length; i++) {
      bts[i].addEventListener("click", function () {
        document.querySelector(".pink").className = "";
        this.className = "pink";
      });
    }
  </script>
</body>
```

## 1.2_JS_书写位置

_回顾 CSS 书写位置_

- 行内
- 外部链接
- style 标签

_同样的，JS 也类似分为此三类_

- 行内
- 内部标签
- 外部

**内部标签**

- `<script></script>`标签包裹
- 紧挨`</body>`正上方

**外部引入**（常用）

- `<script src="my.js"></script>`引入外部 js

.html

```html
<body>
  <!-- 内部js -->
  <script>
    // 页面弹出警示框
    alert("你好,js");
  </script>
  <!-- 外部js -->
  <script src="./try.js">
    //中间不要写内容
  </script>
</body>
```

.js

```js
alert("我是外部的js文件");
```

内联会在`vue`中使用

## 1.3_JS_的注释和结束符

**注释**

- 单行注释`//` vscode 中`ctrl + /`
- 多行注释`/**/` vscode 中`shift + alt + a`

**结束符**

- `;`可写可不写(和 CSS 区别)
- _通常不加分号_

_vscode 中`shift + alt + 下箭头`将当前行复制到下一行_

_通常不加分号_

.js

```js
// 1.JavaScript注释
// 1.1单行注释 ctrl + /
/* 1.2多行注释 shift + alt + a */

//  2.JavaScript结束符
alert("第一句话");
alert("第二句话");
```

## 1.4_输入和输出

_通过键盘鼠标向计算机输入，计算机处理后，进行输出_

**输出语法**

_语法 1_

- `document.write('要输出的内容')`
- 向 body 内输出内容
- 可以写字，也可以写标签

_语法 2_

- `alert('要输出内容)`
- 页面弹出警告对话框

_语法 3_

- `console.log('控制台打印')`
- 控制台输出语法，程序员调试使用

**输入语法**

- `prompt('请输入您的姓名')`
- 显示一个对话框，对话框中包含一条文字信息，用来提示用户输入文字

```js
// 1. 文档输出内容
document.write("我是div标签");
document.write("<h1>我是标题</h1>");

// 2. 控制台打印输出 给程序员
console.log("看看对不对");
console.log("日志");
prompt("请输入你的年龄:");
```

**JS 代码执行顺序**

- 顺序执行
- 有以下特殊情况,如`alert`，`prompt`优先执行（跳过页面渲染）

**字面量**

- 工资为 1000,1000 为数字字面量
- '黑马程序员'为字符串字面量
- []数组字面量 {}对象字面量等

## 1.5_变量

_用户的数据如何存储？变量_

_计算机存储数据的容器_

**_并非数据本身，而是一个存储数据的容器_**

### 1.5.1_变量的声明

**语法**

- `let 变量名`
- 变量名也叫标识符

**声明多个变量可以`,`分隔**

- `let age = 19, uname = 'pink'`
- 不建议

### 1.5.2_变量的赋值

**语法**

- `=`

```js
// 1. 声明一个年龄变量
// let age
// 2. 赋值 = 赋值
// age = 18
// console.log(age)
// 2. 声明的同时直接赋值 变量的初始化
let age = 18;
console.log(age);
```

### 1.5.3_更新变量

_给变量赋值后，可以简单再给它赋一个不同的值来更新_

_不要重复声明！_

```js
// 1. 变量更新
let age = 18;
age = 19;
console.log(age);

// 2. 声明多个变量
let name = "Galaxy",
  uname = "pink";
// log和write打印也可以,隔开同时进行
// 提倡声明拆开单个进行，打印无所谓
console.log(age, uname);
// alert(age,uname) 不行
document.write(age, uname);
```

### 1.5.4_变量的本质_命名规则

**内存** 计算机中存储临时数据的空间

**变量的本质** 程序在**内存中申请的**一块用来存放数据的小**空间**

- 开辟这块空间是在变量声明时完成的

**变量名** 即为这个小空间的名字，便于操作这块内存

**命名规则与规范**

- 规则: **不遵守会报错** <br> 不可使用关键字，如`let` `var` `if` `for` <br> 只可由 数字，字母，下划线和`$`组成，数字不能开头 <br> 字母严格大小写 `Age` 和 `age` 是不同的变量
- 规范:**业内通识** <br> 起名要有意义 `aa` `a1` 不规范 <br> 遵循小驼峰命名法，第一个单词小写，后续单词首字母大写

**var 和 let 的区别**

- `let`解决了老版声明变量关键字`var`的一些问题:<br> 可以先使用，再声明 -> 不合理 <br> var 声明过的变量可以重复声明 -> 不合理 <br> 变量提升，全局变量，没有块级作用域等

## 1.6_数组

_一个变量中保存多个数据_

**数组的声明方式**

- `let arr = [数据1，数据2,...,数据n]`
- `[]` 数组字面量

_按顺序保存，每个数据有自己的编号 索引从 0 开始_

**取出数组中的元素**

- `数组名[索引]`

**数组中的一些术语**

- 元素 数组中的每一个数据
- 下标 数组中元素的索引
- 长度 数组中元素的个数 可通过`arr.length`属性获取 <br> 等于最后一个元素索引号 + 1

```js
// 1. 声明数组 有序
// let arr = [10, 20, 30]
let arr = ["刘德华", "张学友", "黎明", "郭富城", "pink"];
// 2.使用数组
console.log(arr[4]);

let days = [
  "星期一",
  "星期二",
  "星期三",
  "星期四",
  "星期五",
  "星期六",
  "星期日",
];
console.log(days.length);
```

## 1.7_常量

_使用`const`修饰的变量_

_当某个变量**永远不会变**，使用`const`声明，而不是`let`_

**注意**

- 常量初始化后不可更改值
- 常量声明时必须赋值，也就是要初始化

```js
// 1. 常量 不允许更改值
const PI = 3.14;
console.log(PI);
/* PI = 3.1415
console.log(PI); */ 报错;

// 2. 常量声明时必须赋值
/* const z
z = 3.14 */
```

## 1.8_基本数据类型

_计算机区分数据类型的作用 充分高效地利用内存 方便程序员使用_

_js 是一种弱数据类型语言_

### 1.8.1_数字类型`number`

_可以是整数，小数，正数，负数_

**算数运算符**

- `+ - * /`
- `%` 取余 _常来判断能不能被整除_

**算数运算符的优先级**

_优先级相同按照从左到右_

1. `()`
2. `* / %`
3. `+ -`

.js

```js
// js 弱数据类型的语言
// 只有赋值后，才知道数据类型
let num = 1 / 2;
console.log(num);
// java 强数据类型的语言
console.log(4 / 2);
console.log(4 % 2); // 求余数
```

**NaN**

_not a number_

- 一个特殊值，代表一个不正确或对一个未定义的数学操作得到的结果
- 对 NaN 操作结果仍为 NaN

### 1.8.2_字符串类型`string`

_通过单引号/双引号/反引号包裹的数据_

_js 中单引号和双引号无本质区别，推荐使用单引号_

**注意**

- 单引号/双引号可以互相嵌套，但不可嵌套自身
- 可以使用转义符`\`使得引号失效而输出

**字符串拼接**

- `+`运算符
- 不仅仅可以拼接两个字符串，还可以拼接一个字符串和其它类型

```js
let str = "pink";
let str1 = "pink";
let str2 = `中文`;

console.log(str2);

console.log(11); // 数字型
console.log(`11`); // 字符串型
console.log(str);
console.log(`str`);

// console.log('pink老师讲课非常有'激情'');
console.log('pink老师讲课非常有"激情"'); // 嵌套
console.log("pink老师讲课非常有'激情'"); // 转义符

// 字符串的拼接

console.log(1 + 1);
console.log("pink" + "老师");
console.log(str1 + str2);

let age = 25;
document.write("我今年" + age + "岁了");
```

### 1.8.3_模版字符串

_拼接字符串和变量(简化`+`拼接)_

**语法**

- ``反引号
- 用`${}`包裹住最终字符串中需要变化的变量
- 格式化标签的打印也是通过这种方式

```js
let age = 18;
// 模版字符串 外面用``包含，里面${变量名}
document.write(`我今年${age}岁了`);
```

### 1.8.4_其它基本数据类型

**布尔类型`boolean`**

_计算机中表示肯定或否定_

_取值 `true` `false`_

```js
// true false 是布尔型字面量

let isCool = true;
console.log(isCool);

console.log(3 > 4);
```

**未定义类型`undedfined`**

_取值 `undefined`_

_只声明，不赋值时的默认值_

```js
// 未定义类型 声明一个变量，未赋值(定义)

let num;
console.log(num);
```

_开发中通常声明一个变量后，等待用户传送数据，可以检测这个变量是否`undefined`判断用户是否传送数据_

**空类型`null`**

_在 js 中，`null`仅代表无，空或值未知_
_取值 `null`_

_与`undefined`区分_

- `null`赋值了，但内容为空
- `undefined`没有赋值

```js
let obj = null;
console.log(obj);
```

_使用场景 创建对象的初值_

### 1.8.5_检测数据类型

**语法**

- `typeof x`常用
- `typeof(x)`

```js
// 检测数据类型
let num = 10;
console.log(typeof num); //number
let str = "pink";
console.log(typeof str);
let str1 = "10";
console.log(typeof str1);
let flag = false;
console.log(typeof flag);
let un;
console.log(typeof un);
let obj = null;
console.log(typeof obj);
```

## 1.9_类型的转换

_用户的输入(prompt,表单)都是 string 类型_

### 1.9.1_隐式转换

_某些运算符执行，系统内部自动将数据转换_

- `+` 两边有一个字符串，会把另外一个转成字符串
- `- * / %`(除`+`外的算数运算符)，会把非数字类型转换为数字类型
- 当`+`左侧无值，如`+'12'`会使其它数据转换为数字型`12`

```js
// 隐式转换
console.log(1 + 1); // 2
console.log("pink" + 1); // pink1
console.log(2 + 2); // 4
console.log(2 + "2"); // 22 **
console.log(2 - 2); // 0
console.log(2 - "2"); // 0 **
console.log(+12);
console.log(+"123");
```

### 1.9.2_显示转换

**转换为数字类型**

_Number()_

- `Number()`
- 字符串中有非数字，转化为 NaN
- NaN 也是 number 类型

_parseInt()_

- `parseInt()`
- 字符串中**后面**有非数字，略掉
- 前面有非数字，返回 NaN
- 只保留整数

_parseFloat()_

- `parseFloat`
- 字符串中**后面**有非数字，略掉
- 前面有非数字，返回 NaN
- 可保留小数

```js
// 显式转换
let str = "123";
console.log(typeof Number(str));
console.log(Number("pink")); // NaN
let num = prompt("输入年薪");
console.log(Number(num));
console.log(+num);

console.log(parseInt("12px"));
console.log(parseInt("12.34px"));
console.log(parseInt("12.94px"));

console.log(parseFloat("12px"));
console.log(parseFloat("12.34px"));
console.log(parseFloat("12.94px"));
```

_CSS 中，给 table 添加 border-collapse: collapse;可以合并各元素的边框 bdcl_

## 1.10_赋值运算符

**语法**

- `=`
- 对变量进行赋值的运算符
- 其它 `+=` `-=` `*=` `/=` `%=`

```js
let num = 1;
// num = num + 1
num += 1;
console.log(num);
```

## 1.11_自增运算符

_二元运算符 + - _ / % =\*

_一元运算符 +'123'_

**自增运算符**

- `++`
- 前置自增`++num`，先自增,再返回值
- 后置自增`num++`,先返回值，再自增,**通常使用**

```js
// 前置自增
let i = 1;
console.log(++i); // 2
console.log(i); // 2

// 后置自增
let j = 1;
console.log(j++); // 1
console.log(j); // 2
```

## 1.12_比较运算符

**比较运算符**

- `>` `<` `>=` `<=`
- `==`判断两边**值**是否相同(会把字符型转化为数字型)
- `===` 判断两边**值和类型**是否都相同 **常用** `NaN不等于任何人包括它自`
- `!==` 左右两边是否不全等,用`===`的方式取反

```js
console.log(3 > 5);
console.log(3 >= 5);
console.log(3 >= 3);
console.log(2 == 2);
console.log(2 == "2"); // true 只判断值
console.log(2 === "2"); // false 判断值和数据类型
console.log(undefined == null); // true
console.log(NaN === NaN); // false NaN不等于任何人包括它自己
console.log("a" >= 65); //NaN
```

**字符串的比较**

- 按照 ASCII 码比较
- 两边同时都为字符串，否则会隐式转换为 number 再比较(===除外),转换不成 number,则为 NaN，`false`
- 逐个比较，直到第一个不同
- 涉及到 NaN 都为 false

## 1.13_逻辑运算符

**语法**

- `&&` `||` `!`

```js
// 逻辑与 1假则假
console.log(true && true);
console.log(false && true);
console.log(3 < 5 && 3 > 2);
console.log(3 < 5 && 3 < 2);

// 逻辑或 1真则真
console.log(true || true);
console.log(true || false);
console.log(false || false);

// 逻辑非 取反
console.log(!true);
console.log(!false);
```

## 1.14_运算符优先级\*\*

1. `()`
2. 一元运算符 `++ -- !`
3. 算数运算符 (1)`* / %` (2)`+ -`
4. 关系运算符 (1)`> >= < <=` (2)`== != === !==`
5. 逻辑运算符 (1)`&&` (2)`||`
6. `=`
7. `,`

## 1.15_分支语句

### 1.15.1_if_单分支

```js
if (条件) {
  满足条件要执行的代码;
}
```

```js
// 单分支语句
if (true) {
  console.log("执行语句");
}

if (false) {
  console.log("不执行语句");
}

// 除了0，任意数字都为真
if ("pink老师") {
  console.log("执行");
}

if ("") {
  console.log("不执行");
}
// 除了空字符串，任意字符串都为真
```

### 1.15.2_if_双分支

```js
if (条件) {
  满足条件的代码;
} else {
}
```

```js
let year = +prompt("请输入年份");
if ((!(year % 4) && year % 100) || !(year % 400)) {
  alert(`${year}年是闰年`);
} else {
  alert(`${year}年是平年`);
}
```

### 1.15.3_if_多分支

```js
if(){

}
else if(){

}
else if(){

}
...
else{

}
```

```js
let score = +prompt("请输入成绩");
if (score > 90) {
  alert("优秀");
} else if (score >= 70) {
  alert("良好");
} else if (score >= 60) {
  alert("及格");
} else {
  alert("不及格");
}
```

### 1.15.4_三元运算符

_适用于双分支结构的简化_

**语法**

- `条件?满足执行代码:不满足执行代码`

_常用来双分支返回数据_

- `= 条件?返回值1:返回值2`

### 1.15.5_switch_分支语句

```js
switch(数据){
  case 值1:
    代码1
    break
  case 值2:
    代码2
    break
    ...
  case 值n:
    代码n
    break
  default:
    代码d
}
```

- **全等匹配**

```js
// switch语句
switch (5) {
  case 1:
    console.log("您选择的是1");
    break;
  case 2:
    console.log("您选择的是2");
    break;
  case 3:
    console.log("您选择的是3");
    break;
  default:
    console.log("没有符合条件的");
}
```

_`switch`多用于固定值的情况,`if`多用于范围的情况_
_`switch`其中的查找效率较高,分支较多，可以采用_

## 1.16_循环语句

### 1.16.1_while

```js
while (条件) {
  满足执行代码(循环体);
}
```

```js
let i = 0;
while (i < 3) {
  document.write("我要循环三次<br>");
  i++;
}
```

### 1.16.2_退出循环

- `continue` `break`

_注意`continue`和`while`配合时可能出现由于没有更新判定值，导致一直死循环的现象_

```js
while (1) {
  if (prompt("你爱我吗") === "爱") {
    break;
  }
}
```

### 1.16.3_for

```js
for (let i = 0; i < n; i++) {
  循环体;
}
```

_for 配合`continue`不会出现和 while 一样跳过条件更新的情况,无需再次手动更新_

```js
let arr = ["马超", "赵云", "张飞", "关羽", "黄忠"];
for (let i = 0; i < arr.length; i++) {
  document.write(`${arr[i]}<br>`);
}
```

`for(;;)`同样可以构建死循环

## 1.17_数组

_一种顺序保存数据的数据类型(实际是一种对象)_

### 1.17.1_数组的基本使用

**数组的初始化**

_js 中的数组可以存放不同数据类型的数据_

- 字面量声明`let arr = [1, 2, true, 'pink']`
- 构造函数声明`let arr1 = new Array(1, 2, 3, 4)`

### 1.17.2_数组的修改

- `数组[下标] = 新值`

```js
let arr = [];
console.log(arr);
console.log(arr[0]); // undefined
arr[0] = 1;
console.log(arr[0]); // 1
arr[5] = 2;
console.log(arr); // [1, 空 ×4, 2]
let colors = ["pink", "red", "green"];
colors[0] = "yellow";
console.log(colors);
for (let i = 0; i < colors.length; i++) {
  colors[i] = colors[i] + "老师";
}
console.log(colors);
```

### 1.17.3_数组的新增

- `数组.push(元素1, 元素2, 元素3,...)` 将一个/多个元素添加到数组的末位，**并返回新数组的长度**

- `数组.unshift(元素1, 元素2, 元素3,...)` 将一个/多个元素添加到数组的开头，**并返回新数组的长度** (_添加多个元素时，新添加元素的顺序不变_)

```js
let arr = ["pink", "hotpink"];
arr.push("deeppink");
console.log(arr);
arr.push(1, 2, 3);
console.log(arr);
arr.unshift(1, 2, 3);
console.log(arr);
```

### 1.17.4_数组的删除

- `数组.pop()`删除数组中的**最后一个**元素，**返回删除元素的值**
- `数组.shift()`删除数组中的**第一个**元素，**返回删除元素的值**
- `数组.splice(起始位置, 删除几个元素)`如果删除几个元素不写，默认删到最后 **返回删除元素的值** **常用**

```js
let arr = ["red", "green", "blue"];
// console.log(arr.pop())
// console.log(arr)

// console.log(arr.shift())
// console.log(arr)

// 删除指定元素
arr.splice(1, 1);
console.log(arr);
```

### 1.17.5_数组的排序

```js
arr.sort(function (a, b) {
  return a - b;
});
```

升序排序

```js
arr.sort(function (a, b) {
  return b - a;
});
```

降序排序

## 1.18_函数

_实现代码复用提高开发效率_

### 1.18.1_函数的使用

_先声明，后调用_

**函数的声明**

```js
function 函数名() {
  函数体;
}
```

**函数的命名规范**

- 小驼峰
- 前缀尽量用动词

**函数的调用**

- `函数名()`

```js
function getSum(a, b) {
  return a + b;
}

function getSum100() {
  let sum = 0;
  for (let i = 0; i < 100; i++) {
    sum += i + 1;
  }
  return sum;
}

console.log(getSum(1, 6));
console.log(getSum100());
```

### 1.18.2_函数的参数

**语法**

```js
function 函数名(参数列表) {
  函数体;
}
```

_形参和实参_

**默认参数**

```js
function 函数名(参数 = 默认值) {
  函数体;
}
```

_有些参数设置默认值，在赋值时，顺序不变，仍从左往右，因此，设置默认值的参数，放到后面会好一些_

_开发中参数都设置默认值是使程序更健壮_

```js
function getSum(end, start = 1) {
  let sum = 0;
  for (let i = start - 1; i < end; i++) {
    sum += i + 1;
  }
  return sum;
}

console.log(getSum(5));
```

_js 中，形参和实参个数可以不同，形参多:自动补 undefined，实参多:多的省略_

### 1.18.3_函数的返回值

**语法**

- `return`

```js
// 函数的返回值
function fn() {
  return 20;
}

console.log(fn());
```

_return 以后的代码不会执行，因此不要换行写_

_return 后面不写或没有 return,返回值为 undefined_

### 1.18.4_作用域

_可用性的代码范围_

**全局作用域**

- **文件/script 标签内有效，函数内有效**
- 函数外定义的变量

**局部作用域**

- 函数内有效
- 函数内定义

### 1.18.5_匿名函数

**语法**

- `function() {}`

**使用方法**

- 函数表达式 `let fn = function() {}` <br> _和具名函数的区别_ 具名函数的调用可以写到定义前，而函数表达式不行。

- 立即执行函数 _避免全局变量之间的污染_

```js
/* fn = function(){}
fn() */
(function () {})();
```

_立即执行函数**的前后**必须加分号_

```js
(function () {})();
```

## 1.19_逻辑中断

- `x = x || 0`常用于替代函数默认参数

**逻辑运算符中的短路**

- `&&`左边为假，则不再执行右边
- `||`左边为真，则不再执行右边

`log(11 && 22)//22`两边都真，返回最后一个真值
`log(undefined || 0)//0`两边都假，返回最后一个假值

## 1.20_转换为布尔型

- `''` `0` `undefined` `null` `false` `NaN`转换后为假，其余为真
- `[]`为真！！

## 1.21_对象

_一种数据类型 object，可以详尽描述某个事物_

_一种无序的数据集合，注意:数组是有序的数据集合_

_行为和属性_

### 1.21.1_对象的使用

**声明对象**

- `let 对象名 = {}`
- `let 对象名 = new Object()`

_对象由属性和方法组成_

```js
let 对象名 = {
  属性名: 属性值,
  方法名: 函数,
};
```

```js
let goods = {
  goodsname: "小米（MI）",
  num: "100012816024",
  weight: "0.55kg",
  address: "中国大陆",
};
console.log(goods);
```

### 1.21.2_对象的增删改查

**查**

- `对象名.属性`

- `对象名['属性名']`

**改**

- `对象名.属性 = 新值`

**增**

- `对象名.新属性 = 新值`

**删**

- `delete 对象名.属性` **不建议，严格模式下不允许**

```js
console.log(goods.address);
console.log(goods.name);

goods.weight = "0.56kg";
console.log(goods);

goods.state = "运输中";
console.log(goods);

delete goods.weight;
console.log(goods);
```

_查的另外方法_

```js
let goods = {
  "goods-name": "小米小米10 青春版",
  num: "100012816024",
  weight: "0.55kg",
  address: "中国大陆",
};
console.log(goods);

goods["goods-name"] = "小米10 PLUS";
goods.color = "粉色";

document.write(
  goods["goods-name"],
  "<br>",
  goods.num,
  "<br>",
  goods.weight,
  "<br>",
  goods.address,
  "<br>",
  goods.color
);
```

### 1.21.3_对象的方法

```js
let obj = {
  uname: "刘德华",
  // 方法
  sing: function () {
    console.log("冰雨");
  },
};
//
obj.sing();
```

### 1.21.4_遍历对象

_对象是无序的，不能通过索引号变量_

**语法** `for in`

```js
let arr = ["pink", "red", "blue"];
for (let k in arr) {
  console.log(k); // k是数组的下标/索引号 字符串型！
  console.log(arr[k]); // 不推荐遍历数组
}

let obj = {
  uname: "pink",
  age: 18,
  gender: "男",
};
for (let k in obj) {
  console.log(obj[k]);
}
```

_一定要注意通过[]而不是.(由于 k 字符型)_

### 1.21.5_内置对象

_js 中提供的内置对象，包含各种属性和方法提供给开发者_

**内置对象-Math**

```js
// 属性
console.log(Math.PI);
// 方法
console.log(Math.ceil(1.1)); // 向上取整
console.log(Math.floor(1.1)); // 向下取整
console.log(Math.round(1.1)); // 四舍五入
console.log(Math.round(-1.5)); // 四舍五入 -.5特殊,    为-1

console.log(Math.max(1, 2, 3, 4, 5));
console.log(Math.min(1, 2, 3, 4, 5));

console.log(Math.abs(-1)); //绝对值
console.log(Math.pow(2, 3)); //幂
```

**随机数**

- `Math.random()`返回一个[0-1)之间的随机小数

```js
console.log(Math.random());
// 左闭右开，能取到0，但是取不到1的随机小数
console.log(10 * Math.random());
console.log(Math.floor((10 + 1) * Math.random())); // 0 - 10的整数

// 闭
function getRandomInt(start, end) {
  return Math.floor(start + (end - start + 1) * Math.random());
}

console.log(getRandomInt(4, 8));
```

