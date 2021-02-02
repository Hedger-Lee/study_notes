# oracle创建表空间并使用dump文件

```sql
create tablespace V5_TS logging datafile'/data/oracle/oradata/HEDGER/V5_TS.dbf' size 1024m autoextend on next 100m maxsize 10240m extent management local;

create tablespace V5_INDEX logging datafile'/data/oracle/oradata/HEDGER/V5_INDEX.dbf' size 1024m autoextend on next 100m maxsize 10240m extent management local;
```

```sh
impdp djbx_v5/djbx_v5 dumpfile=dump文件名 logfile=djbx_v5_20210105.log remap_schema=djbx_v5:djbx_v5;
```

### 查询dump文件默认路径

```
select * from dba_directories where directory_name='DATA_PUMP_DIR';
```

