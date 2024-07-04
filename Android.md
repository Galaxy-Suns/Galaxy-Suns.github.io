# Android

**Android Studio的工程目录结构**

*以 FirstApp 工程为例*

> - FirstApp工程目录
> - - app模块
> - - - libs文件夹 用于存放开发使用的架包，so文件等文件
> - - - src 源码存放目录
> - - - - main文件夹 主要用来存放源码的目录
> - - - - - java文件夹
> - - - - - - 多级包名(创建工程时命名)
> - - - - - - - MainActivity 第一个页面的代码
> - - - - - res文件夹 图片资源，布局资源等等资源
> - - - - - AndroidManifest 清单文件 声明权限等
> - - - build gradle 声明版本 包名等等
> - - build gradle 声明一下编译时使用的插件，依赖

**打包apk操作**

>Build -> Bulid Bundle / APK -> Build APK
>success后在app模块下outputs文件夹下debug文件夹的apk文件


**创建内置模拟器**

>Device Manager -> Create Virtual Device
>选择相应分辨率 版本 下载

*点小三角发布到模拟器*

**观察App运行日志**

* log工具
* *Log.e*错误信息
* *Los.w*警告信息
* *Log.i***一般信息**
* *Log.d***调试信息**
* *Log.v*冗余信息

## 壹 UI 控件

### 1.1 TextView

