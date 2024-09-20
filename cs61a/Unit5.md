# 装饰器 函数内部访问自身

## 装饰器

```py
def trace1(fn):
    """返回 fn 的另一个版本，在其调用开始阶段先打印一些东西

    fn - 带有一个参数的函数
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x
@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
```

```py
>>> square(12)
Calling <function square at 0x79c931040c20> on argument 12
144
>>> sum_squares_up_to(5)
Calling <function sum_squares_up_to at 0x7ec9014ccd60> on argument 5
Calling <function square at 0x7ec9014ccc20> on argument 1
Calling <function square at 0x7ec9014ccc20> on argument 2
Calling <function square at 0x7ec9014ccc20> on argument 3
Calling <function square at 0x7ec9014ccc20> on argument 4
Calling <function square at 0x7ec9014ccc20> on argument 5
55
```

在`def square`上修饰`@trace1`等同于在函数定义后重新赋值`square = trace1(square)`

将一个函数转化为另一个函数

![](img/fdb0fb8c.png)

## 函数中访问自身

### 直接或间接返回自身

在函数中如果不把自身的名称绑定到其他值，那么可以通过名称在其父帧中获取到自身

```py
def print_all(x):
    print(x)
    return print_all
```

```py
>>> print_all(1)(2)(3)(6)
1
2
3
6
<function print_all at 0x75e38d7da2a0>
```

下面这个例子会依次从左至右加和并输出

![](img/c5b16b8b.png)

```py
1
4
9
```

通过一个返回一个调用自身的子函数，完成了状态的保存

### 函数的递归

递归意味着在函数内部直接或**间接**调用自身

递归函数通常是以检查**最基本情况(回归条件)** 开始

之后就是更复杂的一般情况，在我们的例子里就是n不为0的情况，或者更标准的写法下，是n为一位数的情况，返回n

```py
def split(n):
    """把 n 分割成个位和剩余两部分"""
    return n // 10, n % 10

def sum(x):
    """对x的所有位求和"""
    if x == 0:
        return 0
    all_but_last, last = split(x)
    return last + sum(all_but_last)
```

```py
>>> sum(12)
3
```

### 递归的环境图

![](img/fd490f52.png)

这是一个使用递归计算阶乘的函数


