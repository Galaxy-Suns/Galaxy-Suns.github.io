# Java

*本文档着重于Java与C++语法不同方向*

*对于和C++完全相同的语法加以省略*

**特点 跨平台性**

**Java的介绍**

* 混合型语言 *区别于C的编译型，Python的解释型*
* 首先整体**编译为.class**
* 后按行在**虚拟机解释运行** *而非在操作系统运行*
* 通过虚拟机实现**跨平台**

**JVM** java运行的虚拟机

**JRE JDK**

* *JDK* JVM 核心类库 开发工具 组成的成体 *JDK工具包*
* *JRE* JVM 核心类库 运行工具 组成的整体 *JRE运行环境*

## 壹 Java的基本概念

---

### 1.1 IDEA使用

**项目结构**

* 项目，模块，包，类组成
* **项目**包含了 一个或多个模块
* **模块**中包含了 多个包 
* 每个**包**中包含了类似代码方便管理 *文件夹*
* **类**用于编写代码
* **项目 > 模块 > 包 > 类**

**新建模块**

> File -> ProjectStructure -> Modules -> +

**新建包**

> 在模块下src文件夹邮件 -> new -> package

*通常为公司域名的反写 + 作用*

**快速生成程序main函数**

> main

**快速生成输出语句**

> sout

```java
package top.galaxies.maketry;

public class maketry {
    public static void main(String[] args) {
        System.out.println("HelloWorld");
    }
}
```

### 1.2 注释

**单行**

>//

**多行**

```java
/*
多行
*/
```

**文档注释**

```java
/**注释信息/
```

<br>

```java
package top.galaxies.maketry;

public class maketry {
    public static void main(String[] args) {
        int in_1 = 1;
        int in_2 = 2, out_2 = 1;
        int in_3 = 2, out_3 = 1;
        int out_4 = 1;
        int in_5 = 1;
        int res = in_1 + in_2 + in_3 + in_5 - out_2 - out_3 - out_4;
        System.out.println(res);
    }
}
```

### 1.5 数据类型


**整数**

* 除`short` `int`外
* `byte`(-128-127)
* `long`(19位) *数据值后需要加L*

**小数**

* `float` *数据值后加F*

**字符**

* `char`的取值 0 - 65535

**布尔类型** 

* `boolean`

```java
package top.galaxies.maketry;

public class maketry {
    public static void main(String[] args) {
        long l = 782174389218984L;
        System.out.println(l);
        boolean flag = true;
        System.out.println(flag);
        char c = '我';
        System.out.println(c);
        float f = 1.453f;
        System.out.println(f);
    }
}
```

### 1.6 标识符

**命名规范**

* 必须以字母数字下划线和`$`组成，不可以数字开头
* 推荐`小驼峰命名法`

### 1.7 键盘录入

*Scanner类*

**类的使用方式**

1. 导包 *在类定义上方*
```java
import java.util.Scanner;
```
2. 创建对象
```java
Scanner sc = new Scanner(System.in);
```
3. 接收数据
```java
int i = sc.nextInt();
```

<br>

```java
package top.galaxies.maketry;

// 导包
import java.util.Scanner;

public class maketry {
    public static void main(String[] args) {
        // 创建对象
        Scanner sc = new Scanner(System.in);

        // 接收数据
        int i = sc.nextInt();
        System.out.println(i);
    }
}
```

## 贰 运算符

---

### 2.1 算数运算符

<br>

```java
package top.galaxies.maketry;

import java.util.Scanner;

public class  MakeTry {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        System.out.println(num / 100);
        System.out.println(num % 100 / 10);
        System.out.println(num % 10);
    }
}
```

**隐式转换和强制转换**

* 隐式转换 *按照范围从小到大*

> byte -> short -> int -> long -> float -> double
> byte short char 算数计算时都转换为 int



**字符串的"+"**

* 前后数据只要有字符串, `+`表示**原封不动进行连接**, 结果是一个新的字符串


### 2.2 逻辑运算符

* **逻辑或** `|`
* **逻辑与** `&`
* **逻辑非** `!`
* **逻辑异或** `^` 不同为真

>boolean flag = true ^ false;

**短路逻辑运算符**


* `&&` `||` 真正的c语言与或

### 2.3 三目运算符

*和c语言基本相同，这里不过多赘述*

## 叁 程序流程控制

---

### 3.1 分支结构

*和c语言基本相同，这里不过多赘述*

**switch新特性**

* *JDK12*
* 自动包括了`break`
* 一行的话`{}`可以省略

