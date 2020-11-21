# kettle设置变量相关脚本

## 设置变量

```
var prevRow=previous_result.getRows();//获取上一个传递的结果集
if (prevRow == null &&(prevRow.size()=0))
{
    false;

}else{
    parent_job.setVariable("tables", prevRow);//ArrayList存储表名变量
    parent_job.setVariable("size", prevRow.size());//存储执行表的总数量
    parent_job.setVariable("i", 0);//循环控制变量
    parent_job.setVariable("TABLENAME", prevRow.get(0).getString("table_name",""));
    true;
}
```

kettle中使用js打印日志信息

```
var subject="自定义日志输出";
//实例化日志channel对象
var log= new org.pentaho.di.core.logging.LogChannel(subject);
//日志输出
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow);
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow.get(0).getString("table_name",""));
```



```
var prevRow=previous_result.getRows();//获取上一个传递的结果集

var subject="自定义日志输出";
//实例化日志channel对象
var log= new org.pentaho.di.core.logging.LogChannel(subject);
//日志输出
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow);
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow.get(0).getString("table_name",""));

if (prevRow == null &&(prevRow.size()=0))
{
    false;

}else{
    parent_job.setVariable("tables", prevRow);//ArrayList存储表名变量
    parent_job.setVariable("size", prevRow.size());//存储执行表的总数量
    parent_job.setVariable("i", 0);//循环控制变量
    parent_job.setVariable("TABLE_NAME", prevRow.get(0).getString("table_name",""));
    true;
}
```

```
var prevRow=previous_result.getRows();//获取上一个传递的结果集

var subject="自定义日志输出";
//实例化日志channel对象
var log= new org.pentaho.di.core.logging.LogChannel(subject);
//日志输出
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow);
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow.get(0));
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow.get(0).getString("table_name",""));
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+prevRow.get(0).getString("owner",""));

if (prevRow == null &&(prevRow.size()=0))
{
    false;

}else{
    parent_job.setVariable("tables", prevRow);//ArrayList存储表名变量
    parent_job.setVariable("size", prevRow.size());//存储执行表的总数量
    parent_job.setVariable("i", 0);//循环控制变量
    parent_job.setVariable("TABLE_NAME", prevRow.get(0).getString("table_name",""));
	parent_job.setVariable("OWNER", prevRow.get(0).getString("owner",""));
    true;
}
```





## 判断变量脚本

```
var list_Tables =parent_job.getVariable("tables").replace(" ","").replace("[","").replace("]","").split(",");
var size = new Number(parent_job.getVariable("size"));
var i = new Number(parent_job.getVariable("i"))+1;
if(i<size){
    parent_job.setVariable("TABLENAME", list_Tables[i]);
}
parent_job.setVariable("i",i);
true;
```

```
//var list_Tables =parent_job.getVariable("tables").replace(" ","").replace("[","").replace("]","").split(",");
var list_Tables =parent_job.getVariable("tables").replace(" ","").replace("[[","").replace("]]","").replace("]","").split(",\\[");
var subject="自定义日志输出";
//实例化日志channel对象
var log= new org.pentaho.di.core.logging.LogChannel(subject);
//日志输出
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+list_Tables);
//log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+parent_job.getVariable("tables"));
//[[PrpSperson], [SALESCINDA], [PrpSpersonHis], [SALESCINDA], [PrpSteam], [SALESCINDA]]
//PrpSperson,[SALESCINDA,[PrpSpersonHis,[SALESCINDA,[PrpSteam,[SALESCINDA

var size = new Number(parent_job.getVariable("size"));
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+size);
var i = new Number(parent_job.getVariable("i"))+1;
log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+i);
if(i<size){
	log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+list_Tables[i*2]);
	log.logMinimal("XXXXXXXXXXXXXXXXXXXXXXXX"+list_Tables[i*2+1]);
    parent_job.setVariable("TABLE_NAME", list_Tables[i*2]);
	parent_job.setVariable("OWNER", list_Tables[i*2+1]);
}
parent_job.setVariable("i",i);
true;
```

```
var prevRow=previous_result.getRows();
var size = new Number(parent_job.getVariable("size"));
var i = new Number(parent_job.getVariable("i"))+1;
if(i<size){
parent_job.setVariable("id", prevRow.get(i).getString("id", ""));
parent_job.setVariable("name", prevRow.get(i).getString("name", ""));
}
parent_job.setVariable("i",i);
true;
```

