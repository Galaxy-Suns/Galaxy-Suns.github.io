# Vue3

## 壹 初步了解Vue3

*向下兼容Vue2*

*由Options选项式api转变为Composition组合式api, 更易于复用*

* `vue2`中 对于同一功能可能要分别写在`data`，`method`，`computed`，`watch`等配置项，拆散了功能
* `vue3` 对同一功能，**通过函数对这个功能的数据方法等统一组合式管理**

*组件根标签可以为多个*

### 1.1 vite构建Vue3工程

1. **项目目录的上一级**下执行 路径中不要有中文
> npm create vue@latest
2. 起项目名字 不要中文
3. 按需要选择
4. 自动创建好了**项目目录**
5. 在**项目目录**执行`npm i`安装依赖包

### 1.2 项目目录组成

* `.vscode` 用于提示插件安装
* `node_module` 包含了安装的依赖包
* `public` 包含了图标文件
* `src` 在此目录写代码
  * `main.ts`
    * 引入`creatApp`创建了应用
    * 引入`App` 根组件
    * `creatApp(App).mount('#app')`组件进入应用并挂载
  * `components`存放组件
  * `assets`存放`css`图片等资源
* `.gitgnore` git时忽略文件
* `edv.d.ts` 使`import`认识导入的文件类型 
* `index.html` 入口文件 **通过`npm run dev`进行运行,获取到端口号**
* `vite.config.ts` 用来配置文件
* 其余的`JSON`文件, 配置文件

启动项目
> npm run dev 

## 贰 组件配置对象 配置项setup 函数

### 2.1 简单使用 setup

相当于`vue2`中`data`和`methods`的组合版

```js
setup(){
  ...
  return {
    // 属性和方法
  }
}
```

* 不使用`this`, `vue3`中弱化`this`
* `setup`函数的调用时机在`beforeCreate`前

```html
<template>
  <div class="person">
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{age}}</h2>
    <button @click="changeName">修改名字</button>
    <button @click="changeAge">修改年龄</button>
    <button @click="showTel">查看联系方式</button>
  </div>
</template>

<script>
  export default {
    name: 'person',
    setup(props) {
      // 数据
      let name = "张三" // 这种定义数据不是响应式
      let age = 18
      let tel = '138888888'

      // 方法
      function changeName(){
        console.log(1);
        name = "Zhang-San"
      }
      function changeAge(){
        age++
      }
      function showTel(){
        alert(tel)
      }
      return {name, age, changeName, changeAge, showTel}
    }
  }
</script>

<style scoped>
  .person{
    background-color: skyblue;
    box-shadow: 0 0 10px;
    border-radius: 10px;
    padding: 20px;
  }
  button{
    margin: 0 5px;
  }
</style>
```

### 2.2 setup的 函数式返回值 渲染函数

* 不再考虑模版等，将返回值渲染到页面
* 不常用

```js
// 将哈哈绘制到组件
setup(){
  ..
  return () => '哈哈'
}
```

### 2.3 setup与data, method等OptionsAPI的关系

* 可以混用但**不建议**
* `data`等`OptionsAPI`中可以通过`this`读取到`setup`中的数据（由于`setup`的调用时机很早）
* 而`setup`不能读取`OptionsAPI`的数据 无论是`this`（`setup`中根本没有`this`），亦或是直接写

### 2.4 script标签配合setup属性 语法糖 

#### 2.4.1 作用和语法

* 另写一个`script`标签, 添加`setup`属性, 把这个标签当成`setup`函数
* 自动将数据, 函数返回

```html
<script setup>
  // 数据
  let name = "张三"
  let age = 18
  let tel = '138888888'
  let address = '清水路'

  // 方法
  function changeName(){
    console.log(1);
    name = "Zhang-San"
  }
  function changeAge(){
    age++
  }
  function showTel(){
    alert(tel)
  }
</script>
```

#### 2.4.2 简写组件name




