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
