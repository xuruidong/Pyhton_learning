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
    for i in range(5):
        num += 1
        print ("child %d" % num)
        sys.stdout.flush()
        time.sleep(0.5)
    time.sleep(1)
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



from multiprocessing import Queue
def f(q):
    time.sleep(1)
    q.put("xxxx")
    print("child end")
    
    
def multi_queue_test():
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    r = q.get()
    print (r)
    p.join()
    
    

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


from multiprocessing import Pipe

def f_pipe(pipe):
    pipe.send([100, None, "hello"])
    pipe.close()

    
def pipe_test():
    pipe_parent, pipe_child = Pipe()
    p = Process(target=f_pipe, args=(pipe_child, ))
    p.start()
    print(pipe_parent.recv())
    p.join()


from multiprocessing import Value
from multiprocessing import Array
from ctypes import c_char_p

def f_sharememory(n, a, s):
    print ("=======111")
    sys.stdout.flush()
    n.value = 3.1415927
    for i in a:
        a[i] = -a[i]
    
    print ("=======")
    sys.stdout.flush()
    #print (dir(s.value))
    sys.stdout.flush()
    #print (type(s.value))
    print ("-------------")
    sys.stdout.flush()

def sharememory_test():
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    string = Value(c_char_p, b"Hello World")

    print(num.value)
    print(arr[:])
    
    p = Process(target=f_sharememory, args=(num, arr, string))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])


from multiprocessing import Lock
def lock_test_job(v, num, l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print (v.value, end="|")
        # sys.stdout.flush()
    l.release()
    
def lock_test():
    l = Lock()
    v = Value('i', 0)

    p1 = Process(target=lock_test_job, args=(v, 1, l))
    p2 = Process(target=lock_test_job, args=(v, 1, l))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


from multiprocessing import Pool

def pool_test():
    p = Pool(4)
    for i in range(10):
        p.apply_async(run, (i,))

    p.close()
    p.join()

    
def pool_test2():
    with Pool(processes=4) as pool:
        result = pool.apply_async(time.sleep, (3,))
        print (type(result))
        print (dir(result))
        print (result.get(timeout=1))


def map_test_fun(x):
    return (x * x)
    

def map_test():
    with Pool(processes=4) as pool:
        #print (pool.map(map_test_fun, range(10)))
        for r in pool.imap(map_test_fun, range(10)):
            print (r)

import threading

if __name__ == "__main__":
    print ("===  start  ===")
    # args_test()
    # process_test()
    # super_test()
    # multi_queue_test()
    # pipe_test()
    # sharememory_test()
    # lock_test()
    # pool_test()
    # pool_test2()
    map_test()
    print ("===  end  ===")
