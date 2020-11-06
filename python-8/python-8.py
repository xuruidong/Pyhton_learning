# -*- coding:utf-8 -*-

def assign_test():
    a = 123
    b = 123
    c = a
    print(id(a))
    print(id(b))
    print(id(c))
    print(a is b)
    
    # q2: what are the values of a,b,c
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
    
    # q3:
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


import copy
def deep_copy_test():
    old_list = [i for i in range(10)]
    new_list1 = old_list
    print ("old_list:  ", old_list)
    print("id(old_list):  ", id(old_list))
    print ("new_list1: ", new_list1)
    print ("id(new_list1): ", id(new_list1))

    new_list2 = list(old_list)
    print ("new_list2: ", new_list2)
    print ("id(new_list2): ", id(new_list2))
    
    new_list3 = old_list[:]
    print ("new_list3: ", new_list3)
    print ("id(new_list3): ", id(new_list3))
    
    new_list4 = copy.copy(old_list)
    print ("new_list4: ", new_list4)
    print ("id(new_list4): ", id(new_list4))
    
    list1 = [1]
    list1.append(list1)
    print(list1)
    list2 = copy.deepcopy(list1)
    print(list2)

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


from collections import Counter
def counter_test():
    lis = ['a', 'dd', 23, 342]
    c = Counter(lis)
    print (c)
    
    c.update('hello')  # 涔熷彲浠ヤ竴娆℃�update
    print (c)
    
    print (c.most_common(3))
    print(c['l'])
    

class func_class(object):
    def __call__(self):
        return "111"


x = "Global"
def func2():
    x = 'enclosing'
    def func3():
        return x

    return func3

def square(x):
    return x**2

def map_test():
    m = map(square, range(5))
    # m = map(square, 5)
    print (next(m))
    for it in m:
        print (it)
    
from functools import wraps
from functools import reduce
# import wrapt
def add(a, b):
    return a + b

def reduce_test():
    a = [1, 2, 3, 4, 5]
    b = reduce(add, a)
    print (b)
    
def is_odd(x):
    return x % 2 == 0

def filter_test():
    a = [1, 2, 3, 4, 5]
    b = filter(is_odd, a)
    print (type(b))
    print (list(b))

import functools
def partial_test():
    add_1 = functools.partial(add, 1)
    print (add_1(10))

def decorate(func):
    print("in decorate, arg:%s" % (func.__name__))
    # @wraps(func)
    # @wrapt.decorator
    def inner(*args, **kwargs):
        print ("inner: %s" % (func.__name__))
        ret = func(*args, **kwargs)
        print ("inner return: ")
        return ret

    return inner

@decorate
def fun2(a, b):
    print ("fun2: %s" % (fun2.__name__))
    print(f"in func2, {a}, {b}")


import functools
@functools.lru_cache()
def fibonacci(n):
    if (n < 2):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


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


def cls_decorator(old_cls):
    class new_class(old_cls):
        def __init__(self, *args, **kwargs):
            pass



class MyClass(object):
    def __init__(self, *args, **kwargs):
        self.dic = {}

    def __str__(self):
        return "I am MyClass"
    
    def __getitem__(self, key):
        return self.dic[key]

    def __setitem__(self, key, value):
        self.dic[key] = value


def generator_test():
    g = (i for i in range(10))
    print (g)
    print(type(g))
    print (next(g))
    print (next(g))
    print (next(g))
    for i in g:
        print (i, end=' ')


def generator_test2():
    a = [1, 2, 3, 4, 5]
    print(hasattr(a, '__iter__'))  # True
    print(hasattr(a, '__next__'))  # False
    

import itertools
def itertools_test():
    c = itertools.count()
    print (next(c))
    print (next(c))

    cycle = itertools.cycle(('y', 'N'))
    print (next(cycle))
    print (next(cycle))
    print (next(cycle))

    repeat = itertools.repeat(10, times=2)
    for i in range(2):
        print (next(repeat))
        
    chain = itertools.chain("ACB", [3, 6])
    for i in chain:
        print (i)
        

def chain_func(*iterables):
    for it in iterables:
        yield from it


# print (list(chain_func("ABC", [1, 2, 3])))

def iter_valid():
    dict_tmp = {'a': 1, 'b': 2}
    it = iter(dict_tmp)
    print(next(it))     # a
    dict_tmp['b'] = 3
    # builtins.RuntimeError: dictionary changed size during iteration
    print(next(it))

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
    print (next(it_a))

def var_f():
    var_b = 10
    
    def inner(x):
        return var_b + x
    return inner


def var_test():
    f = var_f()
    print(f.__code__.co_varnames)
    print(f.__code__.co_freevars)
    print(f.__closure__[0].cell_contents)
    print (var_test.__code__.co_varnames)
    print (var_test.__code__.co_freevars)

g = "abc"
def global_test():
    print (g)
    g = "111"
    print (g)

def outer():
    v = 2
    def inner():
        nonlocal v
        t = v + 1
        print(t)
        v = t
        return v
    return inner

def nolocal_test():
    o = outer()
    print (o())
    
def counter(start):
    count = start
    def incr():
        nonlocal count
        count += 1
        return count
    return incr

    
if __name__ == "__main__":
    # assign_test()
    # deep_copy_test()
    # namedtuple_test()
    # counter_test()

    # print (dir(__builtins__))
    # map_test()
    # reduce_test()
    # filter_test()
    # partial_test()
    # var_test()
    # fun2(33, 44)
    # import timeit
    # print(timeit.timeit('fibonacci(3)', setup="from __main__ import fibonacci"))
    # print (fibonacci(30))
    count_func1()
    count_func2()
    count_func1()
    # action()
    # generator_test2()
    # iter_valid()
    # global_test()
    # nolocal_test()
    # print (set(dir(var_test)) - set(dir(object)))
    c1 = counter(10)
    # print (c1())
    # print (c1())

    print ("=== end ===")
