# Python 基础

[python 版本](https://www.python.org/doc/versions)

TensorFlow2

查看特性变化

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

### Python 魔术方法

## 虚拟环境
1. 创建虚拟环境 
   python -m venv venv1  创建了一个名为 venv1 的虚拟环境  
2. 进入（激活）虚拟环境  
   source venv1/bin/activate, windows 环境下 venv1\Scripts\activate.bat  
3. 退出虚拟环境
   deactivate
4. 在虚拟环境中，安装的第三方库会被安装到Lib/site-packages
5. 生产环境的部署
   打包代码文件，如 a.py
   保证生产环境上的python 版本可用  
   激活虚拟环境， pip freeze > requirements.txt,  
   进入生产机的虚拟环境，pip install -r requirements.txt

## 看文档
看版本变化
PEP 文档中有描述 功能的演进历史

itertools
functools


github 搜索， in:readme  xxx

康奈尔笔记法
不要 “云学习”