# InfluxDB 

*时序数据库*

* 以时间监控为主要业务的数据库
* 不支持删除和修改
* 主要流程: 采集到数据-发送至InfluxDB-Web UI可视化-监控报警


*下载解压*
```sh
wget https://download.influxdata.com/influxdb/releases/influxdb2-2.0.9-linux-amd64.tar.gz
tar -zxvf influxdb2-2.0.9-linux-amd64.tar.gz  -C /opt/module
```

## bucket 相当于 关系型数据库的database

## InfluxDB行协议

### 协议组成

* 纯文本构成 这种格式的数据才能使用HTTP协议写入数据库
* 每行为一条数据，数据由四部分组成
* `measurement,Tag Set Field Set Timestamp`

#### measurement 测量名称 相当与表名 必须要有

#### Tag Set 标签集 索引的作用 可以省略

* 如果要写使用`,`和`measurement`分隔
* 需要可以枚举，不能超过10w个，且过多影响性能

#### Field Set 字段集 必须要有

* 至少一个
* 多个间`,`分隔
* 前后用空格分隔


#### Timestamp 时间戳 可以省略

* 省略即为插入操作进行时

### 行协议中的数据类型

* 浮点数默认
* 整数 结尾加上标识i
* 无符号整型 标识u
* 字符串 ""
* 布尔值 true/false (t/T/ture/True/TRUE)
* 时间戳
* 注释 #