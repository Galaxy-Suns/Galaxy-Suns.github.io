# Nginx

## 项目目录 nginx

> client_body_temp  conf  fastcgi_temp  html  logs  proxy_temp  sbin  scgi_temp  uwsgi_temp

```sh
|...
|-- conf
|   |...
|   |-- mime.types 配置头信息
|   |...
|   |-- nginx.conf 主配置文件
|   |...
|...
|-- html
|   |-- 50x.html nginx出现错误后对应的页面
|   `-- index.html 访问成功的页面
|-- logs
|   |-- access.log 访问日志
|   `-- error.log 错误日志
|   |-- nginx.pid 记录 master进程的pid
|...
|-- sbin
|   `-- nginx 二进制可执行文件
|...
```

### conf 中 重要的配置文件

* `mime.types` 
* `nginx.conf` 主配置文件

## nginx启动，停止

### kill -.. PID 信号控制

* 用户通过向`master`进程发送信号，从而管理`worker`进程
* 查看`master` `worker`进程及其PID `ps -ef | grep nginx`
* `kill -信号 masterPID`向master发送信号

**信号表**

* `TERM/INT` 关闭服务
* `QUIT` 优雅的关闭服务（等待执行完再关闭）
* `HUP` 改变重读配置文件并使用服务对新配置项生效（可以在改变配置后不重启服务的方式使配置生效）*其关闭了旧的worker进程，启用了新的*
* `USR1` 重新打开日志文件，可以完成对日志文件的切割
* `USR2` 平滑升级到最新的nginx *其启动了新的master和worker，然后可以再向旧的master发送QUIT*
* `WINCH` 使子进程不再接受新请求，处理后关闭worker进程（但不会关闭master）

### sbin/nginx 命令行控制

```sh
Options:
  -?,-h         : this help
  -v            : show version and exit
  -V            : show version and configure options then exit
  -t            : test configuration and exit # 检测 nginx.conf是否有语法错误
  -T            : test configuration, dump it and exit 
  -q            : suppress non-error messages during configuration testing
  -s signal     : send signal to a master process: stop, quit, reopen, reload 
  # stop -> TERM 
  # quit -> QUIT 
  # reopen -> USR1
  # reload -> HUP
  -p prefix     : set prefix path (default: /usr/local/nginx/)
  -c filename   : set configuration file (default: conf/nginx.conf)
  -g directives : set global directives out of configuration file
