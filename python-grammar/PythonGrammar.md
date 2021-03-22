# Python 语法

## Python 基础语法
### python 基本数据类型
|类型||
|-|-|
|None|空对象|
|bool|布尔值|
|数值|整数、浮点数、复数|
|序列|字符串、列表、元组|
|集合|字典、集合|
|可调用|函数|

二进制数 0b10, 八进制 0o34

### python 高级数据类型
|||
|-|-|
|colloctions|容器数据类型|
|nametuple|命名元组|
|dequeue|双端队列|
|Counter|计数器|
|OrderedDict|顺序字典|

https://python.org/collections

搜 Python 标准库，官方文档  

dir(), help(),   
[Python 数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)<br/>
[Pyhton 其他流程控制工具](https://docs.python.org/zh-cn/3/tutorial/controlflow.html)<br/>
[Pyhton 中的类](https://docs.python.org/zh-cn/3/tutorial/classes.html)<br/>
[Python 定义函数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions)


## Python module and Package
* 模块：Python 中一个以 .py 结尾的文件就是一个模块，模块中定义了变量、函数等来实现一些类似的功能。Python 有很多自带的模块（标准库）和第三方模块，一个模块可以被其他模块引用，实现了代码的复用性。
* 包：包是存放模块的文件夹，包中包含 `__init__.py` 和其他模块，`__init__.py` 可为空也可定义属性和方法，在 Python3.3 之前的版本，一个文件夹中只有包含`__init__.py`，其他程序才能从该文件夹引入相应的模块、函数等，之后的版本没有 `__init__.py` 也能正常导入，简单来说就是 Python3.3 之前的版本，`__init__.py` 是包的标识，是必须要有的，之后的版本可以没有。


[Python `__all__`](http://c.biancheng.net/view/2401.html)

模块的导入
```
import MyPackage.Model1
from MyPackage import Model1 as M
```
在module2.py 中使用module.py中的内容：
` from . import Module1`

如果在同级目录下存在包Pkg2
在Module2.py中 `from .Pkg2 import xxx`

## Python Stdand Lib
看官方文档  

### time
time.localtime()
time.strftime('%Y-%m-%d %X', time.localtime())
time.strptime("2021-03-06 21:57:19", '%Y-%m-%d %X') 转成struct_time
timedelta 类， 计算时间偏移

### logging
logging.Baseconfig()

### random
0-100之间的随机偶数：random.randrange(0, 100, 2)   
随机选择元素 choice  
随机抽取多个元素 sample  
```
import random

def random_test():
    print (random.random())
    print (random.random())
    
    print (random.randrange(0, 100, 2))
    print (random.randrange(0, 100, 2))
    
    print (random.choice(["qq", "ww", "ee"]))
    print (random.choice(["qq", "ww", "ee"]))
    
    print (random.sample(["qq", "ww", "ee"], 2))
    print (random.sample(["qq", "ww", "ee"], 2))
```

### pathlib

显示当前路径： p.resolve()
获取文件名： p.name  
去掉扩展名的文件名 p.stem  
显示扩展名 p.suffix
如果有多个扩展名 p.suffixes
路径 p.parent

```
import pathlib
def pathlib_test():
    p = pathlib.Path()
    print (p.resolve())
    
    testpath = 'C:/Users/Public/basic.py.bak'
    p = pathlib.Path(testpath)
    print (p.name)
    print (p.stem)
    print (p.suffix)
    print (p.suffixes)
    print (p.parent)
    for pa in p.parents:
        print (pa)
    
    print(p.parts)
```
```
E:\note\python\python-grammar
basic.py.bak
basic.py
.bak
['.py', '.bak']
C:\Users\Public
C:\Users\Public
C:\Users
C:\
('C:\\', 'Users', 'Public', 'basic.py.bak')
```
### os.path
获取绝对路径： os.path.abspath()
```
import os
def ospath_test():
    print (os.path.abspath('basic.py'))
    testpath = 'C:/Users/Public/basic.py.bak'
    print (os.path.basename(testpath))
    print (os.path.dirname(testpath))
    print (os.path.exists(testpath))
    print (os.path.isfile(testpath))
    print (os.path.isdir(testpath))
    print (os.path.join('a/b', 'c/d'))
```

### 正则表达式
通读官方文档  
多次使用时，建议将表达式编译成正则表达式对象，然后 match
re 常量

匹配数量 ".{11}"
去除匹配成功的内容 group()
匹配的位数,获得匹配索引的起始和结束 span()

如果要对匹配结果进行分组，用“()”将分组的部分括起来，使用group() + 索引来提取分组内容  
查找： search 和 findall  
替换： sub
替换数字 sub('\d', 'a', '123@1234.com')
分割字符串 split。如果要保留分割字符， 加括号

```
import re
def re_test():
    content = '13311112222'
    print(re.match('.{11}', content))
    print(re.match('.{12}', content))
    print(re.match('.{7}', content).group())
    print(re.match('.{7}', content).span())
    
    email = '123@456.com'
    print (re.match('.*@.*com', email))
    
    print (re.match('(.*)@(.*)com', email).group(1))
    print (re.match('(.*)@(.*).com', email).group(2))
    
    print (re.search('@', email))
    print (re.findall('123', '123@1234.com'))
    
    print (re.sub('123', 'abc', '123@1234.com'))
    print (re.sub('\d', 'a', '123@1234.com'))
    
    print (re.split('@', email))
    print (re.split('(@)', email))
```
```
<re.Match object; span=(0, 11), match='13311112222'>
None
1331111
(0, 7)
<re.Match object; span=(0, 11), match='123@456.com'>
123
456
<re.Match object; span=(3, 4), match='@'>
['123', '123']
abc@abc4.com
aaa@aaaa.com
['123', '456.com']
['123', '@', '456.com']
```

### Python Daemon
PEP 3143 Standard daemon process library
https://python.org/dev/peps/pep-3143  

sys.stdout.write()

看看 python-daemon 的实现


## 异常的捕获
异常并不一定是错误。
比如生成器对象在最后一次next操作时，会发生StopIteration异常。

### traceback
[官方文档](https://docs.python.org/zh-cn/3.8/library/traceback.html)
打印异常信息的方法：
+ sys.exc_info(): 返回异常类型，异常value,traceback object
+ traceback.print_tb(), 需要传traceback object参数
+ traceback.print_exception()
+ traceback.print_exc() , print_exception()简化版，方便使用
+ traceback.format_exc()， 得到异常的字符串

```
def exc_func():
    1 / 0

def traceback_test():
    try:
        exc_func()
    except:
        e_type, e_value, tb_obj = sys.exc_info()
        print(e_type, e_value, tb_obj)
        print ("===========")
        traceback.print_tb(tb_obj, 2, sys.stdout)
        print ("=====  print_exception  ======")
        traceback.print_exception(e_type, e_value, tb_obj, 3, sys.stdout)
        print ("=====  print_exc  ======")
        traceback.print_exc()
        print ("=====  format_exc  ======")
        print (traceback.format_exc())
```
### 异常处理机制
* 异常也是一个类
* 异常捕获过程
  > 异常类把错误消息打包到一个Traceback对象
  > 该对象会自动查找调用栈信息
  > 直到运行系统找到明确声明如何处理这些类异常的位置
* 所有异常继承自BaseException

### 自定义异常
使用raise抛出异常
自定义异常类要继承Exception
实现构造函数__init__, 必须要传入ErrorInfo参数，
`super().__init__()`
实现__str__()魔术方法， 使异常可以像字符串一样去使用
```
class MyException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

def my_exc_test():
    try:
        raise MyException("What are you doing?")
    except Exception as e:
        traceback.print_exc()
```
输出：
```
Traceback (most recent call last):
  File "H:\Python\workspace\pythontrain\python-2.py", line 32, in my_exc_test
    raise MyException("What are you doing?")
MyException: What are you doing?
```

### 异常打印之“大美丽”版
安装并import第三方库 pretty_errors

### 对于文件的异常处理
使用[with语句](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-with-statement),免去了关闭文件处理

自己来实现一个[上下文管理器](https://docs.python.org/zh-cn/3/reference/datamodel.html#context-managers)
```
class c_a(object):
    def __init__(self):
        pass

    def call(self):
        print("call a.call()")

    def exc(self):
        print ("raise a exception")
        1 / 0

class ctx_mag:
    def __enter__(self):
        print ("enter")
        a = c_a()
        # 1 / 0
        
        return a
        
    def __exit__(self, exc_type, exc_value, traceback):
        print ("exit")

    def __call__(self):
        print ("run call")

with ctx_mag() as ctx:
    ctx.call()
    ctx.exc()
```
说明： 在ctx.exc()出现异常，`__exit__`会执行， c_a的构造函数和`__enter__`中出现异常，不会执行`__exit__`

```
c = ctx_mag()
c()
```
`__call__`将类伪装成函数来使用



## yield
yield与return的区别
return 一次性返回
yield依次返回

```
def yield_test():
    def chain():
        for i in range(5):
            yield i

    v = chain()
    print (v)  # <generator object yield_test.<locals>.chain at 0x000000000CF00318>
    v2 = next(v)
    print (v2)  # 0
    v3 = next(v)
    print (v3)  # 1
    v4 = list(v)
    print (v4)  # [2, 3, 4]
      
    try:
        v5 = next(v)
        print (v5)
    except Exception as e:
        print (e.__class__)   # <class 'StopIteration'>
```
chain()函数返回一个生成器对象

## 推导式
用来生成list,tuple,dict
生成tuple时要显示指定tuple， 如果不显示指定 tuple, 则会得到一个生成器对象。 
```
g = (i for i in range(10))
print (type(g))
# <class 'generator'>
```