* 需要插件`npm i vite-plugin-vue-setup-extend -D`（注意需要Node.js高版本）
* 在`vue.config.ts`中加入`import VueSetupExtend from 'vite-plugin-vue-setup-extend'`
* 即可`<script setup name="Person">`
* 文件名和组件名一致可以不用配置`name`

## 叁 响应式数据

### 3.1 ref创建 创建基本类型响应式数据

* `import {ref} from 'vue'`
* 对于响应式基本类型数据, 在创建时调用`ref`创建
* `let 变量名 = ref(基本类型字面量)`
* 这样将变量包装成一个`RefImpl`对象, 属性`value`是其真实值
* 在模版处使用变量不需要`.value`会自动读取`.value`
* 但是在js上需要用`.value`读取和修改数据

```js
import {ref} from 'vue'
// 数据
let name = ref("张三")
let age = ref(18)
let tel = '138888888'
let address = '清水路'
console.log(name);
console.log(age);
console.log(tel);
console.log(address);

// 方法
function changeName(){
  console.log(1);
  name.value = "Zhang-San"
}
function changeAge(){
  age.value++
}
function showTel(){
  alert(tel)
  }
```

### 3.2 reactive 创建复杂类型响应式数据

*只能定义复杂类型*

* `import {reactive} from 'vue'`
* `let 变量名 = reactive({...})`
* 把变量包装成一个在`Proxy`下的对象 *响应式对象*
* 无论模版还是js中**都直接用变量名.属性即可访问和修改变量*的属性***
* 但是只有在模版中才可以通过变量名直接访问到原对象, js中访问不到

### 3.3 ref 创建复杂类型响应式数据

```js
import {ref} from 'vue'
let car = ref({
  brand: '奔驰',
  prize: 100
})
function changePrize(){
  car.value.prize += 10;
}
```

* *注意js中用value访问*
* 这种复杂类型的`value`为一个`proxy`（实际上由`reactive`处理）
* 因此js中的`变量.value`不是直接的对象，**但是可以重新赋值为另一对象**

### 3.4 ref 和 reactive 的抉择

*Vue - Official插件的 Auto Insert: Dot Value设置可以自动在js中ref包裹的变量自动添加`.value`*

* `ref`既可以定义响应式简单类型数据，也可以定义复杂类型
  * `js`中需要使用`value`获取到数据
  * 重新赋值不会失去响应式
* `reactive`只可以定义复杂类型
  * 重新赋值会失去响应式 可以用`Object.assign`
* 注意：只有最初可以`ref`，`reactive`，后续不能重新`ref`，`reactive`
* 简单类型数据和层级不深的复杂类型响应式采用`ref`
* 层级深（以及表单相关）使用`reactive`

### 3.5 toRefs 处理 reactive数据以解构使用

* `toRefs(reactive(..))`
* 把`reactive`的数据的每一组key-value变为`ref`过的
* 这样结构赋值后数据仍为响应式
* 且原`reactive数据`和解构的新数据绑定
* `toRef(reactive(..), keyName)`把`reactive`数据的特定属性取出变为`ref`响应式

```js
import {reactive, toRefs} from 'vue'
let person = reactive({
  name: '张三',
  age: 18
})
console.log(toRefs(person));
console.log(person);
let {name, age} = toRefs(person)
function changeName(){
  name.value += '~'
}
function changeAge(){
  age.value ++
}
```

## 肆 计算属性与监视

### 4.1 computed 计算属性

**常见**

```js
import {computed} from 'vue'
let fullName = computed(() => {
  return firstName.value + '-' + lastName.value
})
```

* `computed`在其依赖数据被修改和初次解析模版时调用
* 存在复用，即模版多个位置用了计算属性，会缓存而不是多次调用` computed`
* `computed`的数据为一个`computedref`类型的数据，`js`读取其值需要`.value`
* `computed`还可以传入一个对象，内含`get` `set`函数 可以据此完成对其直接修改等操作

### 4.2 watch 监视 ref 定义基本类型数据

```js
import {watch} from 'vue'
const stopWatch = watch(被监视的数据(无需.value), (newVal, oldVal) => {
  console.log(oldVal, '变化为', newVal);
  if(newVal >= 10) stopWatch()
})
```

