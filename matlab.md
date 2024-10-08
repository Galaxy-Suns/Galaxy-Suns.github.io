# Matlab

### Matlab的操作认识

#### 1.窗口布局

##### 1.1主窗口

##### 1.2命令行窗口

中央位置，用于输入命令

>\>\>

为命令提示符,在其后输入命令

在MATLAB中，一个命令可以以 ; 或 , 结束
 ; 表示仅赋值，不显示结果， , 显示赋值结果
一行可以执行多条命令，当一行的最后一条命令以 , 结尾  , 可以省略

当一行的命令没有执行完，可以以 ... 为续行符，在下一行继续写该命令

注释以%开头书写

变量是内存单元的抽象，变量名是给内存单元起的名字
字母开头，由字母数字下划线组成，区分大小写

预定义变量 
>pi i j ans inf nan

##### 1.3当前文件夹窗口cd

位于左侧，表示工作文件夹，没有特殊指明，数据文件也将存放在当前文件夹下

可以用 cd 命令设置当前文件夹
语法为 
```Matlab
cd e:\matlab
```

##### 1.4工作区空间

位于右侧,是用于储存各种变量和结果的内存空间

可以在工作空间对数据观察编辑保存删除

#### 2.搜索路径

##### 2.1作用

在MATLAB中位于当前文件夹和搜索路径下的文件和函数才能被调用

当在命令行输入命令后，MATLAB将按照一定顺序寻找相关命令对象，顺序如下：
== 变量>内部函数>当前文件夹下程序文件（M文件）>搜索路径下其他M文件 ==

##### 2.2设置搜索路径的方法path

可以用 path 命令临时添加搜索路径
语法为 
```matlab
path(path,'e:\matlab')
```

也可以在‘主页’选项卡中，‘环境’命令组，‘设置路径’点击添加

#### 3.内存变量文件save load

用来保存工作区中的一些有用变量

语句为
```matlab
save( '文件名' (,'变量名')) 
```
不加变量名默认保存工作区所有变量
```matlab
load ('文件名or变量名') 
```
#### 4.m文件，脚本，实时脚本
>绿皮书p77


### MATLAB的数据和运算

#### 1.数据

MATLAB中的数据分为数值数据和字符串数据
以下除了字符串均为数值数据

##### 1.1整型

分为8种，分别是无符号，有符号和8,16,32,64位整型的排列组合，
占用字节数按照位数的递增为1,2,4,8位，
取值范围如无符号8位整型为0-2^8-1，而有符号8位为-2^7-2^7-1（由于符号占用一位），
注意2^8=256

转换为整型使用int8,uint8等函数，
当转换数值超过取值范围置为最大值

##### 1.2浮点型single double

分为单精度（四字节），双精度（八字节）
转换函数分别为 :
```matlab
single() 
double()
```
MATLAB中数据默认为双精度型

##### 1.3复型complex real imag abs

实部和虚部默认为双精度型，虚数用 i 或 j 表示

可以用 complex() 函数生成复数
语法为 
```matlab
complex(2,3) 
```
表示生成 2+3i

```matlab
real() %可以求复数的实部
```
```matlab
imag() %可以求复数的虚部
```
```matlab
abs() %可以求复数的模
```

##### 1.4数值数据的最大最小值intmax intmin(real..)、esp
```matlab
intmax() %整数类型最大值
intmin() %整数类型最小值
realmax() %最大正实数
realmin() %最小正实数
```
>esp

esp是一个约等于0的数，除法运算可以分母加上esp规避0

##### 1.5格式控制format
>format

>绿皮书p21

##### 1.6字符向量与字符串

###### 1.6.1字符向量abs char num2str str.. eval

字符向量是由单引号括起来的字符序列
如果字符向量中包含单引号，这个单引号要用两个单引号表示

字符向量在MATLAB中当作行向量，引用方式和数值向量相同：
```matlab
A(1:3)
```

