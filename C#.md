C#

## Hello World

### 类和命名空间的关系

```c#
using System; // 使用了 System 命名空间，即可直接使用其下的类，如 Console
using System.Collections.Generic;
using System.Linq;
using System.Text;  
using System.Threading.Tasks;

// Program 类 在 CSharpConsoleDemo 命名空间中
// 从 某个 命名空间 找到对应的 类
namespace CSharpConsoleDemo
{
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Hello,World!"); // 使用了 System，相当于 System.Console...
        }
    }
}
```

* 命名空间其下有各种类，解决了**冲突问题**
* `using` 关键字引入命名空间

### 类库

*类和命名空间的存储位置* 

#### 黑盒引入 dll

`... .dll文件`

* 无源代码
* **引入方法** 在`vs`的`资源管理器`的`引用`处添加`dll`文件，即可使用其中包含的命名空间

####  白盒引入 项目源代码

* 有源代码

* **引入方法** 
  1. 在`资源管理器`的`解决方案`处添加项目
  2. 在项目`引用`处添加解决方案中的其他项目，完成

### 类与对象

* `new Form()`

* 使用`new`关键字实例化一个对象
* 返回的是地址，因此在a接受这个对象后，用b接受，二者操作的是同一对象

### 事件

*c# 特有的 类中如同属性和方法的成员*

* 类或对象通知其它类或对象的机制 *善用，不要滥用*.

### 编译过程

源文件 -> exe,dll程序集(方便在.net框架下运行) -> 执行时再实时编译成机器指令（这一步骤很快）

## 差异语法

* `dynamic`关键字模仿弱类型的声明数据方式

### 转义符 @

```c#
@"a\b\c" 等同于 "a\\b\\c"
```

* 此外可以支持字符串字面量为多行

```c#
@"74382
23"
```

### 输入输出 WriteLine, ReadLine

```c#
Console.WriteLine(..);
... = Console.ReadLine();
```

### 字符串转换为数字 Convert.ToInt32

```c#
Convert.ToInt32(字符串); // "32" => 32
```

### 字符串格式化输出 "{0} {1} {2}", a, b, c

```c#
Console.WriteLine("{0}, {1}, {2}", a, b, c);
```

### 数据类型

* C#中 的 long -> long long

#### 值类型和引用类型

* 数字，布尔，结构体，字符，小数，枚举等 值类型
* 字符串，数组，类，函数等 引用类型



* 值类型存在栈区
* 而引用类型的实际数据存在堆区，而变量实际上存放的是引用(地址)（存在栈中），指向堆区的实际数据

### 数据类型的转换 Convert.To...(..)

* 不同数据类型（整数->字符串/布尔...）之间往往不能强制类型转换或隐式类型转换，使用`Convert.To...(val)`

```c#
if (Convert.ToBoolean(3)){
    Console.WriteLine("true");
}
```

### 数组 int []

#### **声明** int age = {...}

```c#
int[] age = {1, 2, 3, 4, 6 // 声明和定义要在同一行

int[] age;
age = new int[10]; // 默认值为 0

int[] age;
age = new int[] {1, 2, 3, 4, 6}; // 第一种的完整版
或 age = new int[5] {1, 2, 3, 4, 6};
```

#### **遍历** foreach

*除了  `for...arr.length` 的形式，还有`foreach`*

```c#
foreach(int temp in age){
    ...
}
```

### 字符串常用方法

*均返回一个新的`string`*

* `str.ToLower()` 字母均转为小写
* `str.ToUpper()` 字母均转为大写

* `str.Trim()`去掉字符串首尾的空格
* `str.TrimStart()`去掉字符串前面的空格
* `str.TrimEnd()`去掉字符串后面的空格



* `str.split(ch)` 按照某字符切割字符串，返回数组

### 函数(方法)

* `(static) 返回值 函数名（形参）{函数体}`

```c#
static bool checkStr(string str) {
    return Convert.ToBoolean(str.Length);
}
```



#### **传入数组** new int[] {..}

```c#
sum1(new int[] {1, 2, 4, 2})
```

#### **传入参数数组** params

* 即把传入实参转换为数组， 赋给`params`形参
* `params`形参的前面可以有其它形参，但是后面不行

```c#
// 定义时
static int sum1(params int[] nums){...}
    
// 使用时
sum1(1, 2, 4, 2)
```

### 枚举类型 （C语言就有）

本质是整数