* 返回的函数可以清除监视

### 4.3 watch deep 监视 ref定义的复杂类型数据

* 对于复杂数据类型`watch`默认监视的是地址值
* 需要开启深度监视
* `watch`的第三个参数是配置对象
  * `deep` 深度监视
  * `immediate: true`第一次渲染时立即执行
* 只有地址值发生变化`newVal`和`oldVal`才不同, `deep`监视到的对象属性变化`newVal`和`oldVal`相同, 

```js
watch(person, (newVal, oldVal) => {
  console.log(oldVal, "变化为", newVal);
}, {deep: true})
``` c

### 4.4 watch 监视 reactive定义的复杂类型数据

```js
watch(person, (newVal, oldVal) => {
  console.log(oldVal, "变化为", newVal);
})
```

* 无需开启深度监视, 可以检测到属性的改变 默认进行了深度监视，不是走`deep: true`

### 4.5 watch监视 getter 复杂类型的子属性

**常见**

#### 4.5.1 监视的子属性为简单类型

* `watch`的第一个参数传入一个函数(`getter`), 返回这个子属性即可
* `watch(() => {return person.name})`

#### 4.5.2 deep 监视的子属性为复杂类型

* 可以直接写，也可以写成函数，建议后者，**因为直接写会深度监视，而不监视地址的变化，这样直接赋予子属性为新对象监视不到**
* 这样使用`getter`不会自动开启深度监视, 而会监视地址变化, 所以此时开始`deep: true`即可

```js
watch(() => {return person.car}, (newVal) => {
  console.log(newVal);
}, {deep: true})
```

### 4.6 watch 监视上述多个数据 

```js
watch([()=>person.name, ()=>person.car], (newVal) => {
  console.log(newVal);
}, {deep: true})
```

### 4.7 watchEffect 自动监视

* 自动检测需要监视的数据（即回调中用到的）
* 在需要监视的数据更改时，才调用回调

```js
watchEffect(() => {
  if(temp.value >= 60 || height.value >= 80) console.log('已发送请求')
})
```
## 标签的ref属性

* 模版中标签上添加`ref`
* js中使用`let ref属性值 = ref()`, `ref属性值.value`获取到该标签
* 在组件标签上使用`ref`获取到的是**组件实例对象**
* 但是父元素通过`ref`获取到子元素拥有的数据，还需要子元素使用`defineExpose({数据1, 数据2})`暴露给父亲

```html
<template>
  <div class="person">
    <h1>中国</h1>
    <h2 ref="h2">湖南</h2>
    <h3>长沙</h3>
    <button @click="showLog">点我输出h2</button>
    
  </div>
</template>

<script setup name="Person">
  import {ref} from 'vue'
  // 存储 ref标记的内容
  let h2 = ref()

  function showLog(){
    console.log(h2.value);
  }
</script>
```

## TS的类型约束

### interface 接口

```ts
export interface PersonInter {
  id: string,
  name: string,
  age: number
}
```

* 可有可无的变量`x?: number`

在`ts`中约束变量格式

```ts
import {type PersonInter} from '@/types'
const person:PersonInter = {
  ...
}
```

### <> 泛型 

* 类似于cpp中的模版, 起到指定内部类型的结构
* 常用`Array<..>` 数组类型, 每一个元素是..类型, 也可以为`..[]`

```ts
let personList:Array<PersonInter> = [
  {..}..
]
```

### type 自定义类型

* 对一些接口的组合的再定义, 类似`typedef`

```ts
type Persons Array<PersonInter>
```

```ts
let personList:Persons...
```

### reactive ref包裹的数据进行类型约束

```ts
const person:PersonInter = {
  ...
}
```

=>

```ts
const person = reactive<PersonInter>({
  ...
})
```

## props 父向子传递数据

* 父元素传递方式和Vue2中类似
* 子元素使用`let obj = defineProps(['list'..])`接收数据，随后模版可以使用`list`，而js中可以用`obj.list`得到数据
* 一些限制类型的功能

