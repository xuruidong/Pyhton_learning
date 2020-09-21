# Python-9 Django 源码分析

## URLconf 的偏函数

URLconf 用来指示如何处理用户请求的路径，如何与view进行匹配。view 关联了Modle， 模板Template。  
以下为一个Django项目的urls.py 示例：
```
from django.urls import path
from django.urls import re_path
from django.urls import register_converter
from . import views
from . import converters

register_converter(converters.IntConverter, 'myint') 

urlpatterns = [
    path('', views.index),
    re_path('(?P<year>[0-9]{4}).html', views.re_year, name='urlyear'),
    path('<myint:year>', views.myint)
]
```
在urlparttens 中，常见有两个函数： path() 和 re_path()。path() 用于匹配固定路径， re_path() 可以使用正则来匹配路径。

### path() 和 re_path() 的实现
查看path 和 re_path 的定义：
```
path = partial(_path, Pattern=RoutePattern)
re_path = partial(_path, Pattern=RegexPattern)
```
它们都是 partial 对象。 partial 在python 标准库中的 functools.py 中。  
查看[partial 文档](https://docs.python.org/zh-cn/3/library/functools.html#functools.partial)，可知，partial 用来固定函数的一些参数得到另一个函数，得到偏函数，方便使用。
path 就是将 _path 的Pattern 固定为RoutePattern 的片函数。

用装饰器（闭包）来实现partial
示例

### include 的实现
在urlpatterns 中通过include 可以引入另外一个文件（app 的 urls.py），来引入app中路径和view的对应关系。

***对元组拆分***
```
def tuple_test():
    *a, b = ("a", "b", "c", "d")
    print (a)   # ['a', 'b', 'c']
    print (b)   # d
```
拆分时不产生歧义。

#### include() 流程
在include函数中， 对参数 arg 进行类型判断。
如果是元组，对其拆分，格式为 (urlconf_module, app_name),
如果是str， 使用 inport_module()函数导入。
在导入的模块中获取 patterns 和 app_name。
对 urlpatterns 校验，
返回 (urlconf_module, app_name, namespace)

#### inport_module()


## view视图的请求过程
view 可以加载Model中的数据，也可以通过render()方法来渲染Template 模板。还有核心功能：处理用户发送的请求，并且将请求结果返回给用户。  
一个views.py示例：
```
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello Django!")
	

def re_year(request, year):
	return render(request, 'yearview.html')


def myint(request, year):
	# return HttpResponse(year+10)
	return redirect("http://www.baidu.com")
```
所有的view 函数都带有参数 request, 也就是用户的请求信息。
### 请求如何到达view

view 函数参数的request, 是 <class 'django.core.handlers.wsgi.WSGIRequest'>， WSGIRequest 继承于django.http.HttpRequest 每收到一个请求，就会产生一个 WSGIRequest 对象。  
那么 request 是在什么地方产生的呢？ 在启动服务时， 运行了 manager.py， 调用了WSGI， request就是由 WSGI 创建的。
处理完请求后，返回内容，可以返回一个 HttpResponse 对象。

WSGIRequest 在`__init__`中并没有调用super, 所以像 META 的属性被重新赋值定义，其他的如GET等被定义为被 cached_property 装饰的方法。 
META 是元信息，保存了系统环境变量，HTTP 头信息，URL请求参数等等。
在 HttpRequest 和 WSGIRequest 中，GET 是 QueryDict， QueryDict 继承自 MultiValueDict ，dict，用来保存url 参数，键对应的是list， 如访问 http://127.0.0.1:8000/?a=1&b=wwwwwwwwwwwwww&a=22，GET 值是 <QueryDict: {'a': ['1', '22'], 'b': ['wwwwwwwwwwwwww']}> ，打印结果为什么是这样的呢？ 因为在 MultiValueDict 中
```
def __repr__(self):
    return "<%s: %s>" % (self.__class__.__name__, super().__repr__())
```

#### cached_property
WSGIRequest 的 GET、COOKIES 等方法被 cached_property 装饰。
```

```

### 对响应的处理
[HttpResponse 用法](https://docs.djangoproject.com/zh-hans/2.2/ref/request-response/#django.http.HttpResponse)

在返回 HttpResponse 对象时，可以通过关键字参数指定header 信息，
`return HttpResponse("Hello Django!", content_type="text/abc")`

返回Json 格式：
```
from django.http import JsonResponse
res = JsonResponse({'a': 1, "b": "ddd"})
```

在 HttpResponseBase（HttpResponse 的父类）中实现了 `__setitem__, __delitem__` 等方法，所以可以像操作字典的方式对响应头信息进行设置：
```
res = JsonResponse({'a': 1, "b": "ddd"})
res['abc'] = "ddddddd"
```
一些常用的的响应子类，如404
```
return HttpResponseNotFound("aaavvvvvvddd")
```

### 总结
![DjangoFlowchart](DjangoFlowchart.png)
1. User requests a page
2. Request reaches ***Request Middlewares***, which could manipulate or answer the request
3. The ***URLConf*** finds the related View using urls.py
4. ***View Middlewares*** are called, which could manipulate or answer the request
5. The ***view*** function is invoked
6. The ***view*** could optionally access data through models
7. All model-to-DB interactions are done via a ***manager***
8. Views could use a special context if needed
9. The context is passed to the ***Template*** for rendering

a. Template uses ***Filters*** and ***Tags*** to render the output
b. Output is returned to the view
c. HTTPResponse is sent to the ***Response Middlerwares***
d. Any of the response middlewares can enrich the response or return a completely new response
e. The response is sent to the user’s browser.

## Model
当自定义Model 类时，要继承 models.Model ，此时 Django 会自动创建 id 主键， 自动拥有查询管理器对象，可以使用查询管理器提供的内置查询等命令。可以使用 ORM API 对数据库实现 CRUD  
以下是一个示例：
```
class Name(models.Model):
    # id 被自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)
```

### id 创建过程
转到 models.Model 的定义，
```
class Model(metaclass=ModelBase):
    ...
```
Model 指定了元类，所以在创建Model 时会使用元类的`__new__`。
ModelBase : `class ModelBase(type):` 符合元类的特点：继承自 type, 实现了`__new__`,并且返回了类。
在 `ModelBase.__new__` 中，先判断初始化的对象是不是本身：
```
# Also ensure initialization is only performed for subclasses of Model
# (excluding Model class itself).
parents = [b for b in bases if isinstance(b, ModelBase)]
if not parents:
    return super_new(cls, name, bases, attrs)
```
***什么情况下会执行到这里？***
然后创建了一个类。
添加 _meta 属性：`new_class.add_to_class('_meta', Options(meta, app_label))`
在返回新类前，执行了：
```
new_class._prepare()
new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
```
8:58