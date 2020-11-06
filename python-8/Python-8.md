# Python-8 

## 变量赋值
Python的基本数据类型非常丰富。赋值时存在一些需要注意的问题， 如连续赋值。

### 测试题：
1. 
```
    a = 123
    b = 123
    c = a
    print(id(a))
    print(id(b))
    print(id(c))
    print(a is b)
```
输出结果：
```
8791162909136
8791162909136
8791162909136
True
```
* 判断两个变量是不是同一个对象，可以使用is。比较的是内存地址，使用id()可以获取
* a 和 b 为什么是同一个对象？

2. 连续赋值

```
    a = 345
    print ("after change a:")
    print(id(a))
    print(id(c))
    c = 789
    print ("after change c:")
    print(id(a))
    print(id(c))
    c = b = a
    print(a, b, c)
```
输出结果：
```
after change a:
57343824
8791162909136
after change c:
57343824
48750896
345 345 345
```
* 改变a的值，a对象改变？
* a对象变了，但对象没变。
* c 改变了，但a
* 连续赋值，和C++行为一样哦

3. 序列对象

```
    x = [1, 2, 3]
    y = x
    x.append(4)
    print ("after : x.append(4)")
    print(y)

    print ("id(x[1])=", id(x[1]))
    x[1] = 7
    print ("after : x[1] = 7")
    print ("id(x[1])=", id(x[1]))
    print(y)

    x[0], x[1], x[2] = 4, 5, 6
    print(y)
    
    x = [9, 9, 6]
    print(y)
```
输出结果：
```
after : x.append(4)
[1, 2, 3, 4]
id(x[1])= 8791162905264
after : x[1] = 7
id(x[1])= 8791162905424
[1, 7, 3, 4]
[4, 5, 6, 4]
[4, 5, 6, 4]
```
* 对x 增加元素，修改部分元素，不改变y
* 对x进行赋值操作，x对象改变

### 变量的划分
从内存使用的角度划分
* 可变数据类型
* 不可变数据类型

#### 不可变数据类型
* 整型
* 浮点型
* 字符串型
* 元组

不可变数据类型 传递对象本身？？？

#### 可变数据类型
* 列表
* 字典

传递引用

在高级语言中，变量是对内存及其地址的抽象。对于python而言，python的一切变量都是对象，变量的存储，采用了引用语义的方式，存储的只是一个变量的值所在的内存地址，而不是这个变量的只本身。  
在C/C++ 中, 变量是内存地址的名字，对变量赋值、修改，不会影响到变量的内存地址；
在Python中，对于不可变数据类型，值（对象）是真实存在于内存中，对变量赋值，只是让变量指向值（对象）。
不可变数据对象，无论有多少个引用，只占一块内存。 比如，某个计算流程不断产生新数字，就会不断产生对象，占用内存空间。

a=1, 内存中会有对象1， a是对象1的引用，a=2, 会在内存中创建对象2， 并将a引用对象2. b=1, 此时 a和b指向的是同一个对象。

## 序列
### 序列的分类
容器序列： list,tuple, collections.deque, 可以存放不同类型的数据
扁平序列：str,bytes,bytearray,memoryview(内存视图)，array.array, 存放的是相同类型的数据
### 容器序列的深浅拷贝

浅拷贝（shallow copy）和深度拷贝（deep copy）是针对容器序列的概念。
#### 浅拷贝
常见的浅拷贝的方法，是使用数据类型本身的构造器，比如下面两个例子：
```
list1 = [1, 2, 3]
list2 = list(list1)
print(list2)
print("list1==list2 ?",list1==list2)
print("list1 is list2 ?",list1 is list2)
set1= set([1, 2, 3])
set2 = set(set1)
print(set2)
print("set1==set2 ?",set1==set2)
print("set1 is set2 ?",set1 is set2)
```
运行结果为：
```
[1, 2, 3]
list1==list2 ? True
list1 is list2 ? False
{1, 2, 3}
set1==set2 ? True
set1 is set2 ? False
```
在上面程序中，list2 就是 list1 的浅拷贝，同理 set2 是 set1 的浅拷贝。

