# 在oracle中根据表名查表属于哪个模式

```
select owner from
(select a.*,
max(last_analyzed) over(partition by table_name) m
from All_tables a
where table_name=UPPER('PrpPdangerUnit')
  )
where last_analyzed=m;
```

