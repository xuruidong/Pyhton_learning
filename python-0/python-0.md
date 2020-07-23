# Python 基础

### help
显示对象的帮助信息

help(x)

type(x)

### 使用set对list去重
a = [1,2,3,4,5,6,5,4,3,2,11]
b = set(a)

### pip 源配置
#### 临时
使用-i选项

#### 永久
在~/.pip/pip.conf（windows系统为c:\Users\xxx\pip\pip.ini, 即%HOMEPATH%\pip\pip.ini）中写入:
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