```c#
// 定义
enum 枚举类型名字
{
     Math, Chinese, English, Physical, Chemistry, 各个值
}
// 使用
枚举类型名字 变量名 = 枚举类型名字.枚举类型值
```

### 结构体中的函数

* 直接访问结构体的各个属性，不需要`this`

### 委托 delegate

*存储函数引用的类型*

可以把符合形参和返回值的函数进行委托

```c#
static double Multiply(double param1, double param2) {
    return param1 * param2;
}
static double Divide(double param1, double param2)
{
    return param1 / param2;
}
// 定义委托
delegate 返回值 委托名(double param1, double param2);

static void Main(string[] args)
{
    Console.WriteLine(Multiply(5, 7));
    Console.WriteLine(Divide(5, 7));
	// 委托的使用
    MyDelegate delegate1 = Multiply;
    Console.WriteLine(delegate1(6, 7));
    delegate1 = Divide;
    Console.WriteLine(delegate1(6, 7));
    Console.ReadLine();
}
```

### 类

习惯上每个类创建一个文件，但是每一个文件是可以包含多个类的

控制台程序中，`vs`会默认创建`Program`文件以及`Program`类

* 类名和文件名(.cs)保持一致
* 命名空间和项目名保持一致

#### 添加类

* 项目处右键添加类

#### 成员

* 每个成员需要在前面指定权限

```c#
// 定义类
internal class Book
{
    public string name;
    public double value;
    public void show()
    {
        Console.WriteLine("姓名: " + this.name);
        Console.WriteLine("价格: " + this.value);
    }
}
...
// 实例化
static void Main(string[] args)
{
    Book math = new Book();
    math.name = "数学";
    math.value = 18.5;
    math.show();
    Console.ReadLine();
}
```

#### 构造函数

* 名字和类名相同，不写返回值

#### 属性 set get

* 可以有自身的get和set
* 可以借此向外返回私有属性控制权限

```c#
public string Name
{
    // get 和 set都可以看做函数
    // get 的返回值作为name属性被访问时调用
    // set 的形参为value
    get
    {
        return this.name;
    }
    set
    {
        this.name = value; // value 是传来的值
    }
}

简写
public string Name
{
    get; // 只读 返回的是private"字段" name(无需定义) 自动转为小写
}
```

#### 继承 : BaseClass

* 每个类有且只有一个父类，默认的父类为`Object`

* 在类内部使用来自父类的属性，方法使用`base.`，类似自身的`this.`

#### 方法重写

*重写继承自父亲的方法*

##### 虚函数 父 Virtual 子 override

```c#
// Father中
public virtual void say()
{
    Console.WriteLine("Hi, I am father!");
}
...
// Son 中
public override void say()
{
    Console.WriteLine("Hi, I am Son");
}    
```

##### 隐藏方法 子 new

```c#
public new void say()
{
    Console.WriteLine("Hi, I am Son");
}
```

#### 抽象类和抽象方法 abstract

*抽象类不能实例化，抽象类的函数可以为抽象函数(只有声明没有函数体)*

```c#
// Father
internal abstract class Father // 抽象类
{
    ...
    public abstract void myClassName(); // 抽象方法
}
  

// 子类必须重写抽象父类中的抽象方法 override
class Son : Father
{
    public new void say()
    {
        Console.WriteLine("Hi, I am Son");
    }
    public override void MyClassName() // 重写抽象方法
    {
		...
    }
}
```

#### 密封类和密封方法 sealed

* 密封类不允许被继承
* 对方法加上 sealed，该方法不允许被子类重写

#### 子类的构造函数

```c#
// Father
public Father(){
	...
}

// Son
public Son() 或 public Son():Father()
{
    ...
}
// 构造子类对象时，会先调用父类无参构造函数
// 如果要调用父类的有参构造
public Son(int a, int fa, int fb):Father(fa, fb)
{
    ...
}
```

#### 成员/类的修饰符

* `public`, `provate`(子不能继承), `protected`(子可以继承)
* `internal`只能在同一程序集中访问(同一项目)
* `protected internal`
* `static`修饰类把其作为静态类，其内的成员必须为静态，不可实例化。静态成员可以通过对象和类来访问。

让别的项目访问到类可以使用修饰符

### 匿名类型 var

`var`不指定类型

```c#
var age = 45;
var name = "hi";

// 仍为强类型 不可更改如 age = "name" 报错
```

