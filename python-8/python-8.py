
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
    print(id(a))
    c = 789
    c = b = a
    print(a, b, c)
    

if __name__ == "__main__":
    assign_test()
