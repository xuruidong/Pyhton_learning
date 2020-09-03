# Python-7 类

[Classes](https://docs.python.org/3/tutorial/classes.html)
[菜鸟教程](https://www.runoob.com/python/python-object.html)
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
Python 中，一切皆对象。  
Python 2.2 之前称之为经典类，之后称之为新式类。新式类继承自object类。
类的两大成员： 属性和方法  

## 类的创建
使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾
```
class Human():
    'the docstring belonging to the class'
    live = True
    def __init__(self, name):
        self.name = name
```
* 类的帮助信息可以通过ClassName.__doc__查看。
* live变量是一个类变量，它的值将在这个类的所有实例之间共享。可以在内部类或外部类使用 Human.live 访问。
* `__init__()`方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法.  
* self 代表类的实例，self 在定义类的方法时是必须有的。self代表类的实例，而非类。

## 属性
属性分为类属性和对象属性。 类属性，静态字段，在内存中只有一份，对象属性相当于是私有的，每创建一个对象，就会分配相应的内存空间。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。  

```
def class_test():
    class Human():
        'the docstring belonging to the class'
        live = True
        def __init__(self, name):
            self.name = name


    print(Human.__doc__)
    h1 = Human("aaa")
    h2 = Human("bbb")
    print("h1.__dict__: %s" % h1.__dict__)
    print("Human.__dict__: %s" % Human.__dict__)
    print("*" * 20)

    print("h1.live=%s" % h1.live)
    print("h1.__dict__: %s" % h1.__dict__)
    h1.live = False
    print("h1.live=%s" % h1.live)
    print("h1.__dict__: %s" % h1.__dict__)
    print("h2.__dict__: %s" % h2.__dict__)
```
输出：
```
the docstring belonging to the class
h1.__dict__: {'name': 'aaa'}
Human.__dict__: {'__module__': '__main__', '__doc__': 'the docstring belonging to the class', 'live': True, '__init__': <function class_test.<locals>.Human.__init__ at 0x00000269EC47E1E0>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>}
********************
h1.live=True
h1.__dict__: {'name': 'aaa'}
h1.live=False
h1.__dict__: {'name': 'aaa', 'live': False}
h2.__dict__: {'name': 'bbb'}
```
* 通过`__dict__` 可以查看类或者对象的数据属性。dir() 也可以，返回形式为list
* 如果用对象去访问类变量，可以获取到类属性的值。如果对象引用了一个不存在的属性，则会自动创建该属性。
* 可以使用 id()， `__class__`来区别对象
```
print(id(h1))
print(id(h2))
print(h1.__class__)
print(h2.__class__)
```

* 类也是对象：
```
c = MyFirstClass
d = c()
d.__class__()
```
### 增加属性
* 直接赋值引用，可以为类增加静态属性
`Human.newattr = 1`
* 使用函数 setattr  
  `setattr(Human, 'attr2', 'value')`
* 内置类型不能增加属性和方法  
`setattr(list, 'attr2', 'value')`
`builtins.TypeError: can't set attributes of built-in/extension type 'list'`

### 属性的作用域
* 形如_attr 的变量，叫人为不可修改变量，变量可见，但约定不去修改。
* 形如__attr的属性, 是私有属性，Python 会对其自动改名，方式其他人对其修改。但也是可以访问的，但不建议访问。
* 形如__attr__的属性, 是魔术方法，不会被自动改名。

### 显示object类所有子类  
[] ---> list类  
() ---> tuple类  
```
print( type( () ) )
<class 'tuple'>
```
获取tuple类的父类  
```
().__class__.__bases__
```
此时的返回结果是一个元组，我们取第一个值[0]
获取object 类的所有子类：  
```
().__class__.__bases__[0].__subclasses__()
```

## 类方法
分三类：  
普通方法，或者称为实例方法。 需要self 参数，表示该方法的对象  
类方法：增加了classmethod语法糖的方法。需要cls 参数，表示该方法的类   
静态方法： 增加了 staticmethod 语法糖的方法。由类调用，无self 或 cls 参数。

### 类方法
#### 类方法调用
```
class obj(object):
    val = 1
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def class_func(cls, arg):
        print("in class_func, arg=%s, val=%d" % (arg, cls.val))

def class_method_test():
    obj.class_func("hahaha")
```
输出：
`in class_func, arg=hahaha`

* 不需要对类进行实例化就可以调用类方法。
* 类方法可以使用类变量
* 魔术方法 `__name__` 在类中是类名
* 类方法是`<bound method obj.class_func of <class '__main__.obj'>>`， 查看类方法描述器
* `__init__()`是初始化函数，`__new__()`是构造函数

#### 类方法描述器
[描述器使用指南](https://docs.python.org/zh-cn/3.8/howto/descriptor.html)
当类实例化后，也可以使用对象调用类方法。 在对象的`__dict__`中，是看不到类方法的，此时，实例对象会自动去自己所属的类中的`__dict__`中查找。

#### 在什么情况下使用类方法
##### 模拟实现构造函数
例如，现有如下类：
```
class Kls2():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')
```
进行实例化时，需要传入两个参数。当我们需要传入其他形式的参数来进行实例化时，有如下三种解决办法：
* 修改`__init__()`
* 增加`__new__()`构造函数
* 增加预处理函数

```
def pre_name(obj,name):
    fname, lname = name.split('-')
    return obj(fname, lname)

me2 = pre_name(Kls2, 'aaa-bbb')
me2.print_name()
```
pre_name 返回的是一个 Kls2 对象。

我们将 pre_name 写到 Kls2 中：
```
class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @classmethod
    def pre_name(cls,name):
        fname, lname = name.split('-')
        return cls(fname, lname)
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')
    
me3 = Kls3.pre_name('aaa-bbb')
me3.print_name()
```
pre_name 成为了Kls3 的类方法。

##### 这叫什么？
对象引用classmethod时，如果`__dict__`中不存在，会去自己所属类中找，如果所属类中也没有，会去父类中找。
```
class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls} ,{value}')
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass
```
当调用Apple.print_total时，会在Fruit 中找print_total。

```
Apple.set(100)
# calling <class '__main__.Apple'> ,100
Orange.set(200)
# calling <class '__main__.Orange'> ,200
org=Orange()
org.set(300)
# calling <class '__main__.Orange'> ,300
Apple.print_total()
# 100
# 140735711069824
# 140735711073024
Orange.print_total() 
# 300
# 140735711069824
# 1998089714064
```
不知道用在什么地方？？？


### 静态方法
静态方法可以由类直接调用
不能使用类和对象的属性

## 描述器高级应用
类实例属性描述符。比如在获取属性时，如果属性不存在，会抛出AttributeError异常。如果想拦截异常，可以使用try-except。AttributeError异常是由`__getattribute__`产生的，可以在这里改变获取属性时的行为。
### 属性的处理
在类中，需要对**实例**获取属性这一行为进行操作，可以使用：
* `__getattribute__()`
* `__getattr__()`
可以理解为，这两个方法可以拦截获取属性的过程。

两个方法的异同点：
* `__getattr__()`适用于未定义的属性
* `__getattribute__()`对所有属性的访问都会调用该方法

### __getattribute__
```
def getattribute_test():
    class Human(object):
        def __init__(self, *args, **kwargs):
            self.name = args[0]
            print(args[0])
            print ("init %s" % self.name)

        
        def __getattribute__(self, item):
            print(f"call getattribute, %s" % item)
        
        
    h = Human("Tom")
    print(h.name)
    print(h.age)
```
输出结果：
```
Tom
call getattribute, name
init None
call getattribute, name
None
call getattribute, age
None
```
* 在获取属性使，执行了`__getattribute__`中的print。
* 如果显示实现了`__getattribute__`，获取已定义属性和未定义属性，都会调用`__getattribute__`。
* item参数是被获取的属性的名字
* 获取不存在的属性时，没有像默认行为那样抛出异常。因为`__getattribute__`被重载。
* `self.name = args[0]` 并没有设置成功，并且其他地方的获取属性行为，也没有得到正确的值。因为`__getattribute__`没有返回值。

```
def getattribute_test():
    class Human(object):
        def __init__(self, *args, **kwargs):
            self.name = args[0]
            print(args[0])
            print ("init %s" % self.name)

        
        def __getattribute__(self, item):
            print(f"call getattribute, %s" % item)
            return super().__getattribute__(item)
        
        
    h = Human("Tom")
    print(h.name)
    print(h.age)
```
* `self.name = args[0]` 设置成功
* 获取未定义属性时， 在`return super().__getattribute__(item)`抛出异常
* super()表示当前实例所属类的父类

```
class Human(object):
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        print(args[0])
        print ("init %s" % self.name)

    
    def __getattribute__(self, item):
        print(f"call getattribute, %s" % item)
        try:
            return super().__getattribute__(item)
        except:
            self.__dict__[item] = 100
            return 100
```
实例中的属性会被注册到`__dict__`中，所以当出现获取未定义属性时，在dict中进行注册，赋予默认值并返回。这样来修改默认的抛异常行为。

### __getattr__

```
def getattribute_test():
    class Human(object):
        def __init__(self, *args, **kwargs):
            self.name = args[0]
            print(args[0])
            print ("init %s" % self.name)

        def __getattr__(self, item):
            print(f"call getattribute, %s" % item)
            return "ok"

        
    h = Human("Tom")
    print(h.name)
    print(h.age)
```
输出结果：
```
Tom
init Tom
Tom
call getattribute, age
ok
```
* 只有在获取未定义属性时才会调用`__getattr__`

同时存在`__getattr__`和`__getattribute__`的情况
```
class Human(object):
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        print(args[0])

    def __getattr__(self, item):
        print(f"call getattr, %s" % item)
        # return super().__getattr__(item)
        
    
    def __getattribute__(self, item):
        print(f"call getattribute, %s" % item)
        # return super().__getattribute__(item)
```
* 先执行`__getattribute__`
* 如果在`__getattribute__` 中返回 `return super().__getattribute__(item)`,会再执行`__getattr__`
* object类中没有 `__getattr__`

## 描述器
描述器就是实现特定协议（描述符）的类。`__getattr__`和`__getattribute__`就是描述器协议的一个高层实现。 

### 属性描述符property
property 类需要实现 `__get__, __set__, __delete__` 方法。

