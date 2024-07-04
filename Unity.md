# Unity

## 面板

* Project  项目面板，包含了项目里所有的资源文件（图片声音脚本等）
* Console 输出面板 输出警告，错误
* Hierarchy 层次（场景）面板，显示场景中所有游戏对象，并显示父子关系
  * Unity中，游戏有一个个场景构成，游戏对象隶属于各个场景
  * 各个游戏对象有父子关系
* Scene 场景演示面板 实时预览当前场景的游戏对象
* game 游戏演示面板 游戏测试时显示内容
* inspector 检视（属性）面板 选择对象时，检视面板会显示其所有数据，并且可以修改

*ctrl+d 克隆*

## 简单认识组件

* 即有一定功能的组成零件，比如思考，跑步，睡觉

* 游戏对象可以挂载一些组件

* 在`inspector`面板中显示, `Transform`, `Sprite Renderer`等

  ![image-20240530215139505](C:\code\md\img\image-20240530215139505.png)

* `Transform`组件是必须的

* `Sprite Renderer` 精灵渲染器 负责2D图像的渲染



## 控制台输出

```c#
Debug.Log(...);
```

## 坐标系

* 相对于父对象，第一级对象相对于中心

## 脚本

* 在`Assets`文件夹下创建`Scripts`文件夹，然后在其中创建脚本

* 脚本(类)需要作为组件挂载到游戏对象

### Start方法

*游戏开始时第一帧调用一次*

### Update方法

*每一帧调用一次(每秒约60次)*

```c#
public class GhostController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 position = transform.position; //Transform组件 position Vector 3类型(结构体，值类型) 包括x y z三个字段
        position.x += 0.1f; // +f表示单精度
        transform.position = position; // 由于是值类型，不是同一结构体，所以需要赋值回
    }
}
```

### 输入

#### 水平输入

在编辑器`Edit-Input Manager-Axes-Horizontal`设置影响`Horizontal`值（水平输入值）的按键

在脚本中使用

```c#
float inputX = Input.GetAxis("Horizontal");
```

* 输入`negetive`值越久，则`Horizontal`值越趋于-1,

* 输入`possitive`值越久，越趋近于1
* 松开后逐渐趋于0

#### 垂直输入

`Vertical`

### 去除帧率影响

```c#
float Time.deltaTime
```

* `1 / 1s的帧数`
* 在数值后 `* Time.deltaTime` 可以把一帧...->一秒..

### 修改帧率

```c#
Application.targetFrameRate = 10; // 修改为1s10帧
```

## 游戏对象的层级设置

在同一深度下(z轴相同)的渲染规则：

* 按照层级渲染，层级大的在前面
* 在`Sprite Renderer`组件中`Order in Layer`设置

可以在层级相同时，控制y轴高的(低的)在前：

* `Edit-Project Setting-Graphics-Transparency Sort Mode:Custom Axis(自定义)-设置下方的值`

## 父子关系解决渲染，旋转参考点

* 把**显示元素放在不可见父元素的上方，然后操作父元素进行旋转，移动，渲染**
* 这样实际可见元素会依赖其父元素的中心点进行渲染旋转

## 预制体

* 游戏物体投入资源文件夹后，作为预制体
* 改变预制体的属性，可以直接批量改变子体的属性
* 子体上`右键-Prefab-Unpack Completely`断开与预制体的连接

## 刚体组件与碰撞检测

* 组件`Rigidbody 2D`开启2D刚体
  * 将`Gravity Scale`设置为0关闭重力
  * 将`Constraints`的`Freeze Rotation`z轴勾选，关闭由物理引起的绕z轴旋转
* 组件`Box Collider2D`开启2D箱子碰撞
  * 发生碰撞检测需要双方均开启碰撞，且一方开启刚体（一般运动）
* 组件`Polygon Collider 2D`多边形碰撞，用于地图地形设计，可以在一个空游戏对象中使用

### 消除碰撞抖动 - 直接控制刚体位置

* 抖动产生的原因是代码修改了物体的位置，但是物理系统检测到位置异常，又将物体移出
* 修改刚体位置则不会发生抖动

```c#
public class LunaController : MonoBehaviour
{
    private Rigidbody2D rigidbody2d;
    // Start is called before the first frame update
    void Start()
    {
                this.rigidbody2d = this.GetComponent<Rigidbody2D>(); // 组件调用GetComponent<Rigidbody2D>()可以访问到自身游戏对象的其他组件
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 position = transform.position;
        position.x += Input.GetAxis("Horizontal") * Time.deltaTime * 5;
        position.y += Input.GetAxis("Vertical") * Time.deltaTime * 5;
        //transform.position = position;
        this.rigidbody2d.MovePosition(position); // 操作刚体对象，调用方法改变位置
    }
}
```

## 触发器

*用来触发一定功能*

* 双方需要有碰撞组件，且一方有刚体组件

* 勾选一方的`Box Collider 2D`下的`is Trigger`

```c#
// 血条触发器脚本
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class Potion : MonoBehaviour
{
    private void OnTriggerEnter2D(Collider2D collsion) // collsion 碰撞的游戏对象身上的Box Collider2D组件
    {
        LunaController lunaController = collsion.GetComponent<LunaController>();
        lunaController.ChangeHealth(1); // 血量 + 1
    }
}
```

## 动画

* 在**显示的游戏对象上添加**`Animator`组件
* 在`Assets`文件夹下创建`Animations`动画文件夹和`Animators`动画控制器文件夹
* `Animators`文件夹下创建`Animator Controller`控制器
* 在`Animation`面板制作动画(可以制作各种属性)，如果是图片动画选择`Sprite`

### 状态机

* 各个动画右键`Make Transition`设置衔接，**2D不需要过渡**

* 通过**状态机参数**，实现过渡的控制，`Animator`面板中的`Parameters`处添加，在各个连线处设置参数要求

```c#
// 代码中的修改参数
this.animator = this.GetComponent<Animator>(); // 获取状态机
...
// 修改参数
this.animator.SetBool("WalkingLeft", Input.GetAxis("Horizontal") < 0);
this.animator.SetBool("WalkingDown", Input.GetAxis("Vertical") < 0);
```

## 生成游戏物体

```c#
public GameObject effectGo;
...
Instantiate(Instantiate(effectGo, collsion.GetComponent<Transform>().position, Quaternion.identity); // 生成于Luna处，不需要旋转角度);
```

## UI

* 创建`Canvas`游戏对象

*  通常将`Canvas`的`Canvas`组件的`Render Mode`设置为`world space`以当作血条等游戏物体
