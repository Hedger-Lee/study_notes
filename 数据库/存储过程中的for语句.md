# 存储过程中的for语句

```
for 临时变量名 in 范围 loop
	执行语句;
end loop;
```

for循环常用场景：

1. 将select查询的结果当做for循环的范围

   ```
   for i in (select 查询语句) loop
   	执行语句;
   end loop;
   ```

   