# JavaScript

---

_一些工具_

- spipaste 截图`f1`和放置在桌面`f3` <br> 可查看颜色，`shift`切换十六进制和 rgb，再按下 c 粘贴

*常用文档*

https://developer.mozilla.org/zh-CN/

## _壹_ JS 基础语法

---

### 1.1 JS 介绍

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

### 1.2 JS 书写位置

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

### 1.3 JS 的注释和结束符

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

### 1.4 输入和输出

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

### 1.5 变量

_用户的数据如何存储？变量_

_计算机存储数据的容器_

**_并非数据本身，而是一个存储数据的容器_**

#### 1.5.1 变量的声明

**语法**

- `let 变量名`
- 变量名也叫标识符

**声明多个变量可以`,`分隔**

- `let age = 19, uname = 'pink'`
- 不建议

#### 1.5.2 变量的赋值

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

#### 1.5.3 更新变量

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

#### 1.5.4 变量的本质、命名规则

**内存** 计算机中存储临时数据的空间

**变量的本质** 程序在**内存中申请的**一块用来存放数据的小**空间**

- 开辟这块空间是在变量声明时完成的

**变量名** 即为这个小空间的名字，便于操作这块内存

**命名规则与规范**

- 规则: **不遵守会报错** <br> 不可使用关键字，如`let` `var` `if` `for` <br> 只可由 数字，字母，下划线和`$`组成，数字不能开头 <br> 字母严格大小写 `Age` 和 `age` 是不同的变量
- 规范:**业内通识** <br> 起名要有意义 `aa` `a1` 不规范 <br> 遵循小驼峰命名法，第一个单词小写，后续单词首字母大写

**var 和 let 的区别**

- `let`解决了老版声明变量关键字`var`的一些问题:<br> 可以先使用，再声明 -> 不合理 <br> var 声明过的变量可以重复声明 -> 不合理 <br> 变量提升，全局变量，没有块级作用域等

### 1.6 数组

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

### 1.7 常量

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

### 1.8 基本数据类型

_计算机区分数据类型的作用 充分高效地利用内存 方便程序员使用_

_js 是一种弱数据类型语言_

#### 1.8.1 数字类型`number`

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

#### 1.8.2 字符串类型`string`

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

#### 1.8.3 模版字符串

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

#### 1.8.4 其它基本数据类型

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

#### 1.8.5 检测数据类型

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

### 1.9 类型的转换

_用户的输入(prompt,表单)都是 string 类型_

#### 1.9.1 隐式转换

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

#### 1.9.2 显示转换

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

### 1.10 赋值运算符

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

### 1.11 自增运算符

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

### 1.12 比较运算符

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

### 1.13 逻辑运算符

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

### 1.14 运算符优先级\*\*

1. `()`
2. 一元运算符 `++ -- !`
3. 算数运算符 (1)`* / %` (2)`+ -`
4. 关系运算符 (1)`> >= < <=` (2)`== != === !==`
5. 逻辑运算符 (1)`&&` (2)`||`
6. `=`
7. `,`

### 1.15 分支语句

#### 1.15.1 if 单分支

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

#### 1.15.2 if 双分支

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

#### 1.15.3 if 多分支

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

#### 1.15.4 三元运算符

_适用于双分支结构的简化_

**语法**

- `条件?满足执行代码:不满足执行代码`

_常用来双分支返回数据_

- `= 条件?返回值1:返回值2`

#### 1.15.5 switch 分支语句

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

### 1.16 循环语句

#### 1.16.1 while

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

#### 1.16.2 退出循环

- `continue` `break`

_注意`continue`和`while`配合时可能出现由于没有更新判定值，导致一直死循环的现象_

```js
while (1) {
  if (prompt("你爱我吗") === "爱") {
    break;
  }
}
```

#### 1.16.3 for

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

### 1.17 数组

_一种顺序保存数据的数据类型(实际是一种对象)_

