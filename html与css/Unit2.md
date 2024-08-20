# *贰*_HTML基础
 
* [2.1_列表标签使用场景](#2.1_列表标签使用场景)
* [2.2_无序列表](#2.2_无序列表)
* [2.3_有序列表](#2.3_有序列表)
* [2.4_自定义列表](#2.4_自定义列表)
* [2.5_表格的使用](#2.5_表格的使用)
* [2.6_表格标题和表头单元格标签](#2.6_表格标题和表头单元格标签)
* [2.7_表格的结构标签](#2.7_表格的结构标签)
* [2.8_合并单元格](#2.8_合并单元格)
* [2.9_表单标签_input系列标签](#2.9_表单标签_input系列标签)
* [2.10_text_password_占位符(提示信息)](#2.10_text_password_占位符(提示信息))
* [2.11_表单_radio_checkbox_单选功能和默认选中](#2.11_表单_radio_checkbox_单选功能和默认选中)
* [2.12_file_上传多个文件](#2.12_file_上传多个文件)
* [2.13_input按钮](#2.13_input按钮)
* [2.14_表单_button_按钮标签](#2.14_表单_button_按钮标签)
* [2.15_表单_select下拉菜单](#2.15_表单_select下拉菜单)
* [2.16_表单_textarea文本域标签](#2.16_表单_textarea文本域标签)
* [2.17_表单_label标签](#2.17_表单_label标签)
* [2.18_语义化标签](#2.18_语义化标签)
* [2.19_字符实体](#2.19_字符实体)

---

## 2.1_列表标签使用场景

*整齐排列的内容*

* 无序列表
* 有序列表
* 自定义列表

## 2.2_无序列表

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

## 2.3_有序列表

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

## 2.4_自定义列表

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

## 2.5_表格的使用

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

## 2.6_表格标题和表头单元格标签

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

## 2.7_表格的结构标签

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

## 2.8_合并单元格

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

## 2.9_表单标签_input系列标签

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

## 2.10_text_password_占位符(提示信息)

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

## 2.11_表单_radio_checkbox_单选功能和默认选中

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

## 2.12_file_上传多个文件

**语法**

* multiple属性 (mu)

```html
<input type="file" multiple>
```

## 2.13_input按钮

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

## 2.14_表单_button_按钮标签

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

## 2.15_表单_select下拉菜单

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

## 2.16_表单_textarea文本域标签

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

## 2.17_表单_label标签

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

## 2.18_语义化标签

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

## 2.19_字符实体

*网页对多个空格会合并为一个空格*

*实现网页中多个空格的效果*

**语法**  `&nbsp;`

```html
这是HTML文档&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;现在要学习字符实体。
```

