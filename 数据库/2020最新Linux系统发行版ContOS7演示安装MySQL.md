# 2020最新Linux系统发行版ContOS7演示安装MySQL

为防止操作权限不足，建议切换root用户，当然如果你对Linux命令熟悉，能够自主完成权限更新操作，可以不考虑此推荐。

## 1、检查安装

　　　登录Linux，命令检查是否已经安装过mysql，执行命令。如果没有任何显示信息，则说明未安装，如果存在信息，则执行卸载。

```
1 [root@localhost ~]# rpm -qa | grep mysql　　　　// 检测系统是否自带安装 MySQL:
2 rpm -e mysql　　　　　　　　// 普通删除模式
3 rpm -e --nodeps mysql　　// 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令可以对其进行强力删除
```

　　实际完成这第一步骤就可以卸载掉MySQL了，直接学习安装即可。当然如果想清除更多卸载残留（更完整的卸载），可以选择第二步骤的方式卸载MySQL。

 

## 2、卸载MySQL

　　当然如果在第一次检测时就没有显示什么，那么这一步可以忽略……

　　1、查看MySQL服务

　　　　登录Linux后执行service mysqld status 或者service mysql status命令查看MySQL服务状态

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 ####命令
 2 [root@localhost ~]# service mysqld status
 3 
 4 ####执行结果：标识没有该服务
 5 Redirecting to /bin/systemctl status mysqld.service
 6 Unit mysqld.service could not be found.
 7 
 8 ####执行结果：标识服务已启动
 9 [root@localhost ~]# service mysqld status
10 Redirecting to /bin/systemctl status mysqld.service
11 ● mysqld.service - MySQL Server
12 Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
13 Active: active (running) since 一 2020-10-19 10:54:07 CST; 2min 1s ago
14 Docs: man:mysqld(8)
15 http://dev.mysql.com/doc/refman/en/using-systemd.html
16 Process: 1563 ExecStart=/usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid $MYSQLD_OPTS (code=exited, status=0/SUCCESS)
17 Process: 1111 ExecStartPre=/usr/bin/mysqld_pre_systemd (code=exited, status=0/SUCCESS)
18 Main PID: 1579 (mysqld)
19 Tasks: 27
20 CGroup: /system.slice/mysqld.service
21 └─1579 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid
22 
23 10月 19 10:53:01 localhost.localdomain systemd[1]: Starting MySQL Server...
24 10月 19 10:54:07 localhost.localdomain systemd[1]: Started MySQL Server.
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　2、关闭MySQL服务（not be found就是没找到服务，则忽略该步骤）　　

　　　　如果MySQL服务正在运行，则执行service mysqld stop或者service mysql stop命令停止MySQL服务

```
1 [root@localhost ~]# service mysql stop
```

　　3、卸载MySQL

```
1 [root@localhost ~]# rpm -e --nodeps mysql　　　　　
```

　　4、查找与MySQL相关的残留目录

　　　　和Windows系统一样，MySQL的卸载不仅仅是卸载程序，也需要删除与程序相关的文件夹。才能保证卸载的完整性！

　　　　使用命令：find  / -name mysql　　或者　　whereis  mysql

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 ####find命令查询：速度会慢点
 2 [root@localhost ~]# find / -name mysql
 3 find: ‘/run/user/1000/gvfs’: 权限不够 4 /usr/lib64/mysql
 5 /usr/share/mysql
 6 
 7 ####whereis命令搜索，速度较快
 8 [root@localhost ~]# whereis mysql
 9 mysql: /usr/lib64/mysql /usr/share/mysql
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　5、删除残留

　　　　删除残留的目录，只删除MySQL目录即可，当前登录的已经是root权限了，find查询的结果对于权限不足的，就无需操作了。

　　　　命令：rm  -rf  目录

```
1 [root@localhost mysql]# rm -rf  /usr/lib64/mysql/
2 [root@localhost mysql]# rm -rf  /usr/share/mysql
```

　　6、删除MySQL配置文件

