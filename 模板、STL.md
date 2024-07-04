# 模板、STL

## 第一章 模版

---

_泛型编程_

通用的模具，大大提高复用性

_只是框架，不能直接使用，其通用不是万能的_

**分为函数模版和类模版**

### 1.1 函数模版

---

_建立一个通用函数，其返回值和形参类型可以不指定，用一个虚拟类型替代_

```c++
template<typename/class T(大写字母)>
函数声明或定义
```

```c++
#include <iostream>
#include <cstdio>

using namespace std;

// 交换两个整型函数
void swapInt(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

// 交换两个浮点型函数
void swapDouble(double &a, double &b)
{
    double temp = a;
    a = b;
    b = temp;
}

// 函数模版
template <typename T> // 声明一个模版，告诉编译器后面代码紧跟着的T不要报错，T是一个通用的数据类型
void mySwag(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

void test01()
{
    int a = 10;
    int b = 20;
    // swapInt(a, b);
    // 利用函数模版交换
    // 两种方式使用函数模版
    // 1、自动类型推导
    // mySwag(a, b);
    // 2、显示指定类型
    mySwag<int>(a, b);
    printf("a=%d\nb=%d\n", a, b);
    double c = 1.1;
    double d = 2.2;
    swapDouble(c, d);
    printf("c=%.1lf\nd=%.1lf\n", c, d);
}

int main()
{
    test01();

    return 0;
}
```

### 1.2 注意事项

---

- 自动类型推导要推导出**一致的数据类型 T**
- 模版必须要确定出 T 的数据类型，才可以使用

```c++
#include <iostream>
#include <cstdio>

using namespace std;

// 函数模版使用注意事项
template <typename T> // typename可以替换成class
void mySwap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

// 1、自动类型推导，必须推导出一致的数据类型T，才可以使用
void test01()
{
    int a = 10;
    int b = 20;
    mySwap(a, b); // 正确
    char c = 'c';
    // mySwap(a, c); // 错误 推导不出一致的T类型

    printf("a = %d\nb = %d\n", a, b);
}

// 2、模版必须要确定出T的数据类型才可以使用
template <typename T>
void func()
{
    printf("func 调用\n");
}

void test02()
{
    // func(); // 错误 没有确定T的类型
    func<int>();
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 1.3 函数模版案例

---

- 利用函数模版封装一个排序函数，可**对不同数据类型数组排序**
- 排序规则从大到小排，排序算法为选择排序
- 分别利用 char 数组和 int 数组排序

```c++
#include <iostream>
#include <cstdio>

using namespace std;

// 实现通用 对数组进行排序的函数
// 规则 从大到小
// 算法 选择排序
// 测试 char 数值、int 数值

// 交换函数模板
template <typename T>
void mySwap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

// 数组选择排序模版
template <typename T>
void mySort(T *arr, int len)
{
    for (int i = 0; i < len; i++)
    {
        int max = i; // 认定最大值的下标
        for (int j = i + 1; j < len; j++)
        {
            // 认定的最大值比遍历出的数值要小，说明j下标的元素才是真正的最大值
            if (arr[max] < arr[j])
            {
                max = j;
            }
        }
        if (max != i)
        {
            // 交换max和i元素
            mySwap(arr[i], arr[max]);
        }
    }
}

// 提供打印函数模版
template <typename T>
void printArray(T *arr, int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << arr[i] << " ";
    }
    printf("\n");
}

void test01()
{
    // 测试char数组
    char charArr[] = "badcfe";
    mySort(charArr, sizeof(charArr) / sizeof(char));
    printArray(charArr, sizeof(charArr) / sizeof(char));
}

void test02()
{
    // 测试int数组
    int intArr[] = {7, 5, 1, 3, 9, 2, 4, 6, 8};
    mySort(intArr, sizeof(intArr) / sizeof(int));
    printArray(intArr, sizeof(intArr) / sizeof(int));
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 1.4 普通函数与函数模版的区别

---

- 普通函数调用时可以发生自动类型转换(隐式类型转换)
- 函数模版调用时，如果利用**自动类型推导，不会发生隐式类型转换**
- 如果利用显示指定类型的方法，可以发生隐式类型转换

```c++
#include <iostream>
#include <cstdio>

using namespace std;

// 普通函数与函数模版区别

// 1、普通函数调用时可以发生隐式类型转换
// 2、函数模版用自动类型推导，不可以发生隐式类型转换
// 3、函数模版 用显示指定类型，可以发生隐式类型转换

// 普通函数
int myAdd01(int a, int b)
{
    return a + b;
}

void test01()
{
    int a = 10;
    int b = 20;
    char c = 'c'; // a - 97 c - 99
    printf("%d\n", myAdd01(a, c));
}

// 函数模版
template <typename T>
T myAdd02(T a, T b)
{
    return a + b;
}

void test02()
{
    int a = 10;
    int b = 20;
    char c = 'c';
    // 自动类型推导
    // printf("%d\n", myAdd02(a, c)); 错误 不会发生隐式类型转换
    // 显示指定类型
    printf("%d\n", myAdd02<int>(a, c)); //正确 发生隐式类型转换
}

int main()
{
    test01();
    test02();
    return 0;
}
```

_建议采用显示指定类型调用函数模版_

### 1.5 重载下普通函数和函数模版的调用规则

---

- 如果普通函数和函数模版都可以实现，**优先调用普通函数**
- 可以通过**空模板参数列表强制调用函数模版**
- 函数模版也可以发生重载
- 如果函数模版可以产生**更好的匹配，优先调用函数模版**

```c++
#include <iostream>
#include <cstdio>

using namespace std;

// 重载下普通函数和函数模版的调用规则
// 1、如果函数模版和普通函数都可以调用，优先调用普通函数
// 2、可以通过空模版参数列表 强制调用 函数模版
// 3、函数模版可以发生重载
// 4、如果函数模版可以产生更好的匹配，优先调研函数模版

void myPrint(int a, int b)
{
    printf("调用普通函数\n");
}

template <typename T>
void myPrint(T a, T b)
{
    printf("调用函数模版\n");
}

template <typename T>
void myPrint(T a, T b, T c)
{
    printf("调用重载函数模版\n");
}

void test01()
{
    int a = 10;
    int b = 20;
    myPrint(a, b); // 优先调用普通函数
}
void test02()
{
    int a = 10;
    int b = 20;
    // 通过空模版参数列表，强制调用函数模版
    myPrint<>(a, b);
}
void test03()
{
    int a = 10;
    int b = 20;
    // 函数模版也可以重载
    myPrint(a, b, 100);
}
void test04()
{
    char c1 = 'a';
    char c2 = 'b';
    // 如果函数模版产生更好的匹配，优先调用函数模版
    myPrint(c1, c2);
}

int main()
{
    test01();
    test02();
    test03();
    test04();
    return 0;
}
```

_既然提供了函数模版，最好不要提供普通函数，否则容易产生二义性_

### 1.6 模板的局限性

---

- 在模版的一些赋值，比较功能，如果传入数组、自定义类型，则无法完成
- 为例解决这种问题，c++提供模版的重载，可以为这些特定类型提供具体化的模版

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 模版局限性
// 模版并不是万能的，有些特定数据类型，需要用具体化的方式做特殊的实现

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_age = age;
    }

    // 姓名
    string m_Name;
    // 年龄
    int m_age;
};

