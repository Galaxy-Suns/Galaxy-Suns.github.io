# HTML 与 CSS

## *壹* HTML认知

---

### 1.1 网页的组成

**网页的本质** 前端程序员写的代码

*通过浏览器的渲染和解析转换成网页*

### 1.2 浏览器

**浏览器** 网页显示、运行的平台，是前端开发必备利器

**渲染引擎/浏览器内核** 浏览器中对代码进行解析渲染的部分

* 内核不同，加载代码的性能速度效果不同

### 1.3 Web标准

*针对不同浏览器内核对代码的渲染解析效果不同而指定的标准*

**Web标准的构成**

* **结构** HTML **页面元素**和内容
* **表现** CSS  网页元素的外观和位置等**页面样式**（如:颜色，大小等）
* **行为** JavaScript 网页模型的定义与**页面交互**

### 1.4 HTML感知

**HTML** 超文本标记语言

标签 : < >开始  </ >结束

```html
<strong> hello world </strong>
```

### 1.5 HTML骨架

*网页类似于一篇文章，右固定的结构*

**固定结构** 整体 头部 标题 主体等

```html
<html>
    <head>
        <title> Galaxies </title>
    </head>
    <body>
        你好，GALAXY
    </body>
</html>
```

vscode中`!`+`Tab`快捷生成骨架
vscode中`Alt`+`B`快捷在默认浏览器中打开

### 1.6 HTML注释

```html
<!--这是注释-->
```

vscode中 `ctrl`+`/` 快捷注释掉/取消注释光标所在行

### 1.7 HTML标签的结构

**标签的结构**

开始标签 包裹内容 结束标签（双标签）

**标签的分类**

* 双标签 有开始，有结束
* 单标签 自成一体，无法包裹内容 `<br>` 换行 `<hr>` 分割线

**标签的关系**

* 父子关系(嵌套关系) 大范围标签**包裹住**小范围标签
* 兄弟关系(并列关系) 并列在**一个大范围标签内，不相包裹**

```html
<!--父子关系-->
<head>
    <title>
         ...
    </title>
</head>
<!--并列关系-->
<head>
    ...
</head>
<body>
    ...
</body>
```

### 1.8 标题和段落

**标题标签**

* 共6个，重要程度依次递减
* 独占一行自动折行

```html
<h1> hs </h1>
<h2> hs </h2>
<h3> hs </h3>
<h4> hs </h4>
<h5> hs </h5>
<h6> hs </h6>
```

在vscode中，直接输入标签的英文即可生成框架

**段落标签**

* 用于**分段显示**
* 段落之间**有间隙**
* 独占一行(段)

```html
<p>我是一段文字</p>
```

### 1.9 换行和水平分割线

**换行标签** 

* 让文字强制换行

```html
<br>
```

**水平分割线标签**

* 独占一行

```html
<hr>
```

### 1.10 文本格式化标签

*突出**重要性的强调语境用英文单词**标签*

* 加粗 b **strong**
* 下划线 u **ins**
* 倾斜 i **em**
* 删除线 s **del**

```html
    <b>加粗</b><br>
    <strong>加粗</strong>
    <hr>
    <u>下划线</u><br>
    <ins>下划线</ins>
    <hr>
    <i>倾斜</i><br>
    <em>倾斜</em>
    <hr>
    <s>删除线</s><br>
    <del>删除线</del>
```

### 1.11 图片的基本使用

**语法**

* img单标签
* 添加**标签属性**
* src、alt 为 **属性名** 多个属性之间**用空格隔开**
* “”内为 **属性值**
* src 属性值为 **路径** <br> 与代码在同一文件夹下 可采用相对路径 ./文件名  文件名 
* alt 属性值为 **替换文本** <br> 当图片加载失败，才显示alt的文本
* title 属性值为 **提示文本** <br> 当鼠标悬停时出现 
* width 、 height 属性值为 **宽度和高度** <br> 当设置一个后，另一个等比例缩放 <br> 当同时设置两个比例，可能出现图片变形
  

```html
<img src=" " alt=" ">
```

```html
<img src="./1.gif" alt="哭哭" title="我在哭哭" width="200" height="400">
    <!-- src : 图片路径 -->
    <!-- alt : 替换文本，当图片不显示时候显示的文字 -->
    <!-- title : 提示文本，当鼠标悬停时出现 -->
    <!-- width : 宽度 -->
    <!-- height : 高度 -->
```

### 1.12 绝对路径

*src 也可以使用绝对路径（一般不用）*

**定义** 

文件中 根目录下的绝对路径 通常从盘符出发 <br> 网站中 完整的网址

```html
<img src="C:/code/galaxy_web/html学习/1.gif">
```

### 1.13 相对路径

*从**当前文件**出发，开始找目标文件*

**同级目录** 目标文件和当前文件在同一文件夹

* `./目标文件名`
* `文件名`

**下级目录** 目标文件的某一级父目录与当前文件在同一文件夹

* `./目标文件夹目录/目标文件名`
* `目标文件夹目录/目标文件名`

**上级目录** 目标文件在当前文件的某一级父目录中

* 返回一级 `../`
* 返回两级 `.../`
* ...

```html
    <b>同级别</b><br>
    <img src="./1.gif"><br>
    <img src="1.gif">
    <hr>
    <b>下级</b><br>
    <img src="./son/grandson/2.gif"><br>
    <img src="son/grandson/2.gif">
    <hr>
    <b>上级</b><br>
    <img src="../3.gif">
```

### 1.14 音频标签

**语法** 

* audio双标签
* 常用属性 <br> **src** <br> **controls** 显示播放的控件 <br> **autoplay** 自动播放(部分浏览器不支持) <br> **loop** 循环播放
* 支持 **.mp3** .wav .ogg

```html
<audio src="./1.mp3" controls autoplay loop></audio>
```

### 1.15 视频标签

**语法**

* video双标签
* 常用属性 <br> **src** <br> **controls** <br> **autoplay** <br> **muted** 静音播放，只有采用此属性才能让autoplay生效(google) <br> **loop** 
* 支持 **.mp4** .webm .ogg

```html
<video src="./1.mp4" autoplay muted loop></video>
```

### 1.16 超链接

*点击某处跳转到另外的界面*

**语法**

* a双标签
* 常用属性 <br> **href** 跳转地址 <br> **target** 控制目标网页的打开形式 取值 **_self** 默认，在当前网页跳转 **_blank** 在新窗口跳转

```html
<a href="jmphtml.html" target="_blank"><h1>跳转!!</h1></a><br>
<!-- 当开发网站的初期，我们还不知道跳转地址的时候，href的值书写为 # -->
<a href="#">空链接</a>
```

## *贰* HTML基础

---

### 2.1 列表标签使用场景

*整齐排列的内容*

* 无序列表
* 有序列表
* 自定义列表

### 2.2 无序列表

**语法**

* ul双标签嵌套li双标签
* ul表示无序列表整体
* li表示无序列表的每一行 **自动折行**

**注意**

* ul标签中**只能包含li标签**
* li标签可包含任意内容

```html
<h1>水果列表</h1>
<ul>
    <li>榴莲</li>
    <li>香蕉</li>
    <li>苹果</li>
    <li>哈密瓜</li>
    <li>火龙果</li>
</ul>
```

### 2.3 有序列表

**语法**

* ol双标签嵌套li双标签
* ol表示有序列表整体
* li表示有序列表的每一行 **自动折行**

**注意**

* ol标签中**只能包含li标签**
* oi标签可包含任意内容

```html
<h1>成绩排行榜</h1>
<ol>
    <li>小姐姐:100</li>
    <li>小可爱:80</li>
    <li>小帅哥:60</li>
</ol>
```

### 2.4 自定义列表

**语法**

* dl表示自定义列表整体，用于包裹dt/dd等内容 
* dt表示自定义列表的主题 **自动折行**
* dd表示自定义列表针对主题的每一项内容 **自动折行**

**注意**

* dl标签中只允许包含dt/dd标签
* dt/dd标签可以包含任何内容

```html
<dl>
    <dt>张三的一天</dt>
    <dd>吃饭</dd>
    <dd>喝水</dd>
    <dd>睡觉</dd>
</dl>
```

### 2.5 表格的使用

**基本标签**

* table 表格整体，可用于包裹多个tr
* tr 表格每行，可用于包裹td
* td 表格单元格，可用于包裹内容

**嵌套关系** *table > tr > td*

**表格的属性**

*没有属性，表格没有边框等外观，只有类似表格排列的文本*

* **border 边框宽度** 属性 数字
* **width 表格宽度** 属性 数字
* **height 表格高度** 属性 数字

```html
<table border="1" width="500" height="300">
    <tr>
        <td>姓名</td>
        <td>成绩</td>
        <td>评语</td>
    </tr>
    <tr>
        <td>小哥哥</td>
        <td>100分</td>
        <td>小哥哥真帅气</td>
    </tr>
    <tr>
        <td>小姐姐</td>
        <td>100分</td>
        <td>小姐姐真漂亮</td>
    </tr>
    <tr>
        <td>总结</td>
        <td>郎才女貌</td>
        <td>郎才女貌</td>
    </tr>
</table>
```

*实际开发中样式效果推荐使用CSS设置*

### 2.6 表格标题和表头单元格标签

**定义及语法**

* caption 表格大标题，默认在表格正上方居中显示，**写于table内(与tr为并列关系/如有结构标签和结构标签并列)**
* th 表头单元格，表示一列小标题，通常位于表格第一行，加粗居中。**与td替换使用**

```html
<table border="1">
    <caption><strong>学生成绩单</strong></caption>
    <tr>
        <th>姓名</th>
        <th>成绩</th>
        <th>评语</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>100分</td>
        <td>真棒，第一名</td>
    </tr>
    <tr>
        <td>李四</td>
        <td>99分</td>
        <td>真棒，第二名</td>
    </tr>
    <tr>
        <td>总结</td>
        <td>郎才女貌</td>
        <td>真棒，相亲成功</td>
    </tr>
</table>
```

### 2.7 表格的结构标签

*将表格结构分组，使**语义**清晰*

**语法**

* thead 表格头部
* tbody 表格主体
* tfoot 表格底部

**注意**

* 结构标签用于包裹tr标签
* 可以省略，**对实际效果无影响**，用作代码结构清晰化,**对浏览器对代码的解析效率也有积极影响**

```html
<table border="1">
    <caption><strong>学生成绩单</strong></caption>
    <thead>
        <tr>
            <th>姓名</th>
            <th>成绩</th>
            <th>评语</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>100分</td>
            <td>真棒，第一名</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>99分</td>
            <td>真棒，第二名</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>总结</td>
            <td>郎才女貌</td>
            <td>真棒，相亲成功</td>
        </tr>
    </tfoot>        
</table>
```

### 2.8 合并单元格

*分为跨行合并和跨列合并*

**语法**

删掉**原有的不需要单元格**，给**保留的单元格 左/上**设置属性

* rowspan 跨行合并 属性值 合并单元格个数（将几个单元格合并）
* colspan 跨列合并 属性值 合并单元格个数（将几个单元格合并）

*本质其实是将单元格横向纵向扩展，使其占位n个单元格的位置*

**注意**

* 只能同结构标签下合并，而不能跨标签合并

```html
<table border="1">
    <caption><strong>学生成绩单</strong></caption>
    <thead>
        <tr>
            <th>姓名</th>
            <th>成绩</th>
            <th>评语</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td rowspan="2">100分</td>
            <td>真棒，第一名</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>真棒，第二名</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>总结</td>
            <td colspan="2">郎才女貌</td>
        </tr>
    </tfoot>        
</table>
```

