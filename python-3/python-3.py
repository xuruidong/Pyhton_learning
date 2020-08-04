
def args_test_func1(*args, **kwargs):
    print ("args len = %d" % (len(args)))
    print (args)
    
    print ("kwargs len = %d" % (len(kwargs)))
    print (kwargs)
    
    print("*"*20)
    

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
    args_test_func1(a1 = "aa1", a2 = "bb2")
    # ()
    # {'a1': 'aa1', 'a2': 'bb2'}
    
    print ("test 5:")
    tmp = {"a1": "aa1", "a2": "bb2", "a3": "cc3",}
    args_test_func1(**tmp)
    # ()
    # {'a1': 'aa1', 'a2': 'bb2', 'a3': 'cc3'}
    
    print ("test 6:")
    args_test_func1(123, "ppp", *a1, **tmp)
    # (123, 'ppp', 2, 3, 4, 5)
    # {'a1': 'aa1', 'a2': 'bb2', 'a3': 'cc3'}
    
    
if __name__ == "__main__":
    args_test()
