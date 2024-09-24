# 链表

## 链表定义

链表对象有两个属性

* `first`是某个表示数据的对象
* `rest` 是另一个链表对象

最终的`rest`存储一个空链表

![](img/b0c461f0.png)

构造的方式如下

![](img/f06f7912.png)

![](img/37710134.png)

`isInstance`不仅能检查`rest`是否为`Link`的实例，而且如果`rest`是`Link`的子类的实例，也会返回`True`

```py
class Link:
    empty = ()
    def __init__(self, data, link=empty):
        assert link is Link.empty or isinstance(rest, Link)
        self.first = data
        self.rest = link
```

```py
>>> Link(3, Link(4, Link(5)))
<__main__.Link object at 0x77a6f8905f70>
>>> s = Link(3, Link(4, Link(5)))                                                                                
>>> s.first
3
>>> s.rest
<__main__.Link object at 0x77a6f8981460>
>>> s.rest.first
4
>>> s.rest.rest.first
5
>>> s.rest.rest.rest is Link.empty
True
```

## 链表操作
