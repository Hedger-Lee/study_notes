# sed

```
sed -e script 指定script
sed -f scriptfile 指定脚本文件
```

sed的动作

```
a : 新增 在当前的下一行
c : 取代 
d : 删除
i : 插入 在当前行的上一行插入
p : 打印
s : 取代
```



- `sed -n "行号p" 文件名 `
  获取文件指定行号的内容，也可以是行号范围，以逗号分隔