```java
switch (inNum){
    case 1 -> {
        System.out.println("壹");
    }
    case 2 -> {
        System.out.println("贰");
    }
    case 3 -> {
        System.out.println("叁");
    }
    case 4 -> {
        System.out.println("肆");
    }
    case 5 -> {
        System.out.println("伍");
    }
    default -> {
        System.out.println("未知");
    }
}
```


## 肆 数组

---

### 4.1 数组的定义和初始化

**定义**

* `int [] arr` **常用**
* `int arr[]`

**初始化**

* **静态** `int[] 数组名 = new int[]{元素, 元素, ...};`
 **简写为** `int[] 数组名 = {元素, 元素, ...};`
* **动态** `int[] 数组名 = new int[5]` 产生执行长度有默认值的数组

### 4.2 数组的地址

*数组名表示数组的地址*

* 如`[I@b4c966a`
* 解析: `[`表示数组 `I`表示`int` `@`后为真正十六进制地址

### 4.3 数组越界

*访问越界会有异常抛出*

### 4.4 随机数

```java
import java.util.Random
...
Random r = new Random();
// 返回 0 - 4
int num = r.nextInt(5);
```

### 4.5 数组的内存

**java的内存分配**

* **栈** 方法运行时使用的内存, 比如`main`方法运行, 加载入栈运行
* **堆** 存储对象或者数组, `new`来进行创建, 都存储在堆空间
* **元空间**(*JDK7前的方法区*) 存储运行的.class文件
* **本地方法栈** JVM使用操作系统功能时使用
* **寄存器** 给CPU使用

**数组的内存**

* 数组**变量**是存储在栈空间，**存的只是一个地址**
* 在创建数组时，堆空间中分配了内存，**返回地址给栈中的数组变量**
* 因此访问数组变量，才为地址
* 而下标访问元素时，**通过变量存的的地址，按照索引访问堆中的相应的数组元素**
* 而在`int [] arr1 = arr0`这种操作时, 只是把`arr0`存的的地址赋值给了`arr1`元素, 因此**改变arr1的同时, arr0也发生改变**

### 4.6 数组的长度

> arr.length


## 伍 方法

---

*方法是程序中的最小**执行单元***

### 5.1 方法的定义和调用

**定义**

*在类内定义*

```java
public static void fun(){
    方法体
0}
```

**调用**

```java
fun();
```
<br>

```java
package top.galaxies.maketry;

import java.util.Scanner;

public class  MakeTry {
    public static int[] copyOfRange(int[] arr, int from, int to){
        int[] res = new int[to - from];
        for (int i = 0; i < to - from; i++) {
            res[i] = arr[i];
        }
        return res;
    }
    public static void printArr(int[] arr){
        for (int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] arr1 = copyOfRange(arr, 0, arr.length);
        //printArr(arr1);
        arr1[1] = 0;
        printArr(arr);
        System.out.println("-------------");
        printArr(arr1);
    }
}
```

### 5.2 方法的内存

*方法调用时进栈*

*方法结束时其中变量随之出栈*

**基本数据类型**

* 整数类型
* 浮点数类型
* 布尔类型
* 字符类型

**引用数据类型**

*除基本数据类型之外的类型*

* `new`出来的
* 变量中**存储的不是真实数据，而是指向其他空间的地址**

### 5.3 方法的值传递

*由于传递是变量的值*

*因此对于基本数据类型，在方法定义中改变形参的值,不会影响到调用时实参的值*

*而对于引用数据类型，由于传递的是地址，所以改变形参会影响到实参*

### 5.4 多维数组

```java
int[][] arr = new int[3][5]
```

## 陆 面向对象

---

### 6.1 创建类

**`main`函数同目录下**`Phone.Java`

```java
package top.galaxies.maketry;

public class Phone {
    // 属性
    String brand;
    double price;

    // 行为
    public void call(){
        System.out.println("手机在打电话");
    }
    public void playGame(){
        System.out.println("手机在玩游戏");
    }
}
```

### 6.2 创建对象

包含`main`函数的`maketry.java`

```java
package top.galaxies.maketry;

public class  MakeTry {
    public static void main(String[] args) {
        Phone p = new Phone();
        p.brand = "小米";
        p.price = 1999.99;
        System.out.println(p.brand);
        System.out.println(p.price);
        p.playGame();
    }
}
```

> ctrl + d IDEA中复制当前行到下一行

**注意**

**这种用来描述一类事物的类叫javabean类**

**区分于编写main方法的测试类**

**一个.java文件中可以编写多个类(不用), 但是只有一个能被`public`修饰，`public`修饰的类名要和文件名相同**

**类中的成员在未赋值前为类型的默认值**

### 6.3 封装之控制权限

**利用修饰符 + 类型 + 变量**

`private int age;`

*`private`只能在本类中访问*

