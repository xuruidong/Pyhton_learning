# -*- coding:utf-8 -*-


def args_test_func1(*args, **kwargs):
    print ("args len = %d" % (len(args)))
    print (args)

    print ("kwargs len = %d" % (len(kwargs)))
    print (kwargs)

    print("*" * 20)


def args_test():
    print ("test 1:")
    args_test_func1(1, 2, 3, 4)
    # (1, 2, 3, 4)
    # {}

    print ("test 2:")
    a1 = (2, 3, 4, 5)
    args_test_func1(a1)
    # ((2, 3, 4, 5),)
    # {}

    print ("test 3:")
    args_test_func1(*a1)
    # (1, 2, 3, 4)
    # {}

    print ("test 4: kwargs")
    args_test_func1(a1="aa1", a2="bb2")
    # ()
    # {'a1': 'aa1', 'a2': 'bb2'}

    print ("test 5:")
    tmp = {"a1": "aa1", "a2": "bb2", "a3": "cc3", }
    args_test_func1(**tmp)
    # ()
    # {'a1': 'aa1', 'a2': 'bb2', 'a3': 'cc3'}

    print ("test 6:")
    args_test_func1(123, "ppp", *a1, **tmp)
    # (123, 'ppp', 2, 3, 4, 5)
    # {'a1': 'aa1', 'a2': 'bb2', 'a3': 'cc3'}


from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor


import time
import multiprocessing
from multiprocessing import Process
import os
import sys

num = 100
def run(*args):
    global num
    print("子进程开启")
    print (args)
    sys.stdout.flush()
    for i in range(10):
        num += 1
        print ("child %d" % num)
        sys.stdout.flush()
        time.sleep(0.5)
    time.sleep(2)
    print("子进程结束")


def process_test():
    global num
    print("父进程启动")
    p = Process(target=run, name="child", args=(1, 2, 3))
    p.start()
    #print (dir(p))
    for i in range(10):
        num -= 1
        print ("father %d" % num)
        time.sleep(0.5)    
    p.join()
    print (multiprocessing.cpu_count())
    time.sleep(2)
    print("父进程结束")
    # time.sleep(2)


def super_test():
    class A(object):
        def __init__(self, arg):
            print ("class A __init__")
            self.arg = arg

        def get_arg(self):
            print (self.arg)
            

    class B(A):
        def __init__(self, arg):
            print ("B __init__")
            self.arg = arg

    class C(A):
        pass

    class D(A):
        def __init__(self, arg):
            print ("D __init__")
            super().__init__(arg)
            self.arg = arg + 2

    class E(B):
        def __init__(self, arg):
            print ("E __init__")
            super().__init__(arg)
            self.arg = arg

    class F(D):
        def __init__(self, arg):
            print ("F __init__")
            super().__init__(arg)
            self.arg = arg
            
    b = B(100)
    b.get_arg()
    
    c = C(200)
    c.get_arg()
    
    d = D(300)
    d.get_arg()
            
    e = E(400)
    e.get_arg()
    
    f = F(500)
    f.get_arg()

if __name__ == "__main__":
    print ("===  start  ===")
    # args_test()
    process_test()
    #super_test()
    print ("===  end  ===")