### 2.9 表单标签 input系列标签

**表单标签的应用场景**

*登录 注册 搜索功能*

**input标签**

* 单标签
* 可随**type属性值的不同，展示不同效果**

<table>
    <caption><strong>input</strong></caption>
    <thead>
        <tr>
            <th>标签名</th>
            <th>type属性值</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="8">input</td>
            <td>text</td>
            <td>文本框，用于输入单行文本</td>
        </tr>
        <tr>
            <td>password</td>
            <td>密码框，用于输入密码</td>
        </tr>
        <tr>
            <td>radio</td>
            <td>单选框，用于多选一</td>
        </tr>
        <tr>
            <td>checkbox</td>
            <td>多选框，用于多选多</td>
        </tr>
        <tr>
            <td>file</td>
            <td>文件选择，用于之后上传文件</td>
        </tr>
        <tr>
            <td>submit</td>
            <td>提交按钮，用于提交</td>
        </tr>
        <tr>
            <td>reset</td>
            <td>重置按钮，用于重置</td>
        </tr>
        <tr>
            <td>button</td>
            <td>普通按钮，默认无功能，之后配合js添加功能</td>
        </tr>
    </tbody>
</table>

```html
<!-- 文本框 -->
文本框 : <input type="text" >

<br>
<br>
<!-- 密码框 -->
密码框 : <input type="password">

<br>
<br>
<!-- 单选框 -->
<input type="radio">

<br>
<br>
<!-- 多选框 -->
<input type="checkbox">

<br>
<br>
<!-- 文件选择 -->
<input type="file">

<br>
<br>
<!-- 提交框 -->
<input type="submit">

<br>
<br>
<!-- 重置 -->
<input type="reset">

<br>
<br>
<!-- 普通按钮 -->
<input type="button">
```

### 2.10 text password 占位符(提示信息)

*提示用户输入内容的文本*

**语法**

* input标签下placeholder属性
* 使用于type属性值为text和passworld

```html
<!-- 文本框 -->
<input type="text" placeholder="请输入用户名">

<br>
<br>
<!-- 密码框 -->
<input type="password" placeholder="请输入密码">
```

### 2.11 表单 radio checkbox 单选功能和默认选中

**单选功能的语法**

* 采用input标签(type radio)下**name属性**
* 有相同name属性的radio表单为一组，一组中仅可选中一个

**默认选择** checked属性

* 适用于radio表单和checkbox表单

```html
<!-- 性别: <input type="radio" >男 <input type="radio">女 -->
性别: <input type="radio" name="sex">男 <input type="radio" name="sex">女
<br>
<!-- 默认选中 -->
性别: <input type="radio" name="sex_1" checked>男 <input type="radio" name="sex_1" checked>女
<br>
<input type="checkbox" checked> 我是Galaxy
```

### 2.12 file 上传多个文件

**语法**

* multiple属性 (mu)

```html
<input type="file" multiple>
```

### 2.13 input按钮

**按钮分类介绍**

* submit 提交按钮 点击之后提交数据给后端服务器
* reset 重置按钮 点击之后恢复表单默认值
* submit和reset标签**正常使用的前提是具有表单域标签**
* button 普通按钮，无默认功能，之后配合js添加功能 
* 给按钮添加显示文字 **属性 value 属性值 按钮文字**

**表单域**

* form双标签
* 属性: <br> action 属性值 数据提交地址
* 作为**其域下表单的父标签**

```html
<form action="">
    用户名: <input type="text">
    <br>
    <br>
    密码: <input type="password">
    <br>
    <br>
    <input type="submit" value="免费注册"><input type="reset"><input type="button" value="普通按钮">
</form>
```

### 2.14 表单 button 按钮标签

*不同于input表单按钮，还有另一种双标签单独表示按钮*

**语法**

* button双标签
* type属性值 <br> submit 提交按钮 <br> reset 重置按钮 <br> button 普通标签
* 功能同input表单按钮

**注意**

* **默认为提交按钮**
* 包裹内容为显示(文字图片等)
* **同样需要form的包裹**

```html
<form action="">
    <input type="text" placeholder="用户名">
    <br><br>
    <input type="password" placeholder="密码">
    <br><br>
    <button>我是按钮</button>
    <button type="submit">提交按钮</button>
    <button type="reset">重置按钮</button>
    <button type="button">普通按钮</button>
</form>
```

### 2.15 表单 select下拉菜单

*在网页中提供**多个选择项的下拉菜单**表单控件*

**语法**

* select双标签 表示下拉菜单整体
* option双标签 表示下拉菜单的每一项 **独占一行** <br> 默认选择 **selected属性** 如无option标签有selected属性，则默认选中第一个

```html
<select>
    <option>北京</option>
    <option>上海</option>
    <option>广州</option>
    <option selected>深圳</option>
</select>
```

### 2.16 表单 textarea文本域标签

*可以输入多行文本，常用于网页评论区域*

**语法**

* textarea双标签
* 常用属性 <br> cols 规定文本域可见宽度 <br> rows 规定文本域可见行数


**注意**

* 右下可以放缩(CSS可以禁用)
* 通过CSS规定大小，而不用属性

```html
<textarea cols="60" rows="30"></textarea>
```

### 2.17 表单 label标签

*用于使非表单内容和表单标签的绑定*

**语法a**

1. 通过label标签将内容(文本等)包裹
2. 在表单标签上添加id属性
3. 在label标签的for属性中设置对应的id属性值

**语法2**

1. 直接使用label标签把内容(文本等)和表单标签一起包裹
2. 把lebel的for属性删掉即可

```html
<form action="">
    性别: 
    <input type="radio" name="sex" id="nan"> <label for="nan">男</label>
    <label>
        <input type="radio" name="sex"> 女
    </label>
</form>
```

### 2.18 语义化标签

**没有语义的标签**

* div双标签 **包裹文字独占一行**
* span双标签 
* 以上两个标签作布局使用，通过CSS添加效果

**有语义的标签**

* header双标签 网页头部
* nav双标签 网页导航
* footer双标签 网页底部
* aside双标签 网页侧边栏
* section 网页区块
* article 网页文章
* 和div一样，独占一行，通过CSS添加效果。**用于手机端网页布局**

```html
<header>网页头部</header>
<nav>网页导航</nav>
<footer>网页底部</footer>
<aside>网页侧边栏</aside>
<section>网页区块</section>
<article>网页文章</article>
```

### 2.19 字符实体

*网页对多个空格会合并为一个空格*

*实现网页中多个空格的效果*

**语法**  `&nbsp;`

```html
这是HTML文档&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;现在要学习字符实体。
```

## *叁* CSS基础

https://caniuse.com 查看适配性

---

### 3.1 体验CSS

**CSS** 

* 层叠样式表
* 美化网页

**CSS写在哪**

* style双标签内
* style标签在head标签内(title下)

**写法**

* 选择器+{属性 : 属性值;...}
* 选择器: 标签名

**注释**

* `/**/`
* vscode中的快捷键同样为`ctrl`+`/`

```html
<head>
    <meta charset="UTF-8">
    <!-- 3s自动刷新 -->
    <meta http-equiv="refresh" content="1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>体验CSS</title>
    <style>
        /* CSS的注释 */
        /* 这里写的都是CSS */
        /* 选择器 {CSS属性} */
        /* 选择器：查找标签 */
        p{
            /* 文字颜色变成红色 */
            color: red;
            /* 字变大 px:像素*/
            font-size: 30px;
            /* 背景颜色 */
            background-color: green;
            /* width height */
            width: 400px;
            height: 400px;
        }
    </style>
</head>
<body>
    <p>这是一个p标签</p>
</body>
```

### 3.2 CSS其它引入方式

* 内嵌式 在head标签内的style标签内
* 外联式 写在独立的.css文件中(常用)，通过link标签在html文件中引入 <br> link单标签在head标签内(title下)
* 行内式 写在标签的style属性中，属性值为前两种写法{}内的内容，后续配合js使用

.html
```html
<head>
    <meta charset="UTF-8">
    <!-- 3s自动刷新 -->
    <meta http-equiv="refresh" content="1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS的引入方式</title> 
    <!-- 关系: 样式表 -->
    <link rel="stylesheet" href="./try.css">   
</head>
<body>
    <!-- css到底能写在哪里 -->
    <p>这是一个p标签</p>
    <div style="color: blue; font-size: 30px;">这是div标签</div>
    <div>这个div是什么颜色</div>
</body>
```

.css
```css
/* 选择器{} */
p{
    color: red;
}
```

### 3.3 CSS选择器

*如何找到要规定样式的标签*

#### 标签选择器

* 标签名{CSS属性名:属性值;}
* **所有的**这个标签都生效

.html
```html
<body>
    <p>ppppp</p>
    <p>这个p是什么颜色呢</p>
    <p>22222</p>
</body>
```

.css
```css
/* 选择器{} */
/* 标签选择器 就是 以标签名命名的选择器 */
p{
    color: red;
}
```

#### 类选择器

* 定义(CSS中)  `.类名{CSS属性名:属性值;}`
* 使用(html中) `标签身上设置class属性 属性值为类名(无.)`

**注意**

* 类名可以由数字字母下划线中划线组成，但**只能以字母和下划线**开头
* 一个标签可同时拥有多个类名，**类名之间以空格隔开（仍在前面的class属性值内）**

.html
```html
<body>
    <!-- 类选择器 需要定义和使用-->
    <!-- 一个标签可以使用多个类名，空格隔开即可 -->
    <p class="red size">111</p>
    <p>222</p>
    <div class="red">这个标签文字也要变红</div>
</body>
```

.css
```css
/* 选择器{} */
/* 标签选择器 就是 以标签名命名的选择器 */
.red{
    color: red;
}

.size{
    font-size: 66px;
}
```

#### id选择器

*id和类相似，但id的作用一般不是CSS，而在后续JS中使用*

* 定义在CSS `#id属性值{CSS属性名:属性值;}`
* 使用在HTML `设置标签的id属性值`

**注意**

* id属性类似身份证号码，在一个页面是**唯一不可重复的**
* **一个标签上只能有一个id属性值**

.html
```html
<body>
    <div id="blue">这个div是蓝色的</div>
    <!-- <p id="blue">111</p> -->
</body>
```

.css
```css
/* 定义id选择器 */
#blue{
    color: skyblue;
}
```

#### 通配符选择器

* `*{CSS属性名:属性值;}`
* 作用为找到页面中的所有标签，设置样式
* 特殊情况下才会使用 如: 清空所有标签的内外边距

.html
```html
<body>
    <div>div</div>
    <p>pppp</p>
    <h1>h1</h1>
    <span>span</span>
</body>
```

.css
```css
*{
    color: red;
}
```

### 3.4 文字基本样式

#### 字体大小

**语法**

* `font-size : 数字 + px`
* 默认字号为31px

.html
```html
<body>
    <!-- 浏览器当中默认字号为16px -->
    <p>段落文字</p>
</body>
```

.css
```css
p{
    font-size: 30px;
}
```

#### 字体粗细

**语法**

* `font-weight : 数字(100-900整百数)`推荐
* `font-weight : normal/bold`
* 默认正常为400，加粗为700

.html
```html
<body>
    <div>这是div</div>
    <h1>一级标题</h1>
</body>
```

.css
```css
div{
    font-weight: 700;
}

h1{
    font-weight: 400;
}
```

#### 字体倾斜

**语法**

* `font-style : normal/italic`

.html
```html
<body>
    <div>div文字</div>
    <em>em</em>
</body>
```

.css
```css
div{
    font-style: italic;
}
em{
    font-style: normal;
}
```

### 3.5 字体

**语法**

