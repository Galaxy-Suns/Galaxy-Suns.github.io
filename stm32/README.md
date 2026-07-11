## 如何开始

使用 STLINK v2烧录应当将3.3v GND SWDIO SWCLK连接

用 [使用 stm32cubemx](stm32cubemx.md) 中的指南生成初始化代码

后用vscode的`stm32-for-vscode`插件或提取了其功能的脚本`flash-config`脚本

如果使用插件

1. `ctrl-shift-p` 命令 `stm32: build stm32 project` 
2. `ctrl-shift-b` `build flash` 完成烧录

如果使用脚本

1. `flash-config 项目目录` 补充生成相关文件
2. `make flash` 完成烧录

## 参考

[STM32的类别和选用](which_stm32.md) 提供了stm32的一些类别和代码解释

[术语解释](term.md) 解释了一些名词
