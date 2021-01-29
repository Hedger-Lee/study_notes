# crontab定时调度脚本

> 需要脚本可以读取到系统的环境变量

## 解决方法

1.所有命令需要写成绝对路径形式

```
sh  ----> /bin/sh
```

2.在脚本开头添加代码读取环境变量信息

```
#! /bin/sh

. /etc/profile
. ~/.bash_profile
```

3.在/etc/crontab中添加环境变量，在可执行命令之前添加命令，使环境变量生效

```
* * * * * . /etc/profile;/bin/sh /var/www/runjob/test.sh
```