* `font-family : 具体字体`
* windows默认字体为**微软雅黑**

**常见字体**

* 无衬线字体 类微软雅黑 笔画均匀，无笔锋 **常用** <br> sans-serif
* 衬线字体 类宋体 笔画粗细不均，有笔锋 <br> serif
* 等宽字体 每个字母占据宽度相同 <br> monospace

.html
```html
<body>
    <div>这是一个div标签</div>
</body>
```

.css
```css
div{
    /* 如果用户电脑没有安装微软雅黑，那么就按黑体显示文字 */
    /* 如果黑体也没安装，那么按任意一种非衬线字体系列显示 */
    font-family:微软雅黑,黑体,sans-serif;
}
```

### 3.6 CSS的层叠性

*给同一个标签设置了相同的样式，最下面的会生效*

.html
```html
<body>
    <p>pppppp</p>
</body>
```

.css
```css
p{
    /* 基于层叠性，后面的覆盖前面的 */
    color: red;
    color:blue;
}
```

### 3.7 font复合属性

*字体相关属性仅用一个属性即可完成*

**语法**

* `font:style weight size family`

**注意**

* **只能省略前两个**(style weight)，省略表示默认值

.html
```html
<body>
    <p>这是p标签</p>
    <div>div</div>
</body>
```

.css
```css
p{
    /* font:style weight size family */
    font:italic 700 66px 微软雅黑;
    font-style: normal;

    /* 一个属性冒号后面书写多个值的写法 -- 复合属性 */
}

div{
    font: 100px 微软雅黑;
}
```

### 3.8 文本缩进

*应用场景&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;常用于段落开头的两个空格*

**语法**

* text-indent:数字+px
* text-indent:数字+em **推荐** (1em = 当前标签的font-size)

.html
```html
<body>
    <p>达奇先生的离世也引起了众多粉丝和同行的惋惜和追思。他的逝去意味着华语电影界损失了一位重要的艺术家，让人倍感惋惜。然而，在这个充满悲痛的时刻，我们应该深思一下这位艺术家为华语电影界所做的贡献。无论是在电影剧情中，还是在人物角色的塑造上，他都以其出色的才华和专业的态度给观众们带来了无尽的欢乐和震撼。</p>
</body>
```

.css
```css
p{
    /* 首行缩进2个字大小 */
    /* 默认字号16px */
    text-indent: 32px;
    font-size: 20px;
    /* em 一个字大小 */
    text-indent: 2em;
}
```

### 2.9 文本水平对齐方式

**语法**

* text-align:left/center/right

**适用对象**

* 文本
* span标签,a标签
* input标签，img标签
* ...

**注意**

* 要居中谁，则要给**包裹住居中对象的标签**加

.html
```html
<body>
    <h1>新闻标题</h1>
    <div>
        <img src="./1.gif">
    </div>
</body>
```

.css
```css
h1{
    text-align: left;
    text-align: right;
    text-align: center;
}

div{
    text-align: center;
    
}
```

### 2.10 文本修饰线

*控制下划线，删除线，上划线的有无*
*常用于清楚a标签的下划线*

**语法**

* text-decoration:underline/line-through/overline/none

.html
```html
<body>
    <div>div</div>
    <p>ppp</p>
    <h2>h2</h2>
    <a href="./jmphtml.html">跳转</a>
</body>
```

.css
```css
div{
    text-decoration: underline;
}
p{
    text-decoration: line-through;
}
h2{
    text-decoration: overline;
}
a{
    text-decoration: none;
}
```

### 2.11 行高

*控制两行文字间距离&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上间距+文本高度+下间距*

**语法**

* line-height:数字px
* lint-height:数字&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;表示font-size的倍数

*vscode中查看-自动换行设置分多行显示*

**注意**

* font复合属性中size可以加line-height
* 写法 font : style weight size **/** line-height family

.html
```html
<body>
    <p>2019年，事件视界望远镜团队让世界首次看到了黑洞的样子。不过，研究人员公布的这张发光环形物体的图像并不是传统的图片，而是经过计算获得的。利用位于美国、墨西哥、智利、西班牙和南极地区的射电望远镜所得到的数据，研究人员进行了数学转换，最终合成了这张标志性的图片。研究团队还发布了实现这一壮举所用的编程代码，并撰文记录这一发现，其他研究者也可以在此基础上进一步加以分析。</p>
</body>
```

.css
```css
p{
    line-height:50px;
    line-height: 1.5;
    font-size: 32px;
    font: italic 700 66px/2 宋体;
}
```

### 2.12 颜色常见取值

* 关键词写法 `red blue yellow...`
* rgb表示法 `rgb(..,..,..)`
* raba表示法 `rgba(..,..,..,..)` <br> a表示透明度 0-1 其余 0-255
* 十六进制表示法 `#...` <br> 六位数 两两分组 分别为r,g,b 如果全部组中每组两个数都一样，可以简写为一个

### 2.13 标签水平居中方法总结

*text-align : center;是让内容水平居中*

**外部标签水平居中的方法**

* margin : 0 auto;
* 0 表示上下居中
* auto 表示左右居中

## *肆* CSS进阶

---

### 4.1 选择器-后代

*根据HTML标签的嵌套关系，选择父元素后代中满足条件的元素*

**语法**

* `选择器1 选择器2 ...{CSS}`
* 从祖先开始找到满足这种嵌套关系的所有选择器
* 可以是标签名，类名，id，通配符

.html
```html
<body>
    <!-- 儿子，孙子，重孙子...... -->
    <p>这是一个p标签</p>
    <span>
        <div>
            <p>这是div的儿子</p>
        </div>
    </span>
</body>
```

.css
```css
/* 找到div的儿子，设置文字颜色为红色 */
/* 父选择器 后代选择器{} */
body div p{
    color: red;
}
```

### 4.2 子代选择器

*与后代不同，子代选择器只能选择儿子*

**语法**

* `选择器1>选择器2>...`
* 从祖先开始找到下一代中的选择器，继续找子代...
* 可以是标签名，类名，id，通配符

.html
```html
<body>
    <div>
        父级
        <a href="#">这是div里面的a</a>
        <p>
            <a href="#">这是div里面的p里面的a</a>
        </p>
    </div>
</body>
```

.css
```css
/* 空格隔开的是后代，儿子，孙子，重孙子(满足嵌套关系) */
/* div a{
    color: red;
} */

/* 只想选中儿子a */
/* div的儿子a文字颜色是红色 */
div>a{
    color: red;
}
```

### 4.3 并集选择器

*同时选择多组标签，设置一样的样式*

**语法**

* `选择器1，选择器2，...{CSS}`
* 每个选择器,结束**换行**
* 可以是标签名，类名，id，通配符

.html
```html
<body>
    <p>ppp</p>
    <div>div</div>
    <span>span</span>
    <h1>h1</h1>
    <h2>h2</h2>
</body>
```

.css
```css
/* p div span h1 文字颜色是红色 */

p,
div,
span,
h1{
    color: red;
}
```

### 4.4 交集选择器

*有些情况仅从类名或标签名无法找到，这时两者都需要*

**语法**

* `选择器标签名类名..`*连写*

.html
```html
<body>
    <!-- 找到第一个p，带box类的，设置文字颜色是红色 -->
    <p class="box">这是p标签:box</p>
    <p>ppppp</p>
    <div class="box">这是div标签</div>
</body>
```

.css
```css
/* p{
    color: red;
} */

/* .box{
    color: red;
} */

/* 必须是p标签，而且添加了box类 */

p.box{
    color: red;
}
```

### 4.5 hover伪类选择器

*设置鼠标悬停在元素上的状态样式*

**语法**

* `选择器:hover{CSS}`
  
.html
```html
<body>
    <a href="#">这是超链接</a>
    <!-- 任何标签都可以添加伪类 -->
    <div>div</div>
</body>
```

.css
```css
/* 悬停的时候文字是红色 */
a:hover{
    color:red;
    background-color: green;
}
/* 鼠标悬停到div的时候文字是绿色 */
div:hover{
    color: green;
}
```

### 4.6 Emmet语法

*vscode的功能，通过简写，快速生成代码*

.html
```html
<body>
    <!-- div -->
    <div></div>
    <!-- h1 -->
    <h1></h1>

    <!-- 生成div 带类名 -->
    <!-- .box -->
    <div class="box"></div>

    <!-- p.box -->
    <p class="box"></p>

    <!-- #fun -->
    <div id="fun"></div>

    <!-- p#box -->
    <p id="box"></p>

    <!-- p#box.red -->
    <p id="box" class="red"></p>

    <!-- div 同级 p -->
    <!-- div+p -->
    <div></div>
    <p></p>
    
    <!-- 父子> -->
    <!-- div>p -->
    <div>
        <p></p>
    </div>

    <!-- ul>li -->
    <ul>
        <li></li>
    </ul>

    <!-- ul有3个li -->
    <!-- ul>li*3 -->
    <ul>
        <li></li>
        <li></li>
        <li></li>
    </ul>

    <!-- ul里面有3个li,li里面有文字 {}-->
    <!-- ul>li{111}*3 -->
    <ul>
        <li>11</li>
        <li>11</li>
        <li>11</li>
    </ul>

    <!-- ul里面有3个li,li里面文字1,2,3 -->
    <!-- ul>li{$}*3 -->
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
</body>
```

.css
```css
div{
    /* font-size: ; */
    /* fsz */
    font-size: ;
    /* 提示CSS属性：单词的首字母 */
    /* fw700 */
    font-weight: 700;
    /* w */
    width: ;
    /* h */
    height: ;
    /* bgc */
    background-color: #fff;
    /* lh */
    line-height: ;

    /* 宽度300，高度200，背景色粉色 */
    /* w300+h200+bgc */
    width: 300px;
    height: 200px;
    background-color: pink;
}
```

### 4.7 背景色

**语法**

* `background-color : 关键字/rgb/rgba/十六进制`
* Emmet `bgc`

**注意**

* 背景色默认为透明 rgba(0,0,0,0)

.html
```html
<body>
    <div>div</div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    /* background-color: pink; */
    /* background-color: #ccc; */
    /* 红绿蓝是三原色，a是透明度0-1 */
    /* background-color: rgba(0,0,0,0.5); */
    background-color: rgba(0,0,0,.5);
}
```

### 4.8 背景图片

**语法**

* `background-image : url(图片的路径)`
* Emmet `bgi`

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
    background-image: url(./1.jpg);
}
```

### 4.9 背景平铺

*当盒子尺寸比背景大，会出现复制现象，通过修改背景平铺方式来修改*

**语法**

* `background-repeat : repeat/no-repeat/repeat-x/repeat-y`
* Emmet `bgr`
* 默认为 `repeat`  

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
    background-image: url(./1.gif);
    /* background-repeat: repeat; */
    background-repeat: no-repeat;
    background-repeat: repeat-x;
    background-repeat: repeat-y;
}
```

### 4.10 背景位置

*对于no-repeat的背景图默认为背景的左上*

**语法**

* `background-position: 水平方向放置 竖直方向放置`
* Emmet `bgp`
* 属性值 <br> 水平方向放置 `left` `center` `right` <br> 竖直方向放置 `top` `center` `bottom` <br> 数字px 原点为左上 x正方向 右 y正方向 下 

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    background-color: pink;
    background-image: url(./1.gif);
    background-repeat: no-repeat;
    background-position: right 0;
    background-position: right bottom;
    background-position: center center;
    background-position: center;
    background-position: 50px 100px;
    background-position: -30px -10px;

    /* 正数：向右向下移动，正数：向左向上移动 */
    /* 注意：背景色和背景图只显示在盒子的里面 */
}
```