// 对比两个数据是否相等函数
template <typename T>
bool myCompare(T &a, T &b)
{
    if (a == b)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// 利用具体化Person的版本实现代码，具体化优先调用
template <>
bool myCompare(Person &p1, Person &p2)
{
    if (p1.m_age == p2.m_age && p1.m_Name == p2.m_Name)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void test01()
{
    int a = 10;
    int b = 20;
    bool ret = myCompare(a, b);
    if (ret)
    {
        printf("a == b\n");
    }
    else
    {
        printf("a != b\n");
    }
}

void test02()
{
    Person p1("Tom", 10);
    Person p2("Tom", 10);
    bool ret = myCompare(p1, p2);
    if (ret)
    {
        printf("p1 == p2\n");
    }
    else
    {
        printf("p1 != p2\n");
    }
}

int main()
{
    test01();
    test02();
    return 0;
}
```

_使用具体化的模版，可以解决自定义类型的通用化_
_学习模版不是为了写模版，而是为了运用 STL 提供的模版_

### 2.1 类模板基本语法

---

```c++
template<class/typename T>
类
```

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 类模版
template <class NameType, class AgeType>
class Person
{
public:
    Person(NameType name, AgeType age)
    {
        this->m_Age = age;
        this->m_Name = name;
    }
    void showPerson()
    {
        cout << "name: " << this->m_Name << " age: " << this->m_Age << endl;
    }

    NameType m_Name;
    AgeType m_Age;
};

void test01()
{
    Person<string, int> p1("孙悟空", 999);
    p1.showPerson();
}

int main()
{
    test01();
    return 0;
}
```

### 2.2 类模板和函数模版区别

---

- 类模版**没有自动类型推导**的使用方式
- 类模板在**模版参数列表中可以有默认参数**

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 类模板与函数模版区别
template <class NameType, class AgeType = int>
class Person
{
public:
    Person(NameType name, AgeType age)
    {
        this->m_Name = name;
        this->m_Age = age;
    }+

    void showPerson()
    {
        cout << "name: " << this->m_Name << " age: " << this->m_Age << endl;
    }

    NameType m_Name;
    AgeType m_Age;
};

// 1、类模板没有自动类型推导的使用方式
void test01()
{
    // Person p("孙悟空", 1000); 错误，无法用自动类型推导

    Person<string, int> p("孙悟空", 1000); // 正确，只能用显示指定类型
    p.showPerson();
}
// 2、类模板在参数列表中可以有默认参数
void test02()
{
    Person<string> p("猪八戒", 999);
    p.showPerson();
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 2.3 类模板中成员函数创建时机

---

- 普通类中成员函数一开始就可以创建
- 类模板中的成员函数在调用时才创建

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 类模板中成员函数创建时机
// 类模板中成员函数在调用时才去创建

class Person1
{
public:
    void showPerson1()
    {
        printf("Person1 show\n");
    }
};

class Person2
{
public:
    void showPerson2()
    {
        printf("Person2 show\n");
    }
};

template <class T>
class myClass
{
public:
    T obj;

    // 类模板中的成员函数
    void func1()
    {
        obj.showPerson1();
    }
    void func2()
    {
        obj.showPerson2();
    }
};

void test01()
{
    myClass<Person2> m;
    // m.func1();
    m.func2();
}

int main()
{
    test01();
    return 0;
}
```

### 2.4 类模板参数做函数参数

---

传入方式

- 指定传入类型 _直接显示对象的数据类型_
- 参数模版化 _将对象中的参数转变为模版进行传递_
- 整个类模板化 _将这个对象类型模板化进行传递_

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 类模版的对象做函数的参数

template <class T1, class T2>
class Person
{
public:
    Person(T1 name, T2 age)
    {
        this->m_Name = name;
        this->m_Age = age;
    }

    void showPerson()
    {
        cout << "姓名: " << this->m_Name << " 年龄: " << this->m_Age << endl;
    }

    T1 m_Name;
    T2 m_Age;
};

// 1、指定传入类型

void printPerson1(Person<string, int> &p)
{
    p.showPerson();
}

void test01()
{
    Person<string, int> p("孙悟空", 100);
    printPerson1(p);
}

// 2、参数模版化

template <typename T1, typename T2>
void printPerson2(Person<T1, T2> &p)
{
    p.showPerson();
    // cout << "T1的类型为: " << typeid(T1).name() << endl;
    // cout << "T2的类型为: " << typeid(T2).name() << endl;
}

void test02()
{
    Person<string, int> p("猪八戒", 90);
    printPerson2(p);
}

// 3、整个类模板化

template <typename T>
void printPerson3(T &p)
{
    p.showPerson();
}

void test03()
{
    Person<string, int> p("唐僧", 30);
    printPerson3(p);
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

_指定传入类型最为常用_

### 2.5 类模版与继承

---

- 当子类继承的父类是一个模版时，子类声明时，要制定出父类中 T 的类型
- 如果不指定，编译器无法给子类分配内存
- 如果想灵活指定出父类中 T 的类型，子类也需变成类模板

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 类模板与继承
template<class T>
class Base
{
public:
    T m;
};

//class Son : public Base // 错误，必须要知道父类中的T类型，才能继承子类
class Son : public Base<int>
{

};

void test01()
{
    Son s1;
}

//如果想灵活指定父类中T类型，子类也需要变类模板

template<class T1, class T2>
class Son2 : public Base<T2>
{
    T1 obj;
};

void test02()
{
    Son2<int,char> S2;
}

int main()
{
    return 0;
}
```

### 2.6 类模版成员函数类外实现

---

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 类模板成员函数类外实现

template <class T1, class T2>
class Person
{
public:
    Person(T1 name, T2 age);
    void showPerson();
    T1 m_Name;
    T2 m_Age;
};

template <class T1, class T2>
Person<T1, T2>::Person(T1 name, T2 age)
{
    this->m_Age = age;
    this->m_Name = name;
}

template <class T1, class T2>
void Person<T1, T2>::showPerson()
{
    cout << "name: " << this->m_Name << " age: " << this->m_Age << endl;
}

void test01()
{
    Person<string, int> P("Tom", 20);
    P.showPerson();
}

int main()
{
    test01();
    return 0;
}
```

### 2.7 类模板分文件编写

---

_由于类模板中成员函数创建时机在调用阶段，导致分文件编写链接不到_

- 方法 1 直接包含.cpp 源文件
- 方法 2 将声明和实现写到同一文件，并更改后缀名是.hpp，_hpp 是约定俗成的名字，不强制_

```c++
#include <iostream>
#include <cstdio>
#include <string>

// 第一种解决方式 直接包含源文件
//#include "person.cpp"

// 第二种解决方式 将.h和.cpp中内容写到一起，将后缀名改为.hpp文件
#include "person.hpp"

using namespace std;

// 类模板分文件编写问题以及解决

void test01()
{
    Person<string, int> p("Jerry", 18);
    p.showPerson();
}

int main()
{
    test01();
    return 0;
}
```

person.hpp 中

```c++
#pragma once
#include <iostream>

using namespace std;

template <class T1, class T2>
class Person
{
public:
    Person(T1 name, T2 age);

    void showPerson();

    T1 m_Name;
    T2 m_Age;
};

template <class T1, class T2>
Person<T1, T2>::Person(T1 name, T2 age)
{
    this->m_Age = age;
    this->m_Name = name;
}

template <class T1, class T2>
void Person<T1, T2>::showPerson()
{
    cout << "姓名: " << this->m_Name << " 年龄: " << this->m_Age << endl;
}
```

### 2.8 类模板与友元

---

- 全局函数雷内实现-直接在雷内声明友元即可
- 全局函数类外实现需要提前让编译器知道全局函数的存在

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 通过全局函数打印Person的信息

// 提前让编译器知道Person类存在
template <class T1, class T2>
class Person;

// 类外实现
template <class T1, class T2>
void printPerson2(Person<T1, T2> p)
{
    cout << "name: " << p.m_Name << " age: " << p.m_Age << endl;
}

template <class T1, class T2>
class Person
{
    // 全局函数类内实现
    friend void printPerson(Person<T1, T2> p)
    {
        cout << "name: " << p.m_Name << " age: " << p.m_Age << endl;
    }
    // 全局函数类外实现
    // 加空模版参数列表
    // 如果全局函数是类外实现，需要让编译器提前知道这个函数的存在
    friend void printPerson2<>(Person<T1, T2> p);

public:
    Person(T1 name, T2 age)
    {
        this->m_Name = name;
        this->m_Age = age;
    }

private:
    T1 m_Name;
    T2 m_Age;
};

// 1、全局函数在类内实现
void test01()
{
    Person<string, int> p("Tom", 20);
    printPerson(p);
}

// 2、全局函数在类外实现
void test02()
{
    Person<string, int> p("Jerry", 20);
    printPerson2(p);
}

int main()
{
    test01();
    test02();
    return 0;
}
```

_建议全局函数类内实现_

## 第二章 STL 容器

### 1.1 STL 简介

---

**标准模板库**

- 广义上分为**容器，算法，迭代器**
- 容器和算法之间通过迭代器无缝衔接
- STL 几乎所有代码都采用模板类或模版函数

**六大组件**

- **容器** 各种数据结构 *vector,list,deque,set,map*等，用来存放数据
- **算法** 各种常用算法 _sort,find,copy,for_each_
- **迭代器** 扮演了容器和算法之间的胶合剂
- **仿函数** 行为类似函数，可作为算法的某种策略
- **适配器(配接器)** 用于修饰容器/仿函数/迭代器的接口
- **空间配置器** 负责空间的配置与管理

**容器** _置物之所也_

STL 的容器将一些最广泛的数据结构实现出来

*数组，链表，树，栈，队列，集合，映射表*等

- **序列式容器** 强调值的排序，序列式容器中每个元素都要固定的位置 _按照放的顺序_
- **关联式容器** 二叉树结构，各元素之间没有严格的物理意义上的顺序关系 _放的同时进行了排序_

**算法** _问题之解法也_

有限的步骤，解决逻辑或数学上的问题，这一门学科称之为算法 _algorithms_

- **质变算法** 在运算过程期间会更改区间内元素的内容 *拷贝，替换，删除*等
- **非质变算法** 在运算过程中不会更改区间内元素的内容*查找、计数、遍历、寻找极值*等

**迭代器** _容器和算法之间的粘合剂_

提供一种方法，使之可以**依序访问某个元容器的各个元素**，又无需暴露该容器的内部表示方法

**每个容器都有自己专属的迭代器**

使用**类似于指针**，初学时可以理解为指针

- 输入迭代器 只读 ++ == ！=
- 输出迭代器 只写 ++
- 前向迭代器 读写，向前推进 ++ == ！=
- 双向迭代器 读写，向前后推进 ++ --
- 随机访问迭代器 读写，可以跳跃方式访问任意数据 ++ -- [n] -n < > <= >=

_常用双向迭代器和随机访问迭代器_

### 1.2 vector 存放内置数据类型

---

- 容器 _vector_
- 算法 _for_each_
- 迭代器 _vector<int>::iterator_

```c++
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm> //标准算法头文件

using namespace std;

// vector容器存放内置数据类型

void myPrint(int val)
{
    printf("%d\n", val);
}

void test01()
{
    // 创建一个vector容器，数组
    vector<int> v;
    // 向容器中插入数据
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);

    // 通过迭代器访问容器中的数据
    // vector<int>::iterator itBegin = v.begin(); // 起始迭代器 指向容器中第一个元素
    // vector<int>::iterator itEnd = v.end();     // 结束迭代器 指向容器中最后一个元素的下一个位置

    // 第一种遍历方式
    // while (itBegin != itEnd)
    // {
    //     printf("%d\n", *itBegin);
    //     itBegin++;
    // }

    // 第二种遍历方式
    // for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    // {
    //     printf("%d\n", *it);
    // }

    // 第三种遍历方式 利用STL提供遍历算法
    for_each(v.begin(), v.end(), myPrint);
}

int main()
{
    test01();
    return 0;
}
```

### 1.3 vector 存放自定义数据类型

---

```c++
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// vector容器中存放自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_Age = age;
    }

    string m_Name;
    int m_Age;
};

void myPrint(Person *p)
{
    cout << "姓名: " << p->m_Name << " 年龄: " << p->m_Age << endl;
}

void test01()
{
    vector<Person> v;
    Person p1("aaa", 10);
    Person p2("bbb", 20);
    Person p3("ccc", 30);
    Person p4("ddd", 40);
    Person p5("eee", 50);

    // 向容器中添加数据
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);
    v.push_back(p5);

    // 遍历容器中的数据
    // for_each(v.begin(), v.end(), myPrint);

    for (vector<Person>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << "姓名: " << it->m_Name << " 年龄: " << it->m_Age << endl;
    }
}

// 存放自定义数据类型的指针
void test02()
{
    vector<Person *> v;
    Person p1("aaa", 10);
    Person p2("bbb", 20);
    Person p3("ccc", 30);
    Person p4("ddd", 40);
    Person p5("eee", 50);

    // 向容器中添加数据
    v.push_back(&p1);
    v.push_back(&p2);
    v.push_back(&p3);
    v.push_back(&p4);
    v.push_back(&p5);

    // 遍历容器中的数据
    // for_each(v.begin(), v.end(), myPrint);

    for (vector<Person *>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << "姓名: " << (*it)->m_Name << " 年龄: " << (*it)->m_Age << endl;
    }
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 1.4 vector 容器嵌套容器

---

```c++
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

void test01()
{
    vector<vector<int>> v;

    // 创建小容器
    vector<int> v1;
    vector<int> v2;
    vector<int> v3;
    vector<int> v4;

    // 向小容器中添加数据
    for (int i = 0; i < 4; i++)
    {
        v1.push_back(i + 1);
        v2.push_back(i + 2);
        v3.push_back(i + 3);
        v4.push_back(i + 4);
        
    }
    // 将小容器插入到大容器中
    v.push_back(v1);
    v.push_back(v2);
    v.push_back(v3);
    v.push_back(v4);

    // 通过大容器，把所有数据 遍历一遍

    for (vector<vector<int>>::iterator it = v.begin(); it < v.end(); it++)
    {
        for (vector<int>::iterator it2 = (*it).begin(); it2 < (*it).end(); it2++)
        {
            cout << *it2 << " ";
        }
        cout << endl;
    }
}

int main()
{
    test01();
    return 0;
}
```

### 2.1 String 容器 String 构造函数

---

*string*是 C++风格字符串，本质是类

与 char \*区别

- char \* 是一个指针
- string 是一个类，类内部封装了 char \*，管理这个字符串，**是一个 char \*的容器**

特点

string 类内部**封装很多成员方法**

- _查找 find,拷贝 copy,删除 delete，替换 replace，插入 insert_
- 管理 char \*所分配的内存，不用担心复制越界和取值越界等，由类内部进行管理

**String 构造函数**

- `String()`无参构造
- `String(const char *s)`有参构造，传入 c 语言字符串
- `String(const string &str)`拷贝构造
- `String(int n, char c)`利用 n 个 c 字符初始化

```c++
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

// string的构造函数

/*
String()无参构造
String(const char *s)有参构造，传入c语言字符串
String(const string &str)拷贝构造
String(int n, char c)利用n个c字符初始化
*/

void test01()
{
    string s1; // 默认构造
    const char *str = "hello world";
    string s2(str);
    cout << "s2 = " << s2 << endl;

    string s3(s2);
    cout << "s3 = " << s3 << endl;

    string s4(10, 'a');
    cout << "s4 = " << s4 << endl;
}

int main()
{
    test01();
    return 0;
}
```

### 2.2 String 赋值操作

---

赋值的函数原型：

- `string& operator=(const char* s);` //char\*类型字符串 赋值给当前的字符串
- `string& operator=(const string &s);` //把字符串 s 赋给当前的字符串
- `string& operator=(char c);` //字符赋值给当前的字符串
- `string& assign(const char *s);` //把字符串 s 赋给当前的字符串
- `string& assign(const char *s, int n);` //把字符串 s 的前 n 个字符赋给当前的字符串
- `string& assign(const string &s);` //把字符串 s 赋给当前字符串
- `string& assign(int n, char c);` //用 n 个字符 c 赋给当前字符串

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// string赋值操作
/*
string& operator=(const char* s); //char*类型字符串 赋值给当前的字符串
string& operator=(const string &s); //把字符串s赋给当前的字符串
string& operator=(char c); //字符赋值给当前的字符串
string& assign(const char *s); //把字符串s赋给当前的字符串
string& assign(const char *s, int n); //把字符串s的前n个字符赋给当前的字符串
string& assign(const string &s); //把字符串s赋给当前字符串
string& assign(int n, char c); //用n个字符c赋给当前字符串
*/

void test01()
{
    string str1;
    str1 = "hello world";
    cout << "str1 = " << str1 << endl;

    string str2;
    str2 = str1;
    cout << "str2 = " << str2 << endl;

    string str3;
    str3 = 'a';
    cout << "str3 = " << str3 << endl;

    string str4;
    str4.assign("hello C++");
    cout << "str4 = " << str4 << endl;

    string str5;
    str5.assign("hello C++", 5);
    cout << "str5 = " << str5 << endl;

    string str6;
    str6.assign(str5);
    cout << "str6 = " << str6 << endl;

    string str7;
    str7.assign(10, 'w');
    cout << "str7 = " << str7 << endl;
}

int main()
{
    test01();
    return 0;
}
```

_一般用等号的方式_

### 2.3 string 字符串拼接

---

字符串拼接函数原型

- `string& operator+=(const char* str);` //重载+=操作符
- `string& operator+=(const char c);` //重载+=操作符
- `string& operator+=(const string& str);` //重载+=操作符
- `string& append(const char *s); ` //把字符串 s 连接到当前字符串结尾
- `string& append(const char *s, int n);` //把字符串 s 的前 n 个字符连接到当前字符串结尾
- `string& append(const string &s);` //同 operator+=(const string& str)
- `string& append(const string &s, int pos, int n);`//字符串 s 中从 pos 开始的 n 个字符连接到字符串结尾

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// string字符串拼接
/*
string& operator+=(const char* str); //重载+=操作符
string& operator+=(const char c); //重载+=操作符
string& operator+=(const string& str); //重载+=操作符
string& append(const char *s); //把字符串s连接到当前字符串结尾
string& append(const char *s, int n); //把字符串s的前n个字符连接到当前字符串结尾
string& append(const string &s); //同operator+=(const string& str)
string& append(const string &s, int pos, int n);//字符串s中从pos开始的n个字符连接到字符串结尾
*/

void test01()
{
    string str1 = "我";
    str1 += "爱玩游戏";
    cout << "str1 = " << str1 << endl;

    str1 += ':';
    cout << "str1 = " << str1 << endl;

    string str2 = "LOL DNF";
    str1 += str2;
    cout << "str1 = " << str1 << endl;

    string str3 = "I";
    str3.append(" love ");
    cout << "str3 = " << str3 << endl;

    str3.append("game abcde", 4);
    cout << "str3 = " << str3 << endl;

    // str3.append(str2);
    // cout << "str3 = " << str3 << endl;

    // str3.append(str2, 0, 3); // 只截取到LOL
    str3.append(str2, 4, 3); // 只截取到DNF 参数2是从哪个位置开始截，参数3是截取字符个数
    cout << "str3 = " << str3 << endl;
}

int main()
{
    test01();
    return 0;
}
```

### 2.4 string 查找和替换

---

- 查找 查找字符串是否存在
- 替换 在指定的位置替换字符串

查找和替换函数原型

- `int find(const string& str, int pos = 0) const;` //查找 str 第一次出现位置,从 pos 开始查找
- `int find(const char* s, int pos = 0) const; ` //查找 s 第一次出现位置,从 pos 开始查找
- `int find(const char* s, int pos, int n) const; ` //从 pos 位置查找 s 的前 n 个字符第一次位置
- `int find(const char c, int pos = 0) const; ` //查找字符 c 第一次出现位置
- `int rfind(const string& str, int pos = npos) const;` //查找 str 最后一次位置,从 pos 开始查找
- `int rfind(const char* s, int pos = npos) const;` //查找 s 最后一次出现位置,从 pos 开始查找
- `int rfind(const char* s, int pos, int n) const;` //从 pos 查找 s 的前 n 个字符最后一次位置
- `int rfind(const char c, int pos = 0) const;  ` //查找字符 c 最后一次出现位置
- `string& replace(int pos, int n, const string& str); ` //替换从 pos 开始 n 个字符为字符串 str
- `string& replace(int pos, int n,const char* s); ` //替换从 pos 开始的 n 个字符为字符串 s

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 字符串查找和替换
/*
int find(const string& str, int pos = 0) const; //查找str第一次出现位置,从pos开始查找
int find(const char* s, int pos = 0) const; //查找s第一次出现位置,从pos开始查找
int find(const char* s, int pos, int n) const; //从pos位置查找s的前n个字符第一次位置
int find(const char c, int pos = 0) const; //查找字符c第一次出现位置
int rfind(const string& str, int pos = npos) const; //查找str最后一次位置,从pos开始查找
int rfind(const char* s, int pos = npos) const; //查找s最后一次出现位置,从pos开始查找
int rfind(const char* s, int pos, int n) const; //从pos查找s的前n个字符最后一次位置
int rfind(const char c, int pos = 0) const; //查找字符c最后一次出现位置
string& replace(int pos, int n, const string& str); //替换从pos开始n个字符为字符串str
string& replace(int pos, int n,const char* s); //替换从pos开始的n个字符为字符串s
*/

// 1、查找

void test01()
{
    string str1 = "abcdefgde";

    int pos = str1.find("de");

    if (pos == -1)
    {
        cout << "未找到字符串" << endl;
    }
    else
    {
        cout << "找到字符串，pos = " << pos << endl;
    }

    // rfind 和 find 区别
    // rfind从右往左查找，find从左往右查找
    pos = str1.rfind("de");
    cout << "pos = " << pos << endl;
}
// 2、替换
void test02()
{
    string str1 = "abcdefg";
    // 从1号位置起 3个字符 替换为1111
    str1.replace(1, 3, "1111");
    cout << "str1 = " << str1 << endl;
}
int main()
{
    test01();
    test02();
    return 0;
}
```

### 2.5 string 字符串比较

---

_按照字符串的 ASCII 码,逐个比较，直到不同_

字符串比较函数原型

- `int compare(const string &s) const; ` //与字符串 s 比较
- `int compare(const char *s) const;` //与字符串 s 比较

= 返回 0

\> 返回 1

< 返回 -1

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 字符串比较操作
/*
int compare(const string &s) const; //与字符串s比较
int compare(const char *s) const; //与字符串s比较
*/

void test01()
{
    string str1 = "hello";
    string str2 = "xello";
    if (str1.compare(str2) == 0)
    {
        cout << "str1 等于 str2" << endl;
    }
    else if (str1.compare(str2) > 0)
    {
        cout << "str1 大于 str2" << endl;
    }
    else if (str1.compare(str2) < 0)
    {
        cout << "str1 小于 str2" << endl;
    }
}

int main()
{
    test01();
    return 0;
}
```

### 2.6 string 字符存取

---

字符存取函数原型

- `char& operator[](int n); ` //通过[]方式取字符
- `char& at(int n);   ` //通过 at 方法获取字符

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// string 字符存取操作
/*
char& operator[](int n); //通过[]方式取字符
char& at(int n); //通过at方法获取字符
*/

void test01()
{
    string str = "hello";

    // cout << "str = " << str << endl;

    // 1、通过[]访问单个字符
    for (int i = 0; i < str.size(); i++)
    {
        cout << str[i] << " ";
    }
    cout << endl;

    // 2、通过at方式访问单个
    for (int i = 0; i < str.size(); i++)
    {
        cout << str.at(i) << " ";
    }
    cout << endl;

    // 修改单个字符
    str[0] = 'x';
    cout << "str = " << str << endl;

    str.at(1) = 'x';
    cout << "str = " << str << endl;
}

int main()
{
    test01();
    return 0;
}
```

### 2.7 string 插入和删除

---

插入和删除函数原型

- `string& insert(int pos, const char* s);  ` //插入字符串
- `string& insert(int pos, const string& str); ` //插入字符串
- `string& insert(int pos, int n, char c);` //在指定位置插入 n 个字符 c
- `string& erase(int pos, int n = npos);` //删除从 Pos 开始的 n 个字符

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// 字符串的插入和删除
/*
string& insert(int pos, const char* s); //插入字符串
string& insert(int pos, const string& str); //插入字符串
string& insert(int pos, int n, char c); //在指定位置插入n个字符c
string& erase(int pos, int n = npos); //删除从Pos开始的n个字符
*/

void test01()
{
    string str = "hello";

    // 插入
    str.insert(1, "111");
    cout << "str = " << str << endl;

    // 删除
    str.erase(1, 3);
    cout << "str = " << str << endl;
}

int main()
{
    test01();
    return 0;
}
```

### 2.8 string 子串获取

子串获取函数原型

- `string substr(int pos = 0, int n = npos) const;` //返回由 pos 开始的 n 个字符组成的字符串

```c++
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

// string求子串
/*
string substr(int pos = 0, int n = npos) const; //返回由pos开始的n个字符组成的字符串
*/

void test01()
{
    string str = "abcdef";
    string subStr = str.substr(1, 3);

    cout << "subStr = " << subStr << endl;
}

// 实用操作
void test02()
{
    string email = "lisi@sina.com";

    // 从邮件的地址获取用户名信息
    int pos = email.find("@");
    string usrName = email.substr(0, pos);
    cout << "id = " << usrName << endl;
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 3.1 vector 容器构造函数

---

**vector**

_与数组行为类似，称为单端数组_
_不同的是可以动态扩展_
_找更大的空间，将原数据拷贝，释放原空间_

**前端封闭，支持尾插和尾删**

**常用迭代器**
`v.begin()`
`v.end()`

_vector 迭代器支持随机访问_

**构造函数**

构造函数原型

- `vector<T> v; ` //采用模板实现类实现，默认构造函数
- `vector(v.begin(), v.end());   ` //将 v[begin(), end())区间中的元素拷贝给本身。
- `vector(n, elem);` //构造函数将 n 个 elem 拷贝给本身。
- `vector(const vector &vec);` //拷贝构造函数。

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

/*
 * `vector<T> v; `               		     //采用模板实现类实现，默认构造函数
 * `vector(v.begin(), v.end());   `       //将v[begin(), end())区间中的元素拷贝给本身。
 * `vector(n, elem);`                            //构造函数将n个elem拷贝给本身。
 * `vector(const vector &vec);`         //拷贝构造函数。
 */

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<int> v1; // 默认构造 无参构造
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    printVec(v1);

    // 通过区间方式构造
    vector<int> v2(v1.begin(), v1.end());
    printVec(v2);

    // n个elem方式构造
    vector<int> v3(10, 100);
    printVec(v3);

    // 拷贝构造
    vector<int> v4(v3);
    printVec(v4);
    return 0;
}
```

### 3.2 vector 容器赋值操作

---

赋值函数原型

- `vector& operator=(const vector &vec);`//重载等号操作符

- `assign(beg, end);` //将[beg, end)区间中的数据拷贝赋值给本身。
- `assign(n, elem);` //将 n 个 elem 拷贝赋值给本身。

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

/*
 vector& operator=(const vector &vec);//重载等号操作符

assign(beg, end); //将[beg, end)区间中的数据拷贝赋值给本身。

assign(n, elem); //将n个elem拷贝赋值给本身。
 */

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<int> v1;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    printVec(v1);

    // 赋值
    vector<int> v2 = v1;
    printVec(v2);

    vector<int> v3;
    v3.assign(v1.begin(), v1.end());
    printVec(v3);

    vector<int> v4;
    v4.assign(10, 100);
    printVec(v4);
    return 0;
}
```

### 3.3 vector 容器大小

---

容器大小函数原型

- `empty(); ` //判断容器是否为空

- `capacity();` //容器的容量

- `size();` //返回容器中元素的个数

- `resize(int num);` //重新指定容器的长度为 num，若容器变长，则以默认值填充新位置。

  ​ //如果容器变短，则末尾超出容器长度的元素被删除。

- `resize(int num, elem);` //重新指定容器的长度为 num，若容器变长，则以 elem 值填充新位置。

  ​ //如果容器变短，则末尾超出容器长度的元素被删除

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// vector容器的容量和大小操作
/*
empty();  //判断容器是否为空

capacity(); //容器的容量

size(); //返回容器中元素的个数

resize(int num); //重新指定容器的长度为num，若容器变长，则以默认值填充新位置。

​ //如果容器变短，则末尾超出容器长度的元素被删除。

resize(int num, elem); //重新指定容器的长度为num，若容器变长，则以elem值填充新位置。

​ //如果容器变短，则末尾超出容器长度的元素被删除
*/

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<int> v1;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    printVec(v1);
    if (v1.empty()) // 为真，代表容器为空
    {
        cout << "v1为空" << endl;
    }
    else
    {
        cout << "v1不为空" << endl;
        cout << "v1的容量为" << v1.capacity() << endl;
        cout << "v1的大小为" << v1.size() << endl;
        v1.resize(17, 100); // 利用重载版本，可以指定默认的填充值
        printVec(v1);       // 如果重新指定的比原来长了，默认用0填充新的位置
        cout << "v1的容量为" << v1.capacity() << endl;
        v1.resize(5);
        printVec(v1); // 如果重新指定的比原来短了，超出部分会删除掉
        cout << "v1的容量为" << v1.capacity() << endl;
    }
    return 0;
}
```

### 3.4 vector 插入删除

---

插入删除函数原型

- `push_back(ele);` //尾部插入元素 ele
- `pop_back();` //删除最后一个元素
- `insert(const_iterator pos, ele);` //迭代器指向位置 pos 插入元素 ele
- `insert(const_iterator pos, int count,ele);`//迭代器指向位置 pos 插入 count 个元素 ele
- `erase(const_iterator pos);` //删除迭代器指向的元素
- `erase(const_iterator start, const_iterator end);`//删除迭代器从 start 到 end 之间的元素
- `clear();` //删除容器中所有元素

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// vector容器插入和删除
/*
push_back(ele); //尾部插入元素ele
pop_back(); //删除最后一个元素
insert(const_iterator pos, ele); //迭代器指向位置pos插入元素ele
insert(const_iterator pos, int count,ele);//迭代器指向位置pos插入count个元素ele
erase(const_iterator pos); //删除迭代器指向的元素
erase(const_iterator start, const_iterator end);//删除迭代器从start到end之间的元素
clear(); //删除容器中所有元素
*/

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<int> v1;
    // 尾插
    v1.push_back(10);
    v1.push_back(20);
    v1.push_back(30);
    v1.push_back(40);
    v1.push_back(50);

    // 遍历
    printVec(v1);

    // 尾删
    v1.pop_back();
    printVec(v1);

    // 插入
    v1.insert(v1.begin(), 100); // 第一个参数是迭代器
    printVec(v1);

    v1.insert(v1.begin(), 2, 1000);
    printVec(v1);

    // 删除 参数也是迭代器
    v1.erase(v1.begin());
    printVec(v1);

    // 情况
    // v1.erase(v1.begin(), v1.end());
    v1.clear();
    printVec(v1);
    return 0;
}
```

### 3.5 vector 数据存取

---

数据存取函数原型

- `at(int idx); ` //返回索引 idx 所指的数据
- `operator[]; ` //返回索引 idx 所指的数据
- `front(); ` //返回容器中第一个数据元素
- `back();` //返回容器中最后一个数据元素

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// vector容器 数据存取
/*
 * `at(int idx); `     //返回索引idx所指的数据
 * `operator[]; `       //返回索引idx所指的数据
 * `front(); `            //返回容器中第一个数据元素
 * `back();`              //返回容器中最后一个数据元素
 */

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<int> v1;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    // 利用[]方式访问数组中的元素
    for (int i = 0; i < v1.size(); i++)
    {
        cout << v1[i] << " ";
    }
    cout << endl;

    // 利用at方式访问元素
    for (int i = 0; i < 10; i++)
    {
        cout << v1.at(i) << " ";
    }
    cout << endl;

    // 获取第一个元素
    cout << "第一个元素为： " << v1.front() << endl;

    // 获取最后一个元素
    cout << "最后一个元素为： " << v1.back() << endl;
    return 0;
}
```

### 3.6 vector 互换容器

---

互换容器函数原型

- `swap(vec);` // 将 vec 与本身的元素互换

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// vector容器 互换
/*
swap(vec); // 将vec与本身的元素互换 * `at(int idx); `     //返回索引idx所指的数据
 */

// 1、基本使用
void test01()
{
    vector<int> v1;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }

    cout << "交换前" << endl;
    printVec(v1);

    vector<int> v2;
    for (int i = 10; i > 0; i--)
    {
        v2.push_back(i);
    }

    printVec(v2);

    cout << "交换后" << endl;
    v1.swap(v2);
    printVec(v1);
    printVec(v2);
}

// 2、实际用途
// 巧用swap可以收缩内存空间
void test02()
{
    vector<int> v;
    for (int i = 0; i < 1e5; i++)
    {
        v.push_back(i);
    }

    cout << "v的容量为： " << v.capacity() << endl;
    cout << "v的大小为： " << v.size() << endl;
    v.resize(3);
    cout << "v的容量为： " << v.capacity() << endl;
    cout << "v的大小为： " << v.size() << endl;

    // 巧用swap收缩内存
    vector<int>(v).swap(v);
    cout << "v的容量为： " << v.capacity() << endl;
    cout << "v的大小为： " << v.size() << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    test02();
    return 0;
}
```

### 3.7 vector 预留空间

---

_减少 vector 在动态扩展容量时的扩展次数_

预留空间函数原型

- `reserve(int len);`//容器预留 len 个元素长度，预留位置不初始化，元素不可访问。

```c++
#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> &v)
{
    for (vector<int>::iterator it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// vector容器 预留空间
/*
reserve(int len);//容器预留len个元素长度，预留位置不初始化，元素不可访问
 */

void test01()
{
    vector<int> v;

    // 利用reserve预留空间
    v.reserve(1e5);
    int num = 0;
    int *p = NULL;
    for (int i = 0; i < 1e5; i++)
    {
        v.push_back(i);

        if (p != &v[0])
        {
            num++;
            p = &v[0];
        }
    }
    cout << "num = " << num << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 4.1 deque 容器构造函数

---

_双向数组，可对头端和尾端进行插入删除操作_

**相比于 vector**

- vector 对于头部插入删除效率低，数据量越大，效率越低
- **deque 相对而言，对头部插入删除效率比 vector 快**
- **vector 访问元素时的速度会比 deque 快**，这和两者内部实现有关

**工作原理**

- **中控器**存储每段缓冲区位置，每段缓冲区存放真实数据。
- 不是一段连续的内存空间
- 其迭代器支持**随机访问**

**deque 容器的构造函数**

构造函数原型

- `deque<T>` deqT; //默认构造形式
- `deque(beg, end);` //构造函数将[beg, end)区间中的元素拷贝给本身。
- `deque(n, elem);` //构造函数将 n 个 elem 拷贝给本身。
- `deque(const deque &deq);` //拷贝构造函数

```c++
#include <iostream>
#include <deque>

using namespace std;

void printDeq(const deque<int> &d)
{
    for (deque<int>::const_iterator it = d.begin(); it < d.end(); it++)
    {
        //*it = 100;  容器中数据不可以修改了
        cout << *it << " ";
    }
    cout << endl;
}

// deque容器 构造函数
/*
deque<T> deqT; //默认构造形式
deque(beg, end); //构造函数将[beg, end)区间中的元素拷贝给本身。
deque(n, elem); //构造函数将n个elem拷贝给本身。
deque(const deque &deq); //拷贝构造函数
 */

void test01()
{
    deque<int> d1;
    for (int i = 0; i < 10; i++)
    {
        d1.push_back(i);
    }
    printDeq(d1);

    deque<int> d2(d1.begin(), d1.end());
    printDeq(d2);

    deque<int> d3(10, 100);
    printDeq(d3);

    deque<int> d4(d3);
    printDeq(d4);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 4.2 deque 容器赋值操作

---

赋值操作函数原型

- `deque& operator=(const deque &deq); ` //重载等号操作符

- `assign(beg, end);` //将[beg, end)区间中的数据拷贝赋值给本身。
- `assign(n, elem);` //将 n 个 elem 拷贝赋值给本身。

```c++
#include <iostream>
#include <deque>

using namespace std;

void printDeq(const deque<int> &d)
{
    for (deque<int>::const_iterator it = d.begin(); it < d.end(); it++)
    {
        //*it = 100;  容器中数据不可以修改了
        cout << *it << " ";
    }
    cout << endl;
}

// deque容器 构赋值操作
/*
deque& operator=(const deque &deq);  //重载等号操作符

assign(beg, end); //将[beg, end)区间中的数据拷贝赋值给本身。

assign(n, elem); //将n个elem拷贝赋值给本身。
 */

void test01()
{
    deque<int> d1;
    for (int i = 0; i < 10; i++)
    {
        d1.push_back(i);
    }
    printDeq(d1);

    deque<int> d2 = d1;
    printDeq(d2);

    deque<int> d3;
    d3.assign(d2.begin(), d2.end());
    printDeq(d3);

    deque<int> d4;
    d4.assign(10, 100);
    printDeq(d4);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 4.3 deque 容器大小

---

- `deque.empty();` //判断容器是否为空

- `deque.size();` //返回容器中元素的个数

- `deque.resize(num);` //重新指定容器的长度为 num,若容器变长，则以默认值填充新位置。

  ​ //如果容器变短，则末尾超出容器长度的元素被删除。

- `deque.resize(num, elem);` //重新指定容器的长度为 num,若容器变长，则以 elem 值填充新位置

```c++
#include <iostream>
#include <deque>

using namespace std;

void printDeq(const deque<int> &d)
{
    for (deque<int>::const_iterator it = d.begin(); it < d.end(); it++)
    {
        //*it = 100;  容器中数据不可以修改了
        cout << *it << " ";
    }
    cout << endl;
}

// deque容器 大小
/*
deque.empty(); //判断容器是否为空

deque.size(); //返回容器中元素的个数

deque.resize(num); //重新指定容器的长度为num,若容器变长，则以默认值填充新位置。

​ //如果容器变短，则末尾超出容器长度的元素被删除。

deque.resize(num, elem); //重新指定容器的长度为num,若容器变长，则以elem值填充新位置
 */

void test01()
{
    deque<int> d1;
    for (int i = 0; i < 10; i++)
    {
        d1.push_back(i);
    }
    printDeq(d1);

    if (d1.empty())
    {
        cout << "d1为空" << endl;
    }
    else
    {
        cout << "d1不为空" << endl;
        cout << "d1的大小为： " << d1.size() << endl;
        // deque容器没有容量的概念
    }
    // 重新指定大小
    // d1.resize(15);
    d1.resize(15, 1);
    printDeq(d1);

    d1.resize(5);
    printDeq(d1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 4.4 deque 插入删除

---

插入删除函数原型

两端插入操作：

- `push_back(elem);` //在容器尾部添加一个数据
- `push_front(elem);` //在容器头部插入一个数据
- `pop_back();` //删除容器最后一个数据
- `pop_front();` //删除容器第一个数据

指定位置操作：

- `insert(pos,elem);` //在 pos 位置插入一个 elem 元素的拷贝，返回新数据的位置。

- `insert(pos,n,elem);` //在 pos 位置插入 n 个 elem 数据，无返回值。

- `insert(pos,beg,end);` //在 pos 位置插入[beg,end)区间的数据，无返回值。

- `clear();` //清空容器的所有数据

- `erase(beg,end);` //删除[beg,end)区间的数据，返回下一个数据的位置。

- `erase(pos);` //删除 pos 位置的数据，返回下一个数据的位置。

```c++
#include <iostream>
#include <deque>

using namespace std;

void printDeq(const deque<int> &d)
{
    for (deque<int>::const_iterator it = d.begin(); it < d.end(); it++)
    {
        //*it = 100;  容器中数据不可以修改了
        cout << *it << " ";
    }
    cout << endl;
}

// deque容器 插入删除
/*
两端插入操作：

- `push_back(elem);`          //在容器尾部添加一个数据
- `push_front(elem);`        //在容器头部插入一个数据
- `pop_back();`                   //删除容器最后一个数据
- `pop_front();`                 //删除容器第一个数据

指定位置操作：

* `insert(pos,elem);`         //在pos位置插入一个elem元素的拷贝，返回新数据的位置。

* `insert(pos,n,elem);`     //在pos位置插入n个elem数据，无返回值。

* `insert(pos,beg,end);`    //在pos位置插入[beg,end)区间的数据，无返回值。

* `clear();`                           //清空容器的所有数据

* `erase(beg,end);`             //删除[beg,end)区间的数据，返回下一个数据的位置。

* `erase(pos);`                    //删除pos位置的数据，返回下一个数据的位置。
 */

// 1、两端插入操作
void test01()
{
    deque<int> d1;

    // 尾插
    d1.push_back(10);
    d1.push_back(20);

    // 头插
    d1.push_front(100);
    d1.push_front(200);
    printDeq(d1);

    // 尾删
    d1.pop_back();
    printDeq(d1);

    // 头删
    d1.pop_front();
    printDeq(d1);
}

// 2、指定位置插入
void test02()
{
    deque<int> d1;
    d1.push_back(10);
    d1.push_back(20);
    d1.push_front(100);
    d1.push_front(200);
    // 200 100 10 20
    printDeq(d1);

    // insert 插入
    d1.insert(d1.begin(), 1000);
    // 1000 200 100 10 20
    printDeq(d1);

    d1.insert(d1.begin(), 2, 10000);
    // 10000 10000 1000 200 100 10 20
    printDeq(d1);

    // 按照区间进行插入
    deque<int> d2;
    d2.push_back(1);
    d2.push_back(2);
    d2.push_back(3);

    d1.insert(d1.begin(), d2.begin(), d2.end());
    printDeq(d1);
}

// 3、指定位置删除
void test03()
{
    deque<int> d1;
    d1.push_back(10);
    d1.push_back(20);
    d1.push_front(100);
    d1.push_front(200);
    // 200 100 10 20

    // 删除
    deque<int>::iterator it = d1.begin();
    it++;
    d1.erase(it);
    // 200 10 20
    printDeq(d1);

    // 按区间方式删除
    // d1.erase(d1.begin(), d1.end());

    // 清空
    d1.clear();
    printDeq(d1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    test02();
    test03();
    return 0;
}
```

### 4.5 deque 数据存取

---

数据存取函数原型

- `at(int idx); ` //返回索引 idx 所指的数据
- `operator[]; ` //返回索引 idx 所指的数据
- `front(); ` //返回容器中第一个数据元素
- `back();` //返回容器中最后一个数据元素

```c++
#include <iostream>
#include <deque>

using namespace std;

void printDeq(const deque<int> &d)
{
    for (deque<int>::const_iterator it = d.begin(); it < d.end(); it++)
    {
        //*it = 100;  容器中数据不可以修改了
        cout << *it << " ";
    }
    cout << endl;
}

// deque容器 数据存取
/*
at(int idx);  //返回索引idx所指的数据
operator[];  //返回索引idx所指的数据
front();  //返回容器中第一个数据元素
back(); //返回容器中最后一个数据元素
 */

void test01()
{
    deque<int> d1;
    d1.push_back(10);
    d1.push_back(20);
    d1.push_back(30);
    d1.push_front(100);
    d1.push_front(200);
    d1.push_front(300);

    // 通过[]方式访问元素
    for (int i = 0; i < d1.size(); i++)
    {
        cout << d1[i] << " ";
    }
    cout << endl;

    // 通过at访问元素
    for (int i = 0; i < d1.size(); i++)
    {
        cout << d1.at(i) << " ";
    }
    cout << endl;

    cout << "第一个元素为： " << d1.front() << endl;
    cout << "最后一个元素为： " << d1.back() << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 4.6 deque 排序操作

---

算法

- `sort(iterator beg, iterator end)` //对 beg 和 end 区间内元素进行排序

```c++
#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

void printDeq(const deque<int> &d)
{
    for (deque<int>::const_iterator it = d.begin(); it < d.end(); it++)
    {
        //*it = 100;  容器中数据不可以修改了
        cout << *it << " ";
    }
    cout << endl;
}

// deque容器 排序操作
/*
sort(iterator beg, iterator end) //对beg和end区间内元素进行排序
 */

void test01()
{
    deque<int> d1;
    d1.push_back(10);
    d1.push_back(20);
    d1.push_back(30);
    d1.push_front(100);
    d1.push_front(200);
    d1.push_front(300);
    printDeq(d1);
    // 排序 默认排序规则 从小到大 升序
    // 对于支持随机访问的迭代器的容器，都可以用sort算法直接对其排序
    // vector容器也可以利用 sort进行排序
    sort(d1.begin(), d1.end());
    printDeq(d1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 5.1 stack 容器基本概念

---

_先进后出，只有一个出口_

_不允许有遍历行为，只有栈顶元素可以访问_

_可以判断是否栈空 empty_

_可以返回元素个数 size_

### 5.2 stack 容器常用接口

---

**构造函数**

- `stack<T> stk;` //stack 采用模板类实现， stack 对象的默认构造形式
- `stack(const stack &stk);` //拷贝构造函数

**赋值操作**

- `stack& operator=(const stack &stk);` //重载等号操作符

**数据存取**

- `push(elem);` //向栈顶添加元素
- `pop();` //从栈顶移除第一个元素
- `top(); ` //返回栈顶元素

**大小操作**

- `empty();` //判断堆栈是否为空
- `size(); ` //返回栈的大小

```c++
#include <iostream>
#include <stack>

using namespace std;

// 栈 stack容器常用接口
/*
构造函数

stack<T> stk; //stack采用模板类实现， stack对象的默认构造形式
stack(const stack &stk); //拷贝构造函数

赋值操作

stack& operator=(const stack &stk); //重载等号操作符

数据存取

push(elem); //向栈顶添加元素
pop(); //从栈顶移除第一个元素
top();  //返回栈顶元素

大小操作

empty(); //判断堆栈是否为空
size();  //返回栈的大小
*/

void test01()
{
    // 特点：符合先进后出的数据结构
    stack<int> s;

    // 入栈
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);

    cout << "栈的大小： " << s.size() << endl;

    // 只要栈不为空，查看栈顶并且执行出栈操作
    while (!s.empty())
    {
        // 查看栈顶元素
        cout << s.top() << endl;

        // 出栈
        s.pop();
    }

    cout << "栈的大小： " << s.size() << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 6.1 queue 容器基本概念

---

_队列容器 先进先出_

_只能从一端（队尾）入队，从另一端出队_

_不允许遍历，只有队尾 back 和队头 front 可以访问_

### 6.2 queue 容器常用接口

---

**构造函数**

- `queue<T> que;` //queue 采用模板类实现，queue 对象的默认构造形式
- `queue(const queue &que);` //拷贝构造函数

**赋值操作**

- `queue& operator=(const queue &que);` //重载等号操作符

**数据存取**

- `push(elem);` //往队尾添加元素
- `pop();` //从队头移除第一个元素
- `back();` //返回最后一个元素
- `front(); ` //返回第一个元素

**大小操作**

- `empty();` //判断堆栈是否为空
- `size(); ` //返回栈的大小

```c++
#include <iostream>
#include <queue>
#include <string>

using namespace std;

// 队列 queue容器常用接口
/*
构造函数

queue<T> que; //queue采用模板类实现，queue对象的默认构造形式
queue(const queue &que); //拷贝构造函数
赋值操作

queue& operator=(const queue &que); //重载等号操作符
数据存取

push(elem); //往队尾添加元素
pop(); //从队头移除第一个元素
back(); //返回最后一个元素
front();  //返回第一个元素
大小操作

empty(); //判断堆栈是否为空
size();  //返回栈的大小
*/

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Age = age;
        this->m_Name = name;
    }
    string m_Name;
    int m_Age;
};

void test01()
{
    // 特点：符合先进先出的数据结构
    queue<Person> q;

    // 准备数据
    Person p1("唐僧", 30);
    Person p2("孙悟空", 1000);
    Person p3("猪八戒", 900);
    Person p4("沙僧", 800);

    // 入队
    q.push(p1);
    q.push(p2);
    q.push(p3);
    q.push(p4);
    cout << "队列大小为： " << q.size() << endl;

    // 判断只要队列不为空，查看队头，队尾，出队
    while (!q.empty())
    {
        // 查看队头
        cout << "队头元素 -- 姓名： " << q.front().m_Name << "年龄： " << q.front().m_Age << endl;

        // 查看队尾
        cout << "队尾元素 -- 姓名： " << q.back().m_Name << "年龄： " << q.back().m_Age << endl;

        // 出队
        q.pop();
    }
    cout << "队列大小为： " << q.size() << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 7.1 list 容器基本概念

---

_链表 链式存储_

**链表**

- 由一系列结点构成
- 节点由数据域和指针域构成
- 优点 可以对任意位置快速**添加/插入/删除**元素
- 缺点 容器的**遍历速度**没有数组快
  **占用空间比数组大**

**list 容器**

- list 容器是一个**双向循环**链表
- 迭代器只支持前移后移，是**双向迭代器**
- 插入删除不会造成迭代器失效（与`vector`不同）
- `vector`和`list`最常使用

### 7.2 list 容器构造函数

构造函数原型

- `list<T> lst;` //list 采用采用模板类实现,对象的默认构造形式：
- `list(beg,end);` //构造函数将[beg, end)区间中的元素拷贝给本身。
- `list(n,elem);` //构造函数将 n 个 elem 拷贝给本身。
- `list(const list &lst);` //拷贝构造函数。

```c++
#include <iostream>
#include <list>

using namespace std;

// list链表容器 构造函数
/*
list<T> lst; //list采用采用模板类实现,对象的默认构造形式：
list(beg,end); //构造函数将[beg, end)区间中的元素拷贝给本身。
list(n,elem); //构造函数将n个elem拷贝给本身。
list(const list &lst); //拷贝构造函数。
*/

void printList(const list<int> &L)
{
    for (list<int>::const_iterator it = L.begin(); it != L.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test01()
{
    // 创建list容器
    list<int> L1; // 默认构造

    // 添加数据
    L1.push_back(10);
    L1.push_back(20);
    L1.push_back(30);
    L1.push_back(40);

    // 遍历容器
    printList(L1);

    // 区间方式构造
    list<int> L2(L1.begin(), L1.end());
    printList(L2);

    // 拷贝构造
    list<int> L3(L2);
    printList(L3);

    // n个elem
    list<int> L4(10, 1000);
    printList(L4);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 7.3 list 容器赋值和交换

---

赋值和交换函数原型

- `assign(beg, end);` //将[beg, end)区间中的数据拷贝赋值给本身。
- `assign(n, elem);` //将 n 个 elem 拷贝赋值给本身。
- `list& operator=(const list &lst);` //重载等号操作符
- `swap(lst);` //将 lst 与本身的元素互换。

```c++
#include <iostream>
#include <list>

using namespace std;

// list容器赋值和交换
/*
assign(beg, end); //将[beg, end)区间中的数据拷贝赋值给本身。
assign(n, elem); //将n个elem拷贝赋值给本身。
list& operator=(const list &lst); //重载等号操作符
swap(lst); //将lst与本身的元素互换。
*/

void printList(const list<int> &L)
{
    for (list<int>::const_iterator it = L.begin(); it != L.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// 赋值
void test01()
{
    list<int> L1;

    L1.push_back(10);
    L1.push_back(20);
    L1.push_back(30);
    L1.push_back(40);

    printList(L1);
    list<int> L2 = L1; // operator= 赋值
    printList(L2);

    list<int> L3;
    L3.assign(L2.begin(), L2.end());
    printList(L3);

    list<int> L4;
    L4.assign(10, 100);
    printList(L4);
}

// 交换
void test02()
{
    list<int> L1;

    L1.push_back(10);
    L1.push_back(20);
    L1.push_back(30);
    L1.push_back(40);

    list<int> L2;
    L2.assign(10, 100);

    cout << "交换前： " << endl;
    printList(L1);
    printList(L2);

    cout << "交换后： " << endl;
    L1.swap(L2);
    printList(L1);
    printList(L2);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    test02();
    return 0;
}
```

### 7.4 list 大小操作

---

大小操作函数原型

- `size(); ` //返回容器中元素的个数

- `empty(); ` //判断容器是否为空

- `resize(num);` //重新指定容器的长度为 num，若容器变长，则以默认值填充新位置。如果容器变短，则末尾超出容器长度的元素被删除。

- `resize(num, elem); ` //重新指定容器的长度为 num，若容器变长，则以 elem 值填充新位置。如果容器变短，则末尾超出容器长度的元素被删除。

```c++
#include <iostream>
#include <list>

using namespace std;

// list容器赋值和交换
/*
assign(beg, end); //将[beg, end)区间中的数据拷贝赋值给本身。
assign(n, elem); //将n个elem拷贝赋值给本身。
list& operator=(const list &lst); //重载等号操作符
swap(lst); //将lst与本身的元素互换。
*/

void printList(const list<int> &L)
{
    for (list<int>::const_iterator it = L.begin(); it != L.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// 赋值
void test01()
{
    list<int> L1;
    L1.push_back(10);
    L1.push_back(20);
    L1.push_back(30);
    L1.push_back(40);
    printList(L1);

    // 判断容器是否为空
    if (L1.empty())
    {
        cout << "L1为空" << endl;
    }
    else
    {
        cout << "L1不为空" << endl;
        cout << "L1的元素个数: " << L1.size() << endl;
    }

    // 重新指定大小
    L1.resize(10, 10000);
    printList(L1);

    L1.resize(2);
    printList(L1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 7.5 list 插入删除

插入删除函数原型

- push_back(elem);//在容器尾部加入一个元素
- pop_back();//删除容器中最后一个元素
- push_front(elem);//在容器开头插入一个元素
- pop_front();//从容器开头移除第一个元素
- insert(pos,elem);//在 pos 位置插 elem 元素的拷贝，返回新数据的位置。
- insert(pos,n,elem);//在 pos 位置插入 n 个 elem 数据，无返回值。
- insert(pos,beg,end);//在 pos 位置插入[beg,end)区间的数据，无返回值。
- clear();//移除容器的所有数据
- erase(beg,end);//删除[beg,end)区间的数据，返回下一个数据的位置。
- erase(pos);//删除 pos 位置的数据，返回下一个数据的位置。
- remove(elem);//删除容器中所有与 elem 值匹配的元素。

```c++
#include <iostream>
#include <list>

using namespace std;

// list容器插入删除
/*
push_back(elem);//在容器尾部加入一个元素
pop_back();//删除容器中最后一个元素
push_front(elem);//在容器开头插入一个元素
pop_front();//从容器开头移除第一个元素
insert(pos,elem);//在pos位置插elem元素的拷贝，返回新数据的位置。
insert(pos,n,elem);//在pos位置插入n个elem数据，无返回值。
insert(pos,beg,end);//在pos位置插入[beg,end)区间的数据，无返回值。
clear();//移除容器的所有数据
erase(beg,end);//删除[beg,end)区间的数据，返回下一个数据的位置。
erase(pos);//删除pos位置的数据，返回下一个数据的位置。
remove(elem);//删除容器中所有与elem值匹配的元素。
*/

void printList(const list<int> &L)
{
    for (list<int>::const_iterator it = L.begin(); it != L.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test01()
{
    list<int> L;

    // 尾插
    L.push_back(10);
    L.push_back(20);
    L.push_back(30);

    // 头插
    L.push_front(100);
    L.push_front(200);
    L.push_front(300);

    // 300 200 100 10 20 30
    printList(L);

    // 尾删
    L.pop_back();
    // 300 200 100 10 20
    printList(L);

    // 头删
    L.pop_front();
    // 200 100 10 20
    printList(L);

    // insert插入
    list<int>::iterator it = L.begin();
    it++;
    it++;
    L.insert(it, 1000);
    // 200 100 1000 10 20
    printList(L);

    // 删除
    it = L.begin();
    L.erase(++it);
    // 200 1000 10 20
    printList(L);

    // 移除
    L.push_back(10000);
    L.push_back(10000);
    L.push_back(10000);
    L.push_back(10000);
    L.push_back(10000);
    printList(L);
    L.remove(10000);
    printList(L);

    // 清空
    L.clear();
    printList(L);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 7.6 list 数据存取

数据存取函数原型

- `front();` //返回第一个元素。
- `back();` //返回最后一个元素。

```c++
#include <iostream>
#include <list>

using namespace std;

// list容器数据存取
/*
front(); //返回第一个元素。
back(); //返回最后一个元素。
*/

void printList(const list<int> &L)
{
    for (list<int>::const_iterator it = L.begin(); it != L.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test01()
{
    list<int> L;
    L.push_back(10);
    L.push_back(20);
    L.push_back(30);
    L.push_back(40);

    // L[0] 不可以用[]的方式访问list容器中的元素
    // L.at(0) 不可以用at的方式访问list容器中的元素
    // 原因是list本质是链表，不是用连续的线性空间存储，迭代器也是不支持随机访问的

    cout << "第一个元素为： " << L.front() << endl;
    cout << "最后一个元素为： " << L.back() << endl;

    // 验证迭代器不支持随机访问
    list<int>::iterator it = L.begin();
    it++; // 支持双向
    it--;
    //it = it + 1; 不支持随机访问
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    return 0;
}
```

### 7.7 list 反转和排序

---

- `reverse();` //反转链表
- `sort();` //链表排序

```c++
#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

// list容器反转和排序
/*
reverse(); //反转链表
sort(); //链表排序
*/

bool myCompare(int v1, int v2)
{
    // 降序 就让第一个数大于第二个数
    return v1 > v2;
}

void printList(const list<int> &L)
{
    for (list<int>::const_iterator it = L.begin(); it != L.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// 反转
void test01()
{
    list<int> L1;

    L1.push_back(20);
    L1.push_back(10);
    L1.push_back(50);
    L1.push_back(40);
    L1.push_back(30);

    cout << "反转前： " << endl;
    printList(L1);

    // 反转
    L1.reverse();
    cout << "反转后： " << endl;
    printList(L1);
}

// 排序
void test02()
{
    list<int> L1;

    L1.push_back(20);
    L1.push_back(10);
    L1.push_back(50);
    L1.push_back(40);
    L1.push_back(30);

    // 排序
    cout << "排序前： " << endl;
    printList(L1);
    // sort(L1.begin(),L1.end()); 所有不支持随机访问迭代器的，不可以用标准算法
    // 所有不支持随机访问迭代器的容器，内部会提供一些算法
    L1.sort();
    cout << "排序后： " << endl;
    printList(L1);
    L1.sort(myCompare);
    printList(L1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    test01();
    test02();
    return 0;
}
```

### 8.1 set 构造和赋值

---

_集合容器_

_关联容器，通过二叉树实现_

_插入时，自动排序_

**set 和 multiset**

- set 不允许容器中有重复元素,而 multiset 允许
- 都是 set 头文件

构造：

- `set<T> st;` //默认构造函数：
- `set(const set &st);` //拷贝构造函数

赋值：

- `set& operator=(const set &st);` //重载等号操作符

```c++
#include <iostream>
#include <set>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// set容器构造和赋值
void test01()
{
    set<int> s1;
    // 插入数据 只有insert方式
    s1.insert(10);
    s1.insert(40);
    s1.insert(20);
    s1.insert(30);
    s1.insert(30);
    // 遍历容器
    printSet(s1);
    // set容器特点: 所有的元素在插入的时候自动被排序
    // set容器重复的值会合并

    // 拷贝构造
    set<int> s2(s1);
    printSet(s2);

    // 赋值
    set<int> s3;
    s3 = s2;
    printSet(s3);
}

int main()
{
    test01();
    return 0;
}
```

### 8.2 set 大小和交换

---

**函数原型：**

- `size();` //返回容器中元素的数目
- `empty();` //判断容器是否为空
- `swap(st);` //交换两个集合容器

```c++
#include <iostream>
#include <set>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// set容器 大小和交换

// 大小
void test01()
{
    set<int> s1;

    // 插入数据
    s1.insert(10);
    s1.insert(20);
    s1.insert(40);
    s1.insert(30);
    // 打印容器
    printSet(s1);

    // 判断是否为空
    if (s1.empty())
    {
        cout << "s1为空" << endl;
    }
    else
    {
        cout << "s1不为空" << endl;
        cout << "s1的大小为: " << s1.size() << endl;
    }
}

// 交换
void test02()
{
    set<int> s1 = {10, 30, 20, 40};
    set<int> s2 = {100, 300, 200, 400};
    cout << "交换前: " << endl;
    printSet(s1);
    printSet(s2);
    s1.swap(s2);
    cout << "交换后: " << endl;
    printSet(s1);
    printSet(s2);
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 8.3 set 插入和删除

---

- `insert(elem);` //在容器中插入元素。
- `clear();` //清除所有元素
- `erase(pos);` //删除 pos 迭代器所指的元素，返回下一个元素的迭代器。
- `erase(beg, end);` //删除区间[beg,end)的所有元素 ，返回下一个元素的迭代器。
- `erase(elem);` //删除容器中值为 elem 的元素。

```c++
#include <iostream>
#include <set>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test01()
{
    set<int> s1;

    // 插入
    s1.insert(10);
    s1.insert(30);
    s1.insert(40);
    s1.insert(20);

    // 遍历
    printSet(s1);

    // 删除
    s1.erase(s1.begin());
    printSet(s1);

    // 删除重载版本
    s1.erase(30);
    printSet(s1);

    // 情况
    // s1.erase(s1.begin(), s1.end());
    s1.clear();
    printSet(s1);
}

int main()
{
    test01();
    return 0;
}
```

### 8.4 set 查找和统计

---

**函数原型：**

- `find(key);` //查找 key 是否存在,若存在，返回该键的元素的迭代器；若不存在，返回 set.end();
- `count(key);` //统计 key 的元素个数 对于 set 只有 01

```c++
#include <iostream>
#include <set>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// set容器的查找和统计

void test01()
{
    // 查找
    set<int> s1;

    // 插入数据
    s1.insert(10);
    s1.insert(30);
    s1.insert(20);
    s1.insert(40);

    set<int>::iterator pos = s1.find(300);

    if (pos != s1.end())
    {
        cout << "找到元素" << *pos << endl;
    }
    else
    {
        cout << "未找到元素" << endl;
    }
}

void test02()
{
    // 统计
    set<int> s1;

    // 插入数据
    s1.insert(10);
    s1.insert(30);
    s1.insert(30);
    s1.insert(30);
    s1.insert(30);
    s1.insert(20);
    s1.insert(40);

    // 统计个数
    int num = s1.count(30);

    cout << "num = " << num << endl;
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 8.5 set 和 multiset

---

- set 在插数据时，会返回结果表示是否成功插入(即重复实际上没有成功插入)
- multiset 允许插入重复数据

```c++
#include <iostream>
#include <set>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// set容器 和 multiset容器的区别

void test01()
{
    set<int> s;
    pair<set<int>::iterator, bool> ret = s.insert(10);

    if (ret.second)
    {
        cout << "第一次插入成功" << endl;
    }
    else
    {
        cout << "第一次插入失败" << endl;
    }

    ret = s.insert(10);

    if (ret.second)
    {
        cout << "第二次插入成功" << endl;
    }
    else
    {
        cout << "第二次插入失败" << endl;
    }

    multiset<int> ms = {10}; // 允许插入重复值

    ms.insert(10);
    ms.insert(10);
    ms.insert(10);

    for (multiset<int>::iterator it = ms.begin(); it != ms.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 8.6 对组 pair

---

_成对出现的一组数据_

**两种创建方式：**

- `pair<type, type> p ( value1, value2 );`
- `pair<type, type> p = make_pair( value1, value2 );`

```c++
#include <iostream>
#include <set>
#include <string>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// 对组pair的创建

void test01()
{
    // 第一种方式
    pair<string, int> p("Tom", 20);

    cout << "姓名: " << p.first << "年龄: " << p.second << endl;

    // 第二种方式
    pair<string, int> p2 = make_pair("Jerry", 30);
    cout << "姓名: " << p2.first << "年龄: " << p.second << endl;
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 8.7 set 排序

---

_默认规则升序，改变规则要用仿函数_

_要在插入数据之前进行指定 使用放仿函数在模版里_

_自定义数据类型一定要指定一个排序规则 注意&和 const 的配合_

```c++
#include <iostream>
#include <set>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// set 容器的排序

class MyCompare
{
public:
    bool operator()(int v1, int v2)
    {
        return v1 > v2;
    }
};

void test01()
{
    set<int> s1;

    s1.insert(10);
    s1.insert(40);
    s1.insert(50);
    s1.insert(20);

    printSet(s1);

    // 指定排序规则为从大到小 要在插入数据之前进行指定 使用放仿函数在模版里
    set<int, MyCompare> s2;

    s2.insert(10);
    s2.insert(40);
    s2.insert(50);
    s2.insert(20);

    for (set<int, MyCompare>::iterator it = s2.begin(); it != s2.end(); it++) // 迭代器也改变
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

```c++
#include <iostream>
#include <set>
#include <string>

using namespace std;

void printSet(set<int> &s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

// set 容器的排序 存放自定义数据类型 需要自己实现排序规则，无法用默认升序排序

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->age = age;
    }
    string m_Name;
    int age;
};

class MyCompare
{

public:
    bool operator()(const Person &p1, const Person &p2) // 这里&一定要有const
    {
        // 按照年龄降序排序
        return p1.age > p2.age;
    }
};

void test01()
{
    set<Person, MyCompare> s;

    // 创建Person对象
    Person p1("刘备", 24);
    Person p2("关羽", 28);
    Person p3("张飞", 25);
    Person p4("赵云", 21);

    s.insert(p1);
    s.insert(p2);
    s.insert(p3);
    s.insert(p4);

    for (set<Person, MyCompare>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << "姓名: " << it->m_Name << "年龄: " << it->age << endl;
    }
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 9.1 map 构造和赋值

_使用率仅次于 vector 和 list_

**基本概念**

- map 中每个元素都是 pair
- pair 中第一个元素为 key 索引键值, 第二个元素为 value 实值
- 所有元素存放时自动根据 key 排序

_map 同样为关联式容器，底层使用二叉树实现_

_快速从大量数据通过 key 找到想要的数据_

**map 和 multimap**

- map 不允许有重复 key 值, 而 multimap 允许

**构造：**

- `map<T1, T2> mp;` //map 默认构造函数:
- `map(const map &mp);` //拷贝构造函数

**赋值：**

- `map& operator=(const map &mp);` //重载等号操作符

```c++
#include <iostream>
#include <map>

using namespace std;

void printMap(map<int, int> m)
{
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

// map容器 构造和赋值

void test01()
{
    // 创建map容器
    map<int, int> m = {pair<int, int>(1, 10)}; // 模版中有两个 键 值

    m.insert(pair<int, int>(3, 30));
    m.insert(pair<int, int>(2, 20));
    m.insert(pair<int, int>(4, 40));

    printMap(m);

    // 拷贝构造
    map<int, int> m2(m);
    printMap(m2);

    // 赋值
    map<int, int> m3;
    m3 = m2;
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 9.2 map 大小和交换

---

函数原型：

- `size();` //返回容器中元素的数目
- `empty();` //判断容器是否为空
- `swap(st);` //交换两个集合容器

```c++
#include <iostream>
#include <map>

using namespace std;

void printMap(map<int, int> m)
{
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

// map容器 大小和交换

void test01()
{
    // 大小
    map<int, int> m;
    m.insert(pair<int, int>(1, 10));
    m.insert(pair<int, int>(2, 20));
    m.insert(pair<int, int>(3, 30));

    if (m.empty())
    {
        cout << "m为空" << endl;
    }
    else
    {
        cout << "m不为空" << endl;
        cout << "m的大小为: " << m.size() << endl;
    }
}

void test02()
{
    // 交换
    map<int, int> m;

    m.insert(pair<int, int>(1, 10));
    m.insert(pair<int, int>(2, 20));
    m.insert(pair<int, int>(3, 30));

    map<int, int> m2;

    m2.insert(pair<int, int>(4, 100));
    m2.insert(pair<int, int>(5, 200));
    m2.insert(pair<int, int>(6, 300));

    cout << "交换前: " << endl;
    printMap(m);
    printMap(m2);

    m.swap(m2);
    cout << "交换后: " << endl;
    printMap(m);
    printMap(m2);
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 9.3 map 插入和删除

---

**函数原型：**

- `insert(elem);` //在容器中插入元素。
- `clear();` //清除所有元素
- `erase(pos);` //删除 pos 迭代器所指的元素，返回下一个元素的迭代器。
- `erase(beg, end);` //删除区间[beg,end)的所有元素 ，返回下一个元素的迭代器。
- `erase(key);` //删除容器中值为 key 的元素。
- `clear()` // 清除

```c++
#include <iostream>
#include <map>

using namespace std;

void printMap(map<int, int> m)
{
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

// map容器 插入和删除

void test01()
{
    map<int, int> m;
    // 插入
    // 第一种
    m.insert(pair<int, int>(1, 10));
    // 第二种
    m.insert(make_pair(1, 10));
    // 第三种
    m.insert(map<int, int>::value_type(3, 30));
    // 第四种
    m[4] = 40; // 4为key 40为value

    // []不建议插入,用途 可以利用key访问到value
    printMap(m);

    // 删除
    m.erase(m.begin());
    printMap(m);

    m.erase(3); // 按照 key 删除
    printMap(m);

    m.erase(m.begin(), m.end()); // 情况
    printMap(m);

    m.clear();
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 9.4 map 查找和统计

---

**函数原型：**

- `find(key);` //查找 key 是否存在,若存在，返回该键的元素的迭代器；若不存在，返回 set.end();
- `count(key);` //统计 key 的元素个数 map 0 1

```c++
#include <iostream>
#include <map>

using namespace std;

void printMap(map<int, int> m)
{
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

// map容器 查找和统计

void test01()
{
    // 查找
    map<int, int> m;
    m.insert(make_pair(1, 10));
    m.insert(make_pair(2, 20));
    m.insert(make_pair(3, 30));
    m.insert(make_pair(3, 40));
    m.insert(make_pair(3, 50));

    map<int, int>::iterator pos = m.find(4);
    if (pos != m.end())
    {
        cout << "查到了元素 key = " << pos->first << " value = " << pos->second << endl;
    }
    else
    {
        cout << "未找到元素" << endl;
    }

    // 统计
    // map不允许插入重复的key元素 故对于count而言 结果为0或1
    // multimap的count结果可能大于1
    int num = m.count(3);
    cout << "num = " << num << endl;
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

### 9.5 map 容器排序

---

_使用仿函数_

```c++
#include <iostream>
#include <map>

using namespace std;

class MyCompare
{

public:
    bool operator()(int m1, int m2)
    {
        return m1 > m2;
    }
};

void printMap(map<int, int> m)
{
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

// map容器 排序

void test01()
{
    map<int, int> m;

    m.insert(make_pair(1, 10));
    m.insert(make_pair(3, 30));
    m.insert(make_pair(2, 20));
    m.insert(make_pair(4, 40));

    printMap(m);

    map<int, int, MyCompare> m2;

    m2.insert(make_pair(1, 10));
    m2.insert(make_pair(3, 30));
    m2.insert(make_pair(2, 20));
    m2.insert(make_pair(4, 40));

    for (map<int, int, MyCompare>::iterator it = m2.begin(); it != m2.end(); it++)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

void test02()
{
}

int main()
{
    test01();
    test02();
    return 0;
}
```

_对于自定义数据类型,同 set_

## 第三章 函数对象

---

**概念**

- 重载函数调用操作符的类，其对象称为函数对象
- 函数对象使用重载的()时，行为类似函数调用，也叫**仿函数**

_本质是一个类，而非函数_

### 1.1 函数对象的使用

---

**特点**

- 函数对象在使用时，可以像普通函数那样调用，可以有参数，可以有返回值
- 函数对象超出普通对象的概念，函数内部可以有自身的状态
- 函数对象可以作为参数传递

```c++
#include <iostream>
#include <string>

using namespace std;

// 函数对象(仿函数)
/*
- 函数对象在使用时，可以像普通函数那样调用，可以有参数，可以有返回值
- 函数对象超出普通对象的概念，函数内部可以有自身的状态
- 函数对象可以作为参数传递
 */

class MyAdd
{
public:
    int operator()(const int &v1, const int &v2)
    {
        return v1 + v2;
    }
};

// 1、函数对象在使用时，可以像普通函数那样调用，可以有参数，可以有返回值
void test01()
{
    MyAdd myAdd;
    cout << myAdd(10, 10) << endl;
}

// 2、函数对象超出普通对象的概念，函数内部可以有自身的状态
class MyPrint
{

public:
    MyPrint()
    {
        this->count = 0;
    }

    void operator()(string text)
    {
        cout << text << endl;
        this->count++;
    }

    int count; // 内部自己的状态
};

void test02()
{
    MyPrint myPrint;
    myPrint("hello world");
    myPrint("hello world");
    myPrint("hello world");
    myPrint("hello world");

    cout << "myPrint调用次数为" << myPrint.count << endl;
}

// 3、函数对象可以作为参数传递

void doPrint(MyPrint &myPrint, string text)
{
    myPrint(text);
}

void test03()
{
    MyPrint myPrint;
    doPrint(myPrint, "Hello C++");
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

### 2.1 一元谓词

---

_谓词 返回布尔类型的伪函数_

_operator()() 接收一个值: 一元谓词_

_operator()() 接收两个值: 二元谓词_

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 谓词 返回值是bool类型的仿函数
// 一元谓词

class GreaterFive
{
public:
    bool operator()(int val)
    {
        return val > 5;
    }
};

void test01()
{
    vector<int> v;
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }

    // 查找容器中 有没有大于5的数字
    // GreaterFive() 无参构造，传入匿名函数对象
    vector<int>::iterator pos = find_if(v.begin(), v.end(), GreaterFive());
    if (pos == v.end())
    {
        cout << "未找到" << endl;
    }
    else
    {
        cout << "找到了大于5的数字为" << *pos << endl;
    }
}

void test02()
{
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

### 2.2 二元谓词

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 谓词 返回值是bool类型的仿函数
// 二元谓词

class MyCompare
{
public:
    bool operator()(int v1, int v2)
    {
        return v1 > v2;
    }
};

void test01()
{
    vector<int> v = {10, 40, 20, 30, 50};
    sort(v.begin(), v.end());
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
    cout << endl;
    // 使用函数对象，改变排序策略,变为从大到小
    sort(v.begin(), v.end(), MyCompare());
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test02()
{
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

### 3.1 内建函数对象 算术仿函数

---

_STL 提供的一些仿函数_

- 使用要包含`#include <functional>`

**算数仿函数** _实现四则运算_

**仿函数原型：**

- `template<class T> T plus<T>` //加法仿函数
- `template<class T> T minus<T>` //减法仿函数
- `template<class T> T multiplies<T>` //乘法仿函数
- `template<class T> T divides<T>` //除法仿函数
- `template<class T> T modulus<T>` //取模仿函数
- `template<class T> T negate<T>` //取反仿函数 一元运算

```c++
#include <iostream>
#include <functional>

using namespace std;

// 内建函数对象 算数仿函数

// negate 一元 取反仿函数
void test01()
{
    negate<int> n;
    cout << n(50) << endl; // -50
}

// plus 二元仿函数 加法
void test02()
{
    plus<int> p;
    cout << p(10, 20) << endl;
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

### 3.2 关系仿函数

---

_实现关系对比_

**仿函数原型：**

- `template<class T> bool equal_to<T>` //等于
- `template<class T> bool not_equal_to<T>` //不等于
- `template<class T> bool greater<T>` //大于 常用
- `template<class T> bool greater_equal<T>` //大于等于
- `template<class T> bool less<T>` //小于
- `template<class T> bool less_equal<T>` //小于等于

```c++
#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>

using namespace std;

// 内建函数对象 关系仿函数
// 大于 greater
void test01()
{
    vector<int> v = {10, 30, 40, 20, 50};
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;

    // 降序
    sort(v.begin(), v.end(), greater<int>());
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test02()
{
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

### 3.3 逻辑仿函数

---

_实现逻辑运算_

**函数原型：**

- `template<class T> bool logical_and<T>` //逻辑与
- `template<class T> bool logical_or<T>` //逻辑或
- `template<class T> bool logical_not<T>` //逻辑非

```c++
#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>

using namespace std;

// 内建函数对象 逻辑仿函数
// 逻辑非 logical_not
void test01()
{
    vector<bool> v = {true, false, true, false};
    for (vector<bool>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
    // 利用逻辑非 将容器v 搬运到 容器v2中，并执行取反操作
    vector<bool> v2;
    v2.resize(v.size()); // 使用transform要提前开辟空间
    transform(v.begin(), v.end(), v2.begin(), logical_not<bool>()); // 最后的参数在搬运过程中的操作
    for (vector<bool>::iterator it = v2.begin(); it != v2.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}

void test02()
{
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

## 第四章 算法

---

**算法头文件**

- `<algorithm>` 所有 STL 头文件中最大的一个,范围涉及到比较，交换，查找，遍历操作，复制，修改等等
- `<numeric>` 体积较小，只包括几个在序列上进行简单数学运算的模版函数
- `<functional>` 定义了一些模版类，用以声明函数对象

### 4.1 遍历算法 for_each

---

**函数原型：**

- `for_each(iterator beg, iterator end, _func);  `

  // 遍历算法 遍历容器元素

  // beg 开始迭代器

  // end 结束迭代器

  // \_func 函数或者函数对象

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// 普通函数
void print01(int val)
{
    cout << val << " ";
}

// 仿函数
class Print02
{
public:
    void operator()(int val)
    {
        cout << val << " ";
    }
};

// 常用遍历算法 for_each()
void test01()
{
    vector<int> v;
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }

    for_each(v.begin(), v.end(), print01);
    cout << endl;
    for_each(v.begin(), v.end(), Print02());
    cout << endl;
}

void test02()
{
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

_常用_

### 4.2 遍历算法 transform

---

_搬运容器到另一个容器_

**函数原型：**

- `transform(iterator beg1, iterator end1, iterator beg2, _func);`

//beg1 源容器开始迭代器

//end1 源容器结束迭代器

//beg2 目标容器开始迭代器

//\_func 函数或者函数对象

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;
vector<int> vTarget;

class Transform
{
public:
    int operator()(int val)
    {
        return val;
    }
};

class MyPrint
{
public:
    void operator()(int val)
    {
        cout << val << " ";
    }
};

// 常用遍历算法 transform()
void test01()
{
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }
    vTarget.resize(v.size()); // 一定要开辟足够空间，否则会崩溃
    transform(v.begin(), v.end(), vTarget.begin(), Transform());
    for_each(vTarget.begin(), vTarget.end(), MyPrint());
}

void test02()
{
}

void test03()
{
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}
```

### 4.3 排序算法 sort

_对容器中元素排序_

**函数原型：**

- `sort(iterator beg, iterator end, _Pred);  `

  // 按值查找元素，找到返回指定位置迭代器，找不到返回结束迭代器位置

  // beg 开始迭代器

  // end 结束迭代器

  // \_Pred 谓词

```c++
#include <bits/stdc++.h>

using namespace std;

class MyPrint
{
public:
    void operator()(int val)
    {
        cout << val << " ";
    }
};

// 常用排序算法 sort

void test01()
{
    vector<int> v;

    v.push_back(10);
    v.push_back(30);
    v.push_back(50);
    v.push_back(20);
    v.push_back(40);

    // 利用sort进行升序
    sort(v.begin(), v.end());
    for_each(v.begin(), v.end(), MyPrint());
    cout << endl;

    sort(v.begin(), v.end(), greater<int>());
    for_each(v.begin(), v.end(), MyPrint());
    cout << endl;
}

int main()
{
    test01();
    return 0;
}
```

### 4.4 排序算法 random_shuffle

_洗牌算法_

_指定范围内元素随机调整次序_

**函数原型：**

- `srand((unsigned int)time(NULL));` 随机数时间种子

* `random_shuffle(iterator beg, iterator end);  `

  // 指定范围内的元素随机调整次序

  // beg 开始迭代器

  // end 结束迭代器

```c++
#include <iostream>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

// 常用排序算法 random_shuffle
void test01()
{
    vector<int> v;
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }
    // 利用洗牌算法打乱顺序 以时间作为种子，否则会出现每次打乱顺序都一样
    srand((unsigned int)time(NULL));
    random_shuffle(v.begin(), v.end());
    for_each(v.begin(), v.end(), [](int val)
             { cout << val << ' '; });
    cout << '\n';
}

int main()
{
    test01();
    return 0;
}
```

### 4.5 排序算法 merge

_归并算法_

_将两个有序容器元素合并，存储到另一容器_

**函数原型：**

- `merge(iterator beg1, iterator end1, iterator beg2, iterator end2, iterator dest);  `

  // 容器元素合并，并存储到另一容器中

  // 注意: 两个容器必须是**有序的**

  // beg1 容器 1 开始迭代器
  // end1 容器 1 结束迭代器
  // beg2 容器 2 开始迭代器
  // end2 容器 2 结束迭代器
  // dest 目标容器开始迭代器

_提前给目标容器分配空间_

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// 常用排序算法 merge
void test01()
{
    vector<int> v1;
    vector<int> v2;

    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
        v2.push_back(i + 1);
    }

    // 目标容器
    vector<int> vTarget;
    // 提前给目标容器分配空间
    vTarget.resize(v1.size() + v2.size());
    merge(v1.begin(), v1.end(), v2.begin(), v2.end(), vTarget.begin());
    for_each(vTarget.begin(), vTarget.end(), [](int val)
             { cout << val << ' '; });
    cout << '\n';
}

int main()
{
    test01();
    return 0;
}
```

### 4.6 排序算法 reverse

_将容器内元素反转_

**函数原型：**

- `reverse(iterator beg, iterator end);  `

  // 反转指定范围的元素

  // beg 开始迭代器

  // end 结束迭代器

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class myPrint
{
public:
    void operator()(int val)
    {
        cout << val << ' ';
    }
};

// 常用排序算法 reverse
void test01()
{
    vector<int> v = {10, 30, 50, 20, 40};
    for_each(v.begin(), v.end(), myPrint());
    cout << '\n';
    reverse(v.begin(), v.end());
    for_each(v.begin(), v.end(), myPrint());
    cout << '\n';
}

int main()
{
    test01();
    return 0;
}
```

### 4.7 查找算法 find

_查找指定元素 找到返回指定元素的迭代器 找不到返回结束迭代器 end()_

**函数原型：**

- `find(iterator beg, iterator end, value);  `

  // 按值查找元素，找到返回指定位置迭代器，找不到返回结束迭代器位置

  // beg 开始迭代器

  // end 结束迭代器

  // value 查找的元素

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_Age = age;
    }
    // 重载 == 底层 find 知道如何对比 Person 数据 ***
    bool operator==(const Person &p)
    {
        return this->m_Age == p.m_Age && this->m_Name == p.m_Name;
    }
    string m_Name;
    int m_Age;
};

// 常用查找算法
// find

// 查找内置数据类型
void test01()
{
    vector<int> v;
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }
    // 查找容器中是否有 5 这个元素
    vector<int>::iterator it = find(v.begin(), v.end(), 5);
    if (it == v.end())
    {
        cout << "没有找到" << '\n';
    }
    else
    {
        cout << "找到：" << *it << '\n';
    }
}

// 查找自定义数据类型
void test02()
{
    vector<Person> v;
    // 创建数据
    Person p1("aaa", 10);
    Person p2("bbb", 20);
    Person p3("ccc", 30);
    Person p4("ddd", 40);
    // 放到容器中
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);

    vector<Person>::iterator it = find(v.begin(), v.end(), p2);
    if (it == v.end())
    {
        cout << "没有找到" << '\n';
    }
    else
    {
        cout << "找到：姓名 " << it->m_Name << " 年龄 " << it->m_Age << '\n';
    }
}
int main()
{
    test01();
    test02();
    return 0;
}
```

_自定义数据类型要重载==(const 引用传参)_

### 4.8 查找算法 find_if

_按条件查找元素_

**函数原型：**

- `find_if(iterator beg, iterator end, _Pred);  `

  // 按值查找元素，找到返回指定位置迭代器，找不到返回结束迭代器位置

  // beg 开始迭代器

  // end 结束迭代器

  // \_Pred 函数或者谓词（返回 bool 类型的仿函数）

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// 常用查找算法
// find_if

// 查找内置数据类型
class GreaterFive
{
public:
    bool operator()(int val)
    {
        return val > 5;
    }
};

void test01()
{
    vector<int> v;
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }
    vector<int>::iterator it = find_if(v.begin(), v.end(), GreaterFive());
    if (it == v.end())
    {
        cout << "没有找到" << '\n';
    }
    else
    {
        cout << "找到大于五的数字为:" << *it << '\n';
    }
}

// 查找自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_age = age;
    }
    string m_Name;
    int m_age;
};

void test02()
{
    vector<Person> v;
    // 创建数据
    Person p1("aaa", 10);
    Person p2("bbb", 20);
    Person p3("ccc", 30);
    Person p4("ddd", 40);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);
    // 找到年龄大于二十的人员
    vector<Person>::iterator it = find_if(v.begin(), v.end(), [](const Person &val)
                                          { return val.m_age > 20; });
    if (it == v.end())
        cout << "没有找到" << '\n';
    else
        cout << "找到: 姓名 " << it->m_Name << " 年龄 " << it->m_age;
}
int main()
{
    test01();
    test02();
    return 0;
}
```

_找到的是第一个符合条件的_

### 4.9 查找算法 adjacent_find

_查找**相邻重复**元素_

**函数原型：**

- `adjacent_find(iterator beg, iterator end);  `

  // 查找相邻重复元素,返回相邻元素的**第一个**位置的迭代器

  // beg 开始迭代器

  // end 结束迭代器

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// 常用查找算法
// adjacent_find

void test01()
{
    vector<int> v;
    v.push_back(0);
    v.push_back(2);
    v.push_back(0);
    v.push_back(3);
    v.push_back(1);
    v.push_back(4);
    v.push_back(3);
    v.push_back(3);
    vector<int>::iterator it = adjacent_find(v.begin(), v.end());
    if (it == v.end())
        cout << "未找到相邻重复元素" << '\n';
    else
        cout << "找到相邻重复元素:" << *it << '\n';
}

// 查找自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_age = age;
    }
    string m_Name;
    int m_age;
};

void test02()
{
}
int main()
{
    test01();
    test02();
    return 0;
}
```

_查找相邻重复自定义类型，提供一个二元谓词，代表两个元素相等_

### 4.10 查找算法 binary_search

_查找指定元素是否存在_

**函数原型：**

- `bool binary_search(iterator beg, iterator end, value);  `

  // 查找指定的元素，查到 返回 true 否则 false

  // 注意: 在**无序序列中不可用**

  // beg 开始迭代器

  // end 结束迭代器

  // value 查找的元素

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// 常用查找算法
// binary_search

void test01()
{
    vector<int> v;
    // 有序序列
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i);
    }
    // 查找容器中是否有9
    if (binary_search(v.begin(), v.end(), 9))
    {
        cout << "找到了元素" << endl;
    }
    else
    {
        cout << "未找到元素" << endl;
    }
}

// 查找自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_age = age;
    }
    string m_Name;
    int m_age;
};

void test02()
{
}
int main()
{
    test01();
    test02();
    return 0;
}
```

_查找自定义类型，提供一个谓词，表示容器的有序规则_

### 4.11 查找算法 count

_统计元素的个数_

**函数原型：**

- `count(iterator beg, iterator end, value);  `

  // 统计元素出现次数

  // beg 开始迭代器

  // end 结束迭代器

  // value 统计的元素

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// 常用查找算法
// count

void test01()
{
    vector<int> v;
    v.push_back(10);
    v.push_back(40);
    v.push_back(30);
    v.push_back(40);
    v.push_back(20);
    v.push_back(40);
    int cnt = count(v.begin(), v.end(), 40);
    cout << "40的元素个数为: " << cnt << '\n';
}

// 查找自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_age = age;
    }
    // 重载 ==  提供给 count 底层 表示何时和待查找数据匹配
    bool operator==(const Person &val)
    {
        return this->m_age == val.m_age;
    }
    string m_Name;
    int m_age;
};

void test02()
{
    vector<Person> v;
    Person p1("刘备", 35);
    Person p2("关羽", 35);
    Person p3("张飞", 35);
    Person p4("赵云", 30);
    Person p5("曹操", 40);

    Person p("诸葛亮", 35);

    // 将人员插入到容器
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);
    v.push_back(p5);

    int cnt = count(v.begin(), v.end(), p);
    cout << "匹配到元素个数: " << cnt << '\n';
}
int main()
{
    test01();
    test02();
    return 0;
}
```

_对于自定义类型的统计，重载==以提供统计规则_

### 4.12 查找算法 count_if

_按条件进行统计_

**函数原型：**

- `count_if(iterator beg, iterator end, _Pred);  `

  // 按条件统计元素出现次数

  // beg 开始迭代器

  // end 结束迭代器

  // \_Pred 谓词

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// 常用查找算法
// count_if

// 统计内置数据类型
void test01()
{
    vector<int> v;
    v.push_back(10);
    v.push_back(40);
    v.push_back(30);
    v.push_back(20);
    v.push_back(40);
    v.push_back(20);
    // 大于二十
    int cnt = count_if(v.begin(), v.end(), [](int val)
                       { return val > 20; });
    cout << "大于二十的元素的个数为： " << cnt << '\n';
}

// 统计自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Name = name;
        this->m_age = age;
    }
    string m_Name;
    int m_age;
};

void test02()
{
    vector<Person> v;
    Person p1("刘备", 35);
    Person p2("关羽", 35);
    Person p3("张飞", 35);
    Person p4("赵云", 40);
    Person p5("曹操", 20);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);
    v.push_back(p5);
    // 统计年龄大于二十
    int cnt = count_if(v.begin(), v.end(), [](const Person &val)
                       { return val.m_age > 20; });
    cout << "年龄大于二十人数: " << cnt << '\n';
}
int main()
{
    test01();
    test02();
    return 0;
}
```

_提供谓词进行统计规则说明_

### 4.13 拷贝算法 copy

**语法**

- `copy(iterator beg, iterator end, iterator dest);  `

  // 按值查找元素，找到返回指定位置迭代器，找不到返回结束迭代器位置

  // beg 开始迭代器

  // end 结束迭代器

  // dest 目标起始迭代器

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 常用拷贝和替换算法 copy

void test01(){
	vector<int> v1;
	for (int i = 0; i < 10; i++){
		v1.push_back(i);
	}
	vector<int> v2;
	// 注意使用 resize 规定容器大小, 而非 reserve 预留空间
	v2.resize(10);
	copy(v1.begin(), v1.end(), v2.begin());
	for_each(v2.begin(), v2.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

*注意利用`resize`使得目标容器足够大*

### 4.14 替换算法 replace

*将容器内**指定值**的旧元素修改为新元素*

**语法**

- `replace(iterator beg, iterator end, oldvalue, newvalue);  `

  // 将区间内旧元素 替换成 新元素

  // beg 开始迭代器

  // end 结束迭代器

  // oldvalue 旧元素

  // newvalue 新元素

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 常用拷贝和替换算法 replace

void test01(){
	vector<int> v = {20, 30, 50, 30, 40, 20, 10, 20};
	cout << "替换前" << '\n';
	for_each(v.begin(), v.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
	cout << "替换后" << '\n';
	replace(v.begin(), v.end(), 20, 2000);
	for_each(v.begin(), v.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

### 4.15 替换算法 replace_if

*按条件替换*

**函数原型：**

- `replace_if(iterator beg, iterator end, _pred, newvalue);  `

  // 按条件替换元素，满足条件的替换成指定元素

  // beg 开始迭代器

  // end 结束迭代器

  // \_pred 谓词

  // newvalue 替换的新元素

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 常用拷贝和替换算法 replace_if

void test01(){
	vector<int> v = {10, 40, 20, 40, 30, 50, 20, 30};
	// 将大于等于 30 替换为 3000
	cout << "替换前" << '\n';
	for_each(v.begin(), v.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
	cout << "替换后" << '\n';
	// 大于等于30 替换为3000 提供谓词
	replace_if(v.begin(), v.end(), [](int val){
		return val >= 30;
	}, 3000);
	for_each(v.begin(), v.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

### 4.16 交换算法 swap

*交换两个**同种类型**容器的元素*

**函数原型：**

- `swap(container c1, container c2);  `

  // 互换两个容器的元素

  // c1 容器 1

  // c2 容器 2

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 常用拷贝和替换算法 swap

void test01(){
	vector<int> v1;
	vector<int> v2;
	for (int i = 0; i < 10; i++){
		v1.push_back(i);
		v2.push_back(i + 100);
	}
	cout << "交换前" << '\n';
	for_each(v1.begin(), v1.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
	for_each(v2.begin(), v2.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
	cout << "交换后" << '\n';
	swap(v1, v2);
	for_each(v1.begin(), v1.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
	for_each(v2.begin(), v2.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

### 4.17 常用算术生成算法 accumulate

*算术生成算法都要包含头文件`#include <numeric>`*

*`accumulate`容器内元素累加求和*

**函数原型：**

- `accumulate(iterator beg, iterator end, value);  `

  // 计算容器元素累计总和

  // beg 开始迭代器

  // end 结束迭代器

  // value 起始值

```c++
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

// 常用拷贝和替换算法 swap

void test01(){
	vector<int> v;
	for(int i = 0; i < 101; i++){
		v.push_back(i);
	}
	// 第三个参数为累加起始值
	int sum = accumulate(v.begin(), v.end(), 0);
	cout << sum << '\n';
}

int main(){
	test01();
	return 0;
}
```

### 4.18 常用算术生成算法 fill

*填充指定元素*

**函数原型：**

- `fill(iterator beg, iterator end, value);  `

  // 向容器中填充元素

  // beg 开始迭代器

  // end 结束迭代器

  // value 填充的值

```c++
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

// 常用拷贝和替换算法 swap

void test01(){
	vector<int> v;
	v.resize(10);
	fill(v.begin(), v.end(), 100);
	for_each(v.begin(), v.end(), [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

*进行后期的填充*

### 4.19 常用集合算法 set_intersection

*求两个容器的交集*

**函数原型：**

- `set_intersection(iterator beg1, iterator end1, iterator beg2, iterator end2, iterator dest);  `

  // 求两个集合的交集

  // **注意:两个集合必须是有序序列**

  // beg1 容器 1 开始迭代器
  // end1 容器 1 结束迭代器
  // beg2 容器 2 开始迭代器
  // end2 容器 2 结束迭代器
  // dest 目标容器开始迭代器

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 集合算法 sett_intersection

void test01(){
	vector<int> v1;
	vector<int> v2;
	for(int i = 0; i < 10; i++){
		v1.push_back(i); // 0 - 9
		v2.push_back(i + 5); // 5 - 14
	}
	vector<int> vTarget;
	// 事先指定容器大小
	vTarget.resize(v1.size() < v2.size() ? v1.size() : v2.size());
    // 求v1和v2的差集
	// 返回迭代器 交集结束的end
	auto itEnd = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), vTarget.begin());
	for_each(vTarget.begin(), itEnd, [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

### 4.19 常用集合算法 set_union

*求两个有序容器的并集*

**函数原型：**

- `set_union(iterator beg1, iterator end1, iterator beg2, iterator end2, iterator dest);  `

  // 求两个集合的并集

  // **注意:两个集合必须是有序序列**

  // beg1 容器 1 开始迭代器
  // end1 容器 1 结束迭代器
  // beg2 容器 2 开始迭代器
  // end2 容器 2 结束迭代器
  // dest 目标容器开始迭代器

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 集合算法 set_union

void test01(){
	vector<int> v1;
	vector<int> v2;
	for(int i = 0; i < 10; i++){
		v1.push_back(i);
		v2.push_back(i + 5);
	}
	vector<int> vTarget;
	vTarget.resize(v1.size() + v2.size());
	// 返回并集元素集合的理论上末迭代器
	auto itEnd = set_union(v1.begin(), v1.end(), v2.begin(), v2.end(), vTarget.begin());
	for_each(vTarget.begin(), itEnd, [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

### 4.20 常用集合算法 set_difference

*求两个有序容器的差集*

**函数原型：**

- `set_difference(iterator beg1, iterator end1, iterator beg2, iterator end2, iterator dest);  `

  // 求两个集合的差集

  // **注意:两个集合必须是有序序列**

  // beg1 容器 1 开始迭代器
  // end1 容器 1 结束迭代器
  // beg2 容器 2 开始迭代器
  // end2 容器 2 结束迭代器
  // dest 目标容器开始迭代器

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 集合算法 set_difference

void test01(){
	vector<int> v1;
	vector<int> v2;
	for(int i = 0; i < 10; i++){
		v1.push_back(i);
		v2.push_back(i + 5);
	}
	vector<int> vTarget;
	vTarget.resize(v1.size());
	// 返回差集元素集合的理论上末迭代器
	auto itEnd = set_difference(v1.begin(), v1.end(), v2.begin(), v2.end(), vTarget.begin());
	for_each(vTarget.begin(), itEnd, [](int val){
		cout << val << ' ';
	});
	cout << '\n';
}

int main(){
	test01();
	return 0;
}
```

## 雜柒雜捌

---

### nth_element 元素归位

_将容器某一位置的元素按照排序后位置归位_

- 复杂度 O(n)

**函数原型**

- `void nth_element(RandomAccessiterator first, RandomAccessIterator nth, RandomAccessIterator last);`
- `void nth_element(RandomAccessIterator first, RandomAccessIterator nth, RandomAccessIterator last, Compare comp);`

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n, tmp;
	cin >> n;
	vector<int> v;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		v.push_back(tmp);
	}
    // 将首元素归位
	nth_element(v.begin(), v.begin(), v.end());
	cout << v.front() << '\n';
	return 0;
}
```

_指定归位元素的排序规则，可以添加一个谓词进行排序_

### setprecision 控制浮点数输出

_需要包含`iomanip`头文件_

- 指定有效数字位数 `cout << setprecision(n) << ..`
- 指定小数点后位数 cout << fixed << setprecision(3) << ..>>``
- 可控制同一输出流 cout 的一整行

```c++
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout << setprecision(2) << 3.2456 << '\n';          // 保留两位有效数字
    cout << fixed << setprecision(2) << 3.2456 << '\n'; // 保留两位小数
    cout << fixed << setprecision(3) << 6.73712 << ' ' << 43.7532 << '\n';
    return 0;
}
```

### tuple 元组

*`pair`的扩展*

*替代一般结构体*

**语法**

* `tuple<..> t = make_tuple(..)`
* `get<0>(元组名)` 可读写

```c++
void test02(){
	tuple<int, int, string> t = make_tuple(18, 99, "小王");
	cout << "我叫" << get<2>(t) << '\n'
	<< "我今年" << get<0>(t) << '\n'
	<< "我考了" << get<1>(t) << '\n'; 
}
```

