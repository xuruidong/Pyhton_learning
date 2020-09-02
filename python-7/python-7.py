
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
    print (obj.__dict__)
    
if __name__ == "__main__":
    # class_test()
    class_method_test()
    print("===== end =====")
