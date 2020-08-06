# Python-3 照猫画虎我最强

## scrapy 并发
### 参数设置
在 settings.py 中可以进行设置相关参数。
```
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
```

### python 可变参数
[英文版](https://book.pythontips.com/en/latest/args_and_kwargs.html)
[中文版](https://docs.pythontab.com/interpy/args_kwargs/Usage_args/)

demo：
```
def args_test_func1(*args, **kwargs):
    print ("args len = %d" % (len(args)))
    print (args)
    
    print ("kwargs len = %d" % (len(kwargs)))
    print (kwargs)
    
    print("*"*20)
    

def args_test():
    print ("test 1:")
    args_test_func1(1, 2, 3, 4)
    # (1, 2, 3, 4)
    # {}
    
    print ("test 2:")
    a1 = (2, 3, 4, 5)
    args_test_func1(a1)
    # ((2, 3, 4, 5),)
    # {}
    
    print ("test 3:")
    args_test_func1(*a1)
    # (1, 2, 3, 4)
    # {}
    
    print ("test 4: kwargs")
    args_test_func1(a1 = "aa1", a2 = "bb2")
    # ()
    # {'a1': 'aa1', 'a2': 'bb2'}
    
    print ("test 5:")
    tmp = {"a1": "aa1", "a2": "bb2", "a3": "cc3",}
    args_test_func1(**tmp)
    # ()
    # {'a1': 'aa1', 'a2': 'bb2', 'a3': 'cc3'}
    
    print ("test 6:")
    args_test_func1(123, "ppp", *a1, **tmp)
    # (123, 'ppp', 2, 3, 4, 5)
    # {'a1': 'aa1', 'a2': 'bb2', 'a3': 'cc3'}
```


###  twisted
[Twisted documentation](https://twistedmatrix.com/documents/current/)

demo 没理解
<font color=#ff0000 size=5 face="黑体">在teisted 中，callbakc 是怎么和事件绑定的？只是添加callback, 确没有指定事件 </font>

## 多进程

#### 进程创建
* `os.fork()` 在类unix中使用， 根据返回值来判断父进程和子进程
* 使用 multiprocessing 库

#### Process
[来源](http://c.biancheng.net/view/2632.html)
multiprocessing 模块提供了 Process 类，该类可用来在 Windows 平台上创建新进程。和使用 Thread 类创建多线程方法类似，使用 Process 类创建多进程也有以下 2 种方式：
1. 直接创建 Process 类的实例对象，由此就可以创建一个新的进程；
2. 通过继承 Process 类的子类，创建实例对象，也可以创建新的进程。注意，继承 Process 类的子类需重写父类的 run() 方法。

##### Process 常用属性和方法
|属性名或方法名|功能|
|-|-|


Process()对象支持的方法 `['_Popen', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_bootstrap', '_check_closed', '_closed', '_config', '_identity', '_name', '_parent_pid', '_popen', '_sentinel', '_start_method', 'authkey', 'close', 'daemon', 'exitcode', 'ident', 'is_alive', 'join', 'kill', 'name', 'pid', 'run', 'sentinel', 'start', 'terminate']`

### 多进程调试
print大法好
可以打印pid, CPU, 等信息
模块名打印 `print (__name__)`
CPU核心数 `print (multiprocessing.cpu_count())`

#### super()
* 如果子类有了`__init__()`, 就不会去执行父类的`__init__()`
* 如果子类没有`__init__()`, 就会去执行父类的`__init__()`
* 可以使用super()执行父类中的函数， 比如`__init__()`
* super() 只是执行上一级父类中的函数，能否迭代调用祖先父类中的函数，要看父类函数如何实现了。

```
def super_test():
    class A(object):
        def __init__(self, arg):
            print ("class A __init__")
            self.arg = arg

        def get_arg(self):
            print (self.arg)

    class B(A):
        def __init__(self, arg):
            print ("B __init__")
            self.arg = arg

    class C(A):
        pass

    class D(A):
        def __init__(self, arg):
            print ("D __init__")
            super().__init__(arg)
            self.arg = arg + 2

    class E(B):
        def __init__(self, arg):
            print ("E __init__")
            super().__init__(arg)
            self.arg = arg

    class F(D):
        def __init__(self, arg):
            print ("F __init__")
            super().__init__(arg)
            self.arg = arg

    b = B(100)
    b.get_arg()

    c = C(200)
    c.get_arg()

    d = D(300)
    d.get_arg()

    e = E(400)
    e.get_arg()

    f = F(500)
    f.get_arg()
```
输出结果：
```
B __init__
100
class A __init__
200
D __init__
class A __init__
302
E __init__
B __init__
400
F __init__
D __init__
class A __init__
500
```

### 进程间通信

#### 进程间数据共享方式

队列
管道
共享内存

Python 中的进程队列原理是什么

#### 队列
Queue的init
`def __init__(self, maxsize=0, *, ctx)`

Queue  init  里的ctx,  是 <class 'multiprocessing.context.SpawnContext'>
import 的过程：  multiprocessing\__init__.py  -->  from . import context  -->

from multiprocessing import Queue  ，其实是导入 multiprocessing.context.BaseContext.Queue，   
```
def Queue(self, maxsize=0):
        '''Returns a queue object'''
        from .queues import Queue
        return Queue(maxsize, ctx=self.get_context())
```
#### 命名关键字参数
用来限制传参的名字， 不想关键字参数 **kwargs 可以传任意参数，不管有用没用
[抄一篇博客，压压惊](https://www.cnblogs.com/wkkkkk/p/5731947.html)



#### 管道





















jk:
root@ubuntu:~# cat /sys/class/net/tap1/tun_flags
0x1901 能通过这个flag间接看出来

jk:
#define IFF_MULTI_QUEUE 0x0100

Hsu Jui-tung:
这个只有标志， 没有队列数量吗

jk:
貌似没有，代码里写死的8个queue

