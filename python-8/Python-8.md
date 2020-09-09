# Python-8 

## 变量赋值
Python的基本数据类型非常丰富。赋值时存在一些需要注意的问题， 如连续赋值。

### 测试题：
1. 
```
    a = 123
    b = 123
    c = a
    print(id(a))
    print(id(b))
    print(id(c))
    print(a is b)
```
输出结果：
```
8791162909136
8791162909136
8791162909136
True
```
* 判断两个变量是不是同一个对象，可以使用is。比较的是内存地址，使用id()可以获取
* a 和 b 为什么是同一个对象？

2. 连续赋值

```
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
```
输出结果：
```
after change a:
57343824
8791162909136
after change c:
57343824
48750896
345 345 345
```
* 改变a的值，a对象改变？
* a对象变了，但对象没变。
* c 改变了，但a
* 连续赋值，和C++行为一样哦

3. 序列对象

```
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
```
输出结果：
```
after : x.append(4)
[1, 2, 3, 4]
id(x[1])= 8791162905264
after : x[1] = 7
id(x[1])= 8791162905424
[1, 7, 3, 4]
[4, 5, 6, 4]
[4, 5, 6, 4]
```
* 对x 增加元素，修改部分元素，不改变y
* 对x进行赋值操作，x对象改变

### 变量的划分
从内存使用的角度划分
* 可变数据类型
* 不可变数据类型

#### 不可变数据类型
* 整型
* 浮点型
* 字符串型
* 元组

不可变数据类型 传递对象本身？？？

#### 可变数据类型
* 列表
* 字典

传递引用

在高级语言中，变量是对内存及其地址的抽象。对于python而言，python的一切变量都是对象，变量的存储，采用了引用语义的方式，存储的只是一个变量的值所在的内存地址，而不是这个变量的只本身。  
在C/C++ 中, 变量是内存地址的名字，对变量赋值、修改，不会影响到变量的内存地址；
在Python中，对于不可变数据类型，值（对象）是真实存在于内存中，对变量赋值，只是让变量指向值（对象）。
不可变数据对象，无论有多少个引用，只占一块内存。 比如，某个计算流程不断产生新数字，就会不断产生对象，占用内存空间。


## 序列
### 序列的分类
容器序列： list,tuple, collections.deque, 可以存放不同类型的数据
扁平序列：str,bytes,bytearray,memoryview(内存视图)，array.array, 存放的是相同类型的数据
### 容器序列的深浅拷贝

浅拷贝（shallow copy）和深度拷贝（deep copy）是针对容器序列的概念。
#### 浅拷贝
常见的浅拷贝的方法，是使用数据类型本身的构造器，比如下面两个例子：
```
list1 = [1, 2, 3]
list2 = list(list1)
print(list2)
print("list1==list2 ?",list1==list2)
print("list1 is list2 ?",list1 is list2)
set1= set([1, 2, 3])
set2 = set(set1)
print(set2)
print("set1==set2 ?",set1==set2)
print("set1 is set2 ?",set1 is set2)
```
运行结果为：
```
[1, 2, 3]
list1==list2 ? True
list1 is list2 ? False
{1, 2, 3}
set1==set2 ? True
set1 is set2 ? False
```
在上面程序中，list2 就是 list1 的浅拷贝，同理 set2 是 set1 的浅拷贝。

对于可变的序列，还可以通过切片操作符“：”来完成浅拷贝，例如：
```
list1 = [1, 2, 3]
list2 = list1[:]
print(list2)
print("list1 == list2 ?", list1 == list2)
print("list1 is list2 ?", list1 is list2)
```
输出结果：
```
[1, 2, 3]
list1 == list2 ? True
list1 is list2 ? False
```
切片操作，虽然是全切，但仍然产生的是新对象。

Python 还提供了对应的函数 copy.copy() 函数，适用于任何数据类型。
```
import copy
list1 = [1, 2, 3]
list2 = copy.copy(list1)
print(list2)
print("list1 == list2 ?",list1 == list2)
print("list1 is list2 ?",list1 is list2)
```
输出结果：
```
[1, 2, 3]
list1 == list2 ? True
list1 is list2 ? False
```