　　　　执行rm -rf  /etc/my.cnf命令删除/etc/my.cnf文件，执行rm -rf  /etc/init.d/mysqld命令删除/etc/init.d/下跟MySQL有关的全部文件，一般包括mysql文件或mysqld文件，如果存在mysql文件则执行：

　　　　rm  -rf/etc/init.d/mysql命令

```
1 [root@localhost etc]# rm  -rf   /etc/my.cnf
2 [root@localhost etc]# rm  -rf   /etc/init.d/mysqld
```

　　7、删除mysql用户及用户组

　　　　执行id mysql命令查看MySQL用户及用户组，执行userdel mysql命令删除MySQL用户及用户组。

```
1 [root@localhost etc]# id mysql
2 uid=27(mysql) gid=27(mysql) 组=27(mysql)
3 [root@localhost etc]# userdel mysql
```

　　再次执行大标题步骤1的检查安装命令，查看是否存在MySQL程序。

　　和Windows系统一样，MySQL的卸载不仅仅是卸载程序，也需要删除与程序相关的文件夹。才能保证卸载的完整性！

## 3、安装MySQL

　　MySQL的安装分为yum安装、rpm安装。通常大部分使用的MySQL版本是5.X的。本次案例演示使用版本MySQL-5.7

　　(本次测试yum安装)

### 1、YUM安装MySQL

##### 　　1、安装mysql源