可以建立多行字符向量，构成字符向量矩阵
要求各行字符数相同，否则要用空格调节

字符向量和数值之间的转换可以用 abs() 和 char() 函数实现
```matlab
abs() %将其中的字符串转换为ASCII码
char() %将其中ASCII码转换为字符串
```
要注意char()只是通过ASCII码转换，例如65转换后不能得到'65'
要做到将数值转换为这种相应字符串要通过
```matlab
num2str(65)
```
>ans='65'

字符向量的比较是在元素个数相同时，用ASCII码对其中各元素比较大小，返回长度相同的01向量

还有一些判断字符串是否相等的函数,返回单个的01:
```matlab
strcmp(a,b) %判断两个字符串是否完全一致
strncmp(a,b,n) %判断前n个字符是否一致
strcmpi(a,b) %忽略大小写
strncmpi(a,b,n) %忽略大小写，判断前n个
```

字符向量的查找，以实例演示：
```matlab
findstr('This is a test','is')
```
>ans= 3  6

字符向量的替换，以实例演示：
```matlab
strrep('This is a test','test','class')
```
>ans= This is a class

一个比较重要的函数：
```matlab
eval()
```
用于去掉一个''，可以直接执行里面的命令

其它的一些字符向量操作
>绿皮书p42

######1.6.2字符串string
字符串由""括起
```matlab
string() %将其它类型转换为字符串类型
```
一些处理函数
>绿皮书p43

##### 1.7判断数据类型is.. class
有以下函数
```matlab
isinteger(n) %是否为整数
isfloat(n) %是否为浮点数
isnumeric(n) %是否为数值型
isreal(n) %是否为实数
```
```matlab
isa(1.23,'double') %isa判断是否为指定类型数据
```
```matlab
class() %返回数据类型
```

#### 2.矩阵

矩阵是MATLAB中最基本的数据对象

##### 2.1建立矩阵

矩阵的输入方式如下:
```matlab
A=[1,2,3;4,5,6;7,8,9] %一行中用,分割元素 ;换行
```
这是一个3*3的矩阵

还可以由小矩阵拼接而成
```matlab
B=[-1,-2,-3;-4,-5,-6;-7,-8,-9]
C=[A,B;B,A]
```
则最终得到6*6的矩阵，左上和右下分别是A的各个元素，右上和左下则是B的元素

复数矩阵通常由实部矩阵和虚部矩阵运算得出

多维矩阵的建立
>绿皮书p30

##### 2.2矩阵的引用sub2ind ind2sub size length numel

矩阵可以通过下标（正整数引用），
```matlab
A(3,2) %表示第三行第二列的元素
```
当下标超出范围时，并对引用矩阵赋值时，将自动扩展矩阵，
如在3\*3的给（5,6）赋值，矩阵自动扩展为5\*6，未赋值元素置为0

矩阵的序号是矩阵在内存中储存顺序，按列储存
引用如
```matlab
A(3)
```
sub2ind() 函数通过矩阵的大小（以1*2向量形式）和行列下标返回序号
```matlab
sub2ind([2,3],[1,2;2,2],[1,1;3,2])
```
ans是一个2*2矩阵代表对应序号

ind2sub()函数则相反，通过矩阵的大小和序号返回行列下标
因此要将其赋给两个值，用1*2向量表示
```matlab
[a,b]=ind2sub([3,3],[1,3,5])
```

介绍 size() 函数
```matlab
size() %返回矩阵的大小，以1*2向量表示
```
与之类似还有
```matlab
length() %获取行数和列数的较大值
numel() %获取元素的个数
```

##### ==2.3冒号表达式linspace==

用于产生行向量

格式为 起始:步长:终止 ，也可 起始:终止 省略步长为1
```matlab
1:0.05:2
1:20
```
也可以用linspace（）函数通过个数生成行向量
```matlab
linspace(1,9,5)
```
>ans= 1,3,5,7,9

