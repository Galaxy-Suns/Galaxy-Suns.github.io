# QSS

### 基本语法

#### 选择器部分

>选择器{声明}

选择器：一般为Q控件类名

```c++
btn->setStyleSheet("QPushButton{color:red}");
```

可以对多个选择器使用同一语句

```c++
btn->setStyleSheet("QLineEdit,QPushButton{color:red}");
```

选择器后可以::子控件

```c++
ui->spinBox->setStyleSheet("QSpinBox::up-arrow{image:url(:/image/7.ico)}");
```

选择器后:伪状态

```c++
btn->setStyleSheet("QPushButton:hover{color:green;background-color:green}");
```
通过#找到部分控件

```c++
this->setStyleSheet("QTextEdit#lbsize{..}");
```

这种权重较高

#### 声明部分

*选择器部分区分大小写，声明部分不区分大小写*

>属性名:属性值

##### 自定义颜色


>rgb(r,g,b)
>rgba(r,g,b,a) //透明度

可以利用qq截图时复制到想要颜色

```c++
ui->btn->setStyleSheet("QPushButton{background-color:rgb(255,128,26)}")
```

##### 添加图片

>background-image:url(路径)

但是大小无法调整，可以提前设置成和窗口一样大小的图片

```c++
this->setStyleSheet("QWidget:hover{background-image:url(:/image/33.jpg)}")
```

###### 防止图片重复

和`background-image`配合使用

>background-repeat

```c++
this->setStyleSheet("QWidget:hover{background-image:url(:/image/33.jpg)};background-repeat:repeat-x(y)")
```
只允许在x(y)上重复

跟`no-repeat`不允许重复

###### 图片初始位置

>background-position

```c++
this->setStyleSheet("QWidget:hover{background-image:url(:/image/33.jpg)};
background-repeat:repeat-x(y);backgroung-position:right(top bottom left) center(top bottom)") //右侧居中
```

###### 图片滚动设置

有滚动条时才用到

>background-attachment:(fixed scroll)

fixed不滚动

scroll滚动

###### 简写

>background:color image repeat position

要按顺序 可省部分
空格隔开






