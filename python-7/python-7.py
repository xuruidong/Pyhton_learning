
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
    #print (p3.__dict__)
    p3.shopping()
    p3.walk()
    p3.work()
    print (p1.gene)


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

class Model(metaclass=ModelBase, Man):
    def __init__(self):
        print ("Model init")

def meta_test():
    # m1 = ModelBase("M", )

    print("create Model===")
    m2 = Model()
    
    
if __name__ == "__main__":
    # class_test()
    # class_method_test()
    # getattribute_test()
    # property_test()
    # property_test2()
    # test()
    # singleton_test()
    # single_test()
    meta_test()
    
    print("object:", object.__class__, object.__base__)
    print("type:", type.__class__, type.__base__)
    print("===== end =====")