将冒号表达式用于矩阵引用以获取子矩阵
```matlab
A(i,:) %表示A矩阵第i行全部元素
A(:,j) %表示全部行第j列的元素（第j列全部元素）
A(i:i+m,k:k+m) %表示i到i+m行，k到k+m列的全部元素
```
也可以加入步长取间隔若干行列，或者直接用向量表示

值得注意的是A(a:b)表示通过序号引用a到b的元素，得到行向量
但A(:)得到的所有元素是纵向量

也可以加入end表示末尾元素
```matlab
A([1,4],3:end)
```

可以用空矩阵删除掉矩阵部分元素

##### 2.4改变矩阵形状reshape

利用 
```matlab
reshape(A,m,n)
```
在总元素不变前提下重新将A排成m\*n矩阵
要求size(A)=m\*n

#### 3.结构数据和单元数据

结构数据指类型不同而结构相关的整体
结构矩阵中的元素是结构数据

建立结构矩阵可以采用赋值的方法
```matlab
a(1).x1=10
```
当然结构矩阵元素的成员也可以是结构数据
```matlab
a(1).x1.x11=9
```
单元矩阵的每个元素就是不同数据类型，要用{}建立

#### 4.运算

##### 4.1函数power rem fix floor ceil round find

自变量是矩阵各元素，函数逐项作用于矩阵各元素上，得到结果为于原矩阵同型的矩阵

常用的函数：
```matlab
sin() cos() tan() asin() acos() atan() %自变量弧度
sind() ... %自变量角度
sqrt() %求平方根
power() %求幂
log() log2() log10()
exp() %e的多少次幂
abs() %可以求实数绝对值，复数模，字符串的ASCII码
rem(a,b) %返回a/b的余数
fix() %取整，舍去小数
floor() %向下取整
ceil() %向上取整
round() %四舍五入，最近
isprime() %判断是否为素数
find() %查找矩阵中非0元素返回其序号
```
```matlab
a=[1,2,3;4,5,6;7,8,9];
find(a,2,"first") %表示在前2个数中找不为0的数（按序号）
find(a,2,"last")
```
##### 4.2算数运算

基本运算：针对矩阵而言
>+-*/\^

点运算，针对矩阵中对应元素而言
>.* ./ .\ .^

##### 4.3关系运算

> < >= <= == ~=

如果比较矩阵则是对应元素比较

##### 4.4逻辑运算

>& | ~

如果运算矩阵则是对应元素运算

##### ==4.5优先级==
优先级： 算数>关系>逻辑
单目运算（1个数参与运算）>双目运算
第二条优先级优先程度更高，如~优先级最高    ^^

### 矩阵操作以及线代相关概念的实现

#### 1.特殊矩阵

##### 1.1线代中的特殊矩阵zeros ones eye true false ..

```matlab
%零矩阵
zeros(m)
zeros(m,n)
zeros(size(..))
```
还有一些生成方法
>绿皮书p50

下面这些线代中会用到的矩阵生成方法与零矩阵类似
```matlab
ones() %元素全部为1
eye() %单位阵
true() %全1逻辑阵
false() %全0逻辑阵
```
范德蒙矩阵
```matlab
A=vander([1,7,3,6]) %从上至下为倒数第二列元素
%倒数第一列元素全为1...
```

对角阵
```matlab
A=[1,2,3;4,5,6;7,8,9]
diag(A) %提取主对角线元素
diag(A,2) %提取主对角线以上第二条对角线
diag([1,2,3]) %以此形成对角阵
diag([1,2,3],1) %以此做为主对角线以上第一条对角线
```
三角阵
```matlab
A=[1,2,3;4,5,6;7,8,9]
triu(A) %上三角阵
triu(A,2) %以主对角线以上第二条对角线起的上三角阵
tril() %类似的，下三角
```

