# awk

> 处理文本文件的语言，强大的文本分析工具

**语法**：

```
awk [选项参数]  'script' var=value file
or
awk [选项参数] -f scriptfile var=value file
```

**选项参数**：

- `-F fs`or`--field-separator fs`
  指定输入文件分隔符，fs是一个字符串或者是一个正则表达式，如-F:。
- `-v var=value`or`--asign var=value`
  赋值一个用户定义变量
- `-f scriptfile`or`--file scriptfile`
  从脚本文件中读取awk命令

**基本用法**：

log.txt文本内容：

```
2 this is a test
3 Are you like awk
This's a test
10 There are orange,apple,mongo
```

**用法一：**

```
awk '{[pattern] action}' {filenames}
# 行匹配语句 awk '' 只能用单引号
```

eg:

```
# 不指定分割字符，默认每行按空格或TAB分割，输出文本中的1、4项
awk '{print $1,$4}' log.txt
结果：
2 a
3 like
This's
10 orange,apple,mongo

# 格式化输出
awk '{printf "%-8s %-10s\n",$1,$4}' log.txt
2        a
3        like
This's
10       orange,apple,mongo
```

**用法二：**


