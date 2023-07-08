# Python-7 类

[Classes](https://docs.python.org/3/tutorial/classes.html)  
[菜鸟教程](https://www.runoob.com/python/python-object.html)  
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
Python 中，一切皆对象, 比如数字，list, 元组等等。  
Python 2.2 之前称之为经典类，之后称之为新式类。新式类继承自object类。
类的两大成员： 两个数据成员（类变量和实例变量）和方法  

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
* `__init__()`方法是一种特殊的方法，被称为类的初始化方法（不是构造函数），当创建了这个类的实例时就会调用该方法.  
* self 代表类的实例，self 在定义类的方法时是必须有的。self代表类的实例，而非类。

## 属性
属性分为**类属性**和**对象属性**。  
类属性，静态字段，在内存中只有一份，对象属性相当于是私有的，每创建一个对象，就会分配相应的内存空间。  
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
* 如果用对象去访问类变量，可以获取到类属性的值。但引用之后，在普通字段中出现了live 属性，Python 自动创建该属性。  
* 可以通过比较类的`__dict__` 和实例的`__dict__` 来识别类属性和对象属性  
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
* 直接赋值引用(直接使用“类名.变量名”)，可以为类增加静态属性
`Human.newattr = 1`
* 使用函数 setattr  
  `setattr(Human, 'attr2', 'value')`
* 内置类型不能增加属性和方法  
`setattr(list, 'attr2', 'value')`
`builtins.TypeError: can't set attributes of built-in/extension type 'list'`

### 属性的作用域
* 形如_attr 的变量，叫做“人为不可修改变量”，变量可见，但约定不去修改。
* 形如__attr的属性, 是私有属性，Python 会对其自动改名，防止其他人对其修改。但也是可以访问的，但不建议访问。
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
  使用类实例调用类方法时，输出`<bound method obj.class_func of <class '__main__.obj'>>`, 实例发现自己的`__dict__` 中没有对应的方法，就会去定义的类中去找，
* `__init__()`是初始化函数，`__new__()`是构造函数


在父类中定义classmethod, 然后两个子类继承父类，子类引用classmethod 时，cls 就成了自己的类名，cls 和类名进行了绑定  

#### 类方法描述器
[描述器使用指南](https://docs.python.org/zh-cn/3.8/howto/descriptor.html)
当类实例化后，也可以使用对象调用类方法。 当对象调用类方法时，会先查找对象的`__dict__`中是查找。在对象的`__dict__`中，是看不到类方法的，此时，实例对象会自动去自己所属的类中的`__dict__`中查找。类方法叫bound method 。

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

预处理函数示例： 
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

##### 对象查找方法的顺序
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
* 在获取属性时，执行了`__getattribute__`中的print
* 如果显式实现了`__getattribute__`，获取已定义属性和未定义属性，都会调用`__getattribute__`。
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
描述器就是实现特定协议（描述符）的类。只要类里有 `__get__()` 、 `__set__()` 、和`__delete__()` 方法的其中一个，就称为类为描述符，它能实现对多个属性运用相同存取逻辑的一种方式。 `__getattr__`和`__getattribute__`就是描述器协议的一个高层实现。 

```
def property_test():
    class Teacher:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, owner):
            print ("get")
            return self.name

        def __set__(self, instance, value):
            print ("set ")
            self.name = value

        def __delete__(self, instance):
            print("__delete__")

    class Cls(object):
        t = Teacher("aaa")
        
    c = Cls()
    c.t
    print("~" * 20)
    c.t = "BBB"
    print("-" * 20)
    print (c.t)
```
输出结果：
```
get
~~~~~~~~~~~~~~~~~~~~
set 
--------------------
get
BBB
```
* 获取属性时，会执行`__get__()`
* 设置属性时，会执行`__set__()`
* 如果一个类同时定义了 `__get__` 方法和 `__set__` 方法，则称之为数据描述符
* 如果只有 `__get__` 方法，则称之为非数据描述符


### 使用属性类型创建描述符
property 类需要实现 `__get__, __set__, __delete__` 方法。
除了使用类当作一个属性描述符，我们还可以使用 property()，就是可以轻松地为任意属性创建可用的描述符。创建 property() 的语法是 `property(fget=None, fset=None, fdel=None, doc=None)`

在Django中，
```
class Model(metaclass=ModelBase):
    def _get_pk_val(self, meta=None):
        meta = meta or self._meta
        return getattr(self, meta.pk.attname)

    def _set_pk_val(self, value):
        return setattr(self, self._meta.pk.attname, value)

    pk = property(_get_pk_val, _set_pk_val)
```
当获取pk属性时会调用`_get_pk_val`, 当设置pk属性时，会调用`_set_pk_val`
示例：
```
class Cls(object):

    def _get_pk_val(self, meta=None):
        print("_get_pk_val")
        return self.v

    def _set_pk_val(self, value):
        print("_set_pk_val")
        self.v = value

    pk = property(_get_pk_val, _set_pk_val) 

c.pk = 200
print (c.pk)
```
输出：
```
_set_pk_val
_get_pk_val
200
```

### property装饰器

使用`@property`将方法封装成属性。
**为什么要这么做？**
在获取属性和设置属性时，可进行一些操作.如判断赋值范围等。
比如，我想在类中有一个私有变量xxx，不让用户随便访问，所以变量名前面两个`_`, 即`__xxx`, 然后给用户暴露两个方法`get_xxx()`,`set_xxx()`， 在设置值时进行一些判断操作等。实现没问题，但在Python中显得不够优雅。

```
def property_test2():
    class Rectangle(object):
        @property
        def width(self):
            #变量名不与方法名重复，改为true_width，下同
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value
            
        @property
        def height(self):
            return self.true_height

        @height.setter
        def height(self, value):
            self.true_height = value
            
    s = Rectangle()
    #与方法名一致
    s.width = 1024
    # print (s.__width) # builtins.AttributeError: 'Rectangle' object has no attribute '__width'
    s.height = 768
    print(s.width,s.height)
```

#### property的实现
```
# property 纯python实现

class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
            self.__doc__ = doc
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
```

#### demo
```
#ORM(flask.ext.sqlalchemy)
# 一个表记录一个节点的心跳更新
# 通过一个属性来获取节点是否可用，而不用写复杂的查询语句
class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated_at = db.Column(db.DateTime) # 节点最后心跳时间
    state = db.Column(db.Integer, nullable=False) # 节点是否禁用

    @property
    def is_active(self):
        if(datetime.datetime.now() - self.updated_at).secondes > 60 \
            and self.vm_state == 0:
            return False
        return True
```

```
# 限制传入的类型和范围（整数，且满足18-65）
class Age(object):
    def __init__(self, default_age = 18):
        self.age_range = range(18,66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)
    
    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value

class Student(object):
    age = Age()

if __name__ == '__main__':
    s1 = Student()
    s1.age = 30
    s1.age = 100
```

## 类继承
封装/继承/重载/多态  
封装：  
继承：Python 支持单继承和多继承。missing 问题  
重载：Python 没有在语法层面实现，需要通过一些编程技巧来实现  
多态：Pyhton更崇尚鸭子类型

在Python 2.2之前，Python 的类叫作经典类。经典类中，Python 内置类和自定义的类的父类不相同，这种情况下，比如自己模拟的list或dict, 和Python 内置的list或dict 是不一致的， 无法做到完全替换（ ***这句话怎么理解？？？*** ）。Python 2.2之后的类，叫作新式类。新式类都继承自 object, 无论是否显式写出。

### object 和 type的关系
type类。有很多类，查询类型时都是<class 'type'>。
* object 和 type都属于tpye类
  ```
  type(object)  # <class 'type'>
  type(type)    # <class 'type'>
  ```
  object 和 type都是由 type 类创建的。
* type 类由type元类自身创建的。object类是由元类type创建的
  Pyhton 中，类也是对象，所以 object 也是对象，这个对象由 type 来生成。type 是创建类的类，也被称作元类。
  创建类的类，不一定是被创建类的父类。
* object 的父类为空，没有任何继承类
* type 的父类是object类 
  
在Python 中，类和类的关系，可以分为 继承关系和创建关系。

https://www.cnblogs.com/busui/p/7283137.html  
[英文版](https://www.eecg.utoronto.ca/~jzhu/csc326/readings/metaclass-class-instance.pdf)  
https://www.cnblogs.com/yhleng/p/7779112.html

类也是对象，所以object也是对象，这个对象由type创建。 type也被称作元类。

```
print("object:", object.__class__, object.__base__)
print("type:", type.__class__, type.__base__)
```
输出：
```
object: <class 'type'> None
type: <class 'type'> <class 'object'>
```
`__class__` 创建者 ？？？
`__base__` 基类


### 类继承的种类
* 单一继承
* 多重继承
* 菱形继承（钻石继承）

```
# 父类
class People(object):
    def __init__(self):
        self.gene = 'XY'
    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self,name):
        self.name = name
    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self,name):
        self.name = name    
    def shopping(self):
        print('buy buy buy')

p1 = Man('Adam')
p2 = Woman('Eve')
```
问题：
1. gene有没有被继承？ 
2. People父类是什么？ 
3. 能否实现多重层级继承？ 
4. 能否实现多个父类同时继承？
   ```
    class Son(Man, Woman):
    def __init__(self,name):
        self.name = name
    
    p3 = Son("sss")
    p3.shopping()
    p3.walk()
    p3.work()
   ```
5. 示例中的子类，是否有gene 属性？

```
print (p1.gene)
class Son(Man, Woman):
    pass

print(People.__class__, People.__base__)
print (Man.__class__, Man.__bases__)
```
结果：
```
builtins.AttributeError: 'Man' object has no attribute 'gene'
<class 'type'> <class 'object'>
<class 'type'> <class '__main__.People'>
```

答案：  
1. 否， `__init__`被覆盖。 如果要继承 gene, 加入super().__init__()
2. object。 即使写成class People: , 也是新式类
3. 可以
4. 可以
5. 否


### 多重继承的顺序问题，菱形继承

在上面的例子中，如果Man 和Woman 类中有相同的方法， 那么Son 中会方法继承自哪个类中呢？

```
class BaseClass(object):
    def callme(self):
        print ("BaseClass callme")

class LeftSubclass(BaseClass):
    # def callme(self):
    #    print ("LeftSubclass callme")
    pass


class RightSubclass(BaseClass):
    def callme(self):
        print ("RightSubclass callme")

class Subclass(LeftSubclass, RightSubclass):
    pass

s = Subclass()
s.callme()
```

输出：
```
RightSubclass callme
```

菱形的继承关系，Subclass 中会继承 LeftSubclass 的方法。当调用的方法不存在，会在 RightSubclass 中查找，如果 RightSubclass 中也不存在 callme 方法，就会在 BaseClass 中查找。这是新式类的查找方式。
如果多个父类存在相同的方法，
经典类，深度优先查找，新式类，广度优先查找。
mro方法，获得继承查找关系:
```
print (Subclass.mro())
```
```
[<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.RightSubclass'>, <class '__main__.BaseClass'>, <class 'object'>]
```
#### 有向无环路图 DAG(Directed Acyclic Graph)
DAG 原本是一种数据结构，因为DAG的拓扑结构带来的优异特性，经常被用于处理动态规划、寻找最短路径的场景。
![DAG](DAG.png)
图中对应的继承关系为：
```
class O4(O5):
    pass

class O3(O5):
    pass

class O1(O4, O2):
    pass

```
在图中会有**入度**为0的节点(1)，即没有被依赖的节点。1依赖2和4，去掉1后，2的入度为0，所以会先在2中查找。去掉2后，4的入度为0，依次类推，查找顺序为1-2-4-3-5


C3算法比较复杂，



* 继承机制（MRO）
* MRO和C3算法

### Python 的重载
语法层面未实现
```
class A(object):
    def ff(self, a, b):
        print ("ff_a_b")
        
    def ff(self):
        print("ff")  
```
后面的方法会覆盖前面的方法。所以示例中只能调用 a.ff()

## 设计模式
### SOLID设计原则
* 单一责任原则 The Single Respinsibility Principle
  减少类承担的职责，降低复杂度。比如Scrapy, 爬取，下载，保存数据，在不同的类中
* 开放封闭原则 The Open Closeed Principle
  对扩展开放，对修改封闭
* 里氏替换原则 The Liskov Substitution Principle
  要求子类实现的方法要完整覆盖父类的方法。
* 依赖倒置原则 The Depedency Inversion Principle
* 接口分配原则 The Interface Segregation Principle

...
### 单例模式
对象只允许创建一个实例

#### `__init__`和`__new__`的区别
* `__new__`是实例创建之前被调用，返回该实例对象，是静态方法
* `__init__`是实例创建之后被调用，是实例方法
* `__new__`先被调用，`__init__`后被调用
* `__new__`的返回值（实例）将传递给`__init__`方法的第一个参数，`__init__`给这个实例设置相关参数

#### 装饰器方式
使用装饰器方式实现单例：
```
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    def __init__(self):
        print ("MyClass init")

def singleton_test():
    c1 = MyClass()
    c2 = MyClass()
    print(id(c1))
    print(id(c2))
```
输出结果：
```
MyClass init
48804360
48804360
```

#### `__new__`方式

```
class Single(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print ("__instance is None")
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name
        print(f"name = {name}")
        
    def func(self):
        print(f"run func, {self.name}")

def single_test():
    c1 = Single("a")
    c2 = Single("b")
    print (id(c1))
    print (id(c2))
    c1.func()
    c2.func()
```
输出：
```
__instance is None
name = a
name = b
48792408
48792408
run func, b
run func, b
```
* 这样的单例不安全啊（不仅仅是说线程安全），创建实例时，虽然返回同一个对象，但可能会将对象的内部变量修改掉

#### 线程安全版
threading + double check
```
class Single(object):
    __instance = None
    __objs_lock = threading.lock() 
```

#### import 版
```
# 利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。
# 但这个方案并不完美，至少还有以下两个问题：
# ·如果Singleton的子类重载了__new__()方法，会覆盖或者干扰Singleton类中__new__()的执行，
# 虽然这种情况出现的概率极小，但不可忽视。
# ·如果子类有__init__()方法，那么每次实例化该Singleton的时候，
# __init__()都会被调用到，这显然是不应该的，__init__()只应该在创建实例的时候被调用一次。
# 这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
# 而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。
# 但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
# 这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
# ·所有的变量都会绑定到模块。
# ·模块只初始化一次。
# ·import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
# 当我们想要实现一个游戏世界时，只需简单地创建World.py就可以了。
```

```
# World.py
import Sun
def run():
    while True:
        Sun.rise()
        Sun.set()

# main.py
import World
World.run()
```

### 工厂模式
#### 简单工厂模式
```
class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Man(Human):
    def __init__(self, name):
        print(f'Hi,man {name}')

class Woman(Human):
    def __init__(self, name):
        print(f'Hi,woman {name}')

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Adam", "M")
```
根据传入不同的参数，生成不同的类实例。

#### 类工厂模式
一般在框架类代码中会见到，如Django， Scrapy。  
主要就是利用 setattr ，对类设置属性，动态加载方法。
```
# 返回在函数内动态创建的类
def factory2(func):
    class klass: pass
    #setattr需要三个参数:对象、key、value
    setattr(klass, func.__name__, func)
    return klass

def say_foo(self): 
    print('bar')

Foo = factory2(say_foo)
foo = Foo()
foo.say_foo()
```

## 元类
[直通车](https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072)
Python 是动态语言，可以在运行时创建类。使用类工厂函数可以创建类，但不够灵活。可以使用元类来创建类。
* 元类是创建类的类，是类的模板
* 元类是用来控制如何创建类的，正如类是创建对象的模板一样
  元类可以在类创建的时候，对创建过程进行拦截，（由元类的`__new__`方法进行操作）
* 元类的实例为类，正如类的实例为对象
* 创建元类的来个年终方法
  * class
  * type
      type(类名，父类的元组，包含属性的字典)

```
def foo(self):
    print("foooooo")
    
def type_test():
    tmp = type('ss', (object,), {"foo": foo})
    t = tmp()
    print (tmp.__dict__)
    print (t.__dict__)
    t.foo()
```
输出：
```
{'foo': <function foo at 0x0000000002E86488>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'ss' objects>, '__weakref__': <attribute '__weakref__' of 'ss' objects>, '__doc__': None}
{}
foooooo
```
type() 函数可以查看一个类型或变量的类型，也可以创建出新的类型。
`Hello = type('Hello', (object,), dict(hello=fn))`

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。如果要创建相对更加复杂的类，比如在初始化时增加一些功能.
```
class DelVal(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        attrs['abc'] = 200
        return type.__new__(cls, name, bases, attrs)


class DelDictVal(dict, metaclass=DelVal):
    pass

d = DelDictVal()
print (d.abc)           #200
print (d.__class__)     # <class '__main__.DelDictVal'>
```

 DelDictVal 类继承自 dict, 为了在创建类时增加功能，在Python2 中，使用`__mtaclass__`.
 也可以增加方法。  

元类必须继承自type  
元类必须实现`__new__`方法

### 抽象基类
基于元类可以实现抽象基类。  
抽象基类（abstract base class, ABC）用来确保派生类实现了基类中的特定方法。使用抽象基类的好处：
* 避免继承错误，是类层次易于理解和维护
* 无法实例化基类
* 当子类没有完全实现父类的方法，会立即报错

通过集成ABC 实现抽象基类：
```
from abc import ABC

class MyABC(ABC):
    pass
```

通过元类实现抽象基类：
```
from abc import ABCMeta, abstractclassmethod

class MyABC(metaclass=ABCMeta):
    @abstractclassmethod
    def foo(self):
        pass
    
    @abstractclassmethod
    def bar(self):
        pass
    
class Concrete(MyABC):
    def foo(self):
        print("foo")
    
c = Concrete()   # builtins.TypeError: Can't instantiate abstract class Concrete with abstract methods bar
```

### mixin 模式
python 可以实现动态修改继承关系。
在程序运行过程中，重定义类的继承，即动态继承。
动态继承的优点：
* 可以在不修改任何源代码的情况下，对已有类进行扩展
* 进行组件的划分： 不同的组件放在不同的类中，当使用到的时候，通过mixin 进行继承

```
def mixin(Class1, MixinClass):
    Class1.__bases__ = (MixinClass, )+Class1.__bases__
    
class Fclass(object):
    def text(self):
        print ("in parents Class")
        
class S1class(Fclass):
    pass

class MixinClass(object):
    def text(self):
        return super().text()
    
class S2class(S1class, MixinClass):
    pass

def mixin_test():
    print ("~"*30)
    print(f' test1 : S1class MRO : {S1class.mro()}')
    s1 = S1class()
    s1.text()  
    
    mixin(S1class, MixinClass)
    print(f' test2 : S1class MRO : {S1class.mro()}')  
    s1 = S1class()
    s1.text()
    
    print(f' test3 : S2class MRO : {S2class.mro()}')
    s2 = S2class()
    s2.text() 
```

```
test1 : S1class MRO : [<class '__main__.S1class'>, <class '__main__.Fclass'>, <class 'object'>]
in parents Class
 test2 : S1class MRO : [<class '__main__.S1class'>, <class '__main__.MixinClass'>, <class '__main__.Fclass'>, <class 'object'>]
in parents Class
 test3 : S2class MRO : [<class '__main__.S2class'>, <class '__main__.S1class'>, <class '__main__.MixinClass'>, <class '__main__.Fclass'>, <class 'object'>]
in parents Class
```
通过修改 `__bases__` 来实现继承关系的修改。  


* 《Python GUI Programming with Tkinter》
```
# Mixin类无法单独使用，必须和其他类混合使用，来加强其他类
class Displayer():
    def display(self, message):
        print("Displayer:", message)

class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super(LoggerMixin, self).display(message)
        self.log(message)

class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')

subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")
print(MySubClass.mro())
```

```
Displayer: This string will be shown and logged in subclasslog.txt
[<class '__main__.MySubClass'>, <class '__main__.LoggerMixin'>, <class '__main__.Displayer'>, <class 'object'>]
```
Displayer 类的 display 方法使用print 输出打印信息，LoggerMixin 增强了 display，将信息输出到文件。

类似的实现， 在socketserver.py 中，
```
class BaseServer:
    def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False
    
    def process_request(self, request, client_address):
        """Call finish_request.

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        self.shutdown_request(request)

class ThreadingMixIn:
    def process_request(self, request, client_address):
    ...


class TCPServer(BaseServer):
    ...
    pass

class HTTPServer(socketserver.TCPServer):
    ...
    pass

class ThreadedHttpServer(ThreadingMixIn,HTTPServer):
    pass

server = ThreadedHttpServer(addr,recvFrontRequestHandler)
server.serve_forever()
```

BaseServer 中， process_request 对请求进行处理，然后关闭连接。使用 ThreadingMixIn 后， process_request 被 Overridden， 接收到请求后，创建线程来处理。