### 4.11 background复合属性

**语法**

* `background: color image repeat position`
* Emmet `bg`
* 可按需求省略

.html
```html
<body>
    <div></div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    background: pink url(./1.gif) no-repeat center;
}
```

### 4.12 img和背景图区别

**都可实现在网页中显示一张图的效果**

* img标签
* div设置背景图

**区别-宽高的设置**

* img标签不设置宽高默认以图片的尺寸显示
* div背景图，需要**设置div的宽高**

**使用场景**

* img-插入图，用来实现较重要的图片
* bgi-背景图，用来实现修饰性图片(没有不影响使用)、可替代的交互效果等

### 4.13 元素显示模式-块

*标签也可以叫做标记、元素*

*显示模式 独占一行 一行可多个...*

**显示特点**

* 独占一行(一行只显示一个)
* 宽度**默认是父元素的宽度**，高度默认由内容撑开
* 可以设置宽高

**代表标签**

* **div**
* **p**
* **h系列**
* ul dl li ... form header

.html
```html
<body>
    <!-- 块:独占一行;宽度默认是父级的100%;添加宽高都生效 -->
    <div>11111</div>
    <br>
    <div>22222</div>
</body>
```
.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

### 4.14 元素显示模式-行内

**显示特点**

* 一行可以显示多个
* 宽度和高度默认由内容撑开
* **不可以设置宽高**

**代表标签**

* **a span** b u i s strong ins em del...

.html
```html
<body>
    <span>span</span>
    <span>span</span>
</body>
```

.css
```css
/* 行内:不换行;设置宽高不生效;尺寸和内容的大小相同 */
span{
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

### 4.15 元素显示模式-行内块

**显示特点**

* 一行可以显示多个
* **可以设置宽高**

**代表标签**

* **input textarea** button select
* img有行内块特点，但Chrome调试工具中显示inline

.html
```html
<body>
    <img src="1.gif" alt="">
    <img src="1.gif" alt="">
</body>
```

.css
```css
/* 行内块:一行显示多个;加宽高生效 */
img{
    width: 100px;
    height: 100px;
}
```

### 4.16 元素显示模式转换

*让元素符合另一种显示模式的布局要求*

**语法**

* `diaplay:block` 转换为块级元素 常用
* `display:inline-block` 转换为行内块元素 
* `display:inline` 转换为行内 很少用

.html
```html
<body>
    <div>11111</div>
    <div>22222</div>
    <span>span</span>
    <span>span</span>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;

    /* 转换为行内块 */
    display: inline-block;

    /* 转为行内 */
    display: inline;
}

span{
    width: 200px;
    height: 200px;
    background-color: pink;

    /* 转换为行内块 */
    display: inline-block;

    /* 转换为块 */
    display: block;
}
```

### 4.17 标签的嵌套规范

**大的准则&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;块套其它一般ok（p不套块），但行内，行内块一般不套块**

<br><br>

**块级元素一般作为大元素，可以嵌套文本，块级元素，行内元素，行内块元素等**

* 但是**p标签中不要嵌套div，p，h等块级元素**
* **h标签中也不能嵌套p标签**

<br><br>

**a标签内部可以嵌套除a标签外的任意标签**

```html
<body>
    <!-- p和h标题不能相互嵌套 -->
    <!-- <p>
        <h1>一级标题</h1>
    </p> -->

    <!-- p里面不能包含div -->
    <!-- <p>
        <div>divdiv</div>
    </p> -->

    <!-- a标签内部可以除a外嵌套任意元素 -->
    <!-- <a href="#">
        aaa
        <a href="#">aaa</a>
    </a> -->
</body>
```

### 4.18 CSS继承性

**特性**

* 子元素默认继承父元素的样式特点

**常见的可继承属性**

* 文字控制属性都可继承
* color
* font类
* text类
* line-height
* ...
* 不是控制文字的都不能继承

**特殊情况**

* a标签的color不从父级继承
* h系列标签的font-size不从父级继承

*自己有就不继承*

.html
```html
<body>
    <div>
        这是div里面的文字
        <span>这是div里面的span</span>
    </div>
    <div>
        <a href="#">这是超链接</a>
        <h1>一级标题</h1>
    </div>
</body>
```

.css
```css
/* 控制文字的属性都能继承，不是控制文字的属性都不能继承 */
div{
    color: pink;
    font-size: 30px;
    height: 300px;
}

a{
    color: red;
}
```

### 4.19 CSS层叠性

**特性**

* 给同一个标签设置不同的样式->层叠->共同作用在标签
* 给同一个标签设置相同样式->层叠->最终写在最后的样式生效

**注意**

* 样式冲突时，只有**选择器优先级相同**时，才能通过层叠判断

*vscode中`Alt`同时选择多个位置写*

## *伍* CSS盒子模型

### 5.1 CSS优先级

**特性**

* 不同的选择器有不同优先级，**优先级高的选择器样式会覆盖优先级低的选择器样式**

**选择器的优先级**

* 继承 < 通配符选择器 < 标签选择器 < 类选择器 < id选择器 < 行内样式 < !important
* 总结而言，**可以更精准选到某一标签的选择器优先**
* !important可以**提高除继承外任意一级优先级至最高** <br> 写在属性值后，;前

.html
```html
<body>
    <!-- 意义: 当一个标签使用多个选择器，样式冲突时，到底谁生效 -->
    <div class="box" id="box" style="color: pink;">测试优先级</div>
</body>
```

.css
```css
#box{
    color: orange;
}

.box{
    color: blue;
}

div{
    color: green;
}

*{
    color: skyblue !important;
}

body{
    color: red;
}

/* ！important不要给继承的添加，自己有样式无法继承父级样式 */
```

### 5.2 权重(优先级)叠加计算

*可表示同一标签的复合选择器要通过权重叠加计算方式来判断最终哪个选择器在这个标签生效*

**叠加计算方法**

* 依次比较`行内样式的个数` `id选择器的个数` `类选择器的个数` `标签选择器的个数` <br> 若**某一环节不同，则多的优先级大** <br> 最终所有环节**比较个数相同，则优先级相同，根据层叠性生效**

.html
```html
<body>
    <div class="father">
        <p class="son" id="one">我是一个标签</p>
    </div>
</body>
```

.css
```css
/* 行内 id 类 标签 */

div #one{
    color: orange;
}

.father .son{
    color: skyblue;
}

.father p{
    color: purple;
}

div p{
    color: pink;
}
```

*注意`!important`的最高优先级效果*

**都是继承的情况**

* **直接继承高于间接继承**（继承于父大于继承于祖）
* 都是直接或都是同级间接继承，**按照叠加顺序比较**

### 5.3 盒子模型-组成

**概念**

* **每个标签可以看做一个盒子**，通过盒子视角更**方便布局**
* 浏览器在渲染页面时，会将页面中的元素看做**一个个矩形区域**，我们也形象称之为**盒子**

**内容组成**

* 内容区域 `content`
* 内边距区域 `padding`
* 边框区域 `border`
* 外边距区域 `margin`

.html
```html
<body>
    <div>内容</div>
    <div></div>
</body>
```

.css
```css
div{
    /* 纸箱子，填充泡沫 */
    width: 300px;
    height: 300px;
    background-color: pink;
    /* 边框线 == 纸箱子*/
    border: 1px solid #000;
    /* 内边距 == 填充泡沫 : 出现在内容和盒子边缘之间*/
    padding: 20px;
    /* 外边距 : 出现在两个盒子之间，出现在盒子的外面 */
    margin: 50px;
}
```

### 5.4 内容的宽度和高度

*width和height默认设置为盒子内容content的大小*

**语法**

* `width: 数字px`
* `height: 数字px`

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

### 5.5 边框border

**语法**

* 复合属性
* `border: 线宽 线条种类(虚实...) 颜色`
* 线条种类 `solid` 实线 `dashed` 虚线 `dotted` 点线
* **不可省略**，不分先后顺序
* Emmet `bd`

**单方向设置**

* 只给盒子的某方向单独设置边框*
* `border-left/right/top/bottom: 线宽 线条种类(虚实...) 颜色`

**单个属性**

* 不常用
* `border(-方位)-width/style/color`

.html
```html
<body>
    <div>内容</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
    background-color: pink;
    
    /* solid : 实线 */
    /* dashed : 虚线 */
    /* dotted : 点线 */
    border: 1px solid #000;
    border: 5px dashed #000;
    border: 5px dotted green;
    /* 单方向 */
    border-left: 1px solid #000;
    border-right: 1px solid red;
    border-top: 1px solid blue;
    /* 单个属性 */
    border-bottom-style: solid;
}
```

*border会撑大盒子的尺寸*
*盒子尺寸要考虑到边框*

### 5.6 内边距

**语法**

* `padding :数字px`上下左右为相同内边距
* 也可作为复合属性 <br> `padding :数字px 数字px 数字px 数字px`分别设置上右下左内边距 <br> `padding :数字px 数字px 数字px`分别设置上右下内边距，左右内边距相同 <br> `padding :数字px 数字px`分别设置上右边距，上下边距相同，左右边距相同
* 也可以`padding-方位`单独设置某一方向内边距

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 300px;
    height: 300px;
    background-color: pink;
    /* 添加了4个方向的内边距 */
    /* padding: 50px; */
    padding: 10px ;

    /* padding属性可以当做复合属性 : 表示单独设置某个方向的内边距 */
    /* 最多取4个值 从上开始，顺时针*/
    padding: 10px 20px 40px 80px;

    /* 三值 */
    padding: 10px 40px 80px;

    /* 两值 */
    padding: 10px 80px;
}
```

*和border类似，padding同样会扩大盒子，计算width和height时要减掉*

### 5.7 自动内减

*代替手动减去border和padding*

**语法**

* `box-sizing: border-box`
* 添加padding和border后，不扩大盒子，自动在内容中减去
* 此时width和height设置的是盒子的大小

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 100px;
    height: 100px;
    background-color: pink;
    border: 10px solid #000;
    padding: 20px;

    /* 内减模式 */
    box-sizing: border-box;
}
```

### 5.8 外边距


**语法**

* `margin`
* 与内边距设置方式完全相同

.html
```html
<body>
    <div>文字</div>
</body>
```

.css
```css
div{
    width: 100px;
    height: 100px;
    background-color: pink;
    margin: 50px;
    margin-left: 100px;
}
```

### 5.9 清除默认内外边距

*浏览器会给一些标签提供默认的内外边距*

**具有默认内外边距的标签**

* body默认 `margin: 8px`
* p标签默认右上下的`margin`
* ul标签默认有上下`margin`和`padding-left`
* ...

**清除语法**

```css
*{
    margin: 0;
    padding: 0;
}
```

### 5.10 版心居中

*版心&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;网页的有效内容*

**语法**

* `margin: 0 auto`
* auto意为左右自动相等，浏览器自动计算出

.html
```html
<body>
    <div>版心</div>
</body>
```

.css
```css
div{
    width: 1000px;
    height: 300px;
    background-color: pink;
    margin: 0 auto;
}
```

### 5.11 块级元素外边距的问题

**外边距合并现象**

* 垂直布局的块级元素，上下的margin会合并,两者中国最大值会合并
* 解决方案 <br> 只给其中一个设置`margin`

.html
```html
<body>
    <div class="one"></div>
    <div class="two"></div>
</body>
```

.css
```css
div{
    width: 100px;
    height: 100px;
    background-color: pink;
}

.one{
    margin-bottom: 100px;
}

