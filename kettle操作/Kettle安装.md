# Kettle安装

先安装jdk，再将压缩包解压即可，没有权限就给权限

## Linux下安装

### 1.解决warnning警告

```
sudo wget ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/matthewdva:/build:/EPEL:/el7/RHEL_7/x86_64/webkitgtk-2.4.9-1.el7.x86_64.rpm

sudo yum install webkitgtk-2.4.9-1.el7.x86_64.rpm
```

### 2.解决启动./spoon.sh报错找不到文件

```
yum -y install redhat-lsb
```

## Windows下安装

### 1.解决运行spoon.bat无法启动，dos窗口一闪而过

```
将
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms1024m" "-Xmx2048m" "-XX:MaxPermSize=256m"
改为
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms512m" "-Xmx512m" "-XX:MaxPermSize=256m"
```