```js
//let obj = defineProps(['list'])
//let obj = defineProps<{list:Persons}>() // 接收 限制类型
//let obj = defineProps<{list?:Persons}>() // 接收 限制类型 必要性
let obj = withDefaults(defineProps<{list?:Persons}>(), {
  list: () => [{id: '000', name: '实例人物', age: 0}]
}) // 接收 限制类型 必要性 默认值
```

*Vue3中`define..`的函数不用引入，为宏函数，全局可用*

## 伍 Vue3的生命周期

* 对应Vue2的四个流程，**创建、挂载、更新、卸载**，`Vue3`保持不变，一些函数和调用方式改变

```js
import {ref, 
  onBeforeMount, 
  onMounted, 
  onBeforeUpdate, 
  onUpdated,
  onBeforeUnmount,
  onUnmounted
} from 'vue'

let sum = ref(0)

function add(){
  sum.value ++
}

// 创建 Vue2 beforeCreate created => setup
console.log("创建前")

// 挂载 beforeMount mounted => onBeforeMount onMounted
onBeforeMount(() => {
  console.log("挂载前")
})

onMounted(() => {
  console.log("挂载完毕")
})

// 更新 beforeUpdate updated => onBeforeUpdate onUpdated 
onBeforeUpdate(() => {
  console.log("更新前")
})

onUpdated(() => {
  console.log("更新完毕")
})

// 销毁 => 卸载 onBeforeUnmount onUnmounted
onBeforeUnmount(() => {
  console.log("卸载前")
})

onUnmounted(() => {
  console.log("卸载完毕")
})
console.log("创建完毕")
```

* 常用`onMounted`, `onUpdated`, `onBeforeUnmount`

## hook 组合式API风格的数据和方法

* 同一功能编写在同一文件，在组件引入这些文件的数据即可
* 形式上形如Vue2的`mixin`
* 文件命名规范`hooks\use..功能`
* 首先提取出组件中与该功能相关内容(同样可以调用钩子监视计算等等)
* 最后暴露一个**返回对象的函数**，返回的对象为组件中需要的数据，方法
* 在组件中引入函数，并解构赋值成相应的数据函数

*hooks/useDog.ts*
```ts
import {reactive} from 'vue'
import axios from 'axios'

let dogList = reactive(["https:\/\/images.dog.ceo\/breeds\/pembroke\/n02113023_5739.jpg"])

  async function getDog(){
    try {
      let res = await axios({
      url: "https://dog.ceo/api/breed/pembroke/images/random"
      })
      dogList.push(res.data.message)
    } catch (error) {
      alert(error)
    }
  }

export default function(){
  return {dogList, getDog}
}
```

*hooks/useSum.ts*
```ts
import {ref} from 'vue'

let sum = ref(0)

function add(){
  sum.value ++
}

export default function(){
  return {sum, add}
}
```

*组件.vue*
```ts
import useDog from '@/hooks/useDog'
import useSum from '@/hooks/useSum'

const {sum, add} = useSum()
const {dogList, getDog} = useDog()
```

## 陆 路由

> npm i vue-router

### 与Vue2的路由完全相同内容

* `children`嵌套路由
* 路由的`name`属性 命名路由
* 历史记录与`push`, `replace` 开启`replace`模式

### 6.1 路由的基本使用

* 和Vue2的模式类似, 几个不同点

*router/index.ts*
* 引入`import {createRouter, createWebHistory} from 'vue-router'`, 使用`export default creatRouter({history..route:[{path..}..]})`创建路由器
* 必须写`history`, `history`模式 `history: createWebHistory()`

*main.ts*
* 在挂载前`app.use(router)`

*调用路由的组件中如App.vue*
* 引入`import {RouterView, RouterLink} from 'vue-router'`
* 两个标签如上所示

