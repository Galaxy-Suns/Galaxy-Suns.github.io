# *叁*_ES6+_语法
 
* [3_1_作用域](#3_1_作用域)
  * [3_1_1_局部作用域](#3_1_1_局部作用域)
    * [函数作用域_](#函数作用域_)
    * [{}_块作用域](#{}_块作用域)
  * [3_1_2_全局作用域](#3_1_2_全局作用域)
  * [3_1_3_作用域链](#3_1_3_作用域链)
  * [3_1_4_垃圾回收机制](#3_1_4_垃圾回收机制)
    * [内存生命周期](#内存生命周期)
    * [内存泄露](#内存泄露)
  * [3_1_5_闭包](#3_1_5_闭包)
  * [3_1_6_var_变量提升](#3_1_6_var_变量提升)
* [3_2_函数](#3_2_函数)
  * [3_2_1_函数提升](#3_2_1_函数提升)
  * [3_2_2_动态参数__剩余参数和展开运算符](#3_2_2_动态参数__剩余参数和展开运算符)
    * [arguments_动态参数](#arguments_动态参数)
    * [___others_剩余参数](#___others_剩余参数)
    * [____展开运算符_(与函数无关__放在此处仅做区分)](#____展开运算符_(与函数无关__放在此处仅做区分))
  * [3_2_3_箭头函数](#3_2_3_箭头函数)
    * [()=>{}_语法](#()=>{}_语法)
    * [this_指向](#this_指向)
* [3_3_解构赋值](#3_3_解构赋值)
  * [3_3_1_const_[]_数组解构](#3_3_1_const_[]_数组解构)
  * [3_3_2_const_{}_对象解构](#3_3_2_const_{}_对象解构)
  * [3_3__forEach_数组变量_（补充内容）](#3_3__forEach_数组变量_（补充内容）)
* [3_4_对象](#3_4_对象)
  * [3_4_1_创建对象的三种方式](#3_4_1_创建对象的三种方式)
  * [3_4_2_构造函数](#3_4_2_构造函数)
  * [3_4_3_实例成员和静态成员](#3_4_3_实例成员和静态成员)
  * [3_4_4_简单数据类型的包装](#3_4_4_简单数据类型的包装)
  * [3_4_5_内置构造函数](#3_4_5_内置构造函数)
    * [Object](#Object)
    * [Array](#Array)
  * [3_4_6_prototype_原型对象](#3_4_6_prototype_原型对象)
    * [挂载实例方法到原型对象](#挂载实例方法到原型对象)
    * [constructor_属性](#constructor_属性)
    * [\_\_proto\_\__对象原型](#\_\_proto\_\__对象原型)
    * [原型继承](#原型继承)
    * [原型链](#原型链)

---

## 3_1_作用域

### 3_1_1_局部作用域

*分为**函数作用域**和**块作用域***

#### 函数作用域_

* **函数内部声明的变量只能在函数内部被访问**, 外部无法访问
* **函数的参数**也是函数内部的**局部变量**

#### {}_块作用域

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

### 3_1_2_全局作用域

* **最外层即为全局作用域**, 全局作用域声明的变量, 在其它作用域均可访问
* 尽可能少声明, 避免污染
* 为`window`对象动态添加的属性默认也为全局, **不推荐**

### 3_1_3_作用域链

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

### 3_1_4_垃圾回收机制

*JS中内存的分配和回收自动完成, 内存在不使用的时候会被**垃圾回收器自动回收***

#### 内存生命周期

1. 内存分配 声明时自动分配内存
2. 内存使用 使用变量, 函数等
3. 内存回收 使用完毕, 垃圾回收器自动回收

* 全局变量一般不会回收, 关闭页面时回收
* 一般局部变量的值, 不用了, 会自动回收

**堆内存的回收算法**

* 引用计数法: 根据对象的引用次数来进行回收, 当引用为0时回收。*会在对象相互引用时造成内存泄露* *不再使用*
* 标记清除法: *回收无法到达的对象*, 从根部出发, 定时扫描堆中对象, 找不到则回收。

#### 内存泄露

程序中分配的内存由于某种原因, 程序未释放或无法释放即为内存泄露

### 3_1_5_闭包

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

### 3_1_6_var_变量提升

*JS的一个缺陷*

* 代码在执行前, 先检测**当前作用域下所有`var`声明的变量**, 并且把**所有`var`声明的变量的*声明*提到*当前作用域*的最前面** *只提升声明, 不提升赋值*

```js
// 由于变量提升 num 的声明被放在最前, 因此不报错, 为 undefined
// 提升: var num;
console.log(num + "件");
var num = 10;
```
## 3_2_函数

### 3_2_1_函数提升

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

### 3_2_2_动态参数__剩余参数和展开运算符

#### arguments_动态参数

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

#### ___others_剩余参数

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

#### ____展开运算符_(与函数无关__放在此处仅做区分)

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

### 3_2_3_箭头函数

*更适用于原本就需要匿名函数的地方*

#### ()=>{}_语法

```js
(形参) => {函数体}
```

* **形参只有一个时**, 括号可以省略 `形参 => {函数体}`
* **无形参时**, 括号不能省略 `() => {函数体}`
* 函数体中**除了返回值外不进行其他操作**, 可以直接写返回值`(形参) => 返回值`

#### this_指向

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

## 3_3_解构赋值

### 3_3_1_const_[]_数组解构

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

### 3_3_2_const_{}_对象解构

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

### 3_3__forEach_数组变量_（补充内容）

> arr.forEach((d, i)=>{...})

* 回调函数  对于数组的每个元素进行操作
  * `d` 数组的每个数据
  * `i` 当前元素的下标 

## 3_4_对象

### 3_4_1_创建对象的三种方式

* 字面量创建 `const o = {..};`
* new关键字创建 `const o = new object({..});`
* 构造函数创建 **可以快速创建多个类似的对象**

### 3_4_2_构造函数

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

### 3_4_3_实例成员和静态成员

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

### 3_4_4_简单数据类型的包装

* 对于**简单数据类型**, JS底层也会进行包装, 构造为一个**对象**, 从而提供相应的方法和属性

> const str = 'abc'; -底-层-包-装-> const str = new String('abc');

### 3_4_5_内置构造函数

#### Object

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

#### Array

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

### 3_4_6_prototype_原型对象

#### 挂载实例方法到原型对象

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

#### constructor_属性

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

#### \_\_proto\_\__对象原型

* **实例对象中** 通过`__proto__`找到构造函数的原型对象`prototype`, 从而给自身挂载属性和方法
* 在浏览器中表现为`[[prototype]]`
* 只读

```js
// 理解 p1 实例对象的对象原型 和 Pig 构造方法的原型对象
const Pig = function(){};
const p1 = new Pig();
console.log(p1.__proto__ === Pig.prototype); // true
```

#### 原型继承

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

#### 原型链

* 实例对象的`__proto__`为构造函数的`prototype`,而构造函数的`prototype`如何创建出来的呢? 底层当然是 `构造函数.prototype = {...}` 那不就是 `new Object({...})`的吗, 那它也是一个实例对象, 它的`__proto__`自然指向`Object.prototype`, 而`Object.prototype`是如何创建的？它自然不能调用自身`new Object`, `Object.prototype.__proto__`为`null`
* 原型链**反映了原型继承的顺序**, 通过`子构造函数.prototype = new 父构造函数()`来原型继承, 可以把**父构造函数**添加到原型链, 而`assign`批量添加成员做不到这点
* **实例对象的成员查找规则** 
  1. 首先查找对象自身是否有该成员
  2. 如果没有找到, 查找其对象原型`__proto__`(也就是其构造函数的原型对象`prototype`)是否有该成员
  3. 如果没有则继续重复上两步: 把`构造函数.prototype`作为一个实例对象, 查找它的`__proto__`, 也就是`new`出`构造函数.prototype`的构造函数的`父级.prototype`, 直到`Object`
* `instanceof` 运算符可以检测构造函数的`prototype`原型对象是否出现在某个实例对象的原型链上 `实例对象 instanceof 构造函数`