##### 1.2随机矩阵rand randn rng
```matlab
rand() %(0,1)内均匀分布
randn() %均值为0，方差为1，标准正态分布
```
生成方法类似零矩阵
matlab生成的是伪随机数
可以在调用随机函数之前用
```matlab
rng("shuffle")
```
选择时间做种子

==常用的随机数操作==
```matlab
x=a+(b-a)*rand(4) %在区间(a,b)均匀分布的四阶随机矩阵
y=a+sqrt(b)*randn(4) %均值是a,方差是b的四阶正态分布随机矩阵
```

##### 1.3特定应用矩阵magic hilb toeplitz pascal
>绿皮书p52

魔方矩阵
```matlab
magic(n)
```
希尔伯特矩阵(病态)
```matlab
hilb(n)
```
托普利兹矩阵:除第一行第一列，其余元素与左上元素相同
```matlab
toeplitz([5,6,7],[5,18,16,12]) %第一行 第一列
```
$$
\begin{pmatrix} 5&18&16&12\\6&5&18&16\\7&6&5&18 \end{pmatrix}
$$
伴随矩阵:与线代中定义不同，matlab中的伴随矩阵是基于多项式定义的
>绿皮书p53

帕斯卡矩阵
```matlab
pascal(5)
```
$$
\begin{pmatrix} 1&1&1&1&1\\1&2&3&4&5\\1&3&6&10&15\\1&4&10&20&35\\1&5&15&35&75 \end{pmatrix}
$$
次对角线元素即为(x+y)^4的展开式系数

#### 2.矩阵操作
##### 2.1矩阵在线代的常见操作pinv det rank trace
转置
```matlab
A.'
```
求逆
```matlab
inv() %求逆
pinv() %求伪逆
```
求行列式
```matlab
det(A)
```
求秩
```matlab
rank(A)
```
求迹
```matlab
trace(A)
```
求特征值和特征向量
```matlab
[特征值，特征向量]=eig(A)
```
##### 2.2其他矩阵常用操作rot90 fliplr flipud norm cond
矩阵旋转与翻转
```matlab
rot90(A,k)%逆时针方向旋转矩阵k次，当k为-改为顺时针
fliplr(A) %左右翻转矩阵
flipud(A) %上下翻转矩阵
```
向量的范数
我们在线代中的向量范数指向量的模
这是2-范数
```matlab
norm(v,p) %p指向量的几-范数常用1,2,inf。默认为2
```
矩阵的范数
```matlab
norm(A,p) %类似地
```
矩阵的条件数(==性能==)
```matlab
cond(A,p) %类似地
```
>绿皮书p64

#### 3.稀疏存储
>绿皮书p69

### 程序流程控制和函数
#### 1.流程控制
##### 1.1输入输出input disp
```matlab
input('提示信息') %输入数值数据，可以是数字矩阵等
input('提示信息','s') %输入字符串数据
disp(A);
```
##### 1.2程序的暂停和延迟pause
```matlab
pause(延迟多少秒) %如果不加秒数则表示暂停，用户按下任意键后继续
```

##### 1.3if语句
```matlab
a=input('请输入一个字符','s')
if a>='A' && a<='Z'
    disp(1);
elseif ...
    ...
else 
    ...
end;
```
值得注意的是==当表达式的值（如矩阵）不包含0元素才为真，否则为假==

##### 1.4switch语句
```matlab
switch 表达式
    case 结果表1
        ...

    case 结果表2
        ...
    ...

    otherwise
    ...
        
end
```
值得注意的有两点
==1. matlab的switch不需要break，只会执行一次==
==2. switch后的数据应为整数/字符（向量），case后的不仅可以是这两种还可以是单元数据==
```matlab
(1,2) %这就是一种单元数据
num2cell() %将向量转换成单元数据
```
##### 1.5for语句
```matlab
for 循环变量 = 向量(常用冒号表达式)
    ...
end
```
==更一般地==
```matlab
for 循环变量 = 矩阵表达式
    ...
end
```
每次取出矩阵的一列赋给循环变量