.two{
    margin-top: 60px;
}
```

**外边距塌陷问题**

* 互相嵌套的**块级元素**，子元素的`margin-top`会导致父元素一起下移
* 解决方案 <br> 1. 给父元素设置`border-top`或`padding-top`（分隔父子元素的`margin-top`）<br> 2. 给父元素设置 `overflow: hidden` **推荐使用** <br> 3. 转换为行内块元素 <br> 4. 设置浮动

.html
```html
<body>
    <div class="father">
        <div class="son">son</div>
    </div>
</body>
```

.css
```css
.father{
    width: 300px;
    height: 300px;
    background-color: pink;
    /* padding-top: 10px; */
    /* 如果设计稿没有border,不能使用这个方法 */
    /* border: 1px solid #000; */
    /* overflow: hidden; */
    display: inline-block;
}

.son{
    width: 100px;
    height: 100px;
    background-color: skyblue;
    margin-top: 50px;
}
```

### 5.12 行内元素的内外边距问题

**如果想要通过`margin`或`padding`改变行内标签垂直位置，无法生效**

* `margin-top` `margin-bottom`不生效
* `padding-top` `padding-bottom`不生效
* 解决方法<br> 行高`line-height`可以改变垂直位置

.html
```html
<body>
    <span>span</span>
    <span>span</span>
</body>
```

.css
```css
span{
    /* margin: 100px; */
    padding: 100px;
}
```

## *陆* CSS浮动

---

### 6.1 结构伪类选择器

*通过元素的结构关系查找元素*

*减少对类的依赖*

**语法**

* `E:first-child{}`
* `E:last-child{}`
* `E:nth-child(n){}` **重点** 某父级元素下的第n个，且为E元素
* `E:nth-last-child(n){}`

.html
```html
<body>
    <ul>
        <li>这是第1个li</li>
        <li>这是第2个li</li>
        <li>这是第3个li</li>
        <li>这是第4个li</li>
        <li>这是第5个li</li>
        <li>这是第6个li</li>
        <li>这是第7个li</li>
        <li>这是第8个li</li>
    </ul>
</body>
```

.css
```css
/* 选中第一个 */
/* li:first-child{
    background-color: green;
} */

/* 最后一个 */
/* li:last-child{
    background-color: green;
} */

/* 任意一个 */
/* li:nth-child(5){
    background-color: green;
} */

/* 倒数第xx个 */
li:nth-last-child(1){
    background-color: blue;
}
```

**公式写法**

* 用来筛选一些**有明显数学关系**的子元素
* `E:nth-child(n){}`中的n可以去取值为公式 <br> 2n 偶数 <br> 2n+1/2n-1 奇数 <br> -n+5 前五个数 *n在前* <br> n+5 第五个及以后
* 在公式中 n的取值从0开始一直自增，能取到的子选择器即为筛选到的

.html
```html
<body>
    <ul>
        <li>这是第1个li</li>
        <li>这是第2个li</li>
        <li>这是第3个li</li>
        <li>这是第4个li</li>
        <li>这是第5个li</li>
        <li>这是第6个li</li>
        <li>这是第7个li</li>
        <li>这是第8个li</li>
    </ul>
</body>
```

.css
```css
/* 偶数 */
/* li:nth-child(2n){
    background-color: green;
} */
/* 奇数 */
/* li:nth-child(2n+1){
    background-color: green;
} */
/* 前三个 */
/* li:nth-child(-n+3){
    background-color: green;
} */
/* 选中4,8 */
li:nth-child(4n){
    background-color: green;
}
```

### 6.2 伪元素

*元素&nbsp;&nbsp;&nbsp;HTML设置的标签<br>伪元素&nbsp;&nbsp;&nbsp;由CSS**模拟**出的标签效果*


*一些装饰性图案可以使用伪元素*

**语法**

* `::before` 在父元素**内容**最前添加一个伪元素
* `::after` 在父元素**内容**最后添加一个伪元素

**注意**

* 必须设置`content`属性才能生效
* 默认为行内元素

.html
```html
<body>
    <!-- 通过CSS创建标签， 装饰性的不重要的小图 -->

    <!-- 找父级，在这个父级里面创建子级标签 -->

    <div class="father">爱</div>

    <!-- 老鼠爱大米 -->
</body>
```

.css
```css
.father{
    width: 300px;
    height: 300px;
    background-color: pink;
}

.father::before{
    /* 内容 */
    /* content必须添加，否则伪元素不生效 */
    content: '老鼠';
    color: green;
    width: 100px;
    height: 100px;
    background-color: blue;
    /* 默认是行内元素，宽高不生效 */
    display: block;
}

.father::after{
    content: '大米';
}
```

### 6.3 标准流

*又称文档流 **显示模式***

**介绍**

* 是浏览器渲染显示网页内容的默认的一套**排版规则**，规定了应该以何种方式排列元素
* 如何更改 **浮动**  **定位**

### 6.4 体验行内块问题

**浮动的作用**

* 让块级元素完美地排在一行
* inline-block会有间距的问题，利用浮动代替

.html
```html
<body>
    <div class="one">one</div><div class="two">two</div>
</body>
```

.css
```css
div{
    /* 浏览器解析行内块或行内标签时，如果标签换行书写会产生一个空格的距离 */
    display: inline-block;
    margin: 0;
    width: 100px;
    height: 100px;
}

.one{
    background-color: pink;
}

.two{
    background-color: skyblue;
}
```

### 6.5 浮动的作用

* 最初的目的&nbsp;&nbsp;&nbsp;图文环绕
* 现在的目的&nbsp;&nbsp;&nbsp;网页布局

**语法**
* `float: left/right`

.html
```html
<body>
    <!-- 1、图文环绕 -->
    <img src="./1.jpg">的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生的奶奶豆绿从都是老处男洞察到的农村你的没打卡MV麻烦到时明白吗覅是MV米没法打深V吗地v打死覅萨米大赛传达赛次阿妈大V啊上大VID是打发打发范德萨发生
    <br>
    <br>   

    <div class="one">one</div>
    <div class="two">two</div>
</body>
```

.css
```css
img{
    width: 150px;
    float: left;
}

div{
    width: 100px;
    height: 100px;
}

.one{
    background-color: pink;
    float: left;
}

.two{
    background-color: skyblue;
    /* flr */
    float: right;
    float: left;
}
```

### 6.6 浮动的特点

* 浮动的标签会脱离标准流的控制（脱标），在**标准流中不占位置**
* 浮动元素比标准流高**半个级别**，可以覆盖标准流中的元素,（**无法覆盖文字**）
* **浮动找浮动**，下一个浮动元素会在上一个浮动元素的左右浮动
* 特殊显示效果 <br> <ul><li>一行可以显示多个</li><li>可以设置宽高</li></ul>

**注意**

* 浮动的元素不能通过`text-align: center`或`margin: auto`

.html
```html
<body>
    <div class="one">one</div>
    <div class="two">two</div>
    <div class="three">three</div>
</body>
```

.css
```css
/* 浮动的标签  顶对齐 */
/* 浮动: 在一行排列，宽高生效--浮动后的标签具备行内块的特点 */
.one{
    width: 100px;
    height: 100px;
    background-color: pink;
    float: left;
    margin-top: 50px;
    margin-right: 10px;
}

.two{
    width: 200px;
    height: 200px;
    background-color: skyblue;
    float: left;
    /* 因为有浮动,不能生效 */
    margin: 0 auto;
}

.three{
    width: 300px;
    height: 300px;
    background-color: orange;
}
```

### 6.7 CSS属性书写顺序

*代码清晰化&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行效率高*

1. `float/display`
2. 盒子模型相关属性`margin` `border` `padding` 宽度高度背景色
3. 文字样式

### 6.8 清除浮动

*清除浮动给别的标签带来的影响*

**影响**

* 子元素浮动不能撑开标准流的块级父元素

.html
```html
<body>
    <!-- 父子级标签，子级浮动，父级没有高度，后面的标准流盒子会受影响，显示到上面的位置 -->
    <div>
        <div class="top">
            <div class="left"></div>
            <div class="right"></div>
        </div>
        <div class="bottom"></div>
    </div>
</body>
```

.css
```css
.top{
    margin: 0 auto;
    width: 1000px;
    height: 300px;
    background-color: pink;
}

.bottom{
    height: 100px;
    background-color: green;
}

.left{
    float: left;
    width: 200px;
    height: 300px;
    background-color: #ccc;
}

.right{
    float: right;
    width: 790px;
    height: 300px;
    background-color: skyblue;
}
```

### 6.9 清除浮动-额外标签

**方法**

1. 在父元素内容的最后添加一个**块级元素**
2. 给添加的块级元素设置`clear:both` <br> clear的属性值 <br> `left`清除左浮动的影响<br>`right` 清除右浮动的影响  <br> `both` 清除左右浮动的影响

**缺点**

* 会在页面中添加额外的标签，会让页面的HTML结构变复杂

.html
```html
<body>
    <!-- 父子级标签，子级浮动，父级没有高度，后面的标准流盒子会受影响，显示到上面的位置 -->
    <div>
        <div class="top">
            <div class="left"></div>
            <div class="right"></div>
            <div class="clearfix"></div>
        </div>
        <div class="bottom"></div>
    </div>
</body>
```

.css
```css
.top{
    margin: 0 auto;
    width: 1000px;
    /* height: 300px; */
    background-color: pink;
}

.bottom{
    height: 100px;
    background-color: green;
}

.left{
    float: left;
    width: 200px;
    height: 300px;
    background-color: #ccc;
}

.right{
    float: right;
    width: 790px;
    height: 300px;
    background-color: skyblue;
}

