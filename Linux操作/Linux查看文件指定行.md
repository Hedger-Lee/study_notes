# Linux查看文件指定行

## tail

```
tail date.log               输出文件末尾的内容，默认10行

tail -20  date.log        输出最后20行的内容

tail -n -20  date.log    输出倒数第20行到文件末尾的内容

tail -n +20  date.log   输出第20行到文件末尾的内容

tail -f date.log            实时监控文件内容增加，默认10行。
```

## head

```
head date.log           输出文件开头的内容，默认10行

head -15  date.log     输出开头15行的内容

head -n +15 date.log 输出开头到第15行的内容

head -n -15 date.log  输出开头到倒数第15行的内容
```

## sed

```
sed -n "开始行，结束行p" 文件名    

sed -n '70,75p' date.log             输出第70行到第75行的内容

sed -n '6p;260,400p; ' 文件名    输出第6行 和 260到400行

sed -n 5p 文件名                       输出第5行
```

