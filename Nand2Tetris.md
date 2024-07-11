# 从与非门到俄罗斯方块

[online-IDE](https://nand2tetris.github.io/web-ide/chip)

[课程地址](https://www.coursera.org/learn/build-a-computer/home/week/1)

## 0 绪论

### 简介

从底层的软硬一构建出一个完整的通用计算机

* 前阶段构建硬件部分
* 第二阶段基于构建出的硬件构建计算机的软件

### 本课程的思想 

* 计算机的内容丰富且冗杂 
    * 源文件中的文本是如何发挥作用的
    * 编译器是如何工作的
    * 在屏幕上打印是如何做到的？如何控制具体像素点的亮度
    * 为什么不需要关心标准库等等的具体实现
        * 具体实现 how
        * 是什么东西（接口） what
    * 编程时不要关心多余东西的实现
* 抽象 从底层逐渐向顶层抽象（本课程采用这种方式）
    * 从基本的门逐渐封装为CPU等复杂芯片
    * 将其放入计算机为软件层服务
    * 将已经封装的抽象到下一个级别

### 本课程要构建的硬件 

* 计算机 CPU RAM ROM 等
* 连接鼠标键盘等
* 编写程序，运行

* 硬件部分专注于逻辑门，而不是芯片的制造等（这不是计算机领域）
    * 组合逻辑
    * CPU, 寄存器等
    * 最终组成计算机
* 使用硬件模拟器

* 硬件部分的课程内容
    * 建造一些基本的逻辑门
    * 建造一个算术逻辑单元 ALU
    * 建造存储系统 寄存器 RAM ROM
    * 用机器语言写一些程序，以了解这台计算机要做什么
    * 组成计算机！
    * 开发适合编写的机器语言的汇编器

### 本课程要构建的软件

* 构建非常低级的汇编语言以编写程序
* 了解软件的层次结构
* 构建一种高级语言，并构建编译器
* 构建标准库

## 1 逻辑门

### 布尔逻辑

| 0 | 1 |
| - | - |
| F | T |
| N | Y |

#### AND OR NOT

#### 布尔逻辑的基本组合计算

NOT(0 OR (1 AND 1))

#### 布尔逻辑表达式

f(x, y, z)=(x AND y) OR (NOT(x) AND z) 

了解此类函数的一种方式是列举所有x, y, z写下函数的值

![](img/truthtable.png)

另一种方式是通过公式化简

**交换定律**

* (x AND y)=(y AND x)
* (x OR y)=(y OR x) 

**结合律**

* (x AND (y AND z))=((x AND y) AND z)
* (x OR (y OR z))=,,

**分配律**

* (x AND (y OR z))=(x AND y) OR (x AND z)
* ..

**摩根定律**

* NOT(x OR y)=NOT(x) AND NOT(y)
* ..

### 从真值表构建布尔函数

* 逐行只关注表中输出取1的值
* 列写表达式,使得该表达式仅在本行的各个输入状态时取得1
* OR连接各行的表达式
* 化简

**任何真值表都能转化为AND, OR, NOT的组合**

*OR和AND可以放弃一个，因为他们可以用另外两种表示，但是不能放弃OR或者放弃两个*

### 与非门 NAND

x NAND y = NOT(x AND y)

*与非们可以用自己完成逻辑运算，因为无论AND, OR, NOT都可以由其表示*

你将要使用NAND构建你的计算机！

### 硬件实现布尔函数

**什么是逻辑门？**

逻辑门是一种独立的芯片，有着自己独立的功能

**复合逻辑门**

是由基本逻辑门和其他复合逻辑门组成的复杂一点的逻辑门

#### 基本逻辑门 

NAND, AND, OR, NOT

*用户如何使用门，只需要关注接口（输入与输出），但是如果希望了解门如何实现的，需要打开黑匣子，了解其内部构成*

#### 电路实现

*AND电路的实现*
![](img/ele.png)

### HDL 电路模拟语言 以异或门为例

在HDL构建的逻辑门可以实际对其模拟，测试

* 首先需要真值表（也被称为接口）
* 构建合适原理图

![](img/fb69ecb2.png)

#### 编写HDL文件

```HDL
/** Xor gate: out = (a AND NOT(b)) OR (NOT(a) AND b) */

CHIP Xor {
    // 接口部分
    IN a, b;
    OUT out;

    PARTS:
    // 实现部分
    // 逐一描述原理图
    // 每一个中间输出起合适的名字
    Not (in=a, out=nota);
    Not (in=b, out=notb);
    And (a=a, b=notb, out=aAndNotb);
    And (a=nota, b=b, out=NotaAndb);  
    Or (a=aAndNotb, b=NotaAndb, out=out);
}
```

HDL是一种声明式的语言，不参与实际程序的运行，是门的静态表述

与先后顺序无关，不过习惯上从I到O

### 硬件模拟

* 测试模拟器, 根据更改不同的输入来获取输出，同时可以看到中间输出
* 编写测试语言文件（可以整理一组预先确定的可复制文件）
* 与脚本文件进行比较

#### 测试脚本

```tst
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/1/Xor.tst

output-list a b out;

set a 0,
set b 0,
eval,
output;

set a 0,
set b 1,
eval,
output;

set a 1,
set b 0,
eval,
output;

set a 1,
set b 1,
eval,
output;
```

### 多位输入输出 bus 

*在操作硬件的时候，有时候会操作一堆具有相同地位的输入，将一堆作为一个实体进行整体操作很方便*

这种整体称为**bus**

#### HDL 关于bus

```HDL
CHIP ADD16{
    IN a[16], b[16];
    OUT out[16];

    PARTS:
        ...
}
```

当16位加法器被实现之后，如果我们想实现一个16位三数加法器，逻辑上显然可以使用两次两位加法器，在HDL中的做法：

![](img/ed8b63c4.png)

即某一芯片的接口规定了bus输入输出，那么在使用的时候可以直接输入输出**整个bus**

如果在不是输入接口不是bus的芯片上输入bus数据的某一位，可以用bus数据[..]

![](img/b4ebafc0.png)

而芯片的bus接口也可以分段输入输出

![](img/7d0bcb08.png)

芯片的输入可以为常量 true 或 false

芯片的输出也不必全部需要，允许只输出一部分

### Project 1 简介

从Nand 开始，建造如下逻辑门

* Not And Or Xor Mux DMux 
* Not16 And16 Or16 Mux16 
* Or8Way Mux4Way16 Mux8Way16 DMux4Way DMux8Way

最常见和广泛，在计算机中广泛运用

#### 一些逻辑门的介绍

* Mux 多路复用器
    * 输入 a b sel
    * 输出 out
    * 当 sel 输入 0 out = a
    * 当 sel 输入 1 out = b
* DMux 解复用器
    * 输入 in sel 
    * 输出 a b
    * 当 sel 输入 0 则 a 输出 in 的值，而 b 保持 0
    * 当 sel 输入 1 则 b 输出 in 的值，而 a 保持 0
* And16
    * 输入 a[16] b[16]
    * 输出 out[16]
    * 16位中的每一位进行AND
* Mux4Way16
    * 输入 a[16] b[16] c[16] d[16] sel[2]
    * 输出 out[16]
    * 根据 sel的四种可能性来选择 a b c d

允许使用之前编写过的逻辑门

允许建立其余的芯片来辅助，但是没有必要

编写逻辑门，运行脚本，diff差异！

### 基本逻辑门 Q&A

**是否可以从非NAND的逻辑门建立计算机？**

是的,比如还有一种逻辑门NOR，它也可以构成任意逻辑门，或者从AND,OR,NOT自然地构建,用NAND门构建很常见，它也很便宜。

**如何去建造一个NAND门？**

这是物理学或者电子学的问题（模电），可以用电阻，晶体管等构建

**我们使用的HDL和硬件工程师使用的HDL相比？**

我们使用的HDL很好，是老师构建的，而工程师使用的更复杂一些，有一些C语言的形式，有循环等内容（16路不用CV16次了）,具有模拟功能，也能模拟时间和时钟，不过掌握时间长一些。

**我们目前建造的芯片很简单，如何制造包含数百个零件和连接的芯片？**

没有通用的方法去设计，需要一些聪明才智，我们已经学到一些技巧比如化简，也有一些编译器来制定功能，它们有一些算法来优化（但不是完美的，因为某种理论）

## 布尔运算和ALU

### 二进制表示整数

| Binary | Decimal |
| - | - |
| 0 | 0 |
| 1 | 1 |
| 10 | 2 |
| 11 | 3 |
| 100 | 4 |
| 101 | 5 |

如8位二进制在计算机中表示2^8=256个数（通常保留一位标识正负但也是128+128=256个数）

十进制转化二进制的一种方式：

每次找到最大的2^n, 余下的用2^(n-1)尝试

如 87 = 64 + 0 * 32 + 16 + 0 * 8 + 4 + 2 + 1 

-> 1 0 1 0 1 1 1

99 = 64 + 32 + 0 * 16 + 0 * 8 + 0 * 4 + 2 + 1 -> 1100011

### 二进制加法

![](img/d02a0312.png)

和十进制加法类似地，当每一位（包括前一位的进位）加和大于等于2之后，减去2,并进位1

当最高位发生进位时（假设输出位数与输入相同），会出现**溢出**，在计算机中会被丢弃

**构建用于加法的硬件**

* 半加器 两位相加
* 全加器 三位相加
* 加法器 两个数加和

#### 半加器

| a | b | sum | carry |
| - | - | - | - |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

#### 全加器

| a | b | c | sum | carry | 
| - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

#### 加法器

按照真实的进位步骤进行

### 二进制负数

一种方式是把最高位（以四位二进制为例）作为符号位，当最高位为1,则为负数

| 二进制 | 数字 |
| - | - |
| 1100 | -4 |
| 1110 | -6 |
| 1000 | -0 | 

存在 -0 的问题，会带来一些问题，不好

改用的方案：

仍然使得最高位为0的为整数（0），为1的是负数，但是使用补码：使用2^n - x

以四bit为例，表示-1则使用16 - 1 = 15 > 1111

这样下来非负数可以表示0000-0111共8个数，负数可以表示1111-1000（-1～-8）共8个数

这种方案还可以直接地得到负数的加法，以及减法（基于某种数学原理）

比如 7 - 5 直接使用 7 - （-5）计算即可得到正确结果 2

因此构建减法器，实际上难点为如何计算出负数的二进制

而我们知道补码法确定-x实际上为2^n - x

即为1 + 2 ^ n - 1 - x 而 2 ^ n - 1 为 111111... - x 翻转 x的各个位即可

所以说**想得到一个负数的二进制，就把它的绝对值二进制的所有位翻转再加1**

最后加一的方式也很特别，可以在这个翻转数从低到高再翻转，直到碰到0,将这个0翻转后结束

### 算术逻辑单元 ALU

*冯诺依曼在论文中构建的体系结构*

![](img/7a22cf33.png)

可见其体系结构中CPU是计算机结构中的重要组成，而ALU是CPU中的重要结构

ALU有两个输入input1, input2

有一个函数控制（可能是逻辑函数或算术函数）

输出为f(input1, input2)

通常的计算有 整数加法、整数乘法、整数除法 逻辑运算如按位与、按位或等

**要在ALU中构建多少功能？**

这是一个权衡问题，如果不再硬件中实现某些东西，可以随时用软件对其扩展


#### 一个示例ALU The Hack ALU

* 输入 x[16] y[16]
* 输出 out[16]
* 功能选择 zx nx zy ny f no 他们的组合可以产生如下功能

![](img/2aebc5d5.png)

* 此外还有两个控制输出 zr, ng

### The Hack ALU 的控制

![](img/2561cca6.png)

#### zx ZEROx 

当 zx = 1 将输入的 x 设置为 0 

#### nx NOTx 

当 nx = 1 将输入的 x 取反

控制**按序而非同时发生**，比如 zx 和 nx 都为 1,先 zx 把输入置零，再取反置一

#### zy ZEROy ny NOTy

#### f

如果 f = 1 则计算 x + y, 否则计算 x AND y

请注意，**目前这五步包括尚未发生的下一步，仍是按序进行**

#### no NOT

如果 no = 1 否定输出结果

### The Hack ALU 输出的控制位

用来表示ALU的主要输出

如果 out = 0 则 zr 会 置1（zero）

如果 out < 0 则 ng 会 置1（negative）

### Project 2 概述

可以使用 Project 1 的全部实现

构建如下芯片

* HalfAdder
* FullAdder
* Add16
* Inc16
* ALU

#### HalfAdder

* 输入 a, b
* 输出 sum, carry
* 将两位相加，并输出两位的总和以及进位

#### FullAdder

* 输入 a, b, c
* 输出 sum, carry
* 将三位相加，并输出三位的总和以及进位

#### Add16

* 输入 a[16], b[16]
* 输出 out[16]
* 进行16位加法运算

#### Inc16

* 输入 In[16]
* 输出 out[16]
* 给传入值加1

#### 最有趣的部分 ALU

如上所述
不到20行代码即可实现