对于可变的序列，还可以通过切片操作符“：”来完成浅拷贝，例如：
```
list1 = [1, 2, 3]
list2 = list1[:]
print(list2)
print("list1 == list2 ?", list1 == list2)
print("list1 is list2 ?", list1 is list2)
```
输出结果：
```
[1, 2, 3]
list1 == list2 ? True
list1 is list2 ? False
```
切片操作，虽然是全切，但仍然产生的是新对象。

Python 还提供了对应的函数 copy.copy() 函数，适用于任何数据类型。
```
import copy
list1 = [1, 2, 3]
list2 = copy.copy(list1)
print(list2)
print("list1 == list2 ?",list1 == list2)
print("list1 is list2 ?",list1 is list2)
```
输出结果：
```
[1, 2, 3]
list1 == list2 ? True
list1 is list2 ? False
```

不过需要注意的是，对于元组，使用 tuple() 或者切片操作符 ':' 不会创建一份浅拷贝，相反它会返回一个指向相同元组的引用：
```
tuple1 = (1, 2, 3)
tuple2 = tuple(tuple1)
print(tuple2)
print("tuple1 == tuple2 ?",tuple1 == tuple2)
print("tuple1 is tuple2 ?",tuple1 is tuple2)
```
输出结果：
```
(1, 2, 3)
tuple1 == tuple2 ? True
tuple1 is tuple2 ? True
```

浅拷贝，指的是重新分配一块内存，创建一个新的对象，但里面的元素是原对象中各个子对象的引用。

#### 深拷贝

对数据采用浅拷贝的方式时，如果原对象中的元素不可变，那倒无所谓；但如果元素可变，浅拷贝通常会出现一些问题，例如：
```
list1 = [[1, 2], (30, 40)]
list2 = list(list1)
list1.append(100)
print("list1:",list1)
print("list2:",list2)
list1[0].append(3)
print("list1:",list1)
print("list2:",list2)
list1[1] += (50, 60)
print("list1:",list1)
print("list2:",list2)
list1[0] = [7, 7, 7]
print("list1:", list1)
print("list2:", list2)
```
输出结果：
```
list1: [[1, 2], (30, 40), 100]
list2: [[1, 2], (30, 40)]
list1: [[1, 2, 3], (30, 40), 100]
list2: [[1, 2, 3], (30, 40)]
list1: [[1, 2, 3], (30, 40, 50, 60), 100]
list2: [[1, 2, 3], (30, 40)]
list1: [[7, 7, 7], (30, 40, 50, 60), 100]
list2: [[1, 2, 3], (30, 40)]
```
* list1和list2是两个对象，所以list1 进行append操作不会影响到list2
* 由于是浅拷贝，list1[0]和list2[0]是同一个对象，会相互影响
* 元组是不可变的，拼接后产生了新的元组对象，作为了list1的第二个元素。而list2并没有引用新元组，所以list2不受影响
* list1[0]是list, 虽然是可变数据类型，但赋值操作使其指向了新的对象，而list2并没有引用新list,所以list2不受影响

使用浅拷贝可能带来的副作用。如果想避免这种副作用，完整地拷贝一个对象，就需要使用深拷贝。所谓深拷贝，是指重新分配一块内存，创建一个新的对象，并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。因此，新对象和原对象没有任何关联。

Python 中以 copy.deepcopy() 来实现对象的深度拷贝。
```
list1 = [[1, 2], (30, 40)]
list2 = copy.deepcopy(list1)

list1[0].append(3)
print("list1:",list1)
print("list2:",list2)
```
输出结果：
```
list1: [[1, 2, 3], (30, 40)]
list2: [[1, 2], (30, 40)]
```

不过，深度拷贝也不是完美的，往往也会带来一系列问题。如果被拷贝对象中存在指向自身的引用，那么程序很容易陷入无限循环，例如：
```
list1 = [1]
list1.append(list1)
print(list1)
list2 = copy.deepcopy(list1)
print(list2)
```
输出结果：
```
[1, [...]]
[1, [...]]
```
此例子中，列表 x 中有指向自身的引用，因此 list1 是一个无限嵌套的列表。但是当深度拷贝 list1 到 list2 后，程序并没有出现栈溢出的现象。这是为什么呢？

