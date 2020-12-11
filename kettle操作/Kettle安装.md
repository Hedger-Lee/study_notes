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

### 3.安装swt插件

```
yum -y install gtk2.i686 gtk2-engines.i686 PackageKit-gtk-module.i686 PackageKit-gtk-module.x86_64 libcanberra-gtk2.x86_64 libcanberra-gtk2.i686
```

### 4.无法图形化界面，安装rpm xorg-x11-xauth

```
yum install xorg-x11-xauth
```



## Windows下安装

### 1.解决运行spoon.bat无法启动，dos窗口一闪而过

```
将
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms1024m" "-Xmx2048m" "-XX:MaxPermSize=256m"
改为
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms512m" "-Xmx512m" "-XX:MaxPermSize=256m"
```

