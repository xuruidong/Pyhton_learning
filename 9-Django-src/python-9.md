# Python-9 Django 源码分析

用户请求路径的处理，如何对应view.  
view 与模板，模型的关联， view 如何对用户请求处理，以及如何返回给用户内容。  
模板
model 查询管理器的实现。

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

#### 用装饰器（闭包）来实现partial
示例：

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
1. 在include函数中， 对参数 arg 进行类型判断。
2. 如果是元组，对其拆分，格式为 (urlconf_module, app_name),
3. 如果是str， 使用 inport_module()函数导入：
```
if isinstance(urlconf_module, str):
    urlconf_module = import_module(urlconf_module)
```
4. 在导入的模块中获取 patterns 和 app_name。
```
patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
app_name = getattr(urlconf_module, 'app_name', app_name)
```
对 urlpatterns 校验:
```
# Make sure the patterns can be iterated through (without this, some
# testcases will break).
if isinstance(patterns, (list, tuple)):
    for url_pattern in patterns:
        pattern = getattr(url_pattern, 'pattern', None)
        if isinstance(pattern, LocalePrefixPattern):
            raise ImproperlyConfigured(
                'Using i18n_patterns in an included URLconf is not allowed.'
            )
```
5. 返回 (urlconf_module, app_name, namespace), 返回元组给path, path 会对类型进行判断：
```
def _path(route, view, kwargs=None, name=None, Pattern=None):
    if isinstance(view, (list, tuple)):
        # For include(...) processing.
        pattern = Pattern(route, is_endpoint=False)
        urlconf_module, app_name, namespace = view
        return URLResolver(
            pattern,
            urlconf_module,
            kwargs,
            app_name=app_name,
            namespace=namespace,
        )
    elif callable(view):
        pattern = Pattern(route, name=name, is_endpoint=True)
        return URLPattern(pattern, view, kwargs, name)
    else:
        raise TypeError('view must be a callable or a list/tuple in the case of include().')
```

#### import_module()
`def import_module(name, package=None):`  
利用此函数可以在程序运行时动态导入模块。

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
```
def index(request):
	print (type(request)) 
	print (request.__class__.__name__)
```
```
<class 'django.core.handlers.wsgi.WSGIRequest'>
WSGIRequest
```
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
在view 中对请求进行响应，一般可以返回 HttpResponse，
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
还有很多子类。

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

请求中间件， 在请求进行url 匹配前进行处理，如防止跨站攻击。  
view 中间件，在请求进入view 前对请求进行处理
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
Model 指定了元类，所以在创建Model 时不使用默认的`__new__`方法，而是会使用元类的`__new__`。  
ModelBase : `class ModelBase(type):` 符合元类的特点：继承自 type, 实现了`__new__`,并且返回了类。  
ModelBase 中实现了创建主键id 的功能。  
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
在 _prepare(cls) 中， opts._prepare(cls) 相当于是 Options._prepare(cls)

在 Options._prepare() 中，`if self.pk is None:` 如果主键是空，添加ID主键

### Model 的查询管理器
```
from .models import DoubanShort

# Create your views here.
def movies(request):
    queryset = DoubanShort.objects.all()
    # queryset = T1.objects.values('sentiment')
    condtions = {'stars__gte': 4}
    res = queryset.filter(**condtions)
    print (res)
    return render(request, 'index.html', locals())
```
自己实现的Model, 当继承了 models.Model ,就有了查询管理器, 进而可以使用objects.all() 等方法对数据库进行查询等操作。

* 如何让查询管理器的名字不是 objects
* 如何利用 Manager(objects) 实现对Model 的 CRUD?
* 为什么查询管理器返回 QuerySet 对象？

在 models.Model --> ModelBase --> _prepare() 中创建了查询管理器 Manager 对象，
在 ModelBase._prepare() 中：
```
if not opts.managers:
    if any(f.name == 'objects' for f in opts.fields):
        raise ValueError(
            "Model %s must specify a custom Manager, because it has a "
            "field named 'objects'." % cls.__name__
        )
    manager = Manager()
    manager.auto_created = True
    cls.add_to_class('objects', manager)
```
Manager 的定义：
```
class Manager(BaseManager.from_queryset(QuerySet)):
    pass
```
from_queryset 是一个类方法，在这里返回了新类 
```
@classmethod
def from_queryset(cls, queryset_class, class_name=None):
    if class_name is None:
        class_name = '%sFrom%s' % (cls.__name__, queryset_class.__name__)
    return type(class_name, (cls,), {
        '_queryset_class': queryset_class,
        **cls._get_queryset_methods(queryset_class),
    })
```
这里动态地创建了一个类。
返回的新类的名为 BaseManagerFromQuerySet ，并且使用 _get_queryset_methods 设置了属性（type 的功能），所以 Manager 继承自 BaseManagerFromQuerySet ，父类都是 QuerySet 。所以 Manager 拥有 QuerySet 大部分方法，如 get, create, filter等。  

