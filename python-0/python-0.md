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

### PEP8
[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)


### 书籍
《流畅的Python》  魔术方法
《Python cook book》 3rd  Python的使用
《编写高质量代码：改善Python程序的91个建议》  如何更高效
设计模式，数据结构，算法

##### args
[知乎](https://zhuanlan.zhihu.com/p/50804195)

wing 中快速注释 Ctrl+.
