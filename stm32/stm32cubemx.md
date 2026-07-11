# 使用 stm32cubemx

stm32cubemx 实际生成了初始化的一些配置代码

1. File > New Project

对于第三方产的芯片如`Blue Pill` 从 MCU/MPU Selector > `Commercial Part Number` 搜索型号如 `f103c8t6`

*对于官方的芯片应从 `Board Selector` 中选*

在 `MCUs/MPUs List` 中选到精确的芯片

Start Project

2. Project Manager

Project > Project Name 项目名 也是项目目录名称
Project > Project Location 会将项目目录作为子目录存放在这个位置

Project > Toolchain 默认为`EWARM` 如果想用外部烧录 如`stm32-for-vscode`插件或外部脚本，需要用更通用的`Makefile`

3. Pinout & Configuration

System Core > SYS > Debug 需要改为 `Serial Wire` 开启 SWCLK 和 SWDIO 引脚来使STLINK v2能正常工作

对于需要控制的引脚如 PC13 在 `Pin view` 中可以更改状态，之后可以右键其以添加`User label` 来起别名，会产生define在代码 可以使用别名访问

4. Timers

TIM1 为高级控制定时器
对于PWM等目的 可以选用剩下的 如 TIM2 

Clock Source 选择内部时钟 `Internal Clock`

此时下方的配置中 Configuration > Parameter Settings > Counter Settings 

Prescaler 预分频器 表示多少+1个时钟周期后计时器加1 `0`表示每个时钟周期计时器都加1
Counter Mode 表示向上还是向下计数
Counter Period 计数器计数到最大值后重新开始计数的次数
Internal Clock Division 另一种分频方式

回到上方的 Channal1-4 对于 PWM 可以设置为 `PWM Generation CH1`

底部出现 `PWM Generation Channel 1`

Pulse 脉冲持续时间 影响占空比 `Pulse / Counter Period` 即占空比
CH Polarity Low 则占空比
