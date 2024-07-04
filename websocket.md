# WebSocket

## 流程

**http**

1. 客户端建立连接
2. 客户端发送请求，服务端响应请求
3. 连接关闭

**WebSocket**

1. 客户端建立连接
2. 握手：客户端发送内容，服务端响应特殊内容，验证
3. 数据互发 
4. 断开连接

## 握手

1. 客户端发送随机字符串
2. 服务端在接收到的字符串后追加`magic string`
3. 对拼接后的字符串进行两次加密并响应
4. 客户端验证响应的加密字符串是否和自己进行加密产生的字符串相同，完成握手

## 互发数据时的加密的一些概念

* `payload len`加密后数据的第二个字节的后七位，`payload len`不同，其数据头和数据的长度不同

## Django 使用 WebSocket

### Django 配置 WebSocket

* `Django`默认不支持`WebSocket`, 需要安装第三方组件`channels`

注册channels
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels'
]
```

添加ASGI_APPLICATION
```py
ASGI_APPLICATION = "DjangoWithWebSocket.asgi.get_asgi_application()"
```

修改asgi.py
```py
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWithWebSocket.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(), # 自动找 urls.py -> 找视图函数 
    "WebSocket": URLRouter(routing.websocket_urlpatterns) # routings <=> urls consumers <=> views
})
```

创建routings.py
```py
from django.urls import re_path
from app01 import consumers

websocket_urlpatterns = [
    # xxxx/room/x1 匹配成功
    re_path(r'room/(?P<group>\w)/$', consumers.ChatConsumer.as_asgi())
]
```

创建consumers.py
```py
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import  async_to_sync

class ChatConsumer(WebsocketConsumer): # 继承 WebsocketConsumer
def websocket_connect(self, message):
    # 有客户端向后端发送websocket连接的请求时，自动触发
    self.accept() # 允许与其创建连接
    # raise StopConsumer 不允许创建连接
def websocket_receive(self, message):
    # 浏览器基于websocket向客户端发送数据，自动触发接受消息
    print(message)
    self.send("不要回复") # 回复
    # self.close() 服务端主动断开连接
def websocket_disconnect(self, message):
    # 客户端与服务器断开连接时，自动触发
    print('断开连接')
    raise StopConsumer
```

### wsgi 和 asgi

* wsgi 接收http请求，并交给django做业务请求，只支持同步 
* asgi 支持异步（wsgi + 异步 + websocket）