#### 1.17.1 数组的基本使用

**数组的初始化**

_js 中的数组可以存放不同数据类型的数据_

- 字面量声明`let arr = [1, 2, true, 'pink']`
- 构造函数声明`let arr1 = new Array(1, 2, 3, 4)`

#### 1.17.2 数组的修改

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

#### 1.17.3 数组的新增

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

#### 1.17.4 数组的删除

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

#### 1.17.5 数组的排序

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

### 1.18 函数

_实现代码复用提高开发效率_

#### 1.18.1 函数的使用

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

#### 1.18.2 函数的参数

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

#### 1.18.3 函数的返回值

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

#### 1.18.4 作用域

_可用性的代码范围_

**全局作用域**

- **文件/script 标签内有效，函数内有效**
- 函数外定义的变量

**局部作用域**

- 函数内有效
- 函数内定义

#### 1.18.5 匿名函数

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

### 1.19 逻辑中断

- `x = x || 0`常用于替代函数默认参数

**逻辑运算符中的短路**

- `&&`左边为假，则不再执行右边
- `||`左边为真，则不再执行右边

`log(11 && 22)//22`两边都真，返回最后一个真值
`log(undefined || 0)//0`两边都假，返回最后一个假值

### 1.20 转换为布尔型

- `''` `0` `undefined` `null` `false` `NaN`转换后为假，其余为真
- `[]`为真！！

### 1.21 对象

_一种数据类型 object，可以详尽描述某个事物_

_一种无序的数据集合，注意:数组是有序的数据集合_

_行为和属性_

#### 1.21.1 对象的使用

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

#### 1.21.2 对象的增删改查

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

#### 1.21.3 对象的方法

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

#### 1.21.4 遍历对象

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

#### 1.21.5 内置对象

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

## _贰_ WebAPIs

_API 通过 js 操作 html 和浏览器_

_分为 DOM 文档对象模型,BOM 浏览器对象模型_

### 2.1 声明变量优先使用`const`

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

### 2.2 DOM 初识

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

### 2.3 获取 DOM 元素

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

### 2.4 操作元素内容

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

### 2.5 操作元素属性

#### 2.5.1 操作元素常用属性

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

#### 2.5.2 操作元素的样式属性

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

#### 2.5.3 操作表单元素的属性

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

#### 2.5.4 自定义属性

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

### 2.6 定时器 间歇函数

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

### 2.7 事件监听

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

### 2.8 事件监听版本

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

### 2.9 鼠标事件

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

### 2.10 焦点事件

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

### 2.11 键盘事件和用户输入事件

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

### 2.12 事件对象

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

### 2.13 环境对象

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

### 2.14 回调函数

_将某一函数作为参数传给另一函数，前者为回调函数_

- `setInterval(fn , 1000)`
- `addEventListener('click',fn)`
- `arr.sort(fn)`

_css 伪类型 checkbox:checked 选择选中的 checkbox 复选框_

### 2.15 事件流

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

### 2.16 解绑事件

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

### 2.17 鼠标经过事件

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

### 2.18 事件委托

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

### 2.19 阻止元素的默认行为

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

### 2.20 其它事件

#### 2.20.1 页面加载事件 load

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

#### 2.20.2 DOMContentLoaded

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

#### 2.20.3 元素滚动事件 scroll

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

#### 2.20.4 页面尺寸事件 resize

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

### 2.21 元素尺寸与位置

_获取页面滚动到某个元素的位置，就去做某个元素_

_而不是去实际测量测量 省去计算_

_通过 js 获取元素在页面的位置_

#### 2.21.1 元素尺寸与位置 尺寸 offsetWidth

- `offsetWidth`和`offsetHeight`**属性**
- 获取元素自身宽高，包含元素自身设置的宽高，`padding`,`border`,滚动条 与`client`系列区别于`border`，滚动条
- 可视宽高，`display: none`获取的是`0`

