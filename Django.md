# Django

https://docs.djangoproject.com/zh-hans/5.0/

## Django项目

### 创建项目

#### 方式一：终端创建

进入将要创建项目目录的父目录，打开终端
>django-admin startproject [项目名称]

#### 方式二：Pycharm创建

1. 创建新项目, **选择Django**
2. 选择项目位置
3. **选择`Custom environment`而非虚拟环境**
4. 选择对应的python路径

### 运行项目

#### 方式一：终端运行

在项目目录下打开终端
> python manage.py renserver

#### 方式二：Pycharm运行

直接右上绿色箭头运行

### 项目目录

* `manage.py`在终端和项目交互使用，`python manage [子命令]`，`python manage help`查看帮助，不应更改
* `settings.py`项目相关的配置项
* `urls.py`存放项目相关的url路由
* `asgi.py`, `wsgi.py`部署时使用，不应更改

### Django中的app

* 一个项目由多个`app`**模块**组成，一个`app`可以用到多个项目
* 可以相应`url`请求，负责完成不同的功能
* 通过`python manage.py startapp [app名字]`创建

## 壹 路由

* 服务器接受到不同的`path`的请求调用不同的函数来处理

### 1.1 urlpatterns列表 path映射到视图函数

* 配置`urls.py`下的urlpatterns列表
* 每一项为`path(路径名, 视图函数)`的形式
* 视图函数的形参为`res`也就是发送的请求
* 视图函数的返回值及为响应给浏览器的内容，用`HttpResponse`函数修饰，在此之前导入`from django.shortcuts import HttpResponse`
* 视图函数一般写在对应`app`的`views.py`，`urlpatterns`使用时`from app包名 import view`

### 1.2 Django中接收query params参数并响应

#### 1.2.1 request.GET.get 接收query参数

* `request.GET`类似一个字典`{id: 3..}`，使用`request.GET.get('id')`访问字典的元素
* 在`path`函数的路径名不包括`query`参数

#### 1.2.2 <book_id> 接收params参数

* 在`path`函数的路径中后用`<参数名>`表示动态参数
* 在视图函数的形参中使用参数名接收到动态参数 `(res, book_id)`
* 可以在占位`<参数名>`的参数名前指定类型`<类型:参数名>`，使得在视图函数中接收到的参数为对应类型，否则为字符串
  * `int` 
  * `str`*默认值*不包含/的字符串
  * `slug`由字母数字下划线中划线组成的字符串
  * `uuid`uuid字符串
  * `path`字母和/组成的字符串

*book/views.py*
```py
from django.shortcuts import HttpResponse
# Create your views here.
# 获取传来的query参数 xxx.xx/xx?id=3
def book_detail_query_string(request):
    # request.GET = {"id": 3, "name": ’三国演义‘}
    return HttpResponse(f'你要找的图书id是{request.GET.get('id')}')

def book_detail_params(req, book_id):
    return HttpResponse(f'你要找的图书id是{book_id}')
```

*urls.py*
```py
from book import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book', views.book_detail_query_string),
    path('book/<int:book_id>', views.book_detail_params)
]
```

### 1.3 path函数

* `path(route, view, name=None, kwargs=None)`
* `route` url匹配规则，当请求url符合`route`时调用后续的视图函数。
* `view` 可以是一个视图函数或者是`类视图.view()`或者是`django.urls.include()`
* `name` 给这个url起名字，会在url反转时用到 传入时要写`name=".."`

### 1.4 include 路由模块化

* 当项目中有大量app时，在项目的urls.py中全部引入views会导致使用混乱，因此在各项目自身中建立`urls.py`配置所属功能下的路由，再在项目的urls.py中引入即可
* app中的`urls.py`中，首先导入`import django.urls import path`，再引入自身的`from . import views`，配置`urlpatterns`列表即可
* 在总项目的urls.py中导入`import django.urls import include`，在`urlpatterns`中导入对应app的urls:`path(父路径, include('app名/urls'))`
* 注意此时处理的请求路径是`父路径/app中的对应url`
* 在app的`urls.py`中加上`app_name = app名`表示命名空间，否则配置的urls名字会和其它app的冲突

*movie/urls.py*
```py
from django.urls import path

from . import views

# 指定应用名称 命名空间

app_name = 'movie'

urlpatterns = [
    path('list', views.movie_list, name='movie_list'),
    path('detail/<int:movie_id>', views.movie_detail, name='movie_detail')
]
```

