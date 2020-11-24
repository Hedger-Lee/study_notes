# awk

> 处理文本文件的语言，强大的文本分析工具
>
> 将每行分割成几部分

`awk [选项参数] 'script' var=value file`

`awk [选项参数] -f scriptfile var=value file`

```
-F 指定分隔符/正则表达式 
-v var=value 赋值定义变量
-f scriptfile 从脚本中读取awk执行操作
```

```
$0 表示当前读取行的内容
$1 当前行的第一列的内容
$2 当前行的第一列的内容
...
```