.clearfix{
    clear: both;
}
```

### 6.10 单伪元素清除法

*将额外元素转为伪元素*

*可额外标签法的原理相同*

*项目中常用*

```css
.clearfix::after{
    content: '';

    /* 伪元素默认添加行内元素，要求块 */
    display: block;
    clear: both;

    /* 为了兼容性 */
    height: 0;
    visibility: hidden;
}
```

*给父标签添加`clearfix`类即可清除浮动*

### 6.11 双伪元素清除法

*项目中常用*

*既可以清除浮动又可以解决块级标签外边距塌陷问题*

```css
/* .clearfix::before的作用在于解决外边距塌陷问题 */
/* 外边距塌陷: 父子标签，都是块级，子级加margin会影响父级的位置 */
.clearfix::before,.clearfix::after{
    content: '';
    display: table;
}
/* 真正清除浮动的标签 */
.clearfix::after{
    clear: both;
}
```

*给父标签添加`clearfix`类即可清除浮动*

### 6.12 清除浮动`overflow-hidden`

给父元素设置`overflow-hidden`

*可以清除浮动和避免塌陷*

## 学成在线项目-项目开发流程

---

### 准备工作

1. 创建根目录(英文名)，将来会上传服务器
2. 后续的所有素材也不可以出现中文名
3. 根目录下包含`images`、`css`文件夹(内含`index.css`)，html文件(名为`index.html`)

### 版心、清除默认样式

版心一般类名为`wrap`

清除默认样式常用代码
```css
/* 清除样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
li {
    list-style: none;
}
a {
    text-decoration: none;
}
.clearfix:before,.clearfix:after {
    content:"";
    display:table; 
}
.clearfix:after {
    clear:both;
}
```

### logo和nav

* logo布局 `h1>a>img`
* nav布局 `div.nav>ul>li>a`

*纯文字区域可以不给宽*

### 搜索

* 搜索布局 `div.search>form>input+button`

*使用表单，搜索图标用提交按钮(`button`双标签) 使用背景图*

**更改属性的CSS**

* `选择器::属性{CSS}`
* 如`input::placehorder{}`以更改placehorder文字的样式

### 用户区

* 布局 `div.user>img+span`

*包裹文字的span用来调节CSS，联动后台和数据*

*同样用户名不要给宽*

*调节图片垂直对齐方式采用`vertical-align:middle`*

### 轮播图

**布局**

* `.banner>.wrapper>.left+.right`

*右侧列表标题可以采用`h2`  列表采用`.right>h2+.(content>dl*3>dt+dd)+a.more`*


## *柒* CSS定位装饰

---

### 7.1 定位的作用和步骤

*页面中两个标签叠在一起*

*学成在线中精品推荐里的'hot'标签*

*标准流+浮动+定位配合才完美实现网页的布局*

**作用**

* 可以让标签摆放在**网页任意位置**
* 定位之后的元素**层级**最高，可以层叠**在其他盒子之上**
* 可以让盒子始终**固定在屏幕中的某个位置**

**使用步骤**

1. 设置定位方式 <br> <ul><li>CSS属性名:`position`</li><li>常见属性值:静态定位(不定位)`static`,**相对定位**`relative`,**绝对定位**`absolute`,**固定定位**`fixed`</li></ul>
2. 设置偏移值 <br> <ul><li>偏移量分为两个方向，水平和垂直方向各选一个</li><li>一般就近选择 CSS属性`left` `right` `top` `bottom` 属性值 `数字+px` or `百分比`</li></ul>

### 7.2 相对定位`relative`

*相对**自己**之前的位置进行移动*

***Emmet** por*

**注意**

* **相对定位**后在页面中仍占(原有)位置，没有脱标
* **相对定位**只有`position`属性，**没有方位属性，不会生效于自身（位置，脱标等），但算作自身已定位(对子级的绝对定位有影响)**
* 同时设置 `bottom` 和 `top` 以 `top` 为准，`bottom` 不生效
* 同时设置 `left` 和 `right` 以 `left` 为准，`right` 不生效


.html
```html
<body>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <div class="box">box</div>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
</body>
```

.css
```css
.box{
    position: relative;
    left: 100px;
    top: 200px;

    /* 
        1. 占用原来的位置 
        2. 仍然具备标签原有的显示模式(块级定位后，仍为块级，独占一行)
        3. 改变位置参照自己原来的位置
    */

    width: 200px;
    height: 200px;
    background-color: pink;
}
```

### 7.3 绝对定位`absolute` 相对于浏览器

*相对于**非静态定位的父元素（祖先）**进行定位，如**不存在这样的父级**，则相对于浏览器*

***Emmet** poa*

**注意**

* **绝对定位**查找的父元素**实际为祖先元素**，从父级开始向上查找，直到找到已定位的祖先，根据其进行绝对定位，否则根据浏览器窗口定位
* **绝对位置**脱标，不占位置
* **绝对定位**只有`position`属性，**没有方位属性，会生效:位置不变，脱标**
* 改变标签的显示模式特点: 具备**行内块显示特点**(可在一行共存，宽高生效,标签**默认由内容撑开 *注意***)

.html
```html
<body>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <div class="box">box</div>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
</body>
```

.css
```css
.box{
    /* 绝对定位:
        先找已经定位的父级，如果有这样的父级，就以这个父级为参照物进行定位。
        如果有父级，但是父级未定位，以浏览器窗口为参照进行定位。
    */
    position: absolute;
    /* left: 50px; */
    left: 0;
    top: 0;

    /* 
    1. 脱标，不占位
    2. 改变标签的显示模式特点: 具备行内块显示特点(可在一行共存，宽高生效)
    */

    width: 200px;
    height: 200px;
    background-color: pink;
}
```

*项目中通常不会采取这种相对于浏览器的定位方式*

### 7.4 绝对定位`absolute` 相对于有定位的父级（祖先）

*项目中常用*

* 项目中一般父级相对定位模式，子级绝对定位模式 **子绝父相**

.html
```html
<body>
    <div class="father">
        <div class="son">
            <div class="sun"></div>
        </div>
    </div>
</body>
```

.css
```css
.father{
    position: relative;
    width: 400px;
    height: 400px;
    background-color: pink;
}

.son{
    /* 相对，绝对 */
    /* 项目中一般父级相对定位模式，子级绝对定位模式 子绝父相*/
    /* position: relative; */
    /* position: absolute; */
    width: 300px;
    height: 300px;
    background-color: skyblue;
}

.sun{
    position: absolute;
    /* left: 20px;
    top: 30px; */
    right: 20px;
    bottom: 50px;
    width: 200px;
    height: 200px;
    background-color: green;
}
```

### 7.5 定位居中

*以前通过margin auto实现标签居中(适用于标准流)*

*当绝对定位后,margin auto失效*

*可以绝对定位配合margin居中（水平垂直均可）*

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    /* 绝对定位的盒子不能使用左右margin auto居中 */
    position: absolute;
    /* margin: 0 auto; */
    /* 相对于定位的父级，没有，相对于浏览器移动浏览器大小的一半 */
    left: 50%;
    top: 50%;
    /* 上面把基线调到浏览器的正中间 */
    /* margin配合把中心调到浏览器的正中间 */
    margin-left: -150px;
    margin-top: -150px;
    
    width: 300px;
    height: 300px;
    background-color: pink;
}
```

### 7.6 位移居中

*CSS中对于尺寸不支持手动计算的小数，可以通过位移间接表示*

*同时位移居中也方便修改代码*


* `transform:translate(a,b);`
* **Emmet** `tft`

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    /* 绝对定位的盒子不能使用左右margin auto居中 */
    position: absolute;
    /* margin: 0 auto; */
    /* 相对于定位的父级，没有，相对于浏览器移动浏览器大小的一半 */
    left: 50%;
    top: 50%;
    /* 上面把基线调到浏览器的正中间 */
    /* margin配合把中心调到浏览器的正中间 */
    /* margin-left: -150.5px;  */
    /* 位移:自己宽度高度的一半 */
    transform:translate(-50%,-50%);
    /* margin-top: -150px; */
    width: 401px;
    height: 300px;
    background-color: pink;
}
```

### 7.7 固定定位`fixed`

*相对于(浏览器)视口固定，不随浏览器的滚动等移动*

* **Emmet** `pof`

**注意**

* **固定定位** 脱标，不占位置
* **固定定位** 不写方位不生效
* **具备行内块特点** **脱标后由内容撑开，注意设置尺寸**

.html
```html
<body>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <div class="box">box</div>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
    <p>测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位测试定位</p>
</body>
```

.css
```css
.box{
    position: fixed;
    left: 0;
    top: 0;

    /* 
        1. 脱标，不占位置
        2. 改变位置参考浏览器窗口
        3. 具备行内块特点
    */

    width: 200px;
    height: 200px;
    background-color: pink;
}
```

### 7.8 定位-显示层级

**不同布局方式**

*标准流 < 浮动 < 定位*

**相同布局方式**

*标准流和浮动没有这种问题*

**对于定位**

* 默认取决于**HTML文件**中的书写顺序，后来者居上
* 可以通过`z-index:整数;`修改在上的优先级，优先级大的在上 <br> z-index的默认值是`0`
* `z-index`**必须配合定位**

.html
```html
<body>
    <div class="two">two</div>
    <div class="one">one</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
}

.one{
    position: absolute;
    left: 20px;
    top: 50px;
    background-color: pink;
}

.two{
    position: absolute;
    left: 50px;
    top: 100px;
    background-color: skyblue;
    /* z-index: 999; */
}

/* 
    默认情况下，定位的盒子 后来者居上(HTML文件中)
    z-index:整数; 取值越大，显示顺序越靠上
*/
```

### 7.9 装饰-vertical-align

**基线**

* 浏览器**文字类型元素**排版中存在**用于对齐**的基线

*浏览器处理**行内和行内块**元素默认按文字解析*

**修改默认对齐方式**

* CSS属性 `vertical-align`
* **Emmet** `va`
* 属性值 <br> `baseline`默认，基线对齐方式 <br> `top` 顶部对齐 <br> `middle` 中部对齐 **常用** <br> `bottom` 底部对齐
* 对行内、行内块添加，都是行内/行内块对**较大的添加即可**

**给图片垂直居中的方式**

* 给父级设置行高(与父级高度相同)
* 给图片设置`va-middle`

### 7.10 光标类型

*设置鼠标在元素上的显示样式*

**语法**

* CSS属性 `cursor`
* **Emmet** cu
* 属性值 <br> `default` 默认值，通常箭头 <br> `pointer` 小手效果，提示用户可以点击 <br> `text` 工字型，提示用户可以选择文字 <br> `move` 十字光标，提示用户可以移动

.html
```html
<body>
    <div>div</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
    background-color: pink;

    /* 手型 */
    cursor: pointer;

    /* 工字型，表示可以复制 */
    cursor: text;

    /* 十字型，表示可以移动 */
    cursor: move;
}
```

### 7.11 圆角边框

*让盒子的四个角变光滑，增加页面细节，提升用户体验*

**语法**

* CSS属性`border-radius`
* **Emmet** `bdrs`
* 属性值 <br> 数字+px ，百分比（半径） 最大值为盒子宽/高的一半
* 从**左上**开始赋值，无赋值看对角（1个值表示全都四个角都赋为该值 **常用**）

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    margin: 50px auto;
    width: 200px;
    height: 200px;
    background-color: pink;
    /* 一个值: 表示4个角是相同的 */
    border-radius: 10px;
    /* 4值: 左上 右上 右下 左下 -- 从左上顺时针转一圈*/
    border-radius: 10px 20px 40px 80px;

    border-radius: 10px 40px 80px;

    border-radius: 10px 80px;
}
```

**常见应用**

* 画一个正圆 <br> <ol style="list-style:decimal;"><li>盒子需要是正方形</li><li>设置边框圆角为盒子宽高的一半(50%)</li></ol>
* 胶囊按钮 <br> <ol style="list-style:decimal;"><li>盒子要求长方形</li><li>设置->border-radius: 盒子高度的一半</li></ol>

### 7.12 溢出部分显示方式`overflow`

*当盒子的**内容部分**超过盒子范围时的效果*

**语法**

* CSS属性`overflow`
* 属性值 <br> `visible` 默认值，溢出部分可见 <br> `hidden` 溢出部分隐藏 <br> `scroll` 无论是否溢出，都显示滚动条 <br> `auto` 根据是否溢出，自动显示或隐藏滚动条

.html
```html
<body>
    <div class="box">我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果我是div，测试溢出显示效果</div>
</body>
```

.css
```css
.box{
    width: 300px;
    height: 300px;
    background-color: pink;
    /* 溢出隐藏（常用） */
    overflow: hidden;
    /* 无论是否超出都显示滚动条(不常用) */
    overflow: scroll;
    /* 自动，根据是否溢出显示滚动条(不常用) */
    overflow: auto;
}
```

### 7.13 显示隐藏

*元素自身的隐藏 如hover时显示子菜单*

**语法**

* `visibility: hidden`不常用 <br> **Emmet** `v` <br> 隐藏后仍占位
* `display: none`常用 <br> 隐藏后不占位

.html
```html
<body>
    <div class="one">one</div>
    <div class="two">two</div>
</body>
```

.css
```css
div{
    width: 200px;
    height: 200px;
}

.one{
    /* 占位隐藏 */
    /* visibility: hidden; */
    /* ****不占位隐藏 */
    display: none;
    background-color: pink;
}

.two{
    background-color: green;
}
```

### 7.14 元素的整体透明度

*修改元素整体（包括内容）的透明度*

**语法**

* CSS属性`opacity`
* **Emmet** `op`
* 属性值 0-1
* 常和js配合使用

.html
```html
<body>
    <div>
        <img src="../study/images/course02.png" alt="">
        这个字透明吗
    </div>
</body>
```

