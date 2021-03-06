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