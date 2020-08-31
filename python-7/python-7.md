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