```ts
// router/index.ts
// 创建一个路由器, 并暴露出去
import {createRouter, createWebHistory} from 'vue-router'
import About from '@/components/About.vue'
import News from '@/components/News.vue'
import Home from '@/components/Home.vue'

// 创建路由器
export default createRouter({
  history: createWebHistory(), // 路由器的工作模式
  routes: [
    {
      path: '/home',
      component: Home
    },
    {
      path: '/news',
      component: News
    },
    {
      path: '/about',
      component: About
    },
  ]
})
```

```ts
// main.ts
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
```

```html
// App.vue
<template>
  <div class="app">
    <h2>Vue路由测试</h2>
    <!-- 导航区 -->
    <div class="navigate">
      <RouterLink to="/home" active-class="active">首页</RouterLink>
      <RouterLink to="/news" active-class="active">新闻</RouterLink>
      <RouterLink to="/about" active-class="active">关于</RouterLink>
    </div>
    <!-- 展示区 -->
    <div class="main-content">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script lang="ts" setup name="App">
  import {RouterView, RouterLink} from 'vue-router'
</script>

<style scoped>
a{
  margin-right: 10px;
}

.active{
  color: chartreuse;
}
</style>
```

### 6.2 路由的query参数传参

* 父组件传递query参数基本和Vue2相同分为`to`对象和字符串两种方法
* 不同点在于子组件中获取到`query`的方式
```ts
import {toRefs} from 'vue'
import {useRoute} from 'vue-router'

let route = useRoute()
let {query} = toRefs(route)
```

### 6.3 路由的params参数传参

* 父组件传递参数，router/index.ts占位和Vue2相同
* 子组件获取到params
```ts
import {toRefs} from 'vue'
import {useRoute} from 'vue-router'

let route = useRoute()
let {params} = toRefs(route)
```
* 对于router/index.ts中的占位，还可以在某一占位参数的结尾加一个`?`控制必要性

### 6.4 路由的props配置项 使模版简洁使用传递的数据

* 和Vue2相似地，`props: true`适用于`param`传参
* 对象写法和vue2相同
* 而函数式`props(route){return route.query}`即可传递`query`参数，注意vue3中只需返回`query`即可
* 在路由组件中，使用`defineProps([传递的参数1, ..])`即可

### 6.5 编程式路由导航

* 不同点在于使用`useRouter()`获取到路由器

### 6.6 路由重定向 常应用于初次进入页面时匹配路由

* 把一个路径重定向到另一个路径
* 把`/`路径重定向到`/home`

```ts
{
  path: '/',
  redirect: '/home'
}
```

## 柒 Vue3状态管理工具 Pinia

https://pinia.vuejs.org/zh/

* 相对于`Vuex`简洁，符合直觉

### nanoid 库 *轻量化 用于生成唯一id*

* `npm i nanoid`
* `import {nanoid} from nanoid`
* `nanoid()`生成一个唯一字符串

### 7.1 createPinia 搭建Pinia环境

> npm i pinia

*main.ts中*
> import {createPinia} from 'pinia' // 引入

*在app创建后*
> const pinia = createPinia()

*安装插件*
> app.use(pinia)

### 7.2 defineStore use..Store 存储读取数据

* `store/count.ts`中存储和`count.vue`组件相关的数据
* `store/...ts`中引入`import {defineStore} from 'pinia'`
* `const useCountStore = defineStore('count', {state(){return {数据（无需响应式）}}})`并向外暴露
* `count.vue`中引入`import {useCountStore} from '@/store/count'`
* `const countStore = useCountStore()`得到`store`
* `countStore.数据`即可得到响应式数据

*store/count.ts*
```ts
import {defineStore} from 'pinia'

export const useCountStore = defineStore('count', {
  // 存储数据的地方
  state(){
    return {
      sum: 0
    }
  }
})
```

*count.vue*
```html
<template>
  <div class="count">
    <h2>当前求和为：{{countStore.sum}}</h2>
    <select v-model="n">
      <option :value="1">1</option>
      <option :value="2">2</option>
      <option :value="3">3</option>
    </select>
    <button @click="add">加</button>
    <button @click="red">减</button>
  </div>
</template>

<script setup lang="ts" name="LoveTalk">
  import {ref} from 'vue'
  import {useCountStore} from '@/store/count'

  const countStore = useCountStore()

  let n = ref(1)
  function add(){
    countStore.sum += n.value
  }
  function red(){
    countStore.sum -= n.value
  }
</script>

<style scoped>
  .count{
    background-color: skyblue;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 0 10px;
  }
  select, button{
    margin: 0 5px;
    height: 25px;
  }
</style>
```

