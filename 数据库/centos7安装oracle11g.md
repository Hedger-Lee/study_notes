# centos7安装oracle11g

## 一、准备工作

### 1.创建运行oracle数据库的系统用户和用户组

```sh
groupadd oinstall #创建用户组oinstall
groupadd dba #创建用户组dba
useradd -g oinstall -g dba -m oracle #创建oracle用户，并加入到oinstall和dba用户组
passwd oracle　　#设置用户oracle的登陆密码，不设置密码，在CentOS的图形登陆界面没法登陆
id oracle # 查看新建的oracle用户
```

### 2.创建oracle数据库安装目录

```sh
mkdir -p /data/oracle　　#oracle数据库安装目录
mkdir -p /data/oraInventory　　#oracle数据库配置文件目录
mkdir -p /data/database　　#oracle数据库软件包解压目录
cd /data
chown -R oracle:oinstall /data/oracle
chown -R oracle:oinstall /data/oraInventory
chown -R oracle:oinstall /data/database
```

### 3.修改os系统标识

```
vi /etc/redhat-release
将
CentOS Linux release 7.2.1511 (Core) 
改为
redhat-7 
```

### 4.安装oracle数据库所需依赖包

```sh
yum -y install binutils compat-libstdc++-33 compat-libstdc++-33.i686 elfutils-libelf elfutils-libelf-devel gcc gcc-c++ glibc glibc.i686 glibc-common glibc-devel glibc-devel.i686 glibc-headers ksh libaio libaio.i686 libaio-devel libaio-devel.i686 libgcc libgcc.i686 libstdc++ libstdc++.i686 libstdc++-devel make sysstat
```

### 5.关闭防火墙

```
systemctl status firewalld.service　　#查看防火墙状态，运行中
systemctl stop firewalld.service　　#关闭防火墙
systemctl disable firewalld.service　　#禁止使用防火墙（重启也是禁止的）
```

### 6.关闭selinux

```sh
vi /etc/selinux/config

SELINUX=disabled   #此处修改为disabled
```

### 7.修改内核参数

```sh
vi /etc/sysctl.conf
添加
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.conf.all.rp_filter = 1
fs.file-max = 6815744 #设置最大打开文件数
fs.aio-max-nr = 1048576
kernel.shmall = 2097152 #共享内存的总量，8G内存设置：2097152*4k/1024/1024
kernel.shmmax = 2147483648 #最大共享内存的段大小
kernel.shmmni = 4096 #整个系统共享内存端的最大数
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 9000 65500 #可使用的IPv4端口范围
net.core.rmem_default = 262144
net.core.rmem_max= 4194304
net.core.wmem_default= 262144
net.core.wmem_max= 1048576
# 实际写的时候将注释去掉

# 使配置参数生效
sysctl -p
```

### 8.对oracle用户设置限制

> 提高软件运行性能（红色为添加部分）

```sh
vi /etc/security/limits.conf 
添加
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
```

### 9.配置用户的环境变量

```sh
vi /home/oracle/.bash_profile 

export ORACLE_BASE=/data/oracle #oracle数据库安装目录
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1 #oracle数据库路径
export ORACLE_SID=HEDGER #oracle启动数据库实例名
export ORACLE_TERM=xterm #xterm窗口模式安装
export PATH=$ORACLE_HOME/bin:/usr/sbin:$PATH #添加系统环境变量
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib #添加系统环境变量
export LANG=C #防止安装过程出现乱码
export NLS_LANG=AMERICAN_AMERICA.ZHS16GBK  #设置Oracle客户端字符集，必须与Oracle安装时设置的字符集保持一致

# 根据实际修改
# 使上述配置立即生效
source /home/oracle/.bash_profile 
```

### 10.解压安装包

```sh
unzip linux.x64_11gR2_database_1of2.zip -d /data/database/
unzip linux.x64_11gR2_database_2of2.zip -d /data/database/

chown -R oracle:oinstall /data/database/database/
```

## 二、图形化界面安装

> 一种是直接在centos图形化操作，一种是远程连接操作，要准备图形化的位置

### 1.启动./runInstaller

```sh
cd /data/database/database/
./runInstaller


# 如果报错
# 切换root账户，配置/etc/profile
export DISPLAY=ip:0.0 # ip是准备图形化的设备ip，比如xshell连接，Xmanager图形化在windows设备
source /etc/profile
xhost +
```

### 2.图形化操作

### 3.swap空间不足解决

```sh
free -m　　#查看当前虚拟内存
dd if=/dev/zero of=/home/swap bs=1024 count=1024000　　#将当前swap空间由2048M 增加到 3048M 新增一个2014的swap文件
mkswap /home/swap
free -m
swapon /home/swap　　#增加并启用虚拟内容
free -m　　#再次查看
```

### 4.缺失包检查有没有安装

> 如果已经安装，ignore all

### 5.执行脚本

> 切换root，根据提示执行两个脚本

### 6.执行netca配置监听

```
如果报错，检查ORACLE_HOME的路径
```

### 7.执行dbca创建数据库实例

```
如果报错，检查ORACLE_HOME的路径
```

## 三、测试是否创建成功

使用sqlplus命令

```sh
sqlplus user/passwd@sid
#如果不知道
sqlplus /nolog
conn /as sysdba
alter user username identified by password;
alter user 用户名 account unlock; 
```

```
oracle有三个默认的用户名和密码~
1.用户名:sys密码:change_on_install
2.用户名:system密码:manager
3.用户名:scott密码:tiger
```

