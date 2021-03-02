# Python 语法

## Python 基础语法
dir(), help(),   
[Python 数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)<br/>
[Pyhton 其他流程控制工具](https://docs.python.org/zh-cn/3/tutorial/controlflow.html)<br/>
[Pyhton 中的类](https://docs.python.org/zh-cn/3/tutorial/classes.html)<br/>
[Python 定义函数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions)

## yield
yield与return的区别
return 一次性返回
yield依次返回

```
def yield_test():
    def chain():
        for i in range(5):
            yield i

    v = chain()
    print (v)  # <generator object yield_test.<locals>.chain at 0x000000000CF00318>
    v2 = next(v)
    print (v2)  # 0
    v3 = next(v)
    print (v3)  # 1
    v4 = list(v)
    print (v4)  # [2, 3, 4]
      
    try:
        v5 = next(v)
        print (v5)
    except Exception as e:
        print (e.__class__)   # <class 'StopIteration'>
```
chain()函数返回一个生成器对象

## 推导式
用来生成list,tuple,dict
生成tuple时要显示指定tuple， 如果不显示指定 tuple, 则会得到一个生成器对象。 
```
g = (i for i in range(10))
print (type(g))
# <class 'generator'>
```