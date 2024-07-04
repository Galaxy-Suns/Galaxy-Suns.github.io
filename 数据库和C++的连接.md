# 数据库mysql和c++的连接以及操作

## 环境

首先要在**VS**中配置项目环境 教程连接如下

[C/C++连接Mysql数据库  陈子青-See](https://www.bilibili.com/video/BV1m24y1a79o/?spm_id_from=333.1296.top_right_bar_window_default_collection.content.click)

本文参考该视频

## 在mysql中创建需要的表

`cmd`打开控制台

登录操作

```shell
mysql -u root -p
```

输入密码

展示有哪些数据库

```shell
show databases;
```

新建数据库

```shell
create database database_test;

show databases;
```

使用创建的数据库

```shell
use database_test;
```

在数据库中创建表

```shell
create table student(student_id int not null auto_increment primary key,student_name vachar(255) not NULL,class_id varchar(255) not null);
```
其中`int`是整型(数字),`varchar`是字符串，`auto_increment`是自增，`primary key`是主键:对应的唯一存在，用于确定一条数据，因此不可修改。

**自增和主键通常用于编号这种定值。**

在数据库中展示表名

```shell
show tables;
```

添加数据

```shell
insert into students values(10000,'张三','软件工程一班');
```

## 和c++的连接以及数据操作

头文件

```c++
#include<mysql.h>
```

连接操作

```c++

MYSQL* con;
const char* host = "127.0.0.1";
const char* user = "root";
const char* pw = "123456";
const char* database_name = "database_test";
const int port = 3306;

con = mysql_init(NULL);
//设置字符编码
mysql_options(con, MYSQL_SET_CHARSET_NAME, "GBK");

if (!mysql_real_connect(con, host, user, pw, database_name, port, NULL, 0))
{
    std::cout << "Fail to connect" << std::endl;
    exit(1);
}
```