#### 2.21.2 元素尺寸与位置 位置 offsetTop

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

#### 2.21.3 元素尺寸与位置 getBoundingClientRect()

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

### 2.22 日期对象的使用

_让网页显示 日期，时间_

_用来表示时间的对象_

_可以得到当前系统时间_

#### 2.22.1 日期对象实例化

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

#### 2.22.2 日期对象方法

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

#### 2.22.3 时间戳的使用

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

### 2.23 节点操作

*对页面元素进行增删改查*

*DOM树的每一个内容都称为结点*

**元素节点***主要*

* **所有的标签**如`body`, `div`
* `html`是根节点

**属性节点**

* **所有的属性**如`href`

**文本节点**

* 所有的文字

#### 2.23.1 查找DOM节点

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

#### 2.23.2 增加节点

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

#### 2.23.3 删除节点

*在JS原生DOM操作中, 要删除元素必须通过父元素删除*

**语法**

* 元素对象方法`父元素.removeChild(要删除的元素)`
* 如不存在**直接父子关系**则删除不成功
* 不同于`display: none ` `removeChild`真正删掉了节点

```js
const ul = document.querySelector('ul')
sul.removeChild(ul.children[0])
```

### 2.24 M端事件

*待补充*


### 2.25 swiper插件

**插件**

* 其他人封装好的一些代码，可以直接实现对应效果

**swiper插件使用的基本流程**

1. 熟悉官网，了解这个插件可以完成什么需求
2. 看在线演示，找到符合自己需求的demo
3. 查看基本使用流程
4. 查看api文档，配置自己的需求
5. *注意 多个swiper同时使用，类名注意区分*

*待补充*

### 2.25 BOM和延迟函数setTimeout

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

### 2.26 事件循环eventloop

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

### 2.27 location对象

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

### 2.28 navigator对象和history对象

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

### 2.29 本地存储

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

### 2.30 本地存储处理复杂数据类型

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

### 2.31 数组映射方法 map()

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

### 2.32 数组拼接字符串方法 join()

*把数组转换成一个字符串*

**语法**

* `arr.join(拼接字符)`
* 不写拼接字符按','分割
* 数组中若有非字符串元素，发生隐式转换

```js
const arr = [1, 'blue', 'pink']
console.log(arr.join(''))
```

### 2.33 对话判断框confirm

**语法**

* `confirm('提示语')`
* 弹出对话框，用户点击是, 返回`true`,点击否,返回`falses` 

```js
if(confirm('你好吗')) alert('真不错, 要开开心心的')
else alert('我很抱歉, 放松一下吧, 一切都会好起来的')
```

### 2.34 正则表达式

#### 2.34.1 正则表达式及其使用

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

#### 2.34.2 元字符-边界符

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

#### 2.34.2 元字符-量词

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

#### 2.34.3 元字符-字符类

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

#### 2.34.4 预定义类

*某些常见模式的简写方式*

* `\d`匹配 0 - 9 的任意**一个**数字，相当于`[0-9]` **常用**
* `\D`相当与`[^0-9]`
* `\w`相当于`[a-zA-Z0-9_]` 
* `\W`相当于`[^a-zA-Z0-9_]`
* `\s`相当于`[\t\r\n\v\f]` 匹配空格 包括换行符,制表符,空格符等
* `^\s`相当于`[^\t\r\n\v\f]`

#### 2.34.5 修饰符

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

### 表单change事件

*当表单**失去焦点**, 且**内容较得到焦点之前发生改变**时触发*

```js
const input = document.querySelector('input')

input.addEventListener('change', function(){
    console.log(111)
})
``` 

## *叁* ES6+ 语法

---

### 3.1 作用域

#### 3.1.1 局部作用域

*分为**函数作用域**和**块作用域***

##### 函数作用域 

* **函数内部声明的变量只能在函数内部被访问**, 外部无法访问
* **函数的参数**也是函数内部的**局部变量**