### 1.5 reverse url反转 通过路由名称获取到路由

* `from django.urls import reverse`
* 对于匹配携带query的路由和不携带参数的路由`reverse(路由名称)` 返回的路径不包含`query`参数
* 对于匹配携带params的路由`reverse(路由名称, kwargs={"参数名称": 值})` 返回的路径包含`params`参数
* 对于模块化，定义在app中的路由，**路由名称前加上`命名空间:`**

## 贰 DTL模版

* 使服务器响应返回HTML
* DTL是一种有特殊语法的HTML文件，可以传递参数实现数据动态化，可以被Django编译成普通的HTML返回浏览器

### 2.1 响应返回HTML

* HTML文件写在项目根目录下的`templates`目录下

#### 方式一 render_to_string 配合 HttpResponse

* `html = render_to_string("...html")`将模板编译后转为HttpResponse可以接收的python字符串
* `return HttpResponse(html)`返回响应

#### 方式二 render

* `return render(req, "...html")`模版编译后转换为响应类型直接返回

### 2.2 settings.py中模版相关配置项

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', #模版引擎
        'DIRS': [BASE_DIR / 'templates'], #模版查询路径
        'APP_DIRS': True, #模版可存放在app目录下的templates文件夹下 如果要使用，需要在 INSTALLED_APPS 添加APP名
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2.3 {{}} context DTL中使用插值语法传递变量

* 在`views.py`中使用`render()`解析模版时, 使用`context={使用名称:变量...}`向模版传入参数
* 在模版中, 无论要使用的是`普通变量`, `列表中的一项`, `对象中的一个属性`, `字典的一个值`均使用`.`的方式获取

*views.py*
```py
def info(req):
    # 普通变量
    username = "张三"
    # 字典类型
    book = {'name': '水浒传', 'author': '施耐庵'}
    # 列表类型
    books = [
        {'name': '水浒传', 'author': '施耐庵'},
        {'name': '三国演义', 'author': '罗贯中'}
    ]
    # 对象类型
    class Person:
        def __init__(self, realname):
            self.realname = realname

    context = {
        'username': username,
        'book': book,
        'books': books,
        'person': Person('李四')
    }

    return render(req, "info.html", context=context)
```

*info.html*
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>{{username}}</p>
    <p>图书名称：{{book.name}}</p>
    <p>下标为1的图书名称为：{{books.1.name}}</p>
    <p>真实姓名为：{{person.realname}}</p>
