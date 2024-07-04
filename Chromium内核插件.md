# Chromium内核插件

https://developer.chrome.com

## 目录结构

* `manifest.json`记录重要的元数据，定义资源，声明权限，并标记哪些文件在后台和页面上运行
* `service worker` 处理和监听浏览器事件（后台持续运行的脚本），可以使用浏览器全部API，但不能和页面内容直接交互
* `content scripts`可以读取和修改DOM元素，但只能使用部分浏览器API
* 插件页面 包括图标和点击后的效果 *popup页面* *options页面：即右键图标后点击选项淡出的页面* 所有页面可以使用全部浏览器API

## 配置 manifest

### 模版

```json
{
    // 必选
  "manifest_version": 3, // 浏览器版本
  "name": "GalaxyDemo", // 插件名称
  "version": "0.0.1", // 插件版本

   // 可选
  "description": "A demo for study.", // 插件描述
  "author": "Galaxy", // 作者名
  "background": { // 后台脚本
    "service_worker": "background.js"
  },
  "options_ui": { // 右键后 选项 显示页面
    "page": "options.html",
    "open_in_tab": true
  },
  "content_scripts": {
    "matches": [
      "*://www.baidu.com/*"
    ],
    "js": [
      "test.js"
    ],
    "all_frames": true,
    "css": []
  },
  "web_accessible_resources": {
    "matches": [
      "*//www.baidu.com/*"
    ],
    "resources": [
      "test.css"
    ]
  },
  "host_permissions": [
    "https://*/*"
  ],
  "permissions": [
    "storage",
    "contextMenus",
    "cookies"
  ],
  "action": {
    "default_icon": {
      "16": "icon16.png",
      "32": "icon32.png",
      "48": "icon48.png",
      "64": "icon64.png",
      "128": "icon128.png"
    },
    "default_popup": "popup.html" 左键显示页面
  },
   "icons": {
      "16": "img/icon.png",
      "32": "img/icon.png",
      "48": "img/icon.png",
      "64": "img/icon.png",
      "128": "img/icon.png"
  }
}
```

### 解析

```json
{
  "manifest_version": 3,
  "name": "GalaxyDemo",
  "version": "0.0.1",


  "description": "A demo for study.",
  "author": "Galaxy",
  "background": {
    "service_worker": "background.js"
  },
  "options_ui": {
    "page": "options.html",
    "open_in_tab": true
  },
  "content_scripts": {
    "matches": [
      "*://www.baidu.com/*"
    ],
    "js": [
      "test.js"
    ],
    "all_frames": true,
    "css": []
  },
  "web_accessible_resources": {
    "matches": [
      "*//www.baidu.com/*"
    ],
    "resources": [
      "test.css"
    ]
  },
  "host_permissions": [
    "https://*/*"
  ],
  "permissions": [
    "storage",
    "contextMenus",
    "cookies"
  ],
  "action": {
    "default_icon": {
      "16": "icon16.png",
      "32": "icon32.png",
      "48": "icon48.png",
      "64": "icon64.png",
      "128": "icon128.png"
    },
    "default_popup": "popup.html"
  },
   "icons": {
      "16": "img/icon.png",
      "32": "img/icon.png",
      "48": "img/icon.png",
      "64": "img/icon.png",
      "128": "img/icon.png"
  }
}
```

## content_scripts 将js，css注入页面

*只能使用部分API*

常用`storage`和`runtime`API

*可以向service worker通过`runtime`, `sendMessage`发送消息*

**content_scripts处于一个孤立的环境中，不会其内部变量影响到页面的变量，同样页面变量也不会影响其自身**

### 静态注入

在`manifest.json`中配置，在匹配的页面上自动注入文件

```json
"content_scripts": {
    "matches": ["https://*.test.com/*"], // 指定次内容脚本被注入到哪些页面
    "css": ["style.css"], // 要注入的css
    "js": ["content.script.js"] // 要注入的js
}
```

### 