##### {} 块作用域

* 在JS中使用`{}`包裹的代码都叫做代码块, 外界**有可能**无法访问 *`var`声明的可以访问* 
* 推荐使用`let`, `const`

```js
// 块作用域
for(let i = 0; i < 3; i++){
  console.log(i);
}
// console.log(i); // 报错 Uncaught ReferenceError: i is not defined
// if while等
```

#### 3.1.2 全局作用域

* **最外层即为全局作用域**, 全局作用域声明的变量, 在其它作用域均可访问
* 尽可能少声明, 避免污染
* 为`window`对象动态添加的属性默认也为全局, **不推荐**

#### 3.1.3 作用域链

*本质为**变量查找机制***

* **优先在当前函数作用域中查找**
* 如果查找不到, **依次逐级查找父级作用域**直到全局作用域
* 子级作用域可以访问父级, 但父级不能查找子级

```js
let a = 1;
let b = 2;
const f = () => {
  let a = 1;
  const g = () => {
    a = 2;
    console.log(a);
  }
  g();
}
f(); // 2
```

#### 3.1.4 垃圾回收机制

*JS中内存的分配和回收自动完成, 内存在不使用的时候会被**垃圾回收器自动回收***

##### 内存生命周期

1. 内存分配 声明时自动分配内存
2. 内存使用 使用变量, 函数等
3. 内存回收 使用完毕, 垃圾回收器自动回收

* 全局变量一般不会回收, 关闭页面时回收
* 一般局部变量的值, 不用了, 会自动回收

**堆内存的回收算法**

* 引用计数法: 根据对象的引用次数来进行回收, 当引用为0时回收。*会在对象相互引用时造成内存泄露* *不再使用*
* 标记清除法: *回收无法到达的对象*, 从根部出发, 定时扫描堆中对象, 找不到则回收。

##### 内存泄露

程序中分配的内存由于某种原因, 程序未释放或无法释放即为内存泄露

#### 3.1.5 闭包

*一个函数对周围状态的引用捆绑在一起, 内层函数中访问到其外层函数的作用域*

*闭包  = 内层函数 + 外层函数作用域的变量*

```js
// f 调用了父函数 outer 作用域下的 a 变量产生了闭包
const outer = () => {
  const a = 1;
  const f = () = {
    console.log(a);
  }
  f();
}
outer();
```

* 简单的内外函数嵌套不会产生闭包, **内函数调用了外函数的变量才会产生**
* 作用: **封闭数据, 提供操作, 由函数维护变量**
* 对于函数维护的变量有**内存泄露**的问题, 当页面关闭时才会回收

```js
// 闭包的基本格式 函数内部维护了变量a
const outer = () => {
  let a = 10;
  const fn = () => {
    console.log(a);
  };
  return fn;
}
const fun = outer();
fun();
```

```js
// 闭包的应用 私有化变量 统计函数调用次数
const outer = () => {
  let cnt = 0;
  const fn = () => {
    console.log("这是我第" + ++ cnt + "次被调用");
  }
  return fn;
}
const f = outer();
for (let i = 0; i < 10; i ++){
  f();
}
```

#### 3.1.6 var 变量提升

*JS的一个缺陷*

* 代码在执行前, 先检测**当前作用域下所有`var`声明的变量**, 并且把**所有`var`声明的变量的*声明*提到*当前作用域*的最前面** *只提升声明, 不提升赋值*

```js
// 由于变量提升 num 的声明被放在最前, 因此不报错, 为 undefined
// 提升: var num;
console.log(num + "件");
var num = 10;
```
### 3.2 函数

#### 3.2.1 函数提升

