# Python-6 Django

## Web 框架
### 常见的 web 框架：
* web.py
* Django
* tronado
* FALSK
* AIOHTTP
* FASTcgi

这些都遵循 MVC 设计模式，

### Django 框架简介
开源
### MTV框架
![Django](Django11.png)

浏览器发送请求
Views 视图层接收请求
Views 视图层调用models
Models 模型层创建模型
Models 模型层实行CURD（获取数据）
Views 视图层调用模板
Trmplates 
Views 视图层将数据填充到模板上再响应客户端

### Django 的特点
采用了MTV框架
强调快速开发和代码复用，DRY (Do Not Repeat Youself)
组件丰富：
ORM(对象关系映射)映射类来构建数据模型
URL支持正则表达式
模板可继承
内置用户认证，提供用户认证和权限功能
admin 管理系统
内置表单模型、Cache缓存系统、国际化系统等


## Getting Start

### 安装
建议使用2.2版本

pip install django==2.2.13

### 创建项目
启动Django 主要分三个步骤：
* 创建Django项目
* 创建应用程序
* 启动

#### 创建Django项目
使用 django-admin 命令
$ django-admin startproject MyDjango
之后会创建如下目录结构：
```
E:\LINUX\NOTE\PYTHON\PYTHON-6\DJANGO_TEST
└─MyDjango
    ├─manage.py
    └─MyDjango
        ├─__init__.py
        ├─settings.py
        ├─urls.py
        └─wsgi.py
```
其中， manage.py 是命令行工具， 通过 python manage.py help 可查看支持的操作。
settings.py是项目配置文件。

#### 创建 Django 应用程序
$python manage.py startapp index
创建名为index的app。之后会创建一系列的文件和目录， 其中models.py 就是模型， views.py是视图相关内容。
```
E:\LINUX\NOTE\PYTHON\PYTHON-6\DJANGO_TEST\MYDJANGO\INDEX
├─__init__.py
├─admin.py
├─apps.py
├─models.py
├─tests.py
├─views.py
└─migrations
    └─__init__.py
```
此时，该项目已经可以运行，显示Django的欢迎界面。
$python manage.py runserver
访问 http://127.0.0.1:8000/ 即可。默认开启DEBUG。
如果需要修改端口或者服务IP， 加参数：
$ python manage.py runserver 0.0.0.0:9000

## settings.py 配置文件
配置文件包括：
* 项目路径
* 密钥
* 域名访问权限
* APP列表 (INSTALLED_APPS)
* 静态资源、包括CSS,JavaScript 图片等
* 模板文件
* 数据库配置
* 缓存
* 中间件

大部分不需要修改。
[For more information on this file](https://docs.djangoproject.com/en/2.2/topics/settings/)
[For the full list of settings and their values](https://docs.djangoproject.com/en/2.2/ref/settings/)

app 列表
```
INSTALLED_APPS = [
    # 内置的后台管理系统
    'django.contrib.admin',
    # 内置的用户认证系统
    'django.contrib.auth',
    # 所有 Model元数据
    'django.contrib.contenttypes',
    # 会话，表示当前访问网站的用户身份
    'django.contrib.sessions',
    # 消息提示
    'django.contrib.messages',
    # 静态资源路径
    'django.contrib.staticfiles',
    # 注册自己的APP
]
```

中间件是request 和 response 对象之间的钩子
url匹配配置， 默认使用 MyDjango.urls， 即 urls.py

Django中的数据库默认使用sqlite，

## url 调度器
URLconf
当一个用户请求 Django 站点的一个页面：
1. 如果传入 HTTPRequest 对象拥有urlconf属性（通过中间件设置），它的值将被用来代替ROOT_URLCONF设置。
2. Django 加载 URLconf 模块并寻找可用的urlpatterns， Django 依次匹配每个URL模式，在与请求的URL匹配的第一个模式停下来。
3. 一旦有URL匹配成功，Django导入并调用相关的视图，视图会获得如下参数：
* 一个 HTTPRequest 实例
* 一个或多个位置参数提供
4. 如果没有URL被匹配，或者匹配过程中出现了异常，Django 会调用一个适当的错误处理视图。

实现 访问http://127.0.0.1:8000 返回固定的字符串
在urls.py中， urlpatterns=[] 
```
urlpatterns = [
    path('admin/', admin.site.urls),
]
```
path函数第一个参数是请求的http://127.0.0.1:8000/admin， 返回admin.site.urls ？？？ 没懂！！！
如果路径不在项目中，而是在app中，除了使用path来做路径和视图的匹配关系外, 还可以通过 include 来导入应用程序，如：
`path('', include('index.urls'))`,当访问 http://127.0.0.1:8000 时，就会找index 下的urls.py文件。
include 需要额外引入。
此时， 要对“”路径和view进行匹配，在index/urls.py中对路径进行解析。
```
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
]
```
对于路径“”， 去找views.index。

在views.py 中实现index函数
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello Django!")
```

## 模块和包
* 模块：Python 中一个以 .py 结尾的文件就是一个模块，模块中定义了变量、函数等来实现一些类似的功能。Python 有很多自带的模块（标准库）和第三方模块，一个模块可以被其他模块引用，实现了代码的复用性。
* 包：包是存放模块的文件夹，包中包含 `__init__.py` 和其他模块，`__init__.py` 可为空也可定义属性和方法，在 Python3.3 之前的版本，一个文件夹中只有包含`__init__.py`，其他程序才能从该文件夹引入相应的模块、函数等，之后的版本没有 `__init__.py` 也能正常导入，简单来说就是 Python3.3 之前的版本，`__init__.py` 是包的标识，是必须要有的，之后的版本可以没有。


[Python __all__](http://c.biancheng.net/view/2401.html)

模块的导入
```
import MyPackage.Model1
from MyPackage import Model1 as M
```
在module2.py 中使用module.py中的内容：
` from . import Module1`

如果在同级目录下存在包Pkg2
在Module2.py中 `from .Pkg2 import xxx`


## URL 匹配
固定url匹配使用起来有局限性。Django 可以判断用户输入的url 类型，如数字，字符串。也支持正则表达式。还可以自定义匹配规则函数。

### 带变量的URL
Django 支持URL 设置变量，变量类型包括：
* str
* int
* slug （备注）
* uuid
* path

使用方法： path( <变量类型：变量名>, 处理函数 )
`path('<int:year>', views.myyear)` 表示传入的参数会赋值给year变量，如果不是纯数字形式，会报错。url path 是整数时匹配。
__Coding Time：__
在index/urls.py 中，urlpatterns 中添加：
```
urlpatterns = [
    path('', views.index),
    path('<int:year>', views.year),
]
```
在views.py中实现year函数：
```
def year(request, year):
	return HttpResponse(year+1)
```
第一个参数必须是 request, 第二个参数只接收来的参数。
如果访问的url path 不能匹配到 urlpatterns， 会返回 404.

对于路径模式 path('<int:year>/<str:name>', views.name), name 函数要接收多个参数，可以使用 **kwargs 
```
def name(request, **kwargs):
	print (kwargs)
	return HttpResponse(kwargs['name'])
```

### 正则 URL
使用正则表达式时，就不能用path函数了，要使用re_path. 