　　　　CentOS 7的yum源中默认没有mysql，要先下载mysql的repo源（[点击此处](http://dev.mysql.com/downloads/repo/yum/)）。并安装它！

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1 ######当前使用的是普通用户下载
2 [xsge@localhost downfiles]$ wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
3 
4 ######软件安装需要切换root用户：使用root账户安装yum源
5 [root@localhost downfiles]# rpm -vih mysql80-community-release-el7-3.noarch.rpm
6 警告：mysql80-community-release-el7-3.noarch.rpm: 头V3 DSA/SHA1 Signature, 密钥 ID 5072e1f5: NOKEY
7 准备中... ################################# [100%]
8 正在升级/安装...
9 1:mysql80-community-release-el7-3 ################################# [100%]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　　　yum源的获取方式如下图

　　　　访问MySQL官网——选择downloads——MySQL Community (GPL) Downloads》——MySQL Community Server

　　　　MySQL官网地址：https://www.mysql.com/

　　　　downloads在导航栏一般比较明显。MySQL Community (GPL) Downloads》一般在页面底部考上位置。MySQL Community Server自己找吧

 　　　而后进入界面如下图即可获取yum源：

　　　　![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201016144328140-2075943258.png)

　　　　点击YUM大企鹅后，进入下面的界面：　　

　　　　![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201016145048948-1413759535.png)

 　　　进入下载界面：

　　![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201016150151481-391472699.png)

 　　　我们可以通过以下方法检测是否已经成功安装了yum源：命令：yum repolist enabled | grep "mysql.*-community.*"

```
1 [root@localhost downfiles]# yum repolist enabled | grep "mysql.*-community.*"
2 mysql-connectors-community/x86_64 MySQL Connectors Community                 165
3 mysql-tools-community/x86_64      MySQL Tools Community                      115
4 mysql80-community/x86_64          MySQL 8.0 Community Server                 193
```

#### 　　2、选择安装版本

　　当你使用此方法进行安装MySQL的时候，会默认安装mysql的最新稳定版本（在我现在安装的时候，最新版本为MySQL 8.0 Community Server ）。如果这就是你想要安装的，那么你就可以忽略这步了。如果想要安装以前的版本，比如5.6或者5.5，那么就可以用下面的方法来配置了。

　　首先我们先查看MySQL的那些源被禁用或者启用了。

　　命令：yum repolist all | grep mysql

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 [root@localhost downfiles]# yum repolist all | grep mysql
 2 mysql-cluster-7.5-community/x86_64  MySQL Cluster 7.5 Community     禁用
 3 mysql-cluster-7.5-community-source  MySQL Cluster 7.5 Community - S 禁用
 4 mysql-cluster-7.6-community/x86_64  MySQL Cluster 7.6 Community     禁用
 5 mysql-cluster-7.6-community-source  MySQL Cluster 7.6 Community - S 禁用
 6 mysql-cluster-8.0-community/x86_64  MySQL Cluster 8.0 Community     禁用
 7 mysql-cluster-8.0-community-source  MySQL Cluster 8.0 Community - S 禁用
 8 mysql-connectors-community/x86_64   MySQL Connectors Community      启用:    165
 9 mysql-connectors-community-source   MySQL Connectors Community - So 禁用
10 mysql-tools-community/x86_64        MySQL Tools Community           启用:    115
11 mysql-tools-community-source        MySQL Tools Community - Source  禁用
12 mysql-tools-preview/x86_64          MySQL Tools Preview             禁用
13 mysql-tools-preview-source          MySQL Tools Preview - Source    禁用
14 mysql55-community/x86_64            MySQL 5.5 Community Server      禁用
15 mysql55-community-source            MySQL 5.5 Community Server - So 禁用
16 mysql56-community/x86_64            MySQL 5.6 Community Server      禁用
17 mysql56-community-source            MySQL 5.6 Community Server - So 禁用
18 mysql57-community/x86_64            MySQL 5.7 Community Server      禁用
19 mysql57-community-source            MySQL 5.7 Community Server - So 禁用
20 mysql80-community/x86_64            MySQL 8.0 Community Server      启用:    193
21 mysql80-community-source            MySQL 8.0 Community Server - So 禁用
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　比如我们看到现在启用的是8.0版本系列的。我们需要安装的是5.x系列的。那么我们就可以执行以下命令：

　　命令：

```
1 [root@localhost downfiles]# yum-config-manager --disable mysql80-community　　　　　　 ##禁用8.0版本的
2 [root@localhost downfiles]# yum-config-manager --enable mysql56-community　　　　　　　##启用5.6版本的（当然启用哪个版本你自己定）　
```

> 上面的命令执行如果提示：-bash: yum-config-manager: 未找到命令　
>
> 那么我们就需要安装执行以下命令来安装一个包：yum install -y yum-utils 执行成功之后就好了，那么我们继续执行上面的命令。

　　启用与禁用命令执行成功后，再次查看MySQL的哪些源被禁用：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 [root@localhost downfiles]# yum repolist all | grep mysql
 2 mysql-cluster-7.5-community/x86_64  MySQL Cluster 7.5 Community     禁用
 3 mysql-cluster-7.5-community-source  MySQL Cluster 7.5 Community - S 禁用
 4 mysql-cluster-7.6-community/x86_64  MySQL Cluster 7.6 Community     禁用
 5 mysql-cluster-7.6-community-source  MySQL Cluster 7.6 Community - S 禁用
 6 mysql-cluster-8.0-community/x86_64  MySQL Cluster 8.0 Community     禁用
 7 mysql-cluster-8.0-community-source  MySQL Cluster 8.0 Community - S 禁用
 8 mysql-connectors-community/x86_64   MySQL Connectors Community      启用:    165
 9 mysql-connectors-community-source   MySQL Connectors Community - So 禁用
10 mysql-tools-community/x86_64        MySQL Tools Community           启用:    115
11 mysql-tools-community-source        MySQL Tools Community - Source  禁用
12 mysql-tools-preview/x86_64          MySQL Tools Preview             禁用
13 mysql-tools-preview-source          MySQL Tools Preview - Source    禁用
14 mysql55-community/x86_64            MySQL 5.5 Community Server      禁用
15 mysql55-community-source            MySQL 5.5 Community Server - So 禁用
16 mysql56-community/x86_64            MySQL 5.6 Community Server      禁用
17 mysql56-community-source            MySQL 5.6 Community Server - So 禁用
18 mysql57-community/x86_64            MySQL 5.7 Community Server      启用:    444
19 mysql57-community-source            MySQL 5.7 Community Server - So 禁用
20 mysql80-community/x86_64            MySQL 8.0 Community Server      禁用
21 mysql80-community-source            MySQL 8.0 Community Server - So 禁用
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　好了，这时我们查看当前系统配置，仅显示启用MySQL命令：yum repolist enabled | grep mysql　　

```
1 [root@localhost downfiles]# yum repolist enabled | grep mysql
2 mysql-connectors-community/x86_64 MySQL Connectors Community                 165
3 mysql-tools-community/x86_64      MySQL Tools Community                      115
4 mysql57-community/x86_64          MySQL 5.7 Community Server                 444
```

　　可以开始安装MySQL了。　　

#### 　　3、使用YUM命令安装

　　执行以下命令来安装（当前续接：演示安装MySQL5.7）。安装过程中会自动加载MySQL依赖，提示你是否下载，输入y表示下载

```
1 [root@localhost downfiles]# yum install mysql-community-server
```

![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201016193704880-923421431.png)

####  　4、MySQL命令管理

　　　　安装完成后验证：

```
1 service mysqld start　　　　　　　　#开启MySQL服务　　　　只要没有错误信息就表示已经正常启动了。
2 service mysqld stop　　　　　　　　#关闭MySQL服务
3 service mysqld restart　　　　　　#重启MySQL服务 
4 service mysqld status　　　　　　#查看服务状态
```

#### 　　5、MySQL密码问题

　　　　一些朋友可能发现安装MySQL没有密码设置项的问题，有人说这是因为MySQL不需要密码！这里说明一下，MySQL5.7会在安装后为root用户生成一个随机临时密码。但无论你安装的MySQL是哪个版本，无论使用哪种方式安装，无论是否需要密码登录，始终记住数据库的安全大于一切，所以请设置密码。又有人会问：如果能使用空密码登录，我登录后面再设置密码也行，可是有密码时，我怎么知道默认密码是多少如何登录呢？

　　　　本次安装的MySQL没有设置密码，但系统赋予了***默认的且临时的\***密码，打开mysql默认日志文件/var/log/mysqld.log，可以查看（前提，你刚刚安装好MySQL，且没有重复重启服务）

　　　　MySQL5.7版本以前，安装后的默认密码为空值（即没有密码）。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1 ####打开日志文件查看
2 cat /var/log/mysqld.log
3 
4 或者
5 
6 ####搜索临时密码，在日志文件中定位
7 grep 'temporary password' /var/log/mysqld.log
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201019113042302-861099848.png)

 　　　拿到密码后可以进行登录，但是当我们执行SQL命令时就会报错（提示我们必须先重置密码）

