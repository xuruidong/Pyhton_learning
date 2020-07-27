# Python训练营2

## 异常的捕获
异常并不完全是错误。
正如[python-1](../python-1/python-1.md)中yield部分中的例子，生成器对象在最后一次next操作时，会发生StopIteration异常。

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
  > 异常类把错误消息打包到一个对象
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

### 异常打印之大美丽版
第三方库 pretty_errors
好像windows下不起作用

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


## 使用pymysql