### 7.3 ..Store. ..Store.$patch actions 修改数据

* `countStore.sum += n.value` 直接修改数据（相对于`vuex`不能直接修改数据只能提交给actions更符合直觉）
* `countStore.$patch({sum: coutStore.sum + 1, school: '中南大学', address: '长沙'})` 批量修改数据（对于多个数据效率更改, 因为只会更改一次）
* 使用`actions`，在`store/...ts`中的store配置对象中，使用`actions`配置项, 其中的方法可供组件调用，进行数据的处理，可接收组件传入的参数，`this`指向`store`，可据此获取数据，用于可复用的逻辑处理

*store/count.ts*
```ts
import {defineStore} from 'pinia'

export const useCountStore = defineStore('count', {
  // 存放方法，用于响应组件中的动作
  actions: {
    increment(value:Number){
      this.sum ++
    }
  },
  // 存储数据的地方
  state(){
    return {
      sum: 0,
      school: 'CSU',
      address: '清水路'
    }
  }
})
```

*Count.vue*
```js
import {ref} from 'vue'
import {useCountStore} from '@/store/count'

const countStore = useCountStore()

let n = ref(1)
function add(){
  // countStore.sum += n.value
  countStore.$patch({
    sum: countStore.sum + 1,
    school: '中南大学',
    address: '长沙'
  })
  // countStore.increment(n.value)
}

function red(){
  countStore.sum -= n.value
}
```

### 7.4 storeToRefs 配合解构赋值简化模版

* `const {sum, school, address} = storeToRefs(countStore)`模版和后续js即可使用简化后的**响应式**数据
* 如果使用`toRefs`会把数据和方法都用`ref`包裹，而`storeToRefs`只会关注数据

### 7.5 getters store中的计算属性

在`store`配置对象中的配置项`getters`中添加计算属性(函数形式)，参数为`state`（也可以使用`this`（指向`store`）），据此获取数据，返回值作为数据值

```ts
getters: {
  bigSum(state){
    return state.sum * 10
  }
}
```

### 7.6 ..Store.$subscribe 订阅数据变更

* store的`watch`当`state`中任意数据发生变更时调用
* `..Store.$subscribe((mutate, state) => {...})`
  * `mutate`一些变更信息
  * `state` 变更后的`state`
* 可用于本地存储，刷新不丢失

### 7.7 store配置对象的组合式写法

* 把`store`的配置对象换成一个函数（箭头）相当于组件的setup
* 数据正常定义响应式变量
* 各个actions定义为函数
* `return ..`

## 捌 组件通信

### 8.1 props 父子组件通信

*和Vue2相同*

* 父向子传递数据`defineProps([..])`
* 子向父传递数据，**调用父亲传递的函数**

*在不是直接父子关系的时候不要使用*

### 8.2 defineEmits 组件自定义事件 子向父通信

* 父组件给子组件绑定事件方式和Vue2相同`@事件名="回调函数"`
* 子组件中使用`const emit = defineEmits([事件名])`声明事件后，使用`emit(事件名[，传参])`即可触发事件并给回调函数传参，完成向父元素传递数据

### 8.3 mitt 任意组件通信

> npm i mitt

*utils/emiter.ts 中配置emiter*
```ts
import mitt from 'mitt'

const emitter = mitt()

export default emitter
```
* 类似与Vue2的事件总线`$bus`
* 需要接收或发送消息的组件中引入`import emitter from '@/utils/emiter'`
* 在需要接收消息的组件中绑定事件`emitter.on('事件名', (接收数据) => {})`
* 在需要发送消息的组件中触发事件`emitter.emit('事件名', 发生数据)`
* 在接收消息（绑定了事件）的组件销毁时调用`emitter.off(事件名)`解绑事件 （`emitter.all.clear()`解绑所有事件）

