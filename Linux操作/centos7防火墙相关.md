# centos7防火墙相关

1、查看默认防火墙状态（关闭后显示not running，开启后显示running）

```
[root@localhost ~]# firewall-cmd --state
not running
12
```

2、检查防火墙的状态

```
[root@localhost ~]# systemctl list-unit-files|grep firewalld.service
firewalld.service                             disabled
或者：
[root@localhost ~]# systemctl status firewalld.service
● firewalld.service - firewalld - dynamic firewall daemon
Loaded: loaded (/usr/lib/systemd/system/firewalld.service; disabled; vendor preset: enabled)
Active: inactive (dead)                 --表示防火墙已经关闭
  Docs: man:firewalld(1)
12345678
```

3、开启防火墙

```
[root@localhost ~]#systemctl start firewalld.service       --启动firewall
[root@localhost ~]# systemctl enable firewalld.service     --开机时启动firewall
Created symlink from /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service to /usr/lib/systemd/system/firewalld.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/firewalld.service to /usr/lib/systemd/system/firewalld.service. 
1234
```

4、关闭防火墙：

```
[root@localhost ~]#systemctl stop firewalld.service            --停止firewall
[root@localhost ~]# systemctl disable firewalld.service        --禁止firewall开机启动
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
1234
```

5、重启防火墙

```
[root@localhost ~]# systemctl restart firewalld.service
1
```

6、查看防火墙是否开机自启

```
[root@localhost ~]# systemctl is-enabled firewalld.service;echo $?
enabled             --自启
0
或者：
[root@localhost ~]# systemctl is-enabled firewalld.service;echo $?
disabled                --不自启
1
1234567
```

7、查看已启动的服务列表

```
[root@localhost ~]# systemctl list-unit-files|grep enabled
auditd.service                                      enabled 
autovt@.service                                     enabled 
avahi-daemon.service                                enabled 
crond.service                                       enabled 
12345
```

8、开启端口

```
[root@localhost ~]# firewall-cmd --zone=public --add-port=80/tcp --permanent
success
命令含义：
–zone #作用域
–add-port=80/tcp #添加端口，格式为：端口/通讯协议
–permanent #永久生效，没有此参数重启后失效
123456
```

9、查看已经开放的端口

```
[root@localhost ~]# firewall-cmd --list-port
80/tcp
12
```

10、屏蔽FirewallD服务

```
[root@localhost ~]#systemctl mask firewalld
还可以通过创建一个firewall.service到/dev/null的符号连接来屏蔽防火墙服务。
12
```

11、反屏蔽FirewallD服务

```
[root@localhost ~]#systemctl unmask firewalld
这是反屏蔽FirewallD服务，它会移除屏蔽FirewallD服务时创建的符号链接，故能重新启用服务。
12
```

12、检查是否已安装防火墙

```
[root@localhost ~]#yum install firewalld firewall-config
1
```

13、下面说下CentOS7和6的默认防火墙的区别

CentOS 7默认使用的是firewall作为防火墙，使用iptables必须重新设置一下

1、直接关闭防火墙

```
systemctl stop firewalld.service #停止firewall
systemctl disable firewalld.service #禁止firewall开机启动
12
```

2、设置 iptables service

```
yum -y install iptables-services
1
```

3、如果要修改防火墙配置，如增加防火墙端口3306

```
vi /etc/sysconfig/iptables 
增加规则
-A INPUT -m state --state NEW -m tcp -p tcp --dport 3306 -j ACCEPT
保存退出后
systemctl restart iptables.service #重启防火墙使配置生效
systemctl enable iptables.service #设置防火墙开机启动
123456
```

4、最后重启系统使设置生效即可

```
systemctl start iptables.service #打开防火墙
systemctl stop iptables.service #关闭防火墙
```