其实，这是因为深度拷贝函数 deepcopy 中会维护一个字典，记录已经拷贝的对象与其 ID。拷贝过程中，如果字典里已经存储了将要拷贝的对象，则会从字典直接返回。通过查看 deepcopy 函数实现的源码就会明白：
```
def deepcopy(x, memo=None, _nil=[]):
    """Deep copy operation on arbitrary Python objects.
       
    See the module's __doc__ string for more info.
    """
   
    if memo is None:
        memo = {}
    d = id(x) # 查询被拷贝对象 x 的 id
    y = memo.get(d, _nil) # 查询字典里是否已经存储了该对象
    if y is not _nil:
        return y # 如果字典里已经存储了将要拷贝的对象，则直接返回
        ...
```

## 字典和扩展内置数据类型
collections用来扩展内置数据类型。
字典的key，必须是可以进行hash的数据类型,不可变的数据类型。


### 用collections用来扩展内置数据类型
collections是Python内建的一个集合模块，提供了许多有用的集合类。
几种常用的数据类型
[教程](https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456)

#### nametuple

namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
```
from collections import namedtuple
def namedtuple_test():
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(1, 2)
    p2 = Point(3, 5)

    print (f"point1 ({p1.x}, {p1.y})")
    print (f"point2 ({p2[0]}, {p2[1]})")
    print ("p1 is Point? ", (p1 is Point))
    print ("p1 is tuple? ", (p1 is tuple))
    print ("p1 is Point? ", isinstance(p1, Point))
    print ("p1 is tuple? ", isinstance(p1, tuple))
```
输出结果：
```
point1 (1, 2)
point2 (3, 5)
p1 is Point?  False
p1 is tuple?  False
p1 is Point?  True
p1 is tuple?  True
```
is 用来判断两个变量是不是同一个对象

#### Counter

```
def counter_test():
lis = ['a', 'dd', 23, 342]
c = Counter(lis)
print (c)

c.update('hello')  # 也可以一次性update
print (c)

print (c.most_common(3))
print(c['l'])
```
输出结果：
```
Counter({'a': 1, 'dd': 1, 23: 1, 342: 1})
Counter({'l': 2, 'a': 1, 'dd': 1, 23: 1, 342: 1, 'h': 1, 'e': 1, 'o': 1})
[('l', 2), ('a', 1), ('dd', 1)]
2
```

#### dequeue

#### defaultdict

#### OrderedDict
能否用来实现LRU ?

#### ChainMap


## 函数
使用类产生函数
函数的调用
函数的作用域
函数的参数处理
函数的返回值

```
class func_class(object):
    def __call__(self):
        return "111"

fc = func_class()
print(fc())
```

### 变量作用域
命名空间

Type Hint
Pyhton 作用域遵循LEGB规则。
LEGB含义：
* L-Local(function): 函数内名字空间
* E-Enclosing function locals;外部嵌套函数的名字空间（例如closure）
* G-Global(module): 函数所在模块（文件）的名字空间
* B-Builtin(Python): Python 内置模块的名字空间

四个不同作用域

```
x = "Global"
def func2():
    x = 'enclosing'
    def func3():
        x = 'Local'
        print(x)  # 函数内变量优先

    func3()
func2()
print(x) # 同作用域变量优先,不会去低等级作用域去查找

```
输出：
```
Local
Global
```

闭包：
```
x = "Global"
def func2():
    x = 'enclosing'
    def func3():
        return x

    return func3

f = func2()
print(f())
print(x)
```

```
enclosing
Global
```

print (dir(__builtins__)) 打印内置变量