##### 1.6while语句
```matlab
while 条件
    ...
end
```

##### 1.7break,continue

##### 1.8try
>绿皮书p84
#### 2.函数
>绿皮书p90
#####2.1函数文件
```matlab
function 输出形参表 = 函数名(输入形参表)
    ...
end
```
matlab的函数采取值传递
==函数文件名一般和函数名相同==
##### 2.2匿名函数
```matlab
函数句柄=@(匿名函数形参表)匿名函数表达式
```
==函数句柄和函数名是一个意思==
##### 2.3全局变量
>绿皮书p94

### Matlab绘图与图像处理
#### 1.二维图像绘制
##### 1.1plot函数 给定点
```matlab
plot(x,y,'选项'..) %x，y是对应向量
```
选项
>绿皮书p109

plot函数可以根据选项绘制线或点，默认绘制线
绘制线时是直接连接相应点

参数形式
>绿皮书p106
##### 1.2fplot函数 给定方程/参数方程
```matlab
fplot(匿名函数名，[自变量范围]，选项)
fplot(x匿名函数名，y匿名函数名，[t范围]，选项) %参数方程绘制
```
fplot可以自适应取点，对于已知方程的曲线更适用
##### 1.3fimplicit函数 隐函数
```matlab
fimplicit(匿名函数名,[a b c d])
```
ab是x范围
cd是y范围
>绿皮书p108

##### 1.4图形标注，坐标控制(axis) 
>绿皮书p112

##### ==1.5多图形显示 subplot函数==
```matlab
subplot(2,2,1) %显示2*2图形，当前为第一个图形
```
==注意2,2,3表示左下元素，不是按照序号==

利用axis也可以进行子图的绘制,代码如下
```matlab
ax1=axes('Position',[0.1 0.1 0.4 0.4],'box','on');
ax2=axes('Position',[0.55 0.1 0.4 0.4],'box','on');
 %坐标分别为左下起始点 高度 宽度
axes(ax1);
x=linspace(-5,5,100);
y=(1/(2*pi))*exp(-x.^2./2);
line(x,y);
axes(ax2);
t=linspace(-1,1,100);
x=t.^2;
y=5*t.^3;
line(x,y);
```

##### ==1.6图形叠加 hold on==
在想让多个plot绘制在同一坐标图上时
采取
```matlab
hold on
```
不再保持
```matlab
hold off
```
>绿皮是p116

##### 1.7其他坐标系下的曲线绘制
>绿皮书p117

#### 2.三维图形绘制
##### 2.1三维曲线绘制 plot3 fplot3
与plot fplot类似
>绿皮书p130

##### 2.2三维曲面绘制
流程
生成网格->(f)surf,f(mesh),fimplicit绘制
###### 2.2.1生成网格坐标meshgrid
这里介绍生成网格坐标的一种方法
```matlab
x=linspace(-2*pi,2*pi,35)
y=linspace(0,3*pi,45)
[X,Y]=meshgrid(x,y)
```
meshgrid()将均匀分布在特定区间的x,y转换成后续绘制能识别的网格坐标X，Y
###### 2.2.2mesh和surf函数
在meshgrid()绘制后
```matlab
Z=X.*sin(Y).*exp(-sqrt(X.^2+Y.^2)/2)
subplot(1,2,1)
mesh(X,Y,Z)
usbplot(1,2,2)
surf(X,Y,Z)
```
mesh()和surf()的区别是surf在网格线条之间会有补色
>绿皮书p133
###### 2.2.3fmesh和fsurf函数
无需网格坐标，自适应设置网格坐标间距
适应匿名函数
```matlab
fmesh(函数名,[xmin,xmax,ymin,ymax])
```
>绿皮书p135
###### 2.2.4一些标准曲面绘制
>绿皮书p136
###### 2.2.5隐函数绘制fimplicit3
适应匿名函数
```matlab
fimplicit3(函数名,[xmin,xmax,ymin,ymax,zmin,zmax])
```
###### 2.2.6其他三维图形
>绿皮书p138

