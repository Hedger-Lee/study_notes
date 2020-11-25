# shell中循环的用法

## for循环

### 列表for循环

#### 数字for循环

```
for value in {1..5}  
#for value in 1 2 3 4 5  
do  
     echo "Now value is $value..."  
done 
```

```
sum=0

for i in {1..100..2}
do
    let "sum+=i"
done    
echo "sum=$sum"
```

```
for i in $(seq 1 5)
do 
echo $(expr $i \* $i + 1);
done
```

#### 字符串for循环

```
for i in v1 v2 v3 ;  
do  
echo value is: $i;  
done 
```

```
list="Earth is the Home of Human! ";
for i in $list;
do
echo word is $i;
done
```

```
for i in $* ;  
do  
echo $i is input value\! ;  
done
```

#### 路径查找for循环

- 查询当前目录下的文件列表

```
for file in $( ls )
do
   echo "file: $file"
done
```

```
for file in `ls`
for file in *
```

- 通配符查找指定路径

```
for file in /root/*;  
do  
echo $file;  
done
```

- 通配符查找指定路径下符合指定扩展名的文件路径

```
for file in /root/study/shell/*.sh;  
do  
echo $file;  
done
```

### 类C风格的for循环

```
for((i=1;i<=5;i++));
do 
echo $(expr $i \* $i + 1);
done
```

```
awk 'BEGIN{
for(i=1; i<=5; i++) 
print (i*i+1)
}'
```

## while循环

```
sum=0
i=1  
while(( i <= 100 ))  
do  
     let "sum+=i"  
     let "i += 2"     
done  
  
echo "sum=$sum"
```

## until循环

```
i=1
sum=0  
until [[ "$i" -gt 100 ]]    #直到i大于100  
do  
    let "sum+=i"  
    let "i += 2"   
done

echo "sum=$sum"
```

## select循环

```bash
select color in "red" "blue" "green" "white" "black"  
do   
    echo $color  
done  
```