./nginx 启动
./
```

## nginx.conf

### 文件结构

* 全局块 设置nginx服务器整体运行的配置指令
* `events`块 配置与用户网络连接相关指令 
* `http`块 内含多个`server`: 与虚拟主机相关配置

### 全局块

#### 推荐配置 user指令 配置运行Nginx服务器worker进程的用户和用户组

* `user 用户名信息=nobody [用户名所属的组=用户名信息]`

* `user www` 可以使得启动运行工作进程的用户及用户组为www，对于不属于自己的目录没有权限访问，对于系统更加安全

#### master_process 指定是否开启工作进程

* `master_process on/off` 默认为 `on` 改成`off`**QUIT重新启动**则不会生成worker进程

#### 推荐配置 worker_processes 配置worker进程的数量 

* worker进程用于处理用户请求
* 理论上越多，处理的工作并发量越多，但需要受到服务器限制
* **一般配置为CPU内核数**
* `worker_processes worker进程数`（前提是master_process默认或者为on）
* 需要`QUIT`重启

#### daemon 设定Nginx是否以守护进程的方式启动

* 守护进程不会随着终端的关闭而停止
* `daemon on/off` 默认为`on`
* 需要`QUIT`重启

#### pid 配置存放Nginx当前master进程pid的文件路径

* `pid file`
* 默认为`usr/local/nginx/logs/nginx.pid`

#### error_log 配置存放Nginx的错误日志路径以及日志级别

* `error_log file [日志级别]`
* `file`默认值为 `logs/error.log`
* `日志级别`默认值`Error`
* `日志级别包括` debug, info, notice, warn, error, crit, alert, emerg 从左到右等级逐渐变高，输出信息越少，输出信息多性能变差，不要设置`info`一下级别

#### include 引入其他配置文件

* `include file`

### events块

#### accept_mutex 设置Nginx网络连接序列化

* `accept_mutex on/off` 默认为`on`
* 常用解决**惊群问题** 
* **惊群问题** 当`accept_mutex` 为 `off`时，用户发送请求，所有worker被激活，竞争处理权，最终只有一个worker处理请求，其余休眠
* 当`accept_mutex`为 `on`，对worker进行序列化，当接受到请求，按顺序激活worker进行处理

#### 推荐配置 multi_accept 设置是否允许同时接收多个网络连接

* `multi_accept on/off` 默认 `off`
* 默认 一个worker只能同一时间处理一个请求
* 实际**建议设置**为`on`

#### worker_connections number 配置单个worker进程的最大连接数

* `worker_connections number` 默认 512
* 不能大于操作系统支持打开最大文件句柄数量

#### 推荐配置 use 选择nginx服务器选择哪种事件驱动来处理网络请求

* nginx多路复用（nginx性能好的原因）的底层实现方式
* `use method`
* `select`, `epoll`, `kqueue`
* 建议linux 2.6以上使用`epoll`

### http块

#### default_type 配置nginx响应前端请求默认的MIME类型

* `default_type mime-type` 默认 `text/plain`文本类型
* `application/json` `text/html` `text/plain`

```nginx
location /get_html {
    default_type text/html;
    return 200 "<h1>This is Nginx's Text</h1>";
}
location /get_json {
    default_type application/json;
    return 200 "{'username': 'TOM', 'age':18}";
}
```

#### 自定义服务日志

* 日志类型分为 `access.log`记录所有用户的访问请求 `error.log`记录本身运行时的错误信息

##### access_log 设置用户访问日志的相关属性

* `access_log path[format[buffer=size]]` 
* `path` 默认值 `logs/access.log`
* `format` 默认值 `combined` 输出日志文件格式名
* `buffer` 输出日志文件大小

##### log_format 指定日志输出格式

* `log_format name [escape=default|json|none] string...`
* `name`默认值 `combined` **注意要和`access_log`的`format`保持一致** 日志输出格式名
* `string` 默认值 ... 具体输出格式

#### 推荐配置 sendfile 设置nginx是否使用sendfile()传输文件

* linux内核中处理静态资源的函数，可以大大提升Nginx处理静态资源的性能
* `sendfile on/off` 默认值 `off`
* **建议设置**为`on`

#### keepalive_timeout 用来设置长连接的超时时间

* http协议是在tcp连接建立后生效，但是tcp协议很耗资源，每一次http发送就要建立一次连接
* 长连接 一次tcp建立后不断开，等待下一次http直接发送
* `keepalive_timeout time` 默认 75s

#### keepalice_requests 设置长连接使用次数

* `keepalice_timeout number` 默认 100

### server块和location块

```nginx
server {
  listen       80; # 监听端口
  server_name  localhost; # 服务名称 ip 域名 
  # 组成访问时url的前半部分

  location / { # 访问时url的后半部分 path部分
    root   /home/www/html; # 资源对应的目录
    index  index.html index.htm; # 访问 / 时 响应的首页 找到第一个为主
  }

  error_page   500 502 503 504 404  /50x.html; # 指定的状态码 返回对应html目录下的页面
  location = /50x.html {
    root   html;
  }
}
```

#### http, server, location块中都设置指令执行的优先级

* 就近原则 最终转发的location最近的指令生效 对应的location>所在server>http

## 配置环境服务和变量，快速启动停止重加载

*存疑，不建议使用*

### 配置系统服务 全局控制nginx启停

> vim /usr/lib/systemd/system/nginx.service
```sh
[Unit]
Description=nginx web service
Documentation=http://nginx.org/en/docs/
After=network.target

[Service]
Type=forking
PIDFile=/usr/local/nginx/logs/nginx.pid
ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf
ExecStart=/usr/local/nginx/sbin/nginx
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/local/nginx/sbin/nginx -s stop
PrivateTmp=true

[Install]
WantedBy=default.target
```

配置后可使用指令

```sh
systemctl start nginx
systemctl status ngixn # 查看状态
systemctl stop nginx
systemctl restart nginx # 重启 （master, worker）
systemctl reload nginx # 重新加载配置 （重启worker）
systemctl enable nginx # 开机自启
```

### 配置系统变量  全局使用nginx .. 指令

> vim /etc/profile

结尾添加 `export PATH=$PATH:/usr/local/nginx/sbin`

> source /etc/profile

> nginx -s reload 此类方式执行nginx

## Nginx 静态资源部署

* 请求后直接返回的部分，而不需要业务处理

### listen指令 监听端口

* 位于 server
* 配置监听端口
* `listen address[:port] [default_server]..` / `listen port [default_server]..`
* 默认 `*:80` 或 `*:8000`
* 常用 `listen 端口号`

*当匹配到端口但是没有匹配到server_name会按照相应端口的第一个server进行匹配（如果listen 8080 default_server会把这个server作为默认的匹配server）*

## ssl

### listen .. ssl 开启ssl监听

### ssl_certificate 为当前虚拟主机指定一个带有PEM格式的证书

* http/server块中
* `ssl_certificate file` 

### ssl_certificate_key 指定PEM secret key 文件的路径

* http/server块中
* `ssl_certificate_key file`

### ssl_session_cache ssl会话缓存

* http, server块中
* `ssl_session_cache ..` 默认值 `none`
* `none`不开启缓存，但客户端可以启用
* `off`禁用缓存
* 。。。


## 反向代理

### proxy_pass 设定处理请求的服务器

* `proxy_pass 服务器`

### proxy_set_header 更改请求头，并发往服务器

* 配置于http, server, location块
* `proxy_set_header field value`
* `field`默认值 Host
* `value`默认值 `$proxt_host`


## Rewrite指令

### rewrite 指令 通过正则表达式匹配并改变url

* 写在server, location, if指令
* 