#### 3.图像处理
##### 3.1图像读写imread imwrite
```matlab
A=imread('文件名','格式')
imwrite(图片变量,'文件名.格式')
```
##### 3.2图像显示image imshow
```matlab
image(A)
```
```matlab
imshow(A)
```
>绿皮书p146
##### 3.3图像捕获和播放view getframe movie
在此之前，需要介绍改变视点的函数view()
```matlab
view(方位角,仰角) %默认-37.5 30
```
>绿皮书 p140

捕获目前显示的图像的函数getframe
```matlab
M=getframe
```
连续播放图像的函数movie
```matlab
movie(存储这些图像的变量,循环播放次数)
```
>绿皮书p147

### 数据分析和多项式计算
#### 1.常用数据统计处理操作
##### 1.1最大值最小值max min
对于向量
```matlab
y=max(x)
[y,l]=max(x) %l是最大值的位置
```
对于矩阵
```matlab
max(A) %返回行向量->每一列的最大值
[Y,U]=max(A) %U记录每一列最大值的行号
```
min()与max()用法相同
>绿皮书p156
##### 1.2求和求积sum prod
```matlab
sum(x) %向量->和
sum(X) %矩阵->每一列和
```
求积prod同理
>绿皮书p158
##### 1.3求平均值中值mean median
方法和sum()同理
>绿皮书p159
##### 1.4求累加和累乘积cumsum cumprod
同理
>绿皮书p160
##### 1.5排序sort 
方法类似于max
>绿皮书p160
#### 2.标准差方差相关系数协方差std var corrcoef cov
>绿皮书p161
#### ==3.数据插值interp==
用于已知一些离散点，但不知f(x),插值构造g(x)，g(xi)=f(xi),且间隙用g(x)过渡
==注意与拟合区分==
```matlab
interbp(x,y,new_x,method)%一维插值
%当y为矩阵，每一列代表一系列因变量
interbp2(x,y,z,new_x,new_y,method)%二维插值
```
方法详见
>绿皮书p165
#### ==4.曲线拟合polyfit==
与插值的区分是不一定通过采样点
```matlab
P=polyfit(X,Y,n) %使用n次多项式拟合
```
>绿皮书p170
#### ==5.多项式计算==
多项式采用各项系数储存由an->a0
##### 5.1加减+-
要处理成各项对应的长度相同的向量(用0补)
>\+ 
##### 5.2乘conv
对应即可，长度不用相同
```matlab
C=conv(A,B)
```
##### 5.3除deconv
对应即可
```matlab
[P,r]=deconv(A,B) %P为商,r为余数
```
##### 5.4求导polyder
```matlab
p=polyder(P)
p=polyder(P,Q) %P*Q的导数
[p,q]=polyder(P,Q) 
%P/Q的导数，分母->p,分子->q
```
##### 5.5求值polyval polyvalm
```matlab
polyval(P,x)
%x为一个数or向量or矩阵->对每一个元素
polyvalm(P,X)
%X为一个方阵->整个作为自变量
```
##### 5.6求根roots
```matlab
x=roots(P)
```
>绿皮书p175

### Matlab方程求解
#### 1.方程/组求解
##### 1.1线性方程组求解
###### 1.1.1左除运算符 \ 求逆pinv
线性方程组Ax=b
```matlab
x=A\b
```
也可使用求逆 A为方阵
```matlab
x=pinv(A)*b
```
###### 1.1.2分解矩阵法lu qr chol(chloesky)
>绿皮书p182

###### 1.1.3迭代法
>绿皮书p186