#### nonlocal 语句
[nonlocal 语句](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#the-nonlocal-statement)

```
def outer():
    v = 2
    def inner():
        t = v + 1
        print(t)
        v = t
        return v
    return inner
```
在 `t = v + 1` 处报错， builtins.UnboundLocalError: local variable 'v' referenced before assignment。
因为这个作用域里有改变 v 本身的操作：v = t，所以 v 被认为是一个内部的变量，而我们并不能在这个作用域里找到它的定义。
这个时候需要使用 nonlocal 关键字，把 v 声明为外部作用域的变量。
```
def outer():
    v = 2
    def inner():
        nonlocal v
        t = v + 1
        print(t)
        v = t
        return v
    return inner
```
同理，局部作用域里引用全局变量是可以的，但是当你要改变它时，需要加上global关键字。
```
g = "abc"
def global_test():
    print (g)
    # g = "111"  # builtins.UnboundLocalError: local variable 'g' referenced before assignment  at  print (g)
    print ("end", g)
```


### 函数参数
位置参数(arg1,arg2)，
关键字参数(arg1="abc",arg2="bcd")
包裹位置传递(*args)
包裹关键字传递(**kwargs)
可变长参数: 包裹位置传递 和 包裹关键字传递
[笔记链接](../python-3/python-3.md)

#### 偏函数
functools.partial: 返回一个可调用的partial对象
使用方法： partial(func, *args, **kwargs)

比如某函数func 需要多个参数，但一部分参数经常是固定的，此时就可以使用partial对其进行包裹。比如Django 的urlconf 中的path, 

```
import functools

def add(a, b):
    return a + b
    
def partial_test():
    add_1 = functools.partial(add, 1)
    print (add_1(10))
```

#### 高阶函数
函数的参数和返回值是函数。???
现在不常用，被lambda表达式代替。

lambda表达式相当于是匿名函数，实现简单的功能，使用高阶函数的使用一般使用lambda表达式。

常见的高阶函数： man, reduce, filter, apply(在python 2.3中被移除)
reduce 被放在了 functools包中。
推导式和生成器可以替代map 和 filter函数。

##### map

[教程](https://www.runoob.com/python/python-func-map.html)
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map() 函数语法：

map(function, iterable, ...)

```
def square(x):
    return x**2

def map_test():
    m = map(square, range(5))
    print (next(m))
    for it in m:
        print (it)
```
```
0
1
4
9
16
```

##### reduce
```
from functools import reduce
def add(a, b):
    return a + b

def reduce_test():
    a = [1, 2, 3, 4, 5]
    b = reduce(add, a)
    print (b) # 15
```
依次进行两两相加

##### filter

```
def is_odd(x):
    return x % 2 == 0

def filter_test():
    a = [1, 2, 3, 4, 5]
    b = filter(is_odd, a)
    print (type(b)) #<class 'filter'>
    print (list(b)) #[2, 4]
```

***看 functools 和 itertools文档***


### 函数返回值
函数返回，可以使用关键字return 和yield。
如果返回的是可调用对象，叫作闭包。

#### 闭包

内部函数对外部函数作用域里变量的引用（非全局变量），称你不函数为闭包。  
闭包，又称闭包函数或者闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，闭包中外部函数返回的不是一个具体的值，而是一个函数。一般情况下，返回的函数会赋值给一个变量，这个变量可以在后面被继续执行调用。
例如，计算某直线上点的值：
```
def y(a, b, x):
    return a * x + b
```
如果求同一条直线上的点：
```
y1 = y(2, 1, 100)
y1 = y(2, 1, 103)
y1 = y(2, 1, 104)
```
写成闭包形式：
```
def y(a, b):
    def _y(x):
        return a * x + b
    return _y

f = y(2, 1)
y1 = f(100)
y2 = f(103)
y3 = f(104)
```
比较简洁，优雅很多。
闭包可以避免使用全局值并提供某种形式的数据隐藏。它还可以提供面向对象的解决问题的解决方案。
当在类中几乎没有方法(大多数情况下是一种方法)时，闭包可以提供一个替代的和更优雅的解决方案。 但是当属性和方法的数量变大时，更好地实现一个类。

比如要实现对函数调用次数计数的功能：
```
def counter(start):
    count = [start]
    def incr():
        count[0] += 1
        return count[0]
    return incr

c1 = counter(10)
print (c1())        # 11
print (c1())        # 12
```

也可以写出这样：
```
def counter(start):
    count = start
    def incr():
        nonlocal count
        count += 1
        return count
    return incr
```

#### 函数中的变量
打印函数使用的局部变量：
```
def var_f():
    var_b = 10
    
    def inner(x):
        return var_b + x
    return inner

def var_test():
    f = var_f()
    print(f.__code__.co_varnames)
    print (var_test.__code__.co_varnames)
```
输出：
```
('x',)
('f',)
```
函数的自由变量：
```
def var_test():
    f = var_f()
    print(f.__code__.co_freevars)
    print(f.__closure__[0].cell_contents)
    print (var_test.__code__.co_freevars)
```
输出：
```
('var_b',)
10
()
```
自由变量就是使用的外部变量. __closure__[0].cell_contents 是自由变量的值  

### 函数和类的区别
```
print (set(dir(var_test)) - set(dir(object)))

{'__qualname__', '__dict__', '__module__', '__code__', '__kwdefaults__', '__name__', '__globals__', '__get__', '__defaults__', '__closure__', '__annotations__', '__call__'}
```


## 装饰器
游戏人物，带装备，数量不确定。如果每种人物+某一种装备，都用一个对象来表示，那么需要N*M个类。
比较合理的做法， A人物+X装备，实现为A人物增加了X相关的属性，X对A进行装饰。

PEP 318 装饰器的引入: 为什么引入，背景
PEP 3129 类装饰器

增强而不改变原有函数
装饰器强调函数的定义而不是运行态
装饰器语法糖展开：
```
@decorate
def target():
    print("do something")
```
相当于：
```
def target():
    print("do something")
target = decorate(target)
```
target是被修饰函数，返回的结果也是函数。闭包的实现。


```
def decorate(func):
    print("in decorate, arg:%s" % (func.__name__))
    def inner():
        return func()

    return inner

@decorate
def fun2():
    print("in func2")
    

if __name__ == "__main__":
    pass
```
执行时会打印 in decorate, arg:fun2， 在定义func2时，就执行了装饰器decorate, 并且将func2传递给了装饰函数decorate，func2 已经被inner()函数替换了。
装饰器在模块导入时就会运行。

### 装饰器的应用
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>hello world </h1>'

# app.add_url_rule('/', 'index')

if __name__ == '__main__':
   app.run(debug=True)
```
app是一个应用程序，类似Django中create app创建的应用。将“/”绑定到index view.

```
# 注册
@route('index',methods=['GET','POST'])
def static_html():
    return  render_template('index.html')

# 等效于
static_html = route('index',methods=['GET','POST'])(static_html)()


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典的结构以'index'为key 以 method static_html  其他参数为value存储绑定关系
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator
```

```
# 包装
def html(func):
    def decorator():
        return f'<html>{func()}</html>'
    return decorator

def body(func):
    def decorator():
        return f'<body>{func()}</body>'
    return decorator

@html
@body
def content():
    return 'hello world'

content()
```
双重装饰。最后运行的content() 其实是 html中的decorate().

### 被装饰函数
根据被装饰函数的三种形式，需要对装饰器进行相关设置。
* 被装饰函数带参数
* 被修饰函数带不定长参数
* 被修饰函数带返回值

#### 被装饰函数带参数

```
def decorate(func):
    print("in decorate, arg:%s" % (func.__name__))
    def inner(a, b):
        print ("inner: %s" % (func.__name__))
        return func(a, b)

    return inner

@decorate
def fun2(a, b):
    print ("fun2: %s" % (fun2.__name__))
    print(f"in func2, {a}, {b}")

func2(33, 44)
```
输出结果：
```
in decorate, arg:fun2
inner: fun2
fun2: inner
in func2, 33, 44
```
func2被替换成了decorate()中的inner, 所以func2中打印`__name__` 是 inner。 inner 函数中，func 是decorate 的参数，传递的是 func2.
inner参数要和被装饰函数保持一致。

#### 被装饰函数带不定长参数
利用 *args, **kwargs

#### 被装饰函数有返回值
在inner函数中返回

```
def decorate(func):
    print("in decorate, arg:%s" % (func.__name__))
    def inner(*args, **kwargs):
        print ("inner: %s" % (func.__name__))
        # do something
        ret = func(*args, **kwargs)
        # do something
        return ret

    return inner

@decorate
def fun2(a, b):
    print ("fun2: %s" % (fun2.__name__))
    print(f"in func2, {a}, {b}")
```

这个例子就是一个装饰器的模板，可以对任何函数进行装饰，预处理+结果处理。 

#### 装饰器带参数
装饰器也是函数，也可以带参数。就像Flask 的route.
```
# 装饰器带参数 

def outer_arg(bar):
    def outer(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            print(bar)
            return ret
        return inner
    return outer

# 相当于outer_arg('foo_arg')(foo)()
@outer_arg('foo_arg')
def foo(a,b,c):
    return (a+b+c)
    
print(foo(1,3,5))
```


#### 装饰器堆叠
```
# 装饰器堆叠

@classmethod
@synchronized(lock)
def foo(cls):
    pass

# 相当于
def foo(cls):
    pass
foo2 = synchronized(lock)(foo)
foo3 = classmethod(foo2)
foo = foo3
```

### Python 内置装饰器
#### wraps
#####介绍
[官方文档](https://docs.python.org/3/library/functools.html#functools.wraps)
python中的装饰器装饰过的函数其实就不是函数本身了.
```
from functools import wraps
def decorate(func):
    print("in decorate, arg:%s" % (func.__name__))
    @wraps(func)
    def inner(*args, **kwargs):
        print ("inner: %s" % (func.__name__))
        return func(*args, **kwargs)

    return inner

@decorate
def fun2(a, b):
    print ("fun2: %s" % (fun2.__name__))
    print(f"in func2, {a}, {b}")
```
不加`@wraps(func)`, fun2.__name__ 是inner, 加`@wraps(func)`, fun2.__name__是 fun2。  
***这样有什么用？***  
比如多个函数被`decorate` 装饰， 被装饰函数中需要使用自己的某些属性，如函数名，如果不加warps，那么获得的都是inner.  

flask 使用 wraps 的案例
```
########################
# flask 使用@wraps()的案例
from functools import wraps
 
def requires_auth(func):
    @wraps(func)
    def auth_method(*args, **kwargs):
        if not auth:
            authenticate()
        return func(*args, **kwargs)
    return auth_method

@requires_auth
def func_demo():
    pass
```
只有经过验证的view 才能被访问，

```
from functools import wraps
 
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator
 
@logit()
def myfunc1():
    pass
 
myfunc1()
# Output: myfunc1 was called
 
@logit(logfile='func2.log')
def myfunc2():
    pass
 
myfunc2()

# Output: myfunc2 was called
```


##### 使用wrapt包代替@wraps
[文档](https://wrapt.readthedocs.io/en/latest/quick-start.html)  
需要安装wrapt  

##### 原理


### lru_cache()

```
import functools
@functools.lru_cache()
def fibonacci(n):
    if (n < 2):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

import timeit
print(timeit.timeit('fibonacci(3)', setup="from __main__ import fibonacci"))
```
加上@functools.lru_cache()，执行时间变得很短。
使用 timeit， 执行时间变长？

### 类装饰器
Python2.6之后支持类装饰器。  
[教程](https://docs.pythontab.com/interpy/decorators/deco_class/)

在类中需要实现`__init__`, `__call__`
#### 类装饰器装饰函数
```
class Equipment(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, func):
        @wraps(func)
        def warpped_funcion(*args, **kwargs):
            print(f"{func.__name__} is called")

            return func(*args, **kwargs)
        
        return warpped_funcion

@Equipment()
def action():
    print ("Action:")
```

调用计数器的实现：
```
class Count(object):
    def __init__(self, func):
        self._func = func
        self.number_calls = 0

    def __call__(self, *args, **kwargs):
        self.number_calls += 1
        print ("num: %d" % self.number_calls)
        return self._func(*args, **kwargs)

@Count
def count_func1():
    pass

@Count
def count_func2():
    pass
```
#### 类装饰器装饰类
对类中的方法进行装饰。
```
# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)
            
        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()
```
未被装饰时， display() 直接打印 self.number。 被装饰后， display() 方法被重写，

疑问：
* 装饰器中的类，不继承被装饰的类？
* 装饰器中的类要实现被装饰类所有的方法？
* 看 装饰器实现的单例模式， 


## 对象协议
由魔术方法来实现对象协议。鸭子类型。
常用的魔术方法：
1. 容器类型协议
* `__str__` 打印对象时，默认输出该方法的返回值
* `__getitem__`, `__setitem__`,`__delitem__` 字典索引操作
* `__iter__` 迭代器
* `__call__` 可调用对象协议

2. 比较大小的协议
* `__eq__`
* `__gt__`

3. 描述符协议和属性交互协议
* `__get__`
* `__set__`

4. 可哈希对象
* `__hash__`

5. 上下文管理器
6. 
自己定义的类，尽量向标准类型靠拢。


## 迭代器和生成器

在函数中使用yield关键字，可以实现生成器。
生成器可以让函数返回可迭代对象。
yield 和 return不同， return 返回后，函数状态终止，yield保持函数的执行状态。
函数被yield会暂停，局部变量也会被保存
迭代器终止时，会抛出StopIteration异常。

`[i for i in range(10)]` 是list  
`(i for i in range(10))` 不是list, 也不是元组，而是生成器

```
def generator_test():
    g = (i for i in range(10))
    print (g)
    print(type(g))
    print (next(g))
    print (next(g))
    print (next(g))
    for i in g:
        print (i, end=' ')
```

```
<generator object generator_test.<locals>.<genexpr> at 0x00000000037A47C8>
<class 'generator'>
0
1
2
3 4 5 6 7 8 9
```

next() 对应的魔术方法是`__next__()`, 迭代的魔术方法是`__iter__`. 迭代器实现了这两个方法。  
如果只实现了`__iter__`, 那么这个对象就是一个可迭代对象。

可迭代iterable, 迭代器Iterator， 生成器Generator 的关系：
可迭代iterable： 实现了`__iter__`方法， 迭代器和生成器都是可迭代的。
迭代器Iterator： 实现了`__next__()` 和 `__iter__()`
生成器Generator: 由yield返回生成， 属于迭代器。

```
def generator_test2():
    a = [1, 2, 3, 4, 5]
    print(hasattr(a, '__iter__'))  # True
    print(hasattr(a, '__next__'))  # False
```
list 属于可迭代对象，但不是迭代器。

### 迭代器使用

#### itertools 三个常见迭代器
##### 计数器
```
import itertools
def itertools_test():
    c = itertools.count()
    print (next(c))  # 0
    print (next(c))  # 1
```

##### 循环遍历
```
    cycle = itertools.cycle(('y', 'N'))
    print (next(cycle))
    print (next(cycle))
    print (next(cycle))
```

##### 重复
```
    repeat = itertools.repeat(10, times=2)
    print (next(repeat))  # 10
    print (next(repeat))  # 10
    print (next(repeat))  # builtins.StopIteration
    # 不指定times, 则无限
```

##### chain
有两个可迭代对象， 如"ABC", [1,2,3], 需要一次获取两个对象的元素。通过两层循环+yield可以实现。
使用 itertools.chain 也可以实现，避免了需要两次循环。
```
chain = itertools.chain("ACB", [3, 6])
for i in chain:
    print (i)
```

在python 3.3 引入了 yield from, 也可以解决类似的问题。PEP-380
```
def chain_func(*iterables):
    for it in iterables:
        yield from it


print (list(chain_func("ABC", [1, 2, 3])))
# ['A', 'B', 'C', 1, 2, 3]
```

#### 迭代器有效性

```
def iter_valid():
    dict_tmp = {'a': 1, 'b': 2}
    it = iter(dict_tmp)
    print(next(it))     # a
    dict_tmp['c'] = 3
    print(next(it))     # builtins.RuntimeError: dictionary changed size during iteration
```
在迭代过程中，对被迭代字典对象进行修改（增，删），字典迭代器失效。 
list 无影响。但是，当遍历完毕后，迭代器会失效，即使对list 进行增加，也无法使用迭代器。
```
al = [1, 2, 3]
    it_a = iter(al)
    print (next(it_a))
    al.append(4)
    print (next(it_a))
    del al[2]
    print (next(it_a))
    for i in it_a:
        print (i)
    al.append(5)
    print (next(it_a))  # builtins.StopIteration
```

### yield表达式


## 协程
当yield作为表达式时，