.css
```css
div{
    width: 400px;
    height: 400px;
    background-color: green;

    opacity: 0.5;
}

img{
    vertical-align: bottom;
}
```

### 7.15 CSS使用精灵图

*项目中将多张小图片，合并成一张大图片(精灵图)*

*减少服务器发送次数，减轻服务器压力，提高页面加载速度*

**精灵图的使用步骤**

1. 创建盒子，盒子**尺寸和小图相同**
2. 将**精灵图**设置为盒子的**背景图**片
3. 修改背景图位置 <br> 通过pxcook测量**图片左上角距离精灵图左上角水平垂直长度**，分别**取负值**给盒子的`background-position ： x，y`

.html
```html
<body>
    <!-- 一般精灵图标签，用行内标签,后修改显示模式 -->
    <span class="phone"></span>
    <span class="animal"></span>
</body>
```

.css
```css
.phone{
    display: block;
    width: 18px;
    height: 24px;
    background-image: url(./资料—前端HTML5+CSS3/day09-小兔鲜项目/day09/01-案例/images/taobao.png);
    /* 背景图位置属性 */
    /* 水平方向位置 垂直方向位置 */
    /* 想左侧上侧移动图片，取负数 */
    background-position: -3px 0;
}

.animal{
    display: block;
    width: 24px;
    height: 21px;
    background-image: url(./资料—前端HTML5+CSS3/day09-小兔鲜项目/day09/01-案例/images/taobao.png);
    background-position: 0 -90px;
}
```

### 7.16 背景图缩放

*不改变盒子大小的情况下，设置背景图片的大小*

**语法**

* CSS属性`background-size`
* 属性值<br> `数字+px` `数字+px` 宽高 <br> `百分比` `百分比` 相对于**当前盒子自身**的宽高百分比 <br> `contain` 包含，将背景图**等比例缩放**，直到**不超过盒子的最大**  <br> `cover` 覆盖，将背景图**等比例缩放**，直到刚搞填满**整个盒子没有空白**

**background复合属性**

 * 完整写法`background: color image repeat position/size` 无顺序，可省略
 * 一般不用，复合前四个，bgs单独写

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    width: 400px;
    height: 300px;
    background-color: pink;
    background-image: url(./资料—前端HTML5+CSS3/day09-小兔鲜项目/day09/01-案例/images/1.jpg);
    background-repeat: no-repeat;
    background-size: 300px;
    background-size: 50%;
    /* 可能导致盒子有留白 */
    background-size: contain;
    /* 可能导数图片不全 */
    background-size: cover;
    /* 项目中图的比例和盒子的比例通常相同 contain和cover效果相同 */
}
```

### 7.17 盒子阴影

**语法**

* CSS复合属性属性`box-shadow`
* 属性值 <br> `h-shadow` 必须，水平偏移量，可负 `v-shadow` 必须，垂直偏移量，可负 `blur` 可选，模糊度 `spread` 可选，阴影扩大 `color` 可选,阴影颜色（常为黑色） `inset` 可选，将阴影改成内部阴影
* 属性值**按顺序书写**，空格隔开
* 除后两个属性值外，都为数字+px

*CSS书写顺序* 定位 浮动/显示模式 盒子模型 文字格式 装饰

**文字阴影** 

* `text-shadow: h-shadow必须 v-shadow必须 blur可选 color可选`

.html
```html
<body>
    <div class="box"></div>
</body>
```

.css
```css
.box{
    height: 200px;
    width: 200px;
    background-color: pink;
    /* 注意: 外阴影，不能添加outset,添加会报错 */
    box-shadow: 5px 10px 20px 10px green inset;
}
```

### 7.18 过渡

***逐渐**变化的效果*

*一般配合`hover`*

**语法**

* CSS复合属性`transition`
* **Emmet** `trs`
* 属性值  `过渡的属性` `过渡的时长+s`
* 过渡属性通常为`all`

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
    background-color: pink;
    /* 从宽度两百到宽度六百，花费1s时长 */
    /* 谁变化(变化前)，谁添加 */
    /* transition: width 1s, background-color 2s; */
    transition: all 1s;
}

.box:hover{
    background-color: blue;
    border-radius: 50%;
}
```

## *捌* 项目前置知识

---

### 8.1 网站和网页的关系

*网站包含多个网页*

*每个网页是一个独立的界面，包含在同一个网站中*

*多个同主题的网页组合在一起，成为一个网站*

### 8.2 骨架标签

* `<!DOCTYPE html>` 文档类型声明，告诉所有浏览器该网页的HTML版本以解析页面，这里的版本`html`是html5
* `<html lang="en">` 语言:英文 `zh-CN`简体中文 `en` 英文
* `<meta charset="UTF-8">` 规定网页的字符编码 `UTF-8` 万国码-容纳了被认证的所有国家的语言 **常用**`GBK2312` 6000+汉字 `GBK` 20000+汉字
* `<meta name="viewport" content="width=device-width, initial-scale=1.0">` 宽度和设备宽度相等-移动端网页需要

### 8.3 SEO三大标签

**什么是SEO**

搜索引擎优化(SEO),可以让网站在搜索引擎上排名靠前

**SEO方法**

* 竞价排名
* 将网页制作为`.html`后缀
* **标签语义化:在合适的地方使用合适的标签**

**SEO三大标签**

* `title` 网页标题双标签
* `description` 网页描述标签 <br> 实为`meta`单标签，`name`属性为`description`,内容写在`content属性` <br> **Emmet** meta:desc
* `keywords` 网页关键词标签 <br> 实为`meta`单标签，`name`属性为`keywords`,内容写在`content属性` <br> **Emmet** meta:kw

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- meta:desc -->
    <meta name="description" content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。">
    <!-- meta:kw -->
    <meta name="keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东">
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title> 
    <link rel="stylesheet" href="./try.css">   
</head>
<body>
    <div class="box"></div>
</body>
</html>
```

### 8.4 `favicon` 标题图标

*标题旁的小图*

*需要.ico格式的图标放在根目录(和html文件同级)*

**语法**

* `<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">`
* **Emmet** `link:favicon`
* .ico图标要命名`favicon.ico`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- meta:desc -->
    <meta name="description" content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。">
    <!-- meta:kw -->
    <meta name="keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东">
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title> 
    <link rel="stylesheet" href="./try.css">  
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon"> 
</head>
<body>
    <div class="box"></div>
</body>
</html>
```

## 小兔鲜项目

---

### 文件和目录准备

1. 创建项目文件夹 xxx-pc-client(根目录)
2. 准备favicon.ico到项目目录
3. 在根目录创建两个图片文件夹<br>images存放网站中固定使用的图片素材（logo,样式修饰图片等） <br>uploads存放网站中非固定使用的图片素材（商品，宣传图片等）
4. 在根目录新建index.html文件
5. 在根目录新建css文件夹，在其中创建<br>base.css基础公共样式<br>common.css 该网站中多个网页相同模块的重复样式，如头部、底部<br>index.css首页样式

### 代码准备

1. 按照base-common-网页的**顺序链接**好样式表(*层叠性*)
2. SEO三大标签以及连接好favicon
3. cv完成base.css

base.css
```css
/* 清除默认样式的代码 */
/* 去除常见标签默认的 margin 和 padding */
body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
ul,
ol,
li,
dl,
dt,
dd,
input {
  margin: 0;
  padding: 0;
}

/* 內减模式 */
* {
    box-sizing: border-box;
}

/* 设置网页统一的字体大小、行高、字体系列相关属性 */
body {
  font: 16px/1.5 "Helvetica Neue", Helvetica, Arial, "Microsoft Yahei",
    "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  color: #333;
}

/* 去除列表默认样式 */
ul,
ol {
  list-style: none;
}

/* 去除默认的倾斜效果 */
em,
i {
  font-style: normal;
}

/* 去除a标签默认下划线，并设置默认文字颜色 */
a {
  text-decoration: none;
  color: #333;
}

/* 设置img的垂直对齐方式为居中对齐，去除img默认下间隙 */
img {
  vertical-align: middle;
}

/* 去除input默认样式 */
input {
  border: none;
  outline: none;
  color: #333;
}

/* 左浮动 */
.fl {
  float: left;
}

/* 右浮动 */
.fr {
  float: right;
}

/* 双伪元素清除法 */
.clearfix::before,
.clearfix::after {
  content: "";
  display: table;
}
.clearfix::after {
  clear: both;
}
```

## *玖* 字体图标

---

*简单的小图案*

### 9.1 字体图片简介

*展示的是图，但本质是文字*

**作用**

* 处理简单的，颜色单一的图片

**优点**

*相比于**css精灵***

* 灵活性高 通过更改文字属性即可改变外观
* 体积小，轻量，渲染速度快
* 兼容性好
* 使用方便<br>1. 下载字体包<br>2. 使用字体包

### 9.2 字体图标的下载

**地点**

* <a href="http://www.iconfont.cn" title="阿里巴巴矢量字体图标库">www.iconfont.cn</a>

**方法**

1. 素材库的官方图表库(<strong style="color:red;">免费!</strong>)
2. 选购，<span style="color:orange;">添加至购物车</span>
3. 选购完成，点击购物车，<span style="color:orange;">添加至项目</span>
4. <span style="color:orange;">统一</span>下载到本地
5. 解压

### 9.3 字体图标的使用

**方法**

1.引入字体图标的样式表<span style="color:orange;">iconfont.css</span>
2.调用图标对应的类名，<span style="color:orange;">必须调用两个类名:iconfont icon-xxx</span>

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>字体图标基本使用-类名</title> 
    <!-- 1、引入样式表  2、调用类名-->
    <link rel="stylesheet" href="./try.css">  
    <link rel="stylesheet" href="./iconfont/iconfont.css">
</head>
<body>
    <!-- iconfont是固定 -->
    <span class="iconfont icon-dingwei"></span>
</body>
</html>
```

### 9.4 字体图标上传

*在iconfont上传.svg矢量图转换为字体图标*

**步骤**

1. 准备好.svg
2. 打开iconfont的上传界面
3. 添加（可多选），**去除颜色并提交**
4. 审核通过后我的图标库->批量操作->添加购物车->同下载图标后续操作

## *拾* 平面转换

---

### 10.1 平面转换简介

**作用**

* 改变盒子在平面内的布局（**位移（常用），旋转（不常用），缩放（常用）**）
* 2D转换

**平面**

* 水平 右+
* 垂直 下+

**语法**

* CSS属性`transform`
* **Emmet**`tf`

### 10.2 位移

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

### 10.3 绝对定位居中

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

### 10.4 平面旋转

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

### 10.5 转换原点

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

### 10.6 多重转换

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

### 10.7 缩放

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

### 10.8渐变

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

## *拾壹* 空间转换

---

*与平面转换类似，实现元素在空间内的位移、旋转、缩放等效果*

*三D转换*

**语法** 仍为`transform`

**z轴** 用户视线方向**相对，指向屏幕外**（*不符合数学意义上的右手定则*）

### 11.1 空间位移

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

### 11.2 透视属性

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

### 11.3 空间旋转

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

### 11.4 立体呈现

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

### 11.5 空间缩放

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

## *拾贰* 动画

---

#### 12.1 动画简介

**过渡的效果**

* 两个状态之间的变化过程

**动画的效果**

* 多个状态间的变化过程
* 动画中间过程可控(重复播放，最终画面，是否暂停)

**动画的本质**

* 大量相关联图片**连续播放**在脑中形成的画面
* 最小单元 **帧/动画帧**

### 12.2 动画 from to

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

### 12.3 动画 百分比

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

