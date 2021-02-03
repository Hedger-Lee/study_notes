# oracle连不上报错The listener supports no services

在listener.ora中添加

```
SID_LIST_LISTENER = 
(SID_LIST = 
  (SID_DESC = 
     (GLOBAL_DBNAME = globe)
     (SID_NAME = globe)
  )
)
```



如果报错oracle not avilable

```
startup amount;
alter database open;
select status from v$instance;
```

