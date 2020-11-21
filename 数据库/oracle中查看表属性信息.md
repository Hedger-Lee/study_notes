# oracle中查看表属性信息

1. 查当前用户所有的表格

   ```
   select * from user_tables;
   --查询的时候根据表名去查询
   ```

2. 查询所有的表格

   ```
   select * from all_tables;
   --查询的时候根据表名和用户名去查询
   ```

3. 查询当前用户所有表的索引

   ```
   select * from user_indexes;
   --根据索引类型去筛选
   ```

4. 查询某个索引被索引的字段

   ```
   select * from user_ind_columns 
   where index_name=upper('索引名');
   ```

5. 查询某个表的索引

   ```
   select t.*,i.index_type from user_ind_columns t,user_indexes i
   where 
   t.index_name=i.index_name 
   and 
   t.table_name='NODE';
   ```

6. 查询某个表的主键

   ```
   select cu.* from user_cons_columns cu, user_constraints au 
   where 
   cu.constraint_name = au.constraint_name 
   and
   au.constraint_type = 'P' 
   AND 
   cu.table_name = 'NODE'
   ```

7. 查询某个表的外键

   ```
   select * from user_constraints c 
   where 
   c.constraint_type = 'R'
   and
   c.table_name = 'NODE';
   ```

8. 查询外键约束的列名

   ```
   select * from user_cons_columns cl 
   where cl.constraint_name = 外键名称;
   ```

9. 查询引用表的键的列名

   ```
   select * from user_cons_columns cl
   where cl.constraint_name = 外键引用表的键名;
   ```

10. 查询表的所有列及其属性
    方法一：

    ```
    select * from user_tab_columns where table_name=upper('表名');
    ```

    方法二：

    ```
    select cname,coltype,width from col where tname=upper('表名');
    ```

11. 查看某个表的约束条件

    ```
    select constraint_name,constraint_type,search_condition,r_constraint_name
    from user_constraints 
    where table_name=upper('表名');
    ```

    ```
    select c.constraint_name,c.constraint_type,cc.column_name
    from user_constraints c,user_cons_columns cc
    where 
    c.owner = upper('&table_owner') 
    and 
    c.table_name = upper('&table_name')
    and 
    c.owner = cc.owner 
    and c.constraint_name = cc.constraint_name
    order by cc.position;
    ```

    