##### 1.2非线性方程/组求解
###### 1.2.1单变量非线性方程数值求解fzero
需要建立函数文件f
```matlab
z=fzero(@f,x0)%x0为搜索的起点(根在x0附近)
```
>绿皮书p190
###### 1.2.2非线性方程组数值求解fsolve
需要建立函数文件f如下
```matlab
function res=f(p) 
%这个函数文件传入的是x1,x2...自变量向量
x1=p(1);
x2=p(2);
res(1)=x1-x2+..
res(2)=..
%返回的是方程组一边（另一边等于0）
end
```
>绿皮书p190
```matlab
options=optimset('Display','off')
x=fsolve(@f,[0.5,0.5]',options)
%[0.5,0.5]'是搜索的起点
```
##### 1.3符号方程求解solve
```matlab
syms 自变量1 自变量2 自变量3 ..
[自变量1,自变量2,自变量3 ..]=...
solve(等式1,等式2,等式3..,自变量1,自变量2,自变量3 ..)
```
>绿皮书p236

#### 2.常微分方程求解
##### 2.1常微分方程数值求解ode
建立函数文件f如下
```matlab
function res=f(t,x)
%传入自变量区间
res(1)=x1'右侧部分%如x1用x(1)表示
res(2)=x2'右侧部分
%返回是各一阶导数的右侧无导数项部分
```
>绿皮书p195

只能解决一阶导数，如有二阶以及更高阶导数项，
要按照如下步骤化为一阶
1. 最高阶不变，令第二高阶x''''..'为x1
2. 第三高阶为x2，以此类推
3. 重写方程：x1'(最高阶)=...(用x1...表示)
4. x2'=x1,x3'=x2...
>绿皮书p195
```matlab
y0=[a,b..]%a是x1(0)...
[t,y]=ode45(@F,[范围],y0)
```
##### 2.2常微分方程符号求解diff dsolve
```matlab
diff(y,x,n) %表示y关于x的n阶导数
```
```matlab
dsolve(式子1，式子2,..初始1，初始2..)
```
初始条件如y(0)=1这样表示
>绿皮书p237
#### 3.最优化问题的求解
>绿皮书p197
### Matlab微分与积分
#### 1.微分
##### 1.1数值导数
###### 1.1.1通过拟合多项式近似求导
>数据分析和多项式计算4.曲线拟合
###### 1.1.2求向前差分diff
```matlab
x=0:pi/24:pi
dx=diff(sin([x,pi+pi/24]))/(pi/24)
%求出的差分/间距(步长)即为导数
注意要再添加一个元素
```
==注意要再添加一个元素==
##### 1.2符号导数diff
```matlab
diff(f,x,n) %对f符号表达式对x求n阶导
```
#### 2.积分
##### 2.1数值积分(定积分)
###### 2.1.1自适应算法integral
```matlab
integral(匿名函数名,xmin,xmax)
```
###### 2.1.2高斯-克朗罗德法quadgk
```matlab
quadgk(匿名函数名,xmin,xmax)
```
可求inf,-inf
###### 2.1.3梯形积分法trapz
用于求离散量的积分
```matlab
trapz(Y) %均匀间距
trapz(X,Y)
```
>绿皮书p213
###### 2.1.4累计梯形积分cumtrapz
>绿皮书p214
###### 2.1.5数值多重积分
>绿皮书p215
##### 2.2符号积分(不定、定)
```matlab
inv(f,x) %以x为自变量，求f的不定积分
inv(f,x,a,b) %求f在a,b的定积分
```
#### 3.离散傅里叶变换
>绿皮书p215
### Matlab其余符号函数内容
#### 1.建立符号对象
```matlab
syms a b;
syms f(x); %建立自变量是x的函数f
syms f(x,y); %建立自变量是x,y的函数f
```
>绿皮书p224
#### 2.符号对象的运算
##### 2.1四则运算
>\+ - * / .* ./
##### 2.2符号多项式系数提取coeff
```matlab
coeff(s) %升序
```
>绿皮书p228
##### 2.3其余运算
>绿皮书p226

#### ==3.级数符号求和==
```matlab
symsum(通项,第几项开始，第几项结束)
```
#### 4.泰勒级数
>绿皮书p235