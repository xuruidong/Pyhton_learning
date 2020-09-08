
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



if __name__ == "__main__":
    # assign_test()
    deep_copy_test()