### 8.4 组件的v-model底层原理

* 在写`<MyInput v-model="username"/>`时，实际上等同于`<MyInput :modelValue="username" @update:modelValue="val => username = val"/>`（类似）也就是给组件props传递了`mpdelValue`参数，同时绑定了事件`update:modelValue`
* 在组件内部, 接收到`modelValue`，在`input`标签写`:value="modelValue"`实现了数据传递给DOM
* 同时`defineEmits(['update:modelValue'])`，在`input`处`@input="emit('update:modelValue', $event.target.value)"`在DOM输入时触发事件, 进而传递目前DOM内容给回调，从而更新了username，完成DOM传递给数据，至此完成双向绑定

*可以绑定把modelValue改成其他名，在`v-model:qwe=".."`* 此时组件内部用到`modelValue`的地方改成`qwe`，`update:modelValue`改成`update:qwe`

* 如此以来可以传递多个双向绑定的参数了

### 8.5 props配合$attrs 祖向孙传递数据

* 父向子传递的数据如果子没有`defineProps`接收数据，数据会出现在子的`$attr`中
* 父向子传递数据`:a=".." :n=".."`还可以写成`v-bind="{a: .., b: ..}"`
* 因此当父向子传递数据时, 子再向孙传递**所有没有动用的数据**`v-bind="$attrs"`完成祖孙间的数据传递

### 8.6 \$refs $parent 父子传递数据

* 父利用子的`ref`标签获取子实例对象，同时子配合父`defineExpose`暴露数据，可以实现父向子通信
* 而父在模版中使用`$refs`，比如点击事件`@click="getChildren($refs)"`可以获取一个对象`{ref值1: 组件实例对象， ...}`, 里面包含了所有具有具有**ref**属性的子组件
* 同样的子在模版中使用`$parent`可以获取到父实例对象，同样父亲需要暴露`difineExpose` 实现子向父通信

```html
<!-- 父亲的模版 -->
<div class="father">
  <h3>父组件</h3>
  <h4>房产：{{house}}</h4>
  <button @click="changeToy">修改Child1的玩具</button>
  <button @click="getChildren($refs)">获取子</button>
  <Child1 ref="c1"/>
  <Child2 />
</div>
```

```ts
// 父亲的setup
function getChildren(refs:object){
  console.log(refs);
}
```

### 8.7 provide inject 祖和后代间直接传递数据

*和`$attrs`不同, 不会打扰父（中间）组件*

* 祖`provide('qian', money)`把`money`提供给后代，注意不要`.value`
* 后代`inject('qian', 200)`获取到祖先传的数据 `200`为默认值

### 8.8 插槽

* 默认插槽和具名插槽与Vue2相同
* 而作用域插槽父元素接收数据对象在`template`上的`v-slot="params"`或者`#default="params"`（默认插槽）获取有名字的插槽传递的数据要用`v-slot:名字=".."`

## 玖 其它API 

待补充

## 拾 Vue3新组件

### 10.1 teleport组件 传送门

* 把其包裹的内容传到`to`属性的元素下 属性值为选择器
* 常用于配合fixed定位传送到body下 `to="body"`

### 10.2 Suspense组件 用于处理子组件中存在异步任务的某些情况

* 当子组件的异步任务用`await`处理时，会在顶层`async`，此时可能子组件会失效
* 需要使用`Suspense`，变为异步组件

```html
<Suspense>
  <!-- 执行完毕显示的内容 -->
  <template v-slot:default>
    <Child />
  </template>
  <!-- 执行中显示的内容 -->
  <template v-slot:fallback>
    <h2>加载中...</h2>
  </template>
</Suspense>
```

## Vue. .. 转移到了 app. .. 

* `Vue.component()` => `app.compontnt()`
* `Vue.config. ..` => `app.config. ..`
* `Vue.prototype.x` => `app.config.grobalProperties.x`