</body>
</html>
```

### 2.4 django常用内置模版标签

https://docs.djangoproject.com/zh-hans/5.0/ref/templates/builtins/

* 使用 

```django
{% .. %}
```

  包裹

* 有起始就要有结束 
```django
{%..end%}
```

#### 2.4.1 if 标签 选择结构 

* 与python中的if对应, 有`elif`, `else`

```django
{% if age > 18 %}
    <p>你的年龄为：{{ age }}，允许进入</p>
{% elif age == 18 %}
    <p>您刚满18岁，还需要观察一下</p>
{% else %}
    <p>您的年龄为：{{ age }}，禁止进入</p>
{% endif %}
```

#### 2.4.2 for 标签 遍历目标 

* 与py中的for对应，也可以遍历列表，元组，字符串，字典等一切可以遍历的对象
* 反向遍历`{% for .... reversed %}`
* 每次循环中可以使用 `forloop.counter`获取当前循环次数，从 1 开始 `forloop.counter0` 从 0 开始
* 不存在`continue`, `break`
* `endfor`前使用`{% empty %}`在for遍历的目标为空时执行内部

```django
<table>
    <thead>
        <tr>
            <th>图书名称</th>
            <th>作者</th>
        </tr>
    </thead>
    <tbody>
        {% for book in books %}
            <tr>
                <td>{{ book.name }}</td>
                <td>{{ book.author }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```

#### 2.4.3 with标签 简化复杂变量的使用

* 在模版中定义变量，存储复杂变量，方便使用
* 注意`with`定义变量时, 赋值`=`左右不能有空格

```django
{% with book1name=books.1.name %}
    <p>作者的名字为：{{ book1name }}</p>
{% endwith %}
```

#### 2.4.4 url标签 反转url

* 常用在a标签的href，把路由名称映射到对应路由
* 不需要end..
* 同样受到url模块化命名空间的约束，要加`命名空间:`
* `<a href="{% url 'info' %}">跳转到info</a>`
* 传递`params`参数`<a href="{% url 'info' 1 %}">跳转到info</a>`/`<a href="{% url 'info' book_id=1 %}">跳转到info</a>`
* 传递`query`参数要手动拼接 `<a href="{% url .. %}?id=1">..`

#### 2.4.5 include标签 组件化

* 可额外在`templates`文件夹下新建`html`包含组件，内容仅含需要的结果
* 在引入组件的`html`中，使用`{% include '组件.html' %}`会在templates文件夹下寻找
* 组件的`html`中, 可以使用其父`html`的上下文，即也可以使用父中的变量, 引入其他变量可用`with`

*组件中*
```html
<div>
    <h2>热门文章</h2>
    <ul>
        <li>文章1</li>
        <li>文章2</li>
    </ul>
</div>
```

*父html*
```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
    {% include 'my_hotarcticle.html' %}
</body>
</html>
```

#### 2.4.6 block extand标签 继承化

* 在`templates`目录新建父模版
* 父模版的作用是供子模版继承使用，子模版可以包含父模版的所有内容，同时可以按父模版的规定有所差异
* 在父模版中使用`{% block 自定义名字 %}可以传给子的内容{% endblock %}`规定子html可以差异的内容, 包括标题，引入js，html结构均可差异化
* 子模版**在第一行**使用`{% extends 'my_base.html' %}`继承父模版
* 子模版使用`{% block 名字 %}内容{% endblock %}`进行个性化,在其中可以使用`block.super`获取父传给子的内容

*父模版*
```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    {% block head %}{% endblock %}
</head>
<body>
    <header>
        <ul>
            <li><a href="/">首页</a>
            <li><a href="/course">创业课堂</a></li>
        </ul>
    </header>
    {% block body %}{% endblock %}
    <footer>
        备案...
    </footer>
</body>
</html>
```

*子模版*
```django
{% extends 'my_base.html' %}

{% block body %}
	{% include 'my_hotarcticle.html' %}
    <div>你好</div>
{% endblock %}

{% block title %}
	主页
{% endblock %}

{% block head %}
    <style>
        body{
            background-color: pink;
        }
    </style>
{% endblock %}
```

### 2.5 常用过滤器

https://docs.djangoproject.com/zh-hans/5.0/ref/templates/builtins/

* 模版中对传来的数据进行处理后使用
* `变量名|过滤器名:操作`
* 注意不要有空格

#### 2.5.1 add 加法/拼接

* `数字|add:'值'/值`
* `字符串|add:'字符串'`

#### 2.5.2 cut 移除数据中所有指定字符串

* `字符串|cut:"要删除的字符串"`

#### 2.5.3 date 配合python datetime格式化日期

* `from datetime import datetime`.. datetime.now()
* 将`datetime`对象按照指定格式字符串转化
* `datetime对象|date:'格式字符串'`
* 格式字符串如下

https://docs.djangoproject.com/zh-hans/5.0/ref/templates/builtins/#date

#### 2.5.4 default 空值的默认值

* 如果值转换为bool为false, 则使用default后的值
* `value|default:'这个家伙很懒，什么都没有写'`

#### 2.5.5 default_if_none none的默认值

* 如果值为none，则用default后的值

#### 2.5.6 first/last 列表/元组/字符串的首尾

* `value|first/last`

#### 2.5.7 floatformat 格式化浮点类型

* `value|floatformat:3`保留3位小数

#### 2.5.8 join 将列表/元组/字符串用指定字符拼接

* `value|join:'/'`

#### 2.5.9 length 获取一个列表/元组/字符串/字典的长度

* `value|length`

#### 2.5.10 lower/upper 将字符串全部转为小写/大写

* `value|lower/upper`

#### 2.5.11 random 在给定的列表/字符串/元组中随机选择一个值

* `value|random`

#### 2.5.12 safe 解除对传来字符串的转义 允许渲染html标签

* `value|safe`

#### 2.5.13 slice 用于列表/字符串切片

* `value|slice:'2:'`

#### 2.5.14 stringtags 删除字符串中的html结构 保留字符串输出

* `<h1>hello</h1>` => `hello`
* `value|stringtags`

#### 2.5.15 truncatechars 字符串超过限制长度，切割并添加...

* `value|truncatechars:5`

#### 2.5.16 truncatechars_html 不切割字符串包含的html标签，而是内容

* `value|truncatechars_html:5`

### 2.6 static加载静态文件

*待补充*

