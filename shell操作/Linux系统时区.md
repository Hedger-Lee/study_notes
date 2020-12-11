# Linux系统时区

## 查看当前时间和时区

```
date
```

## 修改时区

> 使用要修改的时区文件覆盖系统使用时区

```
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

