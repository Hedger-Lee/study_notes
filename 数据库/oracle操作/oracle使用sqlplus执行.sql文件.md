# oracle使用sqlplus执行.sql文件

```
sqlplus -s $DB_INFO > $LOG_FILE 2>&1 <<EOF
whenever oserror exit 1;
@${filepath}/initTable.sql
exit
EOF
```

## 执行多个sql文件

> 整合到一个all.sql中

```
all.sql

@sql文件路径1
@sql文件路径2
...
```

然后执行all.sql即可