# kettle命令行使用

## pan--转换执行器

> 执行转换

- `-version`显示版本信息

- `-file=filename`运行xml文件

- `-param:key=value`指定命名参数

- `-log=logging filename` 设置日志文件

- `-level=logging level` 设置日志级别
  - Error:只显示错误
  - Nothing:不显示任何输出
  - Minimal:只使用最少的记录
  - Basic:这是默认的基本日志记录级别
  - Detailed:详细的日志输出
  - Debug:以调试为目的，非常详细的输出
  - Rowlevel:使用行级记录，会产生大量的数据

- 返回状态，Pan会基于执行状况返回一个错误码：
  - 0：转换执行成功
  - 1：处理过程中发生错误
  - 2：在装载或者运行时发生意外的错误
  - 3：不能初始化转换
  - 7：转换不能从资源库或xml中装载
  - 8：装载步骤或插件错误(通常是装载其中一个插件错误)
  - 9：命令行用法错误

示例：

```
56 11 * * * 
/bin/sh /**/kettle/data-integration/pan.sh 
-file=/***/script/topic_keyindex_device_daily-data-producter-all_income.ktr 
-level=Debug >> 
/tmp/kettle-log/topic_keyindex_device_daily-data-producter-all_income.log

```

| Switch        | Purpose                                                      |
| ------------- | ------------------------------------------------------------ |
| rep           | Enterprise or database repository name, if you are using one |
| user          | Repository username                                          |
| pass          | Repository password                                          |
| trans         | The name of the transformation (as it appears in the repository) to launch |
| dir           | The repository directory that contains the transformation, including the leading slash |
| file          | If you are calling a local KTR file, this is the filename, including the path if it is not in the local directory |
| level         | The logging level (Basic, Detailed, Debug, Rowlevel, Error, Nothing) |
| logfile       | A local filename to write log output to                      |
| listdir       | Lists the directories in the specified repository            |
| listtrans     | Lists the transformations in the specified repository directory |
| listrep       | Lists the available repositories                             |
| exprep        | Exports all repository objects to one XML file               |
| norep         | Prevents Pan from logging into a repository. If you have set the KETTLE_REPOSITORY, KETTLE_USER, and KETTLE_PASSWORD environment variables, then this option will enable you to prevent Pan from logging into the specified repository, assuming you would like to execute a local KTR file instead. |
| safemode      | Runs in safe mode, which enables extra checking              |
| version       | Shows the version, revision, and build date                  |
| param         | Set a named parameter in a name=value format. For example: -param:FOO=bar |
| listparam     | List information about the defined named parameters in the specified transformation. |
| maxloglines   | The maximum number of log lines that are kept internally by PDI. Set to 0 to keep all rows (default) |
| maxlogtimeout | The maximum age (in minutes) of a log line while being kept internally by PDI. Set to 0 to keep all rows indefinitely (default) |

## kitchen--作业执行器

> 执行作业

- `-rep:Repository name`任务包所在存储名

- `-user:Repository username`执行人

- `-pass:Repository password`执行人密码

- `-job:The name of the job to launch`任务包名称

- `-dir:The directory(don't forget the leading / or\)`

- `-file:The filename(JobXML) to launch`

- `-level:The logging level(Basic,Detailed,Debug,Rowlevel,Error,Nothing)`指定日志级别

- `-log:The logging file to write to`指定日志文件

- `-listdir:List the directories in the repository`列出指定存储中的目录结构。

- `-listjobs:List the jobs in the specified directory`列出指定目录下的所有任务

- `-listrep:List the defined repositories`列出所有的存储

- `-norep:Don't log into the repository`不写日志

示例：

```
1.  Windows 中多个参数以 / 分隔，key 和value之间以：分隔

ü 作业存储在文件

Kitchen.bat /level:Basic>D:\etl.log /file:F:\Kettledemo\email.kjb

ü 作业存储在数据库

Kitchen.bat /rep kettle /user admin /pass admin /job F_DEP_COMP

（Rep的值为数据库资源库ID）

2. Linux 中参数以 –分隔

作业存储在文件

kitchen.sh -file=/home/job/huimin.kjb >> /home/ log/kettle.log

作业存储在数据库

./kitchen.sh -rep=kettle1 -user=admin -pass=admin -level=Basic -job=job
```

| Switch          | urpose                                                       |
| --------------- | ------------------------------------------------------------ |
| rep             | Enterprise or database repository name, if you are using one |
| user            | Repository username                                          |
| pass Repository | password                                                     |
| job             | The name of the job (as it appears in the repository) to launch |
| dir             | The repository directory that contains the job, including the leading slash |
| file            | If you are calling a local KJB file, this is the filename, including the path if it is not in the local directory |
| level           | The logging level (Basic, Detailed, Debug, Rowlevel, Error, Nothing) |
| logfile         | A local filename to write log output to                      |
| listdir         | Lists the sub-directories within the specified repository directory |
| listjob         | Lists the jobs in the specified repository directory         |
| listrep         | Lists the available repositories                             |
| export          | Exports all linked resources of the specified job. The argument is the name of a ZIP file. |
| norep           | Prevents Kitchen from logging into a repository. If you have set the KETTLE_REPOSITORY, KETTLE_USER, and KETTLE_PASSWORD environment variables, then this option will enable you to prevent Kitchen from logging into the specified repository, assuming you would like to execute a local KTR file instead. |
| version         | Shows the version, revision, and build date                  |
| param           | Set a named parameter in a name=value format. For example: -param:FOO=bar |
| listparam       | List information about the defined named parameters in the specified job. |
| maxloglines     | The maximum number of log lines that are kept internally by PDI. Set to 0 to keep all rows (default) |
| maxlogtimeout   | The maximum age (in minutes) of a log line while being kept internally by PDI. Set to 0 to keep all rows indefinitely (default) |