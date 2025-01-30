# cmake

通过make来控制c/cpp的编译 需要手动指定一系列相对复杂的依赖关系

cmake可以用相对简洁的语法自动生成这样的`makefile`

cmake默认的配置文件为`CMakeLists.txt`

## 基本的编译过程

```cmake
# cmake 最低版本
cmake_minimum_required(VERSION 3.10)

# 项目名称
project(answer)

# 构建程序需要的源文件 
# 会自动找到 main.cpp 需要的 头文件 无需手动指定
# 这个target名字 是 未来可执行文件的名字
add_executable(answer main.cpp answer.cpp)
```

而编译过程分为两步

生成 构建目录

>cmake -B build

* `-B` 参数 生成一个`makefile`的构建目录 后面是指定生成的目录
* 如果选择其他系统可以`-G`来替代

编译

>cmake --build build

* 传入参数为刚刚生成的目录
* 如果采用`-B` 也可以 `cd`进入目录 来`make`
* 其他`-G`生成的构建系统 也可以使用此命令

之后即可 `./build/answer` 运行

## 静态库

处于复用的目的

现在我们想将`answer.cpp` 抽离为一个静态库

那么可以

```cmake
# STATIC 指示静态
add_library(libanswer STATIC answer.cpp)

# 使用此库的目标 需要连接到此库
target_link_libraries(answer libanswer)
```

而`add_executable` 则不需要`answer.cpp`

```cmake
add_executable(answer main.cpp)
```

## 目录分离

既然我们抽离出了一个静态库 那么可以将其目录和其他分割开来

```shell
├── answerlib
│   ├── answer.cpp
│   ├── CMakeLists.txt
│   └── head
│       └── answer.hpp
├── CMakeLists.txt
└── main.cpp
```

在外部的`CMakeLists.txt`中 我们保留这些

```cmake
cmake_minimum_required(VERSION 3.10)

project(answer)

add_executable(answer main.cpp)

target_link_libraries(answer libanswer)
```

也就是仅仅指定构建目标的源文件 和 依赖库

还要告诉cmake 库的`cmakelists`从哪里找到

```cmake
add_subdirectory(answerlib)
```

在库的`CMakeLists.txt`中


```cmake
# 指定了构建库的源文件
add_library(libanswer STATIC answer.cpp)

# 表示构建目标时额外包含的目录 
# 使得不同目录间 能够 #include "answer.hpp" 这样直接访问到
# 而 PUBLIC 让使用此库 外部目标 也能 这样直接访问到
target_include_directories(libanswer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/head)
``````

## 第三方库

使用第三方库的`CMakeLists.txt`需要找到库 以及链接到库

```cmake
# 在系统中查找此库
# CURL 是 第三方库 提供的名字 查阅相关资料 找到
# REQUIRED 指必须此库 如果没找到则报错
find_package(CURL REQUIRED)

# privte 表示 外部 不能`include`到curl 一种隔离控制
# 这个库的名称查阅资料获得
target_link_libraries(libanswer PRIVATE CURL::libcurl)
```
