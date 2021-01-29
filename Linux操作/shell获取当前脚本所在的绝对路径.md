# shell获取当前脚本所在的绝对路径

## 单脚本

> 这个是有缺陷的，⽐比如脚本A source 了另一个⽬目录下的脚本B, 然后脚本B尝试使⽤用此法获取路路径时得到的是A的路路径

```bash
current_path=$(cd "$(dirname $0)";pwd)
```

或

```bash
current_path=$(
cd $(dirname $0)
pwd
)
```

## 脚本中引用脚本(推荐)

```bash
#current_path=$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)
current_path=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
```

或

```bash
current_path=$(
cd $(dirname "${BASH_SOURCE[0]}")
pwd
)
```