# 迭代_高阶函数_作用域_函数组合_lambda表达式
 
* [迭代](#迭代)
* [控制语句](#控制语句)
  * [逻辑运算的短路行为](#逻辑运算的短路行为)
* [高阶函数](#高阶函数)
  * [断言](#断言)
* [泛化](#泛化)
  * [返回函数的函数_闭包](#返回函数的函数_闭包)
  * [函数传递时的环境相关_作为参数_作为返回值](#函数传递时的环境相关_作为参数_作为返回值)
    * [函数作为参数](#函数作为参数)
    * [函数作为返回值](#函数作为返回值)
    * [手画环境示意图的小tip](#手画环境示意图的小tip)
* [局部名称的作用域](#局部名称的作用域)
* [函数组合_](#函数组合_)
* [Lambda表达式](#Lambda表达式)
* [函数柯里化](#函数柯里化)
  * [为什么使用柯里化](#为什么使用柯里化)

## 迭代

*计算斐波那契数列*

![](img/e042449c.png)

## 控制语句

这个函数可行吗

```py
def if_(c, t, f):
    """当条件 C 为真时，返回 T，否则返回 F"""
    if c:
        return t
    else:
        return f
```

和`if`语句不同，在调用函数前，首先会评估其内所有参数，从而无论条件真假，t和f都会被评估一遍，当在如下所示的函数中调用就会出错

```py
def real_sqrt(x):
    """当 X 大于 0 时返回 sqrt(x)，否则返回 0"""
    return if_(x > 0, sqrt(x), 0)
```

### 逻辑运算的短路行为

`<left> and <right>`

* 如果通过`left`可以得知结果（对于`and`来说，即为假），那么就不会再评估`right`，而是直接返回结果

`or`也相似

![](img/ea04bf78.png)

## 高阶函数

### 断言

`assert 布尔值, '错误信息'`

当布尔值为`False`时，会抛出`'错误信息'`

![](img/81fb4844.png)

## 泛化

*一种推荐的思想*

提取多个相似函数中相同的部分为一个原始函数，并将相异的部分（可以是某个系数，甚至是某个函数），作为参数传递入原始函数，达到差异化的目的

![](img/f4b443cb.png)

### 返回函数的函数_闭包

```py
"""返回函数的函数"""

def make_adder(n):
    """返回一个函数，返回函数接受参数 K，返回 K + N
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
```

* 函数可以传递为参数，也可以被返回

### 函数传递时的环境相关_作为参数_作为返回值

#### 函数作为参数

```py
def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x
```

```py
>>> square(10)
100
>>> apply_twice(square, 3)
81
>>> square
<function square at 0x7b5ba9124b80>
>>> 3
3
```

![](img/b57f4e67.png)

当调用`apply_twice(square, 3)`时

* 首先创建新的帧，然后将传入`square指向的函数`和`3`绑定到形参`f`, `x`
* 如此 f 同样指向 函数`func square(x)`
* 接着执行 `return f(f(x))`，在当前环境中查找`f`的指向，即`func square(x)`
* ...

#### 函数作为返回值

```py
def make_adder(n):
    def adder(k):
        return k + n
    return adder
```

```py
>>> add_three = make_adder(3)
>>> add_three(4)
7
>>> add_three(5)
8
```

![](img/cf08bbdf.png)

* 当`make_adder`被调用时，其定义一个函数，这个函数的父栈帧即为`func make_adder`被调用时所创建帧 *因为在哪里创建其父帧就是谁*
* 而当`make_adder`返回后，调用这个返回的函数时，这个**函数内部仍然可以在当初创建他的`make_adder`的环境中寻找变量** *因为环境为其沿父帧链依次寻找直到全局帧*

#### 手画环境示意图的小tip

1. 当函数被定义时，总是创建这样一个函数`func <name>(<formal parameters>) [parant=<parant>]`
    * 其父帧为定义时所在的当前帧
2. 同时为当前帧创建一个同名名称绑定到这个函数
3. 当函数调用时，创建一个新帧，以被调用函数的名称作为标题
4. 在新帧中创建形参名称并绑定到实参
5. 在新帧作为起始的环境中执行函数体

## 局部名称的作用域

```py
>>> def f(x, y):
...     return g(x)
... 
>>> def g(a):
...     return a + y
... 
>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
  File "<stdin>", line 2, in g
NameError: name 'y' is not defined
```

* 当调用`f(1, 2)`时
* 创建帧，其父帧为全局
* 新帧名称 x y 绑定到实参
* 执行函数体 `return g(x)`，寻找名称`g`
* 在父帧全局帧中找到，创建帧，传递形参
* 在`g`调用所在帧中执行 `return a + y`
* 寻找`y`，但是当前帧的父帧为全局帧，环境中并没有`y`

## 函数组合_

```py
def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def triple(x):
    return 3 * x

def composel(f, g):
    def h(x):
        return f(g(x))
    return h
```

```py
>>> square(5)
25
>>> triple(5)
15
>>> squiple = composel(square, triple)
>>> squiple(5)
225
>>> tripare = composel(triple, square)
>>> tripare(5)
75
>>> squadder = composel(square, make_adder(2))
>>> squadder(5)
49
```

## Lambda表达式

我们希望有一种方式使得名称可以通过赋值的方法绑定一个从未写过的函数 `square = ...`

```py
# :_前为形参
# :_后为返回值
square = lambda x: x * x
```

```py
>>> square = lambda x: x * x
>>> square
>>> square(4)
16
>>> square(10)
100
```

我们也可以直接将其作为匿名函数直接调用

```py
>>> (lambda x: x * x)(3)
9
```

其返回值必须是一个单个的表达式

并且其没有语句

![](img/f9e71df9.png)

区别在于`def`自动给了一个同名名称，并且生成一个内在名称，而`lambda`需要手动赋值，并且函数自身是匿名的

![](img/10df0106.png)

## 函数柯里化

![](img/d41776c3.png)

![](img/fc9b7d28.png)

将多参数函数转换为一个单参数高阶函数的一般途径

### 为什么使用柯里化

*wav文件的原理*

![](img/da25b821.png)

对于声波采样，存储，但不压缩，因此空间占用相对大

可以用真实声音采样，同样可以使用数学函数生成声音

![](img/f317c88e.png)

![](img/90b8ef12.png)

这是一个生成三角波声音的python代码
