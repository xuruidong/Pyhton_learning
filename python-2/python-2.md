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


## 使用pymysql
[Documentation ](https://pymysql.readthedocs.io/en/latest/)
python 的类型提示（type hint）,并不是对类型的约束，也不是定义，

### MySQL的编码
utf8mb4  utf8  utf-8 区别


### API

```
def run(self):
    conn = pymysql.connect(host=self.host, port=self.port,
                            user=self.user, password=self.password, db=self.db)
    cur = conn.cursor()
    # 游标创建时候，开启了一个隐形的事物
    try:
        for command in self.sqls:
            cur.execute(command)
            result.append(cur.fetchone())

        cur.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()
```

## 模拟浏览器头部信息

### 反爬虫的工作原理:
* 根据请求信息识别
* 根据行为来判断, 比如速度等

### 浏览器的基本行为
* 带http头信息：如User-Agent， Referer, host
* 带cookies (包含加密的用户名、密码验证信息)

referer可以用来防止跨站，获取跳转前上一个页面的信息。

### fake_useragent
导入 `from fake_useragent import UserAgent`
使用UserAgent时，会从网络中请求当前常用的一些浏览器的user-agent,通过`verify_ssl=False` 来设置不进行ssl验证，防止下载失败。
```
from fake_useragent import UserAgent
def useragent_test():
    ua = UserAgent(verify_ssl=False)
    print ("=================")
    print (f"chrome:{ua.chrome}")
    print (ua.random)
```

## 模拟登录
cookies有效期

```
def http_post_test():
    r = requests.post("http://httpbin.org/post", data={"key": "value"})
    print(r.json())
```

客户端通过post方式将用户名密码上传给服务器，服务器将其加密返回给客户端，客户端将加密的内容作为cookies的一部分。
模拟用户名密码上传：