```
1 ####登录mysql
2 [root@localhost ~]# mysql -uroot -pve#LoVkeU2u!
3 
4 ####查看所有库
5 mysql> show databases;
```

![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201019113406528-662679970.png)

 　　　MySQL安装时默认安装了 [validate_password](http://dev.mysql.com/doc/refman/5.7/en/validate-password-plugin.html)，MySQL的密码策略比较复杂。这个插件要求密码至少包含一个大写字母，一个小写字母，一个数字和一个特殊字符，并且密码长度至少8个字符。过于简单的密码，不会被通过。（另请参考下面的附录）

```
1 mysql> set password = password('MySQL5.7');　　　　　　#### 重置MySQL（root）登录密码为MySQL5.7　
2 Query OK, 0 rows affected, 1 warning (0.00 sec)
3 
4 或者如下格式：
5 set password for 用户名@localhost/ip/% = password('新密码'); 
```

#### 　　　6、禁止更新（推荐设置）

　　　　我们在安装之后，为了能够正常运行，我们会禁止MySQL进行更新。因为在yum更新了MySQL之后，MySQL会自动重启，这对于我们上线部署项目来说是没有必要的，所以我们可以屏蔽更新。

　　　　将下列代码放到你的`/etc/yum.conf`文件中即可：

```
1 exclude=mysql-community-client,mysql-community-common,mysql-community-libs,mysql-community-server
```

#### 　　　7、更新MySQL（可选操作）

　　　　如果想更新数据库了怎么办？一般在生产环境，我们都是禁用更新的。所以说，如果需要更新，这里只是作为一个参考。 执行的更新命令即可：

```
1 yum update mysql-server
```

　　　　我们也可以指定更新单个组件。首先我们先运行以下命令来查看MySQL的组件列表：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1 [root@localhost ~]# yum list installed | grep "^mysql"
2 mysql-community-client.x86_64               5.7.31-1.el7               @mysql57-community
3 mysql-community-common.x86_64               5.7.31-1.el7               @mysql57-community
4 mysql-community-libs.x86_64                 5.7.31-1.el7               @mysql57-community
5 mysql-community-libs-compat.x86_64          5.7.31-1.el7               @mysql57-community
6 mysql-community-server.x86_64               5.7.31-1.el7               @mysql57-community
7 mysql80-community-release.noarch            el7-3                      installed
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　　　使用以下命令实现更新任何一个组件包：（package-name就是你要更细的组件包名字）

```
1 yum update  package-name
```

　　注意： 在使用 yum 更新之后，MySQL服务器会自动重启。

　　到此基本的安装就OK了。也可以使用命令了。

#### 　　7、防火墙设置（推荐配置）

　　某些时候数据库管理不可能进入机房，所以只能是远程操作，且数据库管理不是每个人都有root账户权限的。所以：如果希望其他主机（或外部主机）可以访问数据库，则需要需要开放访问端口，创建新管理账户，以及设置访问权限。

　　如果有人疑问，为什么要编写防火墙设置这一段时，可以参考我编写的[Tomcat安装](https://www.cnblogs.com/xsge/p/13819537.html)防火墙设置的那部分！（安全问题）

　　1、创建用户并给用户授权：允许在任意IP登录

　　　　Linux中的数据库MySQL，root账户默认只能在本机（Linux系统中）访问。（我们不建议直接修改root用户的信息）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1 ####创建用户并授权
2 grant  all  on  *.*  to  'xsge'@'%'  identified  by  'SQLxsge1.';　　　　#创建用户xsge，密码SQLxsge1.  授权所有权限（all），允许正在任意主机登录（%），任意库任意表（*.*）
3 ----------------------------------如需其他修改请看参考下面的SQL-----------------------------------
4 ####修改xsge主机访问权限范围(前提，该用户xsge已经存在)
5 update  mysql.user  set  host='localhost'  where  user='xsge';　　　#修改xsge账户访问范围：localhost只能在Linux系统本机访问
6 
7 ####修改权限 
8 Grant select，update on test.*  to  'xsge'@'%';　　　　#给xsge授权查询，更新，test库中所有表（test.*）
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　2、开启防火墙mysql 3306端口的外部访问

```
1 ####设置防火墙开放端口
2 [root@localhost ~]# firewall-cmd --zone=public --add-port=3306/tcp --permanent
3 success
4 ####重启防火墙
5 [root@localhost ~]# service firewalld  restart
6 Redirecting to /bin/systemctl restart firewalld.service
```

　　Game Over！！！

####  　8、数据库乱码问题（推荐设置）

　　登录MySQL查看编码问题：

```
1 show variables like 'character_set%';
```

　　修改mysql配置文件/etc/my.cnf。

```
[root@localhost ~]# vim  /etc/my.cnf    打开编辑模式，输入i、I、a等进入插入模式，添加配置信息，添加完成后，按ESC退出插入模式，输入命令：wq 回车。保存并退出
```

　　添加如下配置：（注意下图中配置的所在位置，不要乱了，否则可能无法启动数据库服务了）

```
1 [mysqld]
2 character-set-server=utf8 
3 [client]
4 default-character-set=utf8 
5 [mysql]
6 default-character-set=utf8
```

![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201019164517208-1937345741.png)

 　重启MySQL服务，再次查看编码。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 [root@localhost etc]# service mysqld restart    #重启MySQL服务
 2 
 3 ####登录数据库
 4 [root@localhost etc]# mysql -uxsge -pSQLxsge1.
 5 ………………
 6 ####查看编码
 7 mysql> show variables like 'character_set%';
 8 +--------------------------+----------------------------+
 9 | Variable_name            | Value                      |
10 +--------------------------+----------------------------+
11 | character_set_client     | utf8                       |
12 | character_set_connection | utf8                       |
13 | character_set_database   | utf8                       |
14 | character_set_filesystem | binary                     |
15 | character_set_results    | utf8                       |
16 | character_set_server     | utf8                       |
17 | character_set_system     | utf8                       |
18 | character_sets_dir       | /usr/share/mysql/charsets/ |
19 +--------------------------+----------------------------+
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

###  

### 2、Yum 安装其它的MySQL产品和组件（可选）

　　查看一下有什么可以安装的MySQL产品和组件。

```
1 ####查看其它MySQL组件
2 [root@localhost ~]#  yum --disablerepo=\* --enablerepo='mysql*-community*' list available
3 
4 ####安装MySQL组件，package-name组件的名字。
5 [root@localhost ~]# yum  install  package-name
```

###  

### 3、RPM安装MySQL

#### 　　1、下载MySQL安装包

　　手动下载或wget命令下载

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
看上去太多了
mysql-community-client-5.7.26-1.el7.x86_64.rpm
mysql-community-common-5.7.26-1.el7.x86_64.rpm
mysql-community-libs-5.7.26-1.el7.x86_64.rpm
mysql-community-server-5.7.26-1.el7.x86_64.rpm

可以直接选择套件组（包含了MySQL依赖组价）
mysql-5.7.31-1.el7.x86_64.rpm-bundle.tar
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　命令下载：（在官网下载地址获取下载连接即可）

```
1 wget  https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.31-1.el7.x86_64.rpm-bundle.tar
```

　　手动下载：下载Linux系统的MySQL安装包。自己选择一个一个下载，或者下载组件套。参考MySQL官网如下图：

![img](https://img2020.cnblogs.com/blog/2131507/202010/2131507-20201019165952746-1668225622.png)

 　如果是手动下载，下载后将文件mysql-5.7.31-1.el7.x86_64.rpm-bundle.tar通过XFTP上传到Linux系统目录中。

#### 　　2、安装MySQL

　　1、解压资源：mysql-5.7.31-1.el7.x86_64.rpm-bundle.tar，获取rpm包。

　　2、安装

　　　　安装顺序 common–>libs–>client–>server

```
1 # 安装顺序
2 # common --> libs --> clients --> server
3 
4 # 安装命令
5 rpm -ivh mysql-community-common-5.7.19-1.el6.x86_64.rpm mysql-community-libs-5.7.19-1.el6.x86_64.rpm mysql-community-client-5.7.19-1.el6.x86_64.rpm mysql-community-server-5.7.19-1.el6.x86_64.rpm
```

　　3、可能需要依赖包libaio

　　　　安装命令：yum -y install libaio

　　4、初始化

　　　　命令：mysqld --initialize --user=mysql

　　5、查看登录密码，服务、修改密码、远程访问等同上！！！（略）

##  

## 4、附录

　　　　如果上面的方式不能修改可以使用下面安全模式修改root：

　　　　打开/etc/my.cnf文件，加上一行skip-grant-tables，表示跳过安全检查（即登录时无需密码）。直接用mysql -uroot登录，即可登录成功。切换到mysql库，查看user表结构，需要注意的是5.7以上版本已经没有了Password字段，取而代之的是authentication_string字段。执行sql语句修改密码：update user set authentication_string='密码' where User='root'; 或者5.6及以下版本使用：update user set Password='密码' where User='root'; 然后FLUSH PRIVILEGES即可。

　　　　注意：修改成功后，要删掉配置文件中的skip-grant-tables，否则谁都可以登录了。