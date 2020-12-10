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

### twisted 异步IO框架
scrapy 使用的是twisted 异步 IO 框架。
```
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor

def response(*args, **kwargs):
    # print(args, kwargs)
    print('返回网页的内容')

def callback(*args):
    print('执行了一个回调',args)

@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode('utf-8'))
    d.addCallback(response)
    d.addCallback(callback)
    yield d

def stop(*args, **kwargs):
    reactor.stop()

urls = ['http://www.baidu.com','http://www.sougou.com']
li = []

for url in urls:
    ret = start(url)
    li.append(ret)
print(li)

d = defer.DeferredList(li)
d.addBoth(stop)
reactor.run()
```
twisted 参考文档： https://pypi.org/project/Twisted
asyncio 异步IO学习参考文档： https://docs.python.org/zh-cn/.7/libary/asyncio.html

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

#### 命名关键字参数
用来限制传参的名字， 不像关键字参数 **kwargs 可以传任意参数，不管有用没用
[抄一篇博客，压压惊](https://www.cnblogs.com/wkkkkk/p/5731947.html)

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

Process创建的进程， 主进程默认会等待子进程结束。

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

* 队列
* 管道
* 共享内存

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

#### 管道
```
from multiprocessing import Pipe

def f_pipe(pipe):
    pipe.send([100, None, "hello"])
    pipe.close()

    
def pipe_test():
    pipe_parent, pipe_child = Pipe()
    p = Process(target=f_pipe, args=(pipe_child, ))
    p.start()
    print(pipe_parent.recv())
    p.join()
```


#### 共享内存
```
from multiprocessing import Value
from multiprocessing import Array

def f_sharememory(n, a):
    n.value = 3.1415927
    for i in a:
        a[i] = -a[i]

def sharememory_test():
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    print(num.value)
    print(arr[:])
    
    p = Process(target=f_sharememory, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

### 进程锁
```
from multiprocessing import Lock
def lock_test_job(v, num, l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print (v.value, end="|")
        sys.stdout.flush()
    l.release()
    
def lock_test():
    l = Lock()
    v = Value('i', 0)

    p1 = Process(target=lock_test_job, args=(v, 1, l))
    p2 = Process(target=lock_test_job, args=(v, 1, l))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

好像是用信号量实现的， Posix 信号量，System V信号量
此外还可以使用线程锁共享， 将线程锁设置为进程间共享。
匿名锁与命名锁
[继续抄！](https://blog.csdn.net/luansxx/article/details/7736618)


### 进程池
```
from multiprocessing import Pool

def pool_test():
    p = Pool(4)
    for i in range(10):
        p.apply_async(run, (i,))

    p.close()
    p.join()
```

如果我们用的是进程池，在调用join()之前必须要先close()
并且在close()之后不能再继续往进程池添加新的进程
terminate()：一旦运行到此步，不管任务是否完成，立即终止。

```
def pool_test2():
    with Pool(processes=4) as pool:
        result = pool.apply_async(time.sleep, (3,))
        print (type(result))
        print (dir(result))
        print (result.get(timeout=1))
```
Pool 支持上下文管理器
获取结果可设置超时

#### Pool.map
这是什么？
```
def map_test_fun(x):
    return (x * x)
    

def map_test():
    with Pool(processes=4) as pool:
        #print (pool.map(map_test_fun, range(10)))
        for r in pool.imap(map_test_fun, range(10)):
            print (r)
```
map 以 list 形式返回结果， imap 返回结果的迭代器


## 多线程

### 线程的创建
使用 threading
* 函数方式创建 `threading.Thread(target = f, args=("ddd",))`
* 类方式创建 `class MyThread(threading.Thread)`

使用类方式创建，记得在`__init__` 中执行super()
可以通过is_alive() 方法获取线程运行状态
getName()

### 锁
#### 互斥锁

#### 可重入锁 threading.RLock()
A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it
    again without blocking; the thread must release it once for each time it has acquired it.
RLock 可以嵌套，使得函数可以递归调用

#### Condition
[Condition Objects](https://docs.python.org/3.7/library/threading.html#condition-objects)

wait_for 方法挺奇怪，不知道怎么用。

```
def func(conn,i):
    # print(i)
    while True:
        conn.acquire()
        conn.wait()
        print(i+100)
        conn.release()

def condition_test():
    c = threading.Condition()
    for i in range(5):
        t = threading.Thread(target=func,args=(c,i,))
        t.start()
    while True:
        r = input(">>>")
        if r == "yes":
            c.acquire()
            c.notify()
            c.release()
            print ("notify")
```
在执行 wait(),notify() 时，必须先加锁。


#### BoundedSemaphore
This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he used the names P() and V() instead of acquire() and release()).

A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call. The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().

#### Event

#### timer

#### Barrier Objects


### queue
queue.Queue()
put()
get()
task_done()
qsize()
empty()
full()

PriorityQueue() put操作时指定优先级
### dequeue

### deamon
观察状态

### 线程池
一般的线程池：
from multiprocessing.dummy import Pool as ThreadPool

```
from multiprocessing.dummy import Pool as ThreadPool

def handle(n):
    print("start %d" % n)
    time.sleep(0.5)
    print("end %d" % n)
    return 100 + n
    
def threadPoolTest():
    tmp = [1, 2, 3, 4, 5, 6]
    pool = ThreadPool(4)
    result = pool.map(handle, tmp)
    pool.close()
    pool.join()
    print ("pool.join")
    for r in result:
        print (r)
```

并行任务的高级封装（Python 3.2 以后）：
from concurent.futures import ThreadPoolExecutor

```
from concurrent.futures import ThreadPoolExecutor

def futuresTest():
    tmp = [1, 2, 3, 4, 5, 6]
    with ThreadPoolExecutor(3) as executor:
        executor.submit(handle, tmp)

    print ("submit test end")
    time.sleep(1)

    with ThreadPoolExecutor(3) as executor2:
        executor2.map(handle, tmp)

    print ("map test end")
    time.sleep(1)
```
如果执行函数中出现异常，不会有任何提示？



### 类scrapy 
```
import requests
from lxml import etree
from queue import Queue
import threading
import json

class CrawlThread(threading.Thread):
    '''
    爬虫类
    '''
    def __init__(self,thread_id,queue):
        super().__init__() 
        self.thread_id = thread_id  
        self.queue = queue

    def run(self):
        '''
        重写run方法
        '''
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟任务调度
    def scheduler(self):
        while True:
            if self.queue.empty(): #队列为空不处理
                break
            else:
                page = self.queue.get()
                print('下载线程为：',self.thread_id," 下载页面：",page)
                url = f'https://book.douban.com/top250?start={page*25}'
                headers = {
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                }
                try:
                    # downloader 下载器
                    response = requests.get(url,headers=headers) 
                    dataQueue.put(response.text)
                except Exception as e:
                    print('下载出现异常',e)

class ParserThread(threading.Thread):
    '''
    页面内容分析
    '''
    def __init__(self,thread_id,queue,file):
        threading.Thread.__init__(self)      # 上面使用了super()
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:                      # 这里有什么优化思路？
            try:
                item = self.queue.get(False) # 参数为false时队列为空，抛出异常
                if not item:                 # 为什么要判断？
                    continue
                self.parse_data(item)
                self.queue.task_done() # get之后检测是否会阻塞
            except Exception as e:
                pass
        print(f'结束线程：{self.thread_id}')

    def parse_data(self,item):
        '''
        解析网页内容的函数
        :param item:
        :return:
        '''
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')
                    link = book.xpath('./a/@href')
                    response={
                        'title':title,
                        'link':link
                    } 
                    #解析方法和scrapy相同，再构造一个json
                    json.dump(response,fp=self.file,ensure_ascii=False) 
                except Exception as e:
                    print('book error', e)

        except Exception as e:
            print('page error',e)


dataQueue = Queue() # 存放解析数据的queue
flag = False

if __name__ == '__main__':
    # 将结果保存到一个json文件中
    output = open('book.json','a',encoding='utf-8') 

    # 任务队列，存放网页的队列
    pageQueue = Queue(20) 
    for page in range(0,11): 
        pageQueue.put(page) 
    
    # 爬虫线程
    crawl_threads = []
    crawl_name_list = ['crawl_1','crawl_2','crawl_3'] 
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id,pageQueue)
        thread.start() 
        crawl_threads.append(thread)
    
    # 解析线程
    parse_thread = []
    parser_name_list = ['parse_1','parse_2','parse_3']
    for thread_id in parser_name_list: 
        thread = ParserThread(thread_id,dataQueue,output)
        thread.start() 
        parse_thread.append(thread)

    # 结束crawl线程
    for t in crawl_threads:
        t.join()
    
    # 结束parse线程
    flag = True
    for t in parse_thread:
        t.join() 

    output.close()
    print('退出主线程')
```











```
jk:
root@ubuntu:~# cat /sys/class/net/tap1/tun_flags
0x1901 能通过这个flag间接看出来

jk:
#define IFF_MULTI_QUEUE 0x0100

Hsu Jui-tung:
这个只有标志， 没有队列数量吗

jk:
貌似没有，代码里写死的8个queue
```
