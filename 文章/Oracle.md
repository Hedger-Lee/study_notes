# Oracle

## 1.Oracle内部概念

### 1.1 数据文件dbf

​		数据文件是数据库的物理存储单位。

数据库中的数据是存储在表空间中的，真正是在某一个或者多个数据文件中，而一个表空间可以由一个或多个数据文件组成，一个数据文件只能属于一个表空间。一旦数据文件被加入到某个表空间后，就不能删除这个文件，如果要删除某个数据文件，只能删除其所属的表空间才行。

### 1.2 表空间

​		表空间是Oracle对物理数据库上相关数据文件(ORA或者DBF文件)的逻辑映射。

一个数据库在逻辑上被划分成一个到若干个表空间，每个表空间包含了在逻辑上相关联的一组结构。每个数据库至少有一个表空间(称为system表空间)。每个表空间由同一磁盘上的一个或者多个文件组成，这些文件叫数据库文件(datafile)，一个数据文件只能属于一个表空间。

### 1.3 用户

​		用户是在实例下建立的。不同实例中可以建相同名字的用户。

注：表的数据，是由用户放入某一个表空间的，而这个表空间会随机把这些表数据放到一个或者多个数据文件中。由于Oracle的数据库不是普通的概念，oracle是由用户和表空间对数据进行管理和存放的。但是表不是由表空间去查询的，而是由用户去查的。因为不同用户可以在同一个表空间建立同一个名字的表！这里区分就是用户了！

### 1.4 监听

```shell
# 启动监听
lsnrctl start
# 查看监听状态
lsnrctl status
# 关闭监听
lsnrctl stop

# oracle服务器自动启动监听和数据库
vim /etc/oratab
# 修改
HEDGER:/data/oracle/product/11.2.0/db_1:N
# 为
HEDGER:/data/oracle/product/11.2.0/db_1:Y
# 将N改为Y

vim /etc/rc.d/rc.local
# 添加
su oracle -lc /data/oracle/product/11.2.0/db_1/bin/dbstart
su oracle -lc "/data/oracle/bin/lsnrctl start"
```

### 1.5 字符集

```sql
--查询字符集
select * from v$nls_parameters;
--修改字符集
	--关闭数据库
	shutdown immediate;
	--开启数据库
	startup mount;
	--更改为严格模式
	ALTER SYSTEM ENABLE RESTRICTED SESSION;
	--开启数据库
	ALTER DATABASE OPEN;
	--更改字符集
	ALTER DATABASE CHARACTER SET ZHS16GBK;
	--如果报错
	ALTER DATABASE CHARACTER SET INTERNAL_USE ZHS16GBK;
	--重启
	shutdown immediate;
	startup mount;
--注意点，已经存在的数据字符集没法修改
```

## 2. SQLPLUS

### 2.1 登录连接

- DBA身份登录

  ```sql
  sqlplus / as sysdba
  
  sqlplus /nolog
  conn /as sysdba
  ```

- 普通用户

  ```sql
  sqlplus user/passwd@sid
  or
  sqlplus sys/passwd@sid as sysdba
  ```

```sql
--显示当前用户
show user
--清屏
clean screen
--切换用户
conn user/passwd
```

### 2.2 修改密码

```sql
--修改密码
alter user username identified by newpasswd;
--解锁被锁定用户
alter user username account unlock;
```

### 2.3 文件操作

```sql
--执行sql脚本
@filepath
or
start filepath
--编辑sql脚本
edit filepath

--重定向，将屏幕上的结果输出到指定文件
spool filepath; --开启输出
sql命令查询
--将结果输出到文件中
spool off; -- 输出终止，在两个spool中间的结果会输出到文件中
```

### 2.4 交互式

```sql
&
--输入内容，类似于python的input或者shell中的read
```

```sql
show linesize -- 设置显示行的宽度，默认80个字符
set linesize 90

show pagesize -- 设置每页显示的行数目，默认是14
set pagesize 20
```

### 2.5 启动/关闭数据库

```sql
--启动
startup nomount
启动示例，仅有实例运行。以这种方式打开数据库，将不读取控制文件，不打开数据文件。操作系统启动后台进程，并分配SGA。
--使数据库可用
alter database mount;
alter database open;

startup mount
启动实例，安装数据库。在安装步骤中，Oracle把实例与数据库关联。Oracle打开并关联读取控制文件，获取数据文件和重做日志文件的名称和位置。
--打开数据库
alter database open;

startup
or
startup open
启动、安装、打开数据库
```

```sql
--关闭
shutdown
or 
shutdown normal
Oracle 将在关闭数据库之前等待所有用户断开与数据库的连接。（normal)是Oracle关闭数据库的默认方式。
   (1)、一旦发布此命令，新的用户连接无法再创建。
   (2)、在关闭数据库前，Oracle等待所有用户退出连接。
   (3)、重启数据库时不需要实例恢复，因为Oracle会在关闭数据库以前把所有重做日志缓冲区和数据块缓冲区内容写入磁盘，从而数据库以这种方式关闭时是一致。
   (4)、Oracle关闭数据文件并终止后台进程，Oracle的SGA被解除分配。
   
shutdown transactional 
   Oralce 将在断开所有用户与数据库的连接前等待所有活动事务完成(不能创建新的事务),然后关闭数据库。
   (1)、一旦发布此命令，新的用户连接无法再创建。
   (2)、现有用户不能启动新的事务，并且将断开连接。
   (3)、如果某用户有一个正在执行的事务，在断开该用户连接前，Oracle将等待直到该事务完成。
   (4)、在所有现有事物完成后，Oracle关闭数据库实例并释放内存，Oracle将所有重做日志缓冲区和数据块缓冲区写入磁盘。
   (5)、数据库是一致的，重启数据库时不需要实例恢复。

shutdown immediate
   Oracle 不等待事务完成，回退所有活动的事务，断开已有用户的连接，关闭数据库。
   (1)、一旦发布此命令，新的用户连接无法创建。
   (2)、立即断开所有用户连接。
   (3)、终止所有当前正在执行的事务。
   (4)、回退未完成的事务，数据库保持一致。
   (5)、数据库是一致的，重启数据库时不需要实例恢复。

shutdown abort
   Oracle 不等待当前事务完成，不回退事务，直接断开用户连接。
   (1)、一旦发布此命令，新的用户连接无法创建。
   (2)、现有会话终止，不管是否有活动的事务。
   (3)、不回退终止的事务。
   (4)、不将重做日志缓冲区和数据缓冲区写入磁盘。
   (5)、终止后台进程，立即释放内存并关闭数据库。
   (6)、在重启时，Oracle将执行自动实例恢复，因为不能保证数据库在关闭时是一致的。
```

