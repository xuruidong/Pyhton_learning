
import threading
import time

mutex = threading.RLock()

class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire(1):
            print("thread " + self.name + " get mutex")
            time.sleep(1)
            mutex.acquire()
            mutex.release()
        mutex.release()


import queue


def func(conn,i):
    # print(i)
    while True:
        conn.acquire()
        conn.wait()
        print(i+100)
        conn.release()

def condition_test():
    c = threading.Condition()
    for i in range(5):
        t = threading.Thread(target=func,args=(c,i,))
        t.start()
    while True:
        r = input(">>>")
        if r == "yes":
            c.acquire()
            c.notify()
            c.release()
            print ("notify")


from multiprocessing.dummy import Pool as ThreadPool

def handle(n):
    print("start %s" % n)
    time.sleep(0.5)
    1/0
    print("end %d" % n)

    return 100 + n
    
def threadPoolTest():
    tmp = [1, 2, 3, 4, 5, 6]
    pool = ThreadPool(4)
    result = pool.map(handle, tmp)
    pool.close()
    pool.join()
    print ("pool.join")
    for r in result:
        print (r)

from concurrent.futures import ThreadPoolExecutor

def futuresTest():
    tmp = [1, 2, 3, 4, 5, 6]
    with ThreadPoolExecutor(3) as executor:
        executor.submit(handle, tmp)

    print ("submit test end")
    time.sleep(1)

    with ThreadPoolExecutor(3) as executor2:
        executor2.map(handle, tmp)

    print ("map test end")
    time.sleep(1)
    
if __name__ == "__main__":
    # condition_test()
    futuresTest()
    print ("end")