*推荐全部成员变量采用此方法，提供相关访问接口*

### 6.4 就近原则和this关键字

**就近原则**

*变量名重合，使用近的*

`this.xx` 访问成员变量`xx`

### 6.5 构造方法

*创建对象时给成员赋值*

```java
修饰符 类名(参数){
    方法体;
}
```

**特点**

* **方法名与类名完全一致**
* **没有返回值类型或者`void`**
* **没有`return`**

*系统会提供默认的无参构造*

*一旦定义了某一种构造，系统不再提供默认的无参构造*

***推荐任何时候都手写无参构造或含参构造***

### 6.6 插件 提供标准的Javabean类

*首先自行写好全部的成员变量 private修饰*

**默认插件**

1. `alt + insert` 调出插件
2. 点击`constructor` 进入构造生成
3. 点击`Select None`再`OK`生成无参构造
4. 如果点击相应的成员再`OK`生成有参构造
5. 调出插件后点 `Getter and Setter` 进入权限控制接口生成
6. 选择相应成员`OK`生成相应接口方法

**ptg插件**

>右键 -> ptg to javabean 一键生成


## 柒 String类

---

### 7.1 API: 应用程序编程接口

*别人写好的东西*

**Java API**

如
* `Scanner`
* `Random`
* `String`

**JDK-API帮助文档**

放在galaxy_java目录下 *[Java参考文档].JDK_API_1_6_zh_CN.CHM">*

### 7.2 String的特点

*使用无需导包(由于在`java.lang`包中)*

*字符串文字如:`"hello"`都是`String`类的对象*

*字符串一旦创建不能更改*

### 7.3 创建字符串的两种方式

* 直接赋值 `String name = "张三";` **常用**
* `new`
  `String() ` 无参构造 空字符串
 `String(String original) ` 根据传入的字符串, 创建字符串对象
 `String(char[] value)` 根据字符数组, 创建字符串对象
 `String(byte[] bytes) ` 根据字节数组, 创建字符串对象

```java
package top.galaxies.maketry;

public class  MakeTry {
    public static void main(String[] args) {
        // 1、直接赋值的方式获取字符串对象
        String s = "abc";
        System.out.println(s);
        // 2、new方式获取一个字符串对象
        // 无参构造 空字符串
        String s1 = new String();
        System.out.println("@" + s1 + "!");
        // 根据传入的字符串, 创建字符串对象
        String s2 = new String(s);
        System.out.println("@" + s2 + "1");
        // 根据字符数组, 创建字符串对象
        // 应用: 修改字符串的内容
        char [] chs = {'a', 'b', 'c', 'd'};
        String s3 = new String(chs);
        System.out.println("@" + s3 + "1");
        // 根据字节数组, 创建字符串对象
        // 根据 ASCII 生成字符串
        // 应用: 网络中传输字节信息
        byte [] bys = {97, 98, 99, 100};
        String s4 = new String(bys);
        System.out.println("@" + s4 + "1");
    }
}
```

*键盘输入的也是`new`出来的*

### 7.4 String的内存分析

**串池**

* 存放字符串常量的内存
* `new`出来的字符串对象不在其中,而在堆区，和正常的对象相同，*不会有复用之类的情况*
* 程序运行时, 字符串**直接赋值需要*串池*中的数据**: 如果**串池中没有该字符串新建字符串**，赋值**地址**给变量，接下来如果用到串池里的字符串，不会新建，**复用串池里的数据，变量为相同的地址**
* 因此**会复用的直接赋值推荐使用**


### 7.5 String的比较

**`==`比较原理**

* 对于**基本数据类型**, 比较的是**具体的值**
* 而对于**引用数据类型**, 比较的是**变量存储的地址**

*所以, 对于`String`来说, 显然两个会复用串池的直接赋值法`==`号比较的结果为`true`, 而对于涉及到不会复用的堆区`new`出来的`String`来说,每一次的地址都是新的,一般为`false`*

**String的方法**

*不再考虑地址，比较的是真实内容*

* `boolean equals(Object anObject) ` 完全一样为`true`, 否则为`false`
* `boolean equalsIgnoreCase(String anotherString) ` 忽略大小写

```java
package top.galaxies.maketry;

public class  MakeTry {
    public static void main(String[] args) {
        String s1 = "abc";
        String s2 = "abc";
        String s3 = new String(s2);
        System.out.println(s1 == s2); // true
        System.out.println(s1 == s3); // false
        System.out.println(s1.equals(s3)); // true
        System.out.println(s3.equalsIgnoreCase("ABC")); // true
    }
}
```

### 7.6 String一些常见方法

* `int length() `返回字符串的长度