## 3.Select

### 3.1 基本查询

```sql
select * from test;-- * 仅用在测试中，实际情况下要明确字段
select column1,column2... from test;
```

### 3.2 select ... for update

基本语法

```sql
SELECT ... FOR UPDATE [OF column_list][WAIT n|NOWAIT][SKIP LOCKED];
--of 子句用于指定即将更新的列，即锁定行上的特定列
--WAIT 子句指定等待其他用户释放锁的秒数，防止无限期的等待
```

使用“FOR UPDATE WAIT”子句的优点：

```
1防止无限期地等待被锁定的行；
2允许应用程序中对锁的等待时间进行更多的控制。
3对于交互式应用程序非常有用，因为这些用户不能等待不确定
4若使用了skip locked，则可以越过锁定的行，不会报告由wait n引发的‘资源忙’异常报告
```

两个窗口，同时使用for update查询同一行，只有第一个查询结束事务才能查到结果。

### 3.3 select复制

> 核心：select 需要的字段复制到另一个表中

#### insert into select

语法

```sql
insert into test2(column1,column2...) select value1,value2... from test1; --test2中指定字段
insert into test2 select value1,value2... from test1; --test2所有字段
```

注意事项：

```
1.test2必须已经存在
2.select部分可以使用常量，只要与test2中该位置的类型匹配即可
	insert into test2 select value1,value2,...,5 from test1;
```

#### select into from

语法

```sql
select value1,value2 into test2 from test1;
```

注意事项

```
1.test2必须不存在，语句执行的时候创建，但是创建后的表没有主键
2.该语句只能在代码块中执行，要想作为普通SQL执行，用create as select 代替
```

#### create as select

语法

```sql
create table test2 as select value1,value2... from test1;
```

注意事项

```
test2必须不存在，语句执行的时候创建，但是创建后的表没有主键
```

### 3.4 where

> select 筛选

#### 精确查询(id=1)

```sql
select * from test1 where id=1;
```

#### 模糊查询 like

> 通配符
>
> ```sql
> _ 单个任意字符
> % 任意多个任意字符
> ```

```sql
select * from test1 where name like 'L%';
```

### 3.5 order by

> select 排序

```sql
asc 升序
desc 降序
select value1,value2... from test1 order by value1 asc;
```

## 4.Update

### 4.1 基本更新

```sql
--更新所有行
update test1 set column1=value1,column2=value2...;
--更新指定行
update test1 set column1=value1,column2=value2... where 条件;
```

### 4.2 关联更新

> 通过其他表的字段来更新本表中的内容

```sql
update test1 t1 
set (column1,column2...)=（select value1,value2... from test2 t2 where t1.id=t2.id） 
where exists (select 1 from test2 t2 where t1.id=t2.id);
```

## 5.Delete/Truncate

### 5.1 delete

```sql
--删除所有
delete from test;
--删除指定行
delete from test where 条件;
```

### 5.2 truncate

```sql
--清空表
truncate table test;
```

### 5.3 delete和truncate区别

```sql
1、TRUNCATE 是 DDL 命令，命令执行完就提交，删除的数据不能恢复； 
DELETE 命令是 DML 命令，命令执行完需提交后才能生效，删除后的数据可以通过日志文件恢复。

2、如果表中的数据量较大，TRUNCATE的速度比DELETE速度快很多。

3、truncate删除将重新设置表索引的初始大小，而delete不能。

4、delete能够触发表上相关的delete触发器，而truncate则不会触发。

5、delete删除的原理是一次一条从表中删除数据，并将删除操作当做事务记录在数据库的日志当中，以便进行数据回滚。而truncate是一次性进行数据页的删除，因此执行速度快，但是不能回滚。

总结：truncate命令是属于DDL命令，一次性删除表中所有数据，并且数据不能恢复，在实际开发过程当中truncate命令慎用。
```

## 6.Alter

> 修改结构

### 6.1 alter table

> 修改表结构

```sql
--增加字段
alter table test add column (列名 数据类型);
--删除字段
alter table test drop column 列名;
--修改字段类型
alter table test modify (列名 数据类型);
--重命名字段
alter table test rename column 当前字段名 to 新字段名;
--重命名表名
alter table test rename to 新表名;
```

## 7. impdp

执行报错

```
ORA-39006: internal error
ORA-39213: Metadata processing is not available
```

查看提示

```
oerr ora 39006
oerr ora 39213
```

解决

```sql
以sysdba连接
执行
exec dbms_metadata_util.load_stylesheets;
```

