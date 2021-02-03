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