### 12.4 animation复合属性

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

### 12.5 am拆分写法（不常用）

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


### 12.6 逐帧动画

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

### 12.7 多组动画

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

## 拾叁 移动端开发

---

### 13.1 移动端和pc端开发差异

* 版心 **移动端无版心,pc端有版心**
* 网址 **移动端通常`m.jd.com`** 前缀加m

### 13.2 移动端的分辨率特点

* 电脑上的分辨率(**逻辑分辨率**)是缩放后(或经过软件修改)的出厂分辨率,比出厂分辨率(**物理分辨率**)低一些

*代码的参考分辨率应为**逻辑分辨率***

* 手机端的物理分辨率和逻辑分辨率不会更改，通常程**比例关系**,仍*按逻辑分辨率写代码*
* 设计稿通常以**iphone6/7/8**为基准:750x1334物理 375x667逻辑

### 13.3 视口

*如何保证移动端**网页宽度**和设备的**逻辑分辨率**相同*

**视口标签**

* 使得**网页宽度等于设备的逻辑分辨率**
* vscode生成的骨架标签中**自动包含**
* **语法**`<meta name="viewport" content="width=device-width, initial-scale=1.0">`
* *pc端网页宽度默认等于设备的逻辑分辨率*，故不需要视口标签
* 而移动端默认为*980*,故需要

### 13.4 二倍图

*为了防止在更大的屏幕上失真，设计图通常采用ipone6/7/8逻辑分辨率的二倍(即物理分辨率750x1334)设计*

*也有一些多倍图*

**使用**

* **在pxcook的开发模式中将设计图选到2x**

### 13.5 百分比布局

*流式布局*

*使得宽度自适应,高度固定*


## 十四 flex 布局

*轻松实现元素分布方式, 元素对齐方式, 元素视觉顺序...*

### 14.1 display: flex; 伸缩容器, 伸缩项目

* 给元素添加`display: flex;`或`display: inline-flex;`属性, 使其变为**伸缩容器**, 开启`flex`布局, 其下所有**子元素**(而非后代元素), 为**伸缩项目**, 有并排效果
* `display: inline-flex`做了两个动作, **把元素变为伸缩容器的同时, 给自身赋予了*行内块效果***, *一般不使用*
* 元素成为**伸缩项目**后, **块状化**, 可以正常添加宽, 高


```html
<!-- 元素添加 display 成为伸缩容器 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body{
      display: flex;
    }
    .outer{
      width: 600px;
      height: 600px;
      background-color: #888;
      display: flex; /*将该元素变为伸缩容器, 开启了flex布局*/
    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
    }
    .inner3{
      display: flex;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner">2</div>
    <div class="inner inner3">
      <div>a</div>
      <div>b</div>
      <div>c</div>
    </div>
  </div>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner">2</div>
    <div class="inner inner3">
      <div>a</div>
      <div>b</div>
      <div>c</div>
    </div>
  </div>
</body>
</html>
```

### 14.2 flex-direction 主侧轴方向

* 设置于伸缩容器
* 主轴方向**默认**为从左到右
* 侧轴方向**默认**为从上到下
* 修改主轴`flex-direction` *一般不改*
  * `row` 默认值 主轴从左到右, 侧轴从上到下
  * `row-reverse` 主轴从右到左, 侧轴从上到下
  * `column` 主轴从上到下, 侧轴从左到右
  * `column-reverse` 主轴从下到上, 侧轴从左到右

```css
/* 修改主轴方向 */
.outer{
  width: 1000px;
  height: 600px;
  background-color: #888;
  margin: 0 auto;
  /* 伸缩盒模型相关属性 */
  display: flex; 
  /* 调整主轴方向 从左到右, 默认*/
  flex-direction: row;

  /* 调整主轴方向 从右到左 */
  flex-direction: row-reverse;

  /* 调整主轴方向 从上到下 */
  flex-direction: column;

  /* 调整主轴方向从下到上 */
  flex-direction: column-reverse;
}
```

### 14.3 flex-wrap: wrap; 主轴换行方式

* 设置于伸缩容器
* **主轴**默认不换行, 伸缩项目的总宽度超过伸缩容器后, 会压缩各个**伸缩项目**
* 换行要设置`flex-wrap`属性,
  * `nowrap` 默认值, 一行排列
  * `wrap` 换行
  * `wrap-reverse` *相当于反转了侧轴方向* **不常用**
* 换行后在**侧轴**方向另起新行, 当伸缩项目的总高度小于伸缩容器, 会**产生等大间隔**, 但是如果伸缩项目的总高度大于伸缩容器, 不会压缩**伸缩项目**, 会于**伸缩容器外侧显示**

```html
<!-- 主轴换行, 侧轴上产生等间距 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .outer{
      width: 1000px;
      height: 600px;
      background-color: #888;
      margin: 0 auto;
      /* 伸缩盒模型相关属性 */
      display: flex; 
      /* 主轴换行方式 */
      flex-wrap: wrap;
    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner">2</div>
    <div class="inner">3</div>
    <div class="inner">4</div>
    <div class="inner">5</div>
    <div class="inner">6</div>
    <div class="inner">7</div>
    <div class="inner">8</div>
    <div class="inner">9</div>
  </div>
</body>
</html>
```

### 14.4 flex-flow 复合属性 同时指定主轴方向和换行方式

*不常用* `flex-flow: column wrap;`无顺序


### 14.5 justify-content 主轴对齐方式

* 设置于伸缩容器
* **伸缩项目**默认排在主轴的左侧
* `justify-content`
  * `flex-start` 默认值, 左侧对齐
  * `flex-end` 右侧对齐
  * `center` 居中对齐
  * `space-around` 每个**伸缩项目**的左右都产生等距大小的间隙
  * `space-between` 每个**伸缩项目**的左右都产生等距大小的间隙, **除了和伸缩容器的边缘没有距离!** **多用**
  * `space-evenly` **无论边缘或是项目之间, 距离相同**
* **注意不改变主轴方向, 元素依然按照主轴方向排列**

```html
<!-- space-between方式 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .outer{
      width: 1000px;
      height: 600px;
      background-color: #888;
      margin: 0 auto;
      /* 伸缩盒模型相关属性 */
      display: flex; 

      justify-content: space-between;
      flex-wrap: wrap;
      
    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner">2</div>
    <div class="inner">3</div>
    <div class="inner">4</div>
    <div class="inner">5</div>
    <div class="inner">6</div>
    <div class="inner">7</div>
    <div class="inner">8</div>
    <div class="inner">9</div>
  </div>
</body>
</html>
```

### 14.6 侧轴对齐

#### 14.6.1 align-items 单行侧轴对齐

* 设置于伸缩容器
* 不改变侧轴方向
* `flex-start`侧轴起始位置对齐
* `flex-end` 侧轴终止位置对齐
* `center` 侧轴中间位置对齐
* `baseline` 内部文字基线对齐 *一般不用*
* `stretch` **默认值** **伸缩项目*不给高度情况*下默认为父元素高度**

```html
<!-- align-items 控制侧轴对齐, 仅限于伸缩项目一行排列 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .outer{
      width: 1000px;
      height: 600px;
      background-color: #888;
      margin: 0 auto;
      /* 伸缩盒模型相关属性 */
      display: flex; 

      align-items: flex-start;
    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
    }
    .inner2 {
      height: 300px;
    }
    .inner3{
      height: 100px;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner inner2">2</div>
    <div class="inner inner3">3</div>

  </div>
</body>
</html>
```

#### 14.6.2 align-content 多行侧轴对齐

* 设置于伸缩容器
* `flex-start` 侧轴起始位置对齐 *消除了各**行间**间隔* *注意对于每一行, 此行的**宽度**为该行项目高度最大值, 对于一行中彼此高度不一的情况, 仍有间隔*
* `flex-end` 侧轴结束位置对齐
* `center` 侧轴中间位置对齐
* `space-around` 每个**行**的上下都产生等距大小的间隙
* `space-between` 每个**行**的上下都产生等距大小的间隙, **除了和伸缩容器的边缘没有距离!**
* `space-evenly` **无论边缘或是行之间, 距离相同**
* `stretch` **默认值** **在不设项目高度情况下, 项目高度相同, 每行平分容器高度**

```html
<!-- 多行侧轴对齐 space-between  -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .outer{
      width: 1000px;
      height: 900px;
      background-color: #888;
      margin: 0 auto;
      /* 伸缩盒模型相关属性 */
      display: flex; 

      flex-wrap: wrap;

      align-content: space-between;
    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
    }
    .inner2 {
      height: 300px;
    }
    .inner3{
      height: 100px;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner inner2">2</div>
    <div class="inner inner3">3</div>
    <div class="inner">4</div>
    <div class="inner">5</div>
    <div class="inner">6</div>
    <div class="inner">7</div>
    <div class="inner">8</div>
    <div class="inner">9</div>
    <div class="inner">10</div>
    <div class="inner">11</div>


  </div>
</body>
</html>
```

### 14.7 margin: auto; 单一元素水平垂直居中

1. 父元素 `display: flex;`
2. 子元素 `margin: auto;`

### 14.8 flex-basis 基准长度

*很少设置*

* 设置于伸缩项目
* 可**顶替**主轴方向上**伸缩项目的尺寸** *即便是`width`或`height`写在后*
* 默认值`auto` 默认找`width`或`height`, 给浏览器使用

### 14.9 伸缩性

#### 14.9.1 flex-grow 主轴拉伸

* 写在伸缩项目
* 对于**未填充完的行**进行拉伸
* 属性值是**一个数字**, 表示拉伸权值, **按照所有项目的拉伸权值来瓜分剩余的空间**

```html
<!-- flex-grow 主轴拉伸 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .outer{
      width: 1000px;
      height: 900px;
      background-color: #888;
      margin: 0 auto;
      /* 伸缩盒模型相关属性 */
      display: flex; 

      flex-wrap: wrap;

    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
      flex-grow: 1;
    }

    .inner2{
      width: 300px;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner inner2">2</div>
    <div class="inner">3</div>
    <div class="inner">3</div>
    <div class="inner">3</div>
    <div class="inner">3</div>
  </div>
</body>
</html>
```

#### 14.9.2 flex-shrink 主轴压缩

*一般不用*

* 设置于压缩项目
* 默认值为1
* 需满足可压缩条件才会生效 *不设置wrap*
* **按照所有项目的压缩权值来压缩*自身的比例*以凑齐容器的缺口**

```html
<!-- flex-shrink 主轴压缩 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .outer{
      width: 400px;
      height: 900px;
      background-color: #888;
      margin: 0 auto;
      /* 伸缩盒模型相关属性 */
      display: flex; 

      /* flex-wrap: wrap; */
      align-content: flex-start;
    }
    .inner{
      width: 200px;
      height: 200px;
      background-color: skyblue;
      border: 1px solid #000;
      box-sizing: border-box;
      flex-grow: 1;
      flex-shrink: 1;
    }

    .inner2{
      width: 300px;
    }
  </style>
</head>
<body>
  <div class="outer">
    <div class="inner">1</div>
    <div class="inner inner2">2</div>
    <div class="inner">3</div>
  </div>
</body>
</html>
```

### 14.10 flex复合属性 拉伸 压缩 基准长度

* 常用`flex: 1 1 0;` 可以拉伸可以压缩, 不设置基准长度

### 14.11 order 排序

* 设置于伸缩项目
* 默认值0
* 按照属性值从小到大把项目放到容器，可以为负

### 14.12 align-self 单个项目侧轴对齐

*不常用*

* 属性值同 `algin-items`, 不改变主轴排列位置
* 默认值`auto` **跟随父元素**