_get_queryset_methods :
```
@classmethod
def _get_queryset_methods(cls, queryset_class):
    def create_method(name, method):
        def manager_method(self, *args, **kwargs):
            return getattr(self.get_queryset(), name)(*args, **kwargs)
        manager_method.__name__ = method.__name__
        manager_method.__doc__ = method.__doc__
        return manager_method

    new_methods = {}
    for name, method in inspect.getmembers(queryset_class, predicate=inspect.isfunction):
        # Only copy missing methods.
        if hasattr(cls, name):
            continue
        # Only copy public methods or methods with the attribute `queryset_only=False`.
        queryset_only = getattr(method, 'queryset_only', None)
        if queryset_only or (queryset_only is None and name.startswith('_')):
            continue
        # Copy the method onto the manager.
        new_methods[name] = create_method(name, method)
    return new_methods
```
将属于 queryset_class 的方法，但自身没有的方法（同名方法使用自身的）添加到 new_methods 并返回。对于内置方法（以下划线开头），跳过。

所以 objects 就是一个 Manager 实例，要对objects 改名可以在 Model 中创建一个 Manager 实例.
#### inspect --- 检查对象
在遍历 queryset_class 的方法时， 使用了 inspect  
[文档](https://docs.python.org/zh-cn/3/library/inspect.html)

## Template
### render 如何找到要加载的文件
render() 用于对模板的渲染。这里关注两个功能：
1. 如何找到 templates 目录，templates 名字是固定的，放在每个 app 中的。
2. 在 settings.py 中有一系列模板相关的配置，这些配置起到什么功能？
3. 对 html 中的一些过滤器、变量的替换是如何实现的？

一个栗子：
```
def movies(request):
    queryset = DoubanShort.objects.all()
    # queryset = T1.objects.values('sentiment')
    condtions = {'stars__gte': 4}
    res = queryset.filter(**condtions)
    print (res)
    return render(request, 'index.html', locals())
```
跳转到 render 定义：
```
def render(request, template_name, context=None, content_type=None, status=None, using=None):
    """
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """
    content = loader.render_to_string(template_name, context, request, using=using)
    return HttpResponse(content, content_type, status)
```
这里执行了 loader.render_to_string， 并返回了 HttpResponse 对象。
```
def render_to_string(template_name, context=None, request=None, using=None):
    """
    Load a template and render it with a context. Return a string.

    template_name may be a string or a list of strings.
    """
    if isinstance(template_name, (list, tuple)):
        template = select_template(template_name, using=using)
    else:
        template = get_template(template_name, using=using)
    return template.render(context, request)
```
在 render_to_string 中，实例中传入的是 'index.html', 先看 get_template, 
```
def get_template(template_name, using=None):
    """
    Load and return a template for the given name.

    Raise TemplateDoesNotExist if no such template exists.
    """
    chain = []
    engines = _engine_list(using)
    print ("=======", engines)
    for engine in engines:
        try:
            return engine.get_template(template_name)
        except TemplateDoesNotExist as e:
            chain.append(e)

    raise TemplateDoesNotExist(template_name, chain=chain)
```

_engine_list :
[<django.template.backends.django.DjangoTemplates object at 0x0000000004144128>]
```
def _engine_list(using=None):
    return engines.all() if using is None else [engines[using]]
```

engines 是 EngineHandler 对象。 在 EngineHandler 类中，实现了 `__getitem__`,可以以字典方式操作。  `__iter__` 所以可迭代。  
all() 方法的实现：
```
def all(self):
    return [self[alias] for alias in self]
```
真正被迭代的对象是 self.templates， templates 是被 cached_property 装饰后的方法：
```
@cached_property
def templates(self):
    if self._templates is None:
        self._templates = settings.TEMPLATES

    templates = OrderedDict()
    backend_names = []
    for tpl in self._templates:
        try:
            # This will raise an exception if 'BACKEND' doesn't exist or
            # isn't a string containing at least one dot.
            default_name = tpl['BACKEND'].rsplit('.', 2)[-2]
        except Exception:
            invalid_backend = tpl.get('BACKEND', '<not defined>')
            raise ImproperlyConfigured(
                "Invalid BACKEND for a template engine: {}. Check "
                "your TEMPLATES setting.".format(invalid_backend))

        tpl = {
            'NAME': default_name,
            'DIRS': [],
            'APP_DIRS': False,
            'OPTIONS': {},
            **tpl,
        }

        templates[tpl['NAME']] = tpl
        backend_names.append(tpl['NAME'])

    counts = Counter(backend_names)
    duplicates = [alias for alias, count in counts.most_common() if count > 1]
    if duplicates:
        raise ImproperlyConfigured(
            "Template engine aliases aren't unique, duplicates: {}. "
            "Set a unique NAME for each engine in settings.TEMPLATES."
            .format(", ".join(duplicates)))

    return templates
```
默认 self._templates 是 None， 所以先被赋值为  settings.TEMPLATES. 
all() 返回的是 self._engines[alias] 组成的list, 元素都是engine_cls， 


```
tmp = {'a': 1, 'b': 12}
tmp_b = {'c': 222, 'b': 333, **tmp}
print (tmp_b)
```
```
{'c': 222, 'b': 12, 'a': 1}
```
。。。

### 对模板的渲染
