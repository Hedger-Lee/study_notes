# Linux命令行连接oracle

## oracle客户端安装

判断有没有安装sqlplus：`which sqlplus`

### 安装模块

oracle-instantclient11.2-basic-11.2.0.3.0-1.x86_64.rpm和oracle-instantclient11.2-sqlplus-11.2.0.3.0-1.x86_64.rpm

```
rpm -ivh oracle-instantclient11.2-basic-11.2.0.3.0-1.x86_64.rpm
rpm -ivh oracle-instantclient11.2-sqlplus-11.2.0.3.0-1.x86_64.rpm
```

安装在默认位置

### 配置环境变量

```
export ORACLE_HOME=/usr/lib/oracle/11.2/client64
export TNS_ADMIN=$ORACLE_HOME
export PATH=$ORACLE_HOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
```

`whereis oracle`查看oracle客户端安装路径

### 配置TNS

进入客户端目录，添加tnsnames.ora配置文件，并配置TNS信息

```
zbdbtest =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 10.75.43.2)(PORT = 1522))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = zbdbtest)
    )
  )
```

### 测试连接

测试是否可以连接成功`sqlplus username/password@DATABASENAME`