不过需要注意的是，对于元组，使用 tuple() 或者切片操作符 ':' 不会创建一份浅拷贝，相反它会返回一个指向相同元组的引用：
```
tuple1 = (1, 2, 3)
tuple2 = tuple(tuple1)
print(tuple2)
print("tuple1 == tuple2 ?",tuple1 == tuple2)
print("tuple1 is tuple2 ?",tuple1 is tuple2)
```
输出结果：
```
(1, 2, 3)
tuple1 == tuple2 ? True
tuple1 is tuple2 ? True
```

浅拷贝，指的是重新分配一块内存，创建一个新的对象，但里面的元素是原对象中各个子对象的引用。

#### 深拷贝

对数据采用浅拷贝的方式时，如果原对象中的元素不可变，那倒无所谓；但如果元素可变，浅拷贝通常会出现一些问题，例如：
```
list1 = [[1, 2], (30, 40)]
list2 = list(list1)
list1.append(100)
print("list1:",list1)
print("list2:",list2)
list1[0].append(3)
print("list1:",list1)
print("list2:",list2)
list1[1] += (50, 60)
print("list1:",list1)
print("list2:",list2)
list1[0] = [7, 7, 7]
print("list1:", list1)
print("list2:", list2)
```
输出结果：
```
list1: [[1, 2], (30, 40), 100]
list2: [[1, 2], (30, 40)]
list1: [[1, 2, 3], (30, 40), 100]
list2: [[1, 2, 3], (30, 40)]
list1: [[1, 2, 3], (30, 40, 50, 60), 100]
list2: [[1, 2, 3], (30, 40)]
list1: [[7, 7, 7], (30, 40, 50, 60), 100]
list2: [[1, 2, 3], (30, 40)]
```
* list1和list2是两个对象，所以list1 进行append操作不会影响到list2
* 由于是浅拷贝，list1[0]和list2[0]是同一个对象，会相互影响
* 元组是不可变的，拼接后产生了新的元组对象，作为了list1的第二个元素。而list2并没有引用新元组，所以list2不受影响
* list1[0]是list, 虽然是可变数据类型，但赋值操作使其指向了新的对象，而list2并没有引用新list,所以list2不受影响

使用浅拷贝可能带来的副作用。如果想避免这种副作用，完整地拷贝一个对象，就需要使用深拷贝。所谓深拷贝，是指重新分配一块内存，创建一个新的对象，并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。因此，新对象和原对象没有任何关联。

Python 中以 copy.deepcopy() 来实现对象的深度拷贝。
```
list1 = [[1, 2], (30, 40)]
list2 = copy.deepcopy(list1)

list1[0].append(3)
print("list1:",list1)
print("list2:",list2)
```
输出结果：
```
list1: [[1, 2, 3], (30, 40)]
list2: [[1, 2], (30, 40)]
```

不过，深度拷贝也不是完美的，往往也会带来一系列问题。如果被拷贝对象中存在指向自身的引用，那么程序很容易陷入无限循环，例如：
```
list1 = [1]
list1.append(list1)
print(list1)
list2 = copy.deepcopy(list1)
print(list2)
```
输出结果：
```
[1, [...]]
[1, [...]]
```
此例子中，列表 x 中有指向自身的引用，因此 list1 是一个无限嵌套的列表。但是当深度拷贝 list1 到 list2 后，程序并没有出现栈溢出的现象。这是为什么呢？

其实，这是因为深度拷贝函数 deepcopy 中会维护一个字典，记录已经拷贝的对象与其 ID。拷贝过程中，如果字典里已经存储了将要拷贝的对象，则会从字典直接返回。通过查看 deepcopy 函数实现的源码就会明白：
```
def deepcopy(x, memo=None, _nil=[]):
    """Deep copy operation on arbitrary Python objects.
       
    See the module's __doc__ string for more info.
    """
   
    if memo is None:
        memo = {}
    d = id(x) # 查询被拷贝对象 x 的 id
    y = memo.get(d, _nil) # 查询字典里是否已经存储了该对象
    if y is not _nil:
        return y # 如果字典里已经存储了将要拷贝的对象，则直接返回
        ...
```

## 字典和扩展内置数据类型
collections用来扩展内置数据类型。
字典的key，必须是可以进行hash的数据类型。


### 用collections用来扩展内置数据类型
6:50