* 代码执行前, 会把所有函数定义提升到**当前作用域的最前面**
* 但是把**匿名函数**/**箭头函数**赋给`const`, `let`修饰的变量则不会提升,(`var`由于只提升了声明为`undefined`不是一个函数也会报错)
* 推荐写在前面

```js
// 函数提升, 可以正常调用
fn();
function fn(){
  console.log("函数提升");
}
```

#### 3.2.2 动态参数, 剩余参数和展开运算符

##### arguments 动态参数

* `arguments`是函数内部内置的**伪数组变量**, 包含了调用函数时**传入的所有实参**
* *箭头函数中没有此变量*

```js
const getSum = function (){
  let sum = 0;
  for(let i = 0; i < arguments.length; i++){
    sum += arguments[i];
  }
  return sum;
}
let sum = getSum(1, 4, 3, 2, 2);
console.log(sum);
```

##### ...others 剩余参数

**推荐函数**

* 允许将一个**不定数量的参数表示为一个数组**
* 箭头函数也能用
* 可以有一部分参数, 其余传入的实参传入到剩余参数的数组中 `(a, b, ...arr)`

```js
// ...变量名 定义剩余参数
const getSum = (...other) => {
    let sum = 0;
    for(let i = 0; i < other.length; i++){
        sum += other[i];
    }
    return sum;
}
let sum = getSum(2, 4, 5, 12);
console.log(sum);
```

##### ... 展开运算符 (与函数无关, 放在此处仅做区分)

* 将数组展开
* 不会修改原数组
* 拆成了独立的数组, 可以传入这种 `f(...others)` 这种不定参数函数中
* 应用于求数组的最大最小值, 合并数组等
* 也可以展开对象

```js
// 运用 展开运算符 进行最大值计算 上下两种传入的参数完全相同
const arr = [1, 4, 5, 2]; 
console.log(Math.max(1, 4, 5, 2));
console.log(Math.max(...arr)); // ...arr = 1, 2, 3
const arr2 = [2, 4, 6];
const arr3 = [...arr, ...arr2]; // 合并数组
```

#### 3.2.3 箭头函数

*更适用于原本就需要匿名函数的地方*

##### ()=>{} 语法

```js
(形参) => {函数体}
```

* **形参只有一个时**, 括号可以省略 `形参 => {函数体}`
* **无形参时**, 括号不能省略 `() => {函数体}`
* 函数体中**除了返回值外不进行其他操作**, 可以直接写返回值`(形参) => 返回值`

##### this 指向

**传统函数的指向** 谁调用就指向谁

```js
// 传统函数通过谁调用就指向谁(是谁的方法就指向谁)
const obj = {
  name: 'andy',
  sayHi: function(){
    console.log(this);
  }
}
obj.sayHi();
function fn(){
  console.log(this);
  obj.sayHi();
}
window.fn();
```

**箭头函数不会创建自己的this, 从自己的作用域链的上一层沿用其this**

```js
// 向上一层 找, 上一层是谁的属性/方法就指向谁
const obj = {
  name: 'andy',
  sayHi: () => {
    console.log(this);
  }
}
obj.sayHi();
const fn = () => {
  console.log(this);
  obj.sayHi();
}
fn();
```

*事件监听不推荐使用箭头函数, 因为此时的this不是DOM元素*

### 3.3 解构赋值

#### 3.3.1 const [] 数组解构

*用简洁的语法增强语义*

* 将数组的单元值快速批量赋值给一系列变量的简洁语法

```js
// 简洁地将arr的三个元素赋给三个变量
const arr = [1, 2, 3];
const [min, avg, max] = arr;
console.log(min);
console.log(avg);
console.log(max);
```

```js
// 典型应用 利用数组解构交换两个变量
let a = 1;
let b = 2; // 此处不可省略分号 否则会把下一行的数组认作上一行的结尾
[a, b] = [b, a];
console.log(a);
console.log(b);
```

**一些情况**

* 变量多, 单元值少 `[a, b, c] = [b, a]; // c undefined`
  * 利用默认值优化 `[a = 0, b = 0, c = 0] = [b, a] // c 0`
* 变量少, 单元值多  `[a] = [b, a]; // a为b的值`
  * 利用剩余参数优化 `[a, ...others] = [1, 3, 4, 5]`
* 按需导入赋值 `[a, , , b] = [1, 2, 3, 4, 5] // a 1 b 4`
* 多维数组解构 `[a, , , [, b]] = [1, 2, 3, [3, 4], 5]; // b 4`

#### 3.3.2 const {} 对象解构

* 将对象的属性和方法**简介批量赋值给一系列变量**的简介语法
* **解构的变量名必须要和属性名相同**
* 可以更名  `const {uname: username, age} = obj;`

```js
// 解构 obj 并赋值
const obj = {
    uname: "pink",
    age: 18
};
const {uname, age} = obj;
console.log(uname);
console.log(age);
```

```js
// 数组 和 对象的嵌套解构
const arr = [0, {
    uname: "pink",
    age: 18
}];
const [, {uname:username, age}] = arr;
console.log(username);
console.log(age);
```

*可以巧妙地运用到传参*

#### 3.3 .forEach 数组变量 （补充内容）

> arr.forEach((d, i)=>{...})

* 回调函数  对于数组的每个元素进行操作
  * `d` 数组的每个数据
  * `i` 当前元素的下标 

### 3.4 对象

#### 3.4.1 创建对象的三种方式

* 字面量创建 `const o = {..};`
* new关键字创建 `const o = new object({..});`
* 构造函数创建 **可以快速创建多个类似的对象**

#### 3.4.2 构造函数

在本质上为**常规函数**, 不可为箭头函数

约定:

* 命名以大写字母开头
* 只由`new`操作符执行

```js
// 小猪对象构造函数
const Pig = function(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
}
const p1 = new Pig("sun", 20, "man");
const p2 = new Pig("shi", 19, "man");
console.log(p1);
```

* 通过 `new` 函数调用构造函数称为**实例化**
* 构造函数中无需`return`
* 构造函数的this**指向新的生成对象**

**new操作符的实例化机制**

1. 调用`new`后, 产生一个新的空对象, 后面的构造函数的`this`指向这个空对象
2. 开始执行构造函数, 依次给这个空对象添加属性
3. 结束后`new`自动返回这个新对象

#### 3.4.3 实例成员和静态成员

* 通过构造函数`new`出来的实例对象, 其中的成员为**实例成员**, 分为**实例属性**和**实例方法**
* 通过多次`new`出来的实例对象彼此不影响

```js
// 通过构造函数Pig创建两个实例对象, 尽管结构和值相同, 仍为两个对象, 存储于不同地址
const Pig = function(name){
    this.name = name;
};
const p1 = new Pig("a");
const p2 = new Pig("a");
console.log(p1 === p2); // false
```

* **挂载在构造函数上的属性和方法叫做静态成员**
* 如之前使用的`Math.max()`即为静态属性, 直接通过构造函数调用

```js
// 给构造函数Pig挂载静态属性和方法
const Pig = function(name){
    this.name = name;
};
Pig.eyes = 2;
Pig.sleep = () => {
    console.log("I am sleeping");
}
console.log(Pig.eyes);
Pig.sleep();
```

#### 3.4.4 简单数据类型的包装

* 对于**简单数据类型**, JS底层也会进行包装, 构造为一个**对象**, 从而提供相应的方法和属性

> const str = 'abc'; -底-层-包-装-> const str = new String('abc');

#### 3.4.5 内置构造函数

##### Object

> const user = {...} -等-价-于-> const user = new Object({...})

**Object 常用静态方法**

* `Object.keys` 获取对象中所有的**属性名(key)**
* `Object.values` 获取对象中所有的**属性值(value)**
* `Object.assign(target, source)` 拷贝对象, 仍为两个对象, 不改变`target`原先的, 不和`source`冲突的属性, (冲突则覆盖) **常用于属性追加**

```js
// 通过Object.keys .values 输出p1所有属性名 属性值
const Pig = function(name, age, gender){
    this.name = name;
    this.age = age;
    this.gender = gender;
};
const p1 = new Pig("peiqi", 18, "man");
console.log(p1);
console.log(Object.keys(p1));
console.log(Object.values(p1));
```

```js
// 通过Object.assign 拷贝 p1的成员 到 p2
const Pig = function(name, age, gender){
    this.name = name;
    this.age = age;
    this.gender = gender;
};
const p1 = new Pig("peiqi", 18, "man");
const p2  = {firstname: "sun"};
Object.assign(p2, p1); 
console.log(p2); // 三个属性
console.log(p2 === p1); // false
```

##### Array

> const user = [...] -等-价-于-> const user = new Array(...)

**Array的*实例方法***

* `arr.forEach()` **不返回数组**, 遍历数组元素
* `arr.filter()` **返回新数组**, 返回的是**筛选满足条件**的数组元素组成的数组
* `arr.map()` **返回新数组**, 返回的是处理之后的数组元素组成的数组
* `arr.reduce((prev, current) => {...return newprev} [, 初始值])` **返回累计处理的结果, 常用于求和**
  * 回调函数, 表示对当前元素和累计的结果进行一次处理
    * `prev` 目前累计的结果
    * `current` 当前元素
    * 每一次回调函数执行完毕会把返回值作为下一次(数组下一个元素)的`prev`
    * 当本次回调函数的`current`为数组最后一个元素, 返回值即为最终的`arr.reduce()`的返回值
  * 初始值, 表示最初的`prev`
    * 不传入初始值参数时, `prev`默认为数组第一个值, 此时`current`为数组第二个值
    * 传入初始值参数时, `prev`为初始值, `current`为数组第一个值

```js
// 利用 arr.reduce 数组求和, 无初始值, 因此第一次 prev 4 current 5
// 4 5 => 9
// 9 8 => 17
const arr = [4, 5, 8];
const sum = arr.reduce((prev, current) => {
  console.log(prev);
  console.log(current);
  console.log('---');
  return prev + current;
})
console.log(sum);
```

```js
// 筛选器arr.filter 传入 bool 类型函数, 筛选大于 7 的数
const arr = [4, 5, 8, 9, 10];
const newArr = arr.filter(d => d > 7);
console.log(newArr);
```

#### 3.4.6 prototype 原型对象

##### 挂载实例方法到原型对象

*构造函数用于封装存在着内存浪费的问题: 不同实例对象的实例方法彼此不同, 都是`new`关键字调用构造函数时, 重新创建的函数*

* 构造函数可以通过**原型**分配的函数实现实例对象间**方法共享**
* JS规定, 每一个构造函数都有一个`prototype`属性, 指向一个对象, 即为原型对象
* 这个**对象可以挂载函数, 对象实例化不会多次创建原型上的函数, 节约内存**
* 所以**实例对象的属性应写在构造函数, 方法写在原型对象身上**

```js
// 实例方法挂载在对象原型和直接在构造函数上定义的的对比
const Pig = function(name){
    this.name = name;
    this.tmpf = () => {};
}
Pig.prototype.sayHello = () => {
  
  console.log("sayHello");
}
const p1 = new Pig("a");
const p2 = new Pig("b");
p1.sayHello();
console.log(p1.sayHello === p2.sayHello); // true
console.log(p1.tmpf === p2.tmpf); // false
```

```js
// 手写数组求和 推荐在原型对象挂载实例方法时也采用function 箭头函数的this指向window 
Array.prototype.sum = function(){
  return this.reduce((prev, current) => prev + current);
};
console.log([1, 3, 5].sum());
```

##### constructor 属性

* 指向了构造函数 : 原型对象为构造函数的一个属性, 而构造函数又是原型对象的一个属性, *共轭父子*
* **修改原型对象时, 一定保证`constructor`属性指向构造函数**

```js
// 给原型对象批量挂载方法时, 利用 Object.assign 而非直接 = , 这样保证了原型对象仍保有 constructor 属性
const Pig = function(name){
  this.name = name;
}
console.log(Pig.prototype);
Object.assign(Pig.prototype, {
    sing: function(){
        console.log("singing");
    },
    dance: function(){
        console.log("dancing");
    }
})
console.log(Pig.prototype);
```

##### \_\_proto\_\_ 对象原型

* **实例对象中** 通过`__proto__`找到构造函数的原型对象`prototype`, 从而给自身挂载属性和方法
* 在浏览器中表现为`[[prototype]]`
* 只读

```js
// 理解 p1 实例对象的对象原型 和 Pig 构造方法的原型对象
const Pig = function(){};
const p1 = new Pig();
console.log(p1.__proto__ === Pig.prototype); // true
```

##### 原型继承

* 即为直接把某一对象作为原型, 赋给构造函数的原型对象, 使得实例对象可以调用这个原型中的属性和方法
* 注意原型对象仍要保留`construction`
* 由于属性和方法放在了原型对象中, 所有的实例对象共用这些属性(复杂属性)和方法, *不过简单类型倒是没有这个问题, 我推测实例对象在调用对象原型中的属性和方法时, 还有一步赋值操作, 简单类型赋值后就是另外一个变量了, 因此不冲突, 而复杂类型赋值的是地址, 因此会互相影响*

```js
// 利用 assign 优化原型继承
// 此外, 单纯的 Woman.prototype = Person(即使有construction)还会造成浅拷贝导致的, 多个子类继承同一父亲, 属性方法互相冲突, 可以用 new Person解决, 但我觉得还是不如assign爽快
Object.prototype.add = function(obj){
    Object.assign(this, obj);
};
const Person = {
    ears: 2,
    head: 1
};
const Woman = function(){};
const Man = function(){};
Woman.prototype.add(Person);
const red = new Woman();
console.log(red.ears);
```

##### 原型链

* 实例对象的`__proto__`为构造函数的`prototype`,而构造函数的`prototype`如何创建出来的呢? 底层当然是 `构造函数.prototype = {...}` 那不就是 `new Object({...})`的吗, 那它也是一个实例对象, 它的`__proto__`自然指向`Object.prototype`, 而`Object.prototype`是如何创建的？它自然不能调用自身`new Object`, `Object.prototype.__proto__`为`null`
* 原型链**反映了原型继承的顺序**, 通过`子构造函数.prototype = new 父构造函数()`来原型继承, 可以把**父构造函数**添加到原型链, 而`assign`批量添加成员做不到这点
* **实例对象的成员查找规则** 
  1. 首先查找对象自身是否有该成员
  2. 如果没有找到, 查找其对象原型`__proto__`(也就是其构造函数的原型对象`prototype`)是否有该成员
  3. 如果没有则继续重复上两步: 把`构造函数.prototype`作为一个实例对象, 查找它的`__proto__`, 也就是`new`出`构造函数.prototype`的构造函数的`父级.prototype`, 直到`Object`
* `instanceof` 运算符可以检测构造函数的`prototype`原型对象是否出现在某个实例对象的原型链上 `实例对象 instanceof 构造函数`


## Tip 同步异步

* **同步** *一行一行执行, 等待到结果后, 继续执行*
* **异步** *可以在执行一个可能**长期运行**的任务同时, 继续对其它事件做出反应, 而不必等待任务完成, 在**长期运行**的任务结束后, 可以**通过回调函数显示结果*** *e.g.事件 定时器*

**`async`和`await`**

* 对函数`async`修饰: 使**当前函数变为异步函数**
* 在已经是**异步函数**的内部使用`await`**修饰异步任务**, **暂停代码**, 等待**异步任务**继续执行