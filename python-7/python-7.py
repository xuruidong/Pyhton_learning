# -*- coding:utf-8 -*-
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
    print("*" * 20)
    print(id(h1))
    print(id(h2))
    print(h1.__class__)
    print(h2.__class__)

    Human.newattr = 1
    setattr(Human, 'attr2', 'value')
    print("Human.__dict__: %s" % Human.__dict__)

    # setattr(list, 'attr2', 'value')
    print ([].__class__)
    print (type(()))
    print ( ().__class__.__bases__[0].__subclasses__() )

class obj(object):
    val = 1
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def class_func(cls, arg):
        print("in class_func, arg=%s, val=%d" % (arg, cls.val))
        print(cls.__name__)
        return cls.val
    
    @classmethod
    def get_val(cls):
        return cls.val

    
def class_method_test():
    print(obj.class_func)
    ret = obj.class_func("hahaha")
    print(type(ret))
    o1 = obj()
    print(o1.class_func)
    ret = o1.class_func("ooo")
    print(ret)
    print(o1.__dict__)
    o1.val = 100
    print(o1.__dict__)
    print(o1.get_val())
    print(obj.__dict__)
    print(o1.aaa)

def getattribute_test():
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
        
        
    h = Human("Tom")
    # print(h.name)
    print(h.age)

        

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

        def _get_pk_val(self, meta=None):
            print("_get_pk_val")
            return self.v
    
        def _set_pk_val(self, value):
            print("_set_pk_val")
            self.v = value

        pk = property(_get_pk_val, _set_pk_val)        
        
        
        
    c = Cls()
    c.t
    print("~" * 20)
    c.t = "BBB"
    print("-" * 20)
    print (c.t)
    
    c.pk = 200
    print (c.pk)


def property_test2():
    class Rectangle(object):
        @property
        def width(self):
            #鍙橀噺鍚嶄笉涓庢柟娉曞悕閲嶅�锛屾敼涓簍rue_width锛屼笅鍚�
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
    #涓庢柟娉曞悕涓�嚧
    s.width = 1024
    # print (s.__width) # builtins.AttributeError: 'Rectangle' object has no attribute '__width'
    s.height = 768
    print(s.width,s.height)    


# 鐖剁被
class People(object):
    def __init__(self):
        self.gene = 'XY'
    def walk(self):
        print('I can walk')

# 瀛愮被
class Man(People):
    def __init__(self,name):
        self.name = name
    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self, name):
        self.name = name
    def shopping(self):
        print('buy buy buy')

class Son(Man, Woman):
    def __init__(self,name):
        self.name = name
        
def test():
    p1 = Man('Adam')
    p2 = Woman('Eve')
    p3 = Son("sss")
    # print (p1.gene)
    print ("---", People.__class__, People.__base__)
    print ("---", Man.__class__, Man.__base__)
    print ("===")
    #print (p3.__dict__)
    p3.shopping()
    p3.walk()
    p3.work()


# ---------------------------------------------
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


def mor_test():
    s = Subclass()
    s.callme()
    print (Subclass.mro())
    pass


# =============================================

class A(object):
    

    def ff(self, a, b):
        print ("ff_a_b")
        
    def ff(self):
        print("ff")    
        
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
    print(dir(MyClass))
    c2 = MyClass()
    print(id(c1))
    print(id(c2))


class Single(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        print ("new__, arg=%s" % args)
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

def foo(self):
    print("foooooo")
    
def type_test():
    tmp = type('ss', (object,), {"foo": foo})
    t = tmp()
    print (tmp.__dict__)
    print (t.__dict__)
    t.foo()
    

class DelVal(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        attrs['abc'] = 200
        return type.__new__(cls, name, bases, attrs)


class DelDictVal(dict, metaclass=DelVal):
    pass
    
class ModelBase(type):
    """Metaclass for all models."""
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__

        # Also ensure initialization is only performed for subclasses of Model
        # (excluding Model class itself).
        print (cls)
        print (name)
        print (f"bases={bases}")
        print (attrs)
        parents = [b for b in bases if isinstance(b, ModelBase)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        return super_new(cls, name, bases, attrs)

class Model(metaclass=ModelBase):
    def __init__(self):
        print ("Model init")

def meta_test():
    # m1 = ModelBase("M", )

    print("create Model===")
    # m2 = Model()
    d = DelDictVal()
    print (d.abc)
    print (d.__class__)


from abc import ABCMeta, abstractclassmethod

class MyABC(metaclass=ABCMeta):
    @abstractclassmethod
    def foo(self):
        pass
    
    @abstractclassmethod
    def bar(self):
        pass
'''    
class Concrete(MyABC):
    def foo(self):
        print("foo")
    
c = Concrete()
'''
# -------------  mixin test  ---------------
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
    
# ~~~~~~~~~~~~~~~~~~
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
        
def mixin_test2():
    subclass = MySubClass()
    subclass.display("This string will be shown and logged in subclasslog.txt")
    print(MySubClass.mro())
    
if __name__ == "__main__":
    # class_test()
    # class_method_test()
    # getattribute_test()
    # property_test()
    # property_test2()
    # test()
    # singleton_test()
    # single_test()
    # meta_test()
    # mor_test()
    # type_test()
    mixin_test2()
    
    print("===== end =====")
