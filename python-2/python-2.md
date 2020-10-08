# Python-2 进击的菜鸟

## 异常的捕获
异常并不一定是错误。
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


## 使用pymysql
使用PyMySQL连接MySQL数据库流程：
- 创建connection,需要主机，端口，用户名密码等信息
- 获取游标cursor
- CRUD
- 关闭游标
- 关闭connection

[Documentation ](https://pymysql.readthedocs.io/en/latest/)
[PyMySQL tutorial](http://zetcode.com/python/pymysql/)
python 的类型提示（type hint）,并不是对类型的约束，也不是定义，
```
def func3(s: str):
    print (s)
```

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

### 模拟用户名密码上传：
[httpbin cookies](https://httpbin.org/#/Cookies)

```
def cookies_test():
    s = requests.Session()
    # Sets cookie(s) as provided by the query string and redirects to cookie list.
    # r = s.get('http://httpbin.org/cookies/set/cookies/123457',
    #          allow_redirects=False)
    # Sets a cookie and redirects to cookie list.
    r = s.get("https://httpbin.org/cookies/set?freeform=fffff")
    #print (r.text)
    #print (r.headers)
    #print (r.status_code)
    #print (dir(r))
    r = s.get("http://httpbin.org/cookies")
    print (r.text)
    print (r.status_code)
```
* `requests.Session()` 创建一个session，使两次请求在一个session内。在同一个Session实例发出的请求之间保持cookies。requests默认开启session功能，
  使用urllib3 的connection pooling功能，向同一主机发送多个请求，复用TCP连接
* 通过get httpbin.org/cookies/set 来设置cookies, 然后通过访问 httpbin.org/cookies 来查看cookies
* requests默认会接受重定向，如果使用默认设置，第一种方式可省略第二次请求
* 这里可以使用with语句

一般用户登录是通过post方式提交表单，

## WebDriver

[相关文档](https://pypi.org/project/selenium/)

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def webdriver_test():
    edge = webdriver.Edge("msedgedriver.exe")
    edge.get("http://www.baidu.com")
    print (edge.title)
    #elem = edge.find_element_by_id("kw")
    #elem.send_keys('seleniumhq' + Keys.RETURN)
    
    #elem = edge.find_element_by_xpath('//*[@id="kw"]')
    # elem = edge.find_element_by_link_text()  ????
    # elem = edge.find_element_by_name('wd')
    elem = edge.find_element_by_tag_name()  ???
    
    elem.send_keys('seleniumhq')
```
API没看完

### requests下载大文件
```
def big_file_download(url):
    r = requests.get(url, stream=True)
    with open("download", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
```
防止文件过大无法放入内存。
`param stream: (optional) if ``False``, the response content will be immediately downloaded.`

## 验证码识别
工具安装
* 安装依赖库 libpng, libjpeg,libtiff,leptonica   (未操作)
* 安装tesseract
  https://github.com/tesseract-ocr/tesseract/wiki
* MSYS2 可能会将tesseract安装到mingw64/bin下， 添加到PATH即可
* 设置环境变量 TESSDATA_PREFIX为 D:\msys64\mingw64\share\tessdata
* 考虑到环境变量生效问题，可在命令行下临时设置 TESSDATA_PREFIX
  ```
  set TESSDATA_PREFIX=D:\msys64\mingw64\share\tessdata
  tesseract c_th.jpg out
  ```
* 安装 pillow  `pip install pillow`
* 安装 pytesseract  `pip install pytesseract`

```
from PIL import Image
import pytesseract
def tesseract_test():
    
    im = Image.open('img_test.jpg')
    im.show()
    
    gray = im.convert('L')
    gray.save('c_gray.jpg')
    im.close()
    
    threshold = 100
    table = []

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    out = gray.point(table, '1')
    out.save('c_th.jpg')
    
    th = Image.open('c_th.jpg')
    print(pytesseract.image_to_string(th, lang='eng'))
```

## scrapy中间件
### scrapy日志分析
首先，使用scrapy, 爬取 httpbin.org/ip 可以得到出口IP地址
```
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print ("===========================")
        print (response.text)
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
```
以下是scrapy打印的日志信息：
```
  1 2020-07-31 16:41:48 [scrapy.utils.log] INFO: Scrapy 2.2.1 started (bot: spider1)
  2 2020-07-31 16:41:48 [scrapy.utils.log] INFO: Versions: lxml 4.3.0.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)],     pyOpenSSL 19.0.0 (OpenSSL 1.1.1b  26 Feb 2019), cryptography 2.6.1, Platform Windows-10-10.0.18362-SP0
  3 2020-07-31 16:41:48 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
  4 2020-07-31 16:41:48 [scrapy.crawler] INFO: Overridden settings:
  5 {'BOT_NAME': 'spider1',
  6  'NEWSPIDER_MODULE': 'spider1.spiders',
  7  'ROBOTSTXT_OBEY': True,
  8  'SPIDER_MODULES': ['spider1.spiders']}
  9 2020-07-31 16:41:48 [scrapy.extensions.telnet] INFO: Telnet Password: 650927d40fa72324
 10 2020-07-31 16:41:48 [scrapy.middleware] INFO: Enabled extensions:
 11 ['scrapy.extensions.corestats.CoreStats',
 12  'scrapy.extensions.telnet.TelnetConsole',
 13  'scrapy.extensions.logstats.LogStats']
 14 2020-07-31 16:41:48 [scrapy.middleware] INFO: Enabled downloader middlewares:
 15 ['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 16  'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 17  'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 18  'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 19  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 20  'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 21  'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 22  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 23  'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 24  'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 25  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 26  'scrapy.downloadermiddlewares.stats.DownloaderStats']
 27 2020-07-31 16:41:48 [scrapy.middleware] INFO: Enabled spider middlewares:
 28 ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 29  'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 30  'scrapy.spidermiddlewares.referer.RefererMiddleware',
 31  'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 32  'scrapy.spidermiddlewares.depth.DepthMiddleware']
 33 2020-07-31 16:41:48 [scrapy.middleware] INFO: Enabled item pipelines:
 34 []
 35 2020-07-31 16:41:48 [scrapy.core.engine] INFO: Spider opened
 36 2020-07-31 16:41:48 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
 37 2020-07-31 16:41:48 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
 38 2020-07-31 16:41:49 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://httpbin.org/robots.txt> (referer: None)
 39 2020-07-31 16:41:50 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://httpbin.org/ip> (referer: None)
 40 ===========================
 41 {
 42   "origin": "118.26.73.76"
 43 }
 44
 45 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 46 2020-07-31 16:41:50 [scrapy.core.engine] INFO: Closing spider (finished)
 47 2020-07-31 16:41:50 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
 48 {'downloader/request_bytes': 442,
 49  'downloader/request_count': 2,
 50  'downloader/request_method_count/GET': 2,
 51  'downloader/response_bytes': 425,
 52  'downloader/response_count': 2,
 53  'downloader/response_status_count/200': 2,
 54  'elapsed_time_seconds': 1.627012,
 55  'finish_reason': 'finished',
 56  'finish_time': datetime.datetime(2020, 7, 31, 8, 41, 50, 316774),
 57  'log_count/DEBUG': 2,
 58  'log_count/INFO': 10,
 59  'response_received_count': 2,
 60  'robotstxt/request_count': 1,
 61  'robotstxt/response_count': 1,
 62  'robotstxt/response_status_count/200': 1,
 63  'scheduler/dequeued': 1,
 64  'scheduler/dequeued/memory': 1,
 65  'scheduler/enqueued': 1,
 66  'scheduler/enqueued/memory': 1,
 67  'start_time': datetime.datetime(2020, 7, 31, 8, 41, 48, 689762)}
 68 2020-07-31 16:41:50 [scrapy.core.engine] INFO: Spider closed (finished)
```

* 1~3行输出一些组件版本信息等，使用twisted框架
* 4~8行是一些settings.py中的配置信息
* 9~34行是加载的中间件信息。这里的中间件是scrapy默认加载的中间件。
* 40~45， parse打印的内容
* 47~67， 打印scrapy状态，downloader信息，scheduler信息

如果不关心日志，可以使用--nolog选项来关闭日志。

### scrapy加载系统代理IP
* scrapy默认支持系统代理导入功能。
* 如果是Unix-like系统，可以导出环境变量http_proxy来设置HTTP代理,[一篇blog](https://www.cnblogs.com/EasonJim/p/9826681.html)
windows 可以在Internet属性中设置代理。
* 设置代理后，在settings.py中编辑DOWNLOADER_MIDDLEWARES，填写需要加载的中间件。
  加载'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware'
HttpProxyMiddleware 在 Python37\Lib\site-packages\scrapy\downloadermiddlewares\httpproxy.py
如果是windows, 读取注册表， linux读环境变量
* 下载中间件可以指定优先级， 根据优先级来确定加载顺序。如果需要屏蔽某个中间件，可以将优先级值写为`None`
* 如果要加载自己写的中间件，请转到middlewares.py房间， 编写中间件类。建议继承默认提供的类，然后再进行实现。


### 自己实现下载中间件
自定义中间件需要实现的功能：
读取settings配置

##### 编写一个下载中间件，需要实现的4个主要方法：
|方法|说明|
|-|-|
|`process_request(request, spider)`|request对象经过下载中间件时会被调用，优先级高先调用|
|`process_response(request, response, spider)`|response对象经过下载中间件时会被调用，优先级高后调用|
|`process_exception(request, exception, spider)`|当process_respinse()和process_request()抛出异常时会被调用|
|`from_crawler(cls, crawler)`|使用crawler来创建中间件对象，并**必须**返回一个中间件对象。一般在这里做一些初始化工作|

##### settings.py配置书写规则：
默认配置项名要大写， 自定义配置项建议大写

##### 自定义中间件实现流程
* 在settings.py中实现所需的配置项
* 在middlewares.py中实现中间件类
* 在DOWNLOADER_MIDDLEWARES中填写中间件导入路径，设置优先级。路径为  工程名.middlewares.中间件类名


##### 随机代理中间件的实现
+ settings.py配置项
  ```
  HTTP_PROXY_LIST = [
    'http://52.179.52.52:89',
    'http://112.112.112.112:1122'
  ]
  ```
+ 参考HttpProxyMiddleware类， 所以直接继承HttpProxyMiddleware实现
引入HttpProxyMiddleware 
`from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware `
`class RandomHttpProxyMiddleware(HttpProxyMiddleware):`
+ 读取settings配置
  中间件对象是在 from_crawler 由 crawler 创建的，所以要在 from_crawler 中读配置， 然后传参给 中间件的 `__init__`。
  from_crawler是一个类方法。在这里使用crawler.settings.get()方法来获取配置。如果配置不存在，抛出 NotConfigured 异常
  NotConfigured 在scrapy.exceptions中实现的，直接引入即可。
  ```
    def __init__(self, auth_encoding='latin-1', proxy_list=None):
        self.auth_encoding = auth_encoding
        self.proxies = defaultdict(list)
        for proxy in proxy_list:
            result = urlparse(proxy)
            # self.proxies[result[0]].append(proxy)
            self.proxies[result.scheme].append(proxy)
        print (self.proxies)
        # for type_, url in getproxies().items():
            # self.proxies[type_] = self._get_proxy(url, type_)
        #    print (type_)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        proxy_list = crawler.settings.get('HTTP_PROXY_LIST')
        print ("=============%s", proxy_list)
        if not proxy_list:
            raise NotConfigured
        auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING')
        return cls(auth_encoding, proxy_list)
  ```
+ 实现_set_proxy
  ```
    def _set_proxy(self, request, scheme):
        proxy = random.choice(self.proxies[scheme])
        print ("~~~~~~ ", proxy)

        request.meta['proxy'] = proxy
  ```

##### 其他知识点
[defaultdict](https://docs.python.org/3/library/collections.html)
装饰器

类方法：
```
def classmethod_test():
    class A(object):
        def __init__(self, arg):
            print ("in __init__, arg=%s" % arg)
            self.name = arg

        def age(self):
            print("age=18")
            return 18
        
        @classmethod
        def callme(cls, who):
            print("who am I?")
            print (who)
            cls.age(cls)
            
            return cls(who)

        def getname(self):
            return self.name

    a = A.callme("nb")
    print (a.getname())
```

## 分布式爬虫

scrapy 原生不支持分布式，多机之间需要Redis 实现队列和管道的共享。
scrapy-redis很好地实现了scrapy 和 Redis 的集成。

使用 scrapy-redis 之后，scrapy 的主要变化：
+ 使用了 RedisSpider 类代替了 Spider 类
+ Scheduler 的 queue 由 Redis 实现
+ item pipline 由 Redis 实现