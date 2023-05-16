# python-4 Pandas
大徒弟名叫青头愣 二徒弟名叫愣头青

## pandas 简介

[Pandas 中文](https://www.pypandas.cn/)  
pandas 是对 numpy 的封装

### 测试数据来源
sklearn 提供了机器学习的数据集，暂时免去数据清洗的过程

```
from sklearn import datasets

def sklearn_test():
    iris = datasets.load_iris()
    print (type(iris))
    print (iris)

    x, y = iris.data, iris.target
    # print (x)
    # print (y)

    print (iris.feature_names)
    print (iris.target_names)
```

输出：
```
<class 'sklearn.utils.Bunch'>
{'data': array([[5.1, 3.5, 1.4, 0.2],
       [4.9, 3. , 1.4, 0.2],
       [4.7, 3.2, 1.3, 0.2],
       ...
       [5.9, 3. , 5.1, 1.8]]), 'target': array([0, 0, 0, 0, 0, 0......
       , 2, 2, 2, 2, 2, 2, 2, 2]), 
       'frame': None, 
       'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'), 'DESCR': '.. _iris_dataset:\n\nIris plants dataset\n--------------------\n\n**D ...', 
       'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], 
       'filename': 'd:\\Program Files\\Python\\Python37\\lib\\site-packages\\sklearn\\datasets\\data\\iris.csv'}
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
['setosa' 'versicolor' 'virginica']

```

* 引入数据集 `from sklearn import dateset`
* 加载鸢尾花数据 `iris = datasets.load_iris()`, 其他数据集如 load_Boston 波士顿房价 回归， load_digits 手写体 分类
* 返回的数据类型是 sklearn.utils.Bunch， 继承 dict 的类, 所以它也是一个字典，其中data 和 target 是其中的两个键。使用 `x, y = iris.data, iris.target` 将数据和目标分离， x是花瓣特征（长短宽窄），y是特征对应的花的种类。这个数据集就是每种花瓣特征数据<-->对应的花的种类。
* 使用`iris.feature_names` 可以获得特征名称， `iris.target_names` 获得种类名称
* 使用训练集和测试集分类功能， 可以把x y按照一定的比例来划分，
* ```
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
    ```

### os.path
```
def file_path_test():
    print ("__file__ is ", __file__)
    print ("os.path.realpath(__file__) :", os.path.realpath(__file__))
    print ("os.path.dirname(os.path.realpath(__file__)): ",
           os.path.dirname(os.path.realpath(__file__)))
```
`__file__` 是相对路径
`os.path.realpath(__file__)` 是绝对路径
`os.path.dirname` 用来获取dir

### 示例
```
import pandas as pd
import numpy as np
import matplotlib as plt
import os
pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd,'book_utf8.csv')
# df = pd.read_csv('book_utf8.csv')
df = pd.read_csv(book)
# 输出全部内容
print(df)

# 筛选标题为"还行"这一列
df['还行']

# 切片方式筛选
# 显示前3行
df[1:3]

# 增加列名
df.columns = ['star', 'vote', 'shorts']

# 显示特定的行、列
df.loc[1:3, ['star']]

# 过滤数据
df['star'] == '力荐'
df [ df['star'] == '力荐' ]

# 缺失数据
df.dropna()

# 数据聚合
df.groupby('star').sum()

# 创建新列
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)

print(df)
```

## Pandas 基本数据类型
* Series
  它是一种类似于一维数组的对象，是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成。仅由一组数据也可产生简单的Series对象。
* DataFrame
  DataFrame是Pandas中的一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔型等)，DataFrame即有行索引也有列索引，可以被看做是由Series组成的字典。

### Series 的创建
```
def series_test():
    ret = pd.Series(['a', 'b', 'c'])
    print (type(ret))
    print (ret)
    # print (dir(ret))
    
    s1 = pd.Series(['a', 'b', 'c'], index=['A', 'B', 'C'])
    print(s1)
    s2 = pd.Series({'A': 'a', 'B': 'b', 'C': 'c'})
    print (s2)

    print (s1.index)
    print (s1.values)
    
    print (s1.values.tolist())
```
输出：
```
<class 'pandas.core.series.Series'>
0    a
1    b
2    c
dtype: object

A    a
B    b
C    c
dtype: object
A    a
B    b
C    c
dtype: object

Index(['A', 'B', 'C'], dtype='object')
['a' 'b' 'c']

['a', 'b', 'c']
```
* 可以使用 list 创建
* 建议将 Series 当作一列来看待
* 创建时可以自定义索引，其中有两种方法，字典或指定index
* 使用index 会提升查询性能
  * 如果index 唯一，pandas 会使用hash表优化，查询时间复杂度O(1)
  * 如果index有序不唯一，pandas 会使用二分查找算法
  * 完全随机，遍历查找， O(N)
* 取所有索引 `s.index`, 所有值 `s.values`
* 将值转为 Python 的 list `s.values.tolist()`

```
emails = pd.Series(
        ['abc at aaa.com', 'admin@aa.com', 'aaa@mmm', 'ab@acb.com'])
    import re
    pattern = '[A-Za-z0-9._]+@[A-Za-z0-9._]+\\.[A-Za-z]{2,5}'
    mask = emails.map(lambda x: bool(re.match(pattern, x)))
    print (emails[mask])
```

```
1    admin@aa.com
3      ab@acb.com
```

### DataFrame
```
def DateFrame_test():
    data = [['a','b','c'], ['d','e','f']]
    d = pd.DataFrame(data)
    print (d)
    
    d.columns = ['aa', 'bb', 'cc']
    d.index = ['A', 'B']
    print(d)

    print (type(d.values))
```
输出：
```
   0  1  2
0  a  b  c
1  d  e  f

  aa bb cc
A  a  b  c
B  d  e  f

<class 'numpy.ndarray'>
```
* 可以使用二维 list 创建 DataFrame
* 同样可以设置索引
* DataFrame 和 Series 的值的类型都是 numpy.ndarray

## Pandas 数据导入
通过 `read_xxx()` 方法来从不同类型数据源中导入数据。
```
def pd_read_test():
    data = pd.read_csv()
    data2 = pd.read_excel()
    data3 = pd.read_sql()

import pymysql
def read_from_mysql():
    sql  =  'SELECT *  FROM phone'
    conn = pymysql.connect('10.0.110.34','root','123456','smzdm', 3306, charset='utf8mb4')
    df = pd.read_sql(sql, conn) 
    print (df)
```

## Pandas 数据预处理
缺失值处理  重复值处理
https://pandas.pydata.org/pandas-docs/stable/refernce/series.html

### 缺失值处理
```
import numpy as np

def pre_proc_test():
    s = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 7])
    print ("has nan? ", s.hasnans)

    new_s = s.fillna(value=s.mean())
    print (new_s)
    
    df = pd.DataFrame({"A": [5, 3, None, 4],
                 "B": [None, 2, 4, 3],
                 "C": [4, 3, 8, 5],
                 "D": [5, 4, 2, None]})
    print (df)
    print (df.isnull().sum())
    new_df = df.ffill()
    print (new_df)
    
    new_df = df.ffill(axis=1)
    print (new_df)
    
    new_df = df.dropna()
    print (new_df)
    
    new_df = df.fillna('ok')
    print (new_df)

    new_df = df.drop_duplicates()
    print (new_df)

```
* 空值可以使用 numpy 中的 nan 代表
* Series 的 hasnans 属性可以检查是否存在空值
* fillna方法可以用来填充空值， `value=s.mean()` 表示用平均值来填充
* DataFrame 可以使用 isnull() 方法来查看空值情况，但不方便，可以使用DataFrame.idnull().sum()来查看空值统计情况，这时对列空值的统计
* ffill() 可以使用上一行的值来填充空值，对第一行有空值的情况无法填充
* ffill(axis=1) 用前一列的值来填充
* dropna() 可以删除缺失值
* fillna() 缺失值填充


### 重复值处理
* drop_duplicates() 去掉重复值


## Pandas 数据调整
```
def pandas_adjust_test():
    df = pd.DataFrame({"A": [5, 3, None, 4],
                 "B": [None, 2, 4, 3],
                 "C": [4, 3, 8, 5],
                 "D": [5, 4, 2, None]})
    print('#' * 20)
    print ("")
    ndf = df['B']
    print (ndf)

    ndf = df[['A', 'C']]
    print (ndf)
    
    ndf = df.iloc[:, [0, 1]]
    print (ndf)

    print('###################')
    print ("row choice")
    ndf = df.loc[ [0, 2] ]
    print (ndf)
    ndf = df.loc[0:2]
    print (ndf)
    print ('*' * 20)

    print('##### compare #####')
    ndf = df[df['A'] > 4]
    print (ndf)
    ndf = df[(df['A'] > 3) & (df['C'] > 4)]
    print (ndf)

    print('##### replace #####')
    ndf = df.replace(4, 40)
    print (ndf)
    ndf = df.replace(np.nan, 100)
    print (ndf)
    ndf = df.replace([1, 2, 3], 200)
    print (ndf)
    # 多对多替换
    df.replace({4:400,5:500,8:800})    
    

    print('##### sort #####')
    ndf = df.sort_values(by=['A'], ascending=False)
    print (ndf)
    # 多列排序
    df.sort_values(by=['A', 'C'], ascending=[True, False])

    print('##### drop #####')
    # 删除
    # 删除列
    df.drop( 'A' ,axis = 1)
    
    # 删除行
    df.drop( 3 ,axis = 0)
    
    # 删除特定行
    df [  df['A'] < 4 ]
    
    print('##### swap #####')
    # 行列互换
    print(df.T)
    print(df.T.T)

    df4 = pd.DataFrame([
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ],
        columns=['one', 'two', 'three'],
        index=['first', 'second']
    )
    print (df4)
    print (df4.stack())
    print (df4.unstack())
    print (df4.stack().reset_index())
```
```
####################

0    NaN
1    2.0
2    4.0
3    3.0
Name: B, dtype: float64
     A  C
0  5.0  4
1  3.0  3
2  NaN  8
3  4.0  5
     A    B
0  5.0  NaN
1  3.0  2.0
2  NaN  4.0
3  4.0  3.0
###################
row choice
     A    B  C    D
0  5.0  NaN  4  5.0
2  NaN  4.0  8  2.0
     A    B  C    D
0  5.0  NaN  4  5.0
1  3.0  2.0  3  4.0
2  NaN  4.0  8  2.0
********************
##### compare #####
     A   B  C    D
0  5.0 NaN  4  5.0
     A    B  C   D
3  4.0  3.0  5 NaN
##### replace #####
      A     B   C     D
0   5.0   NaN  40   5.0
1   3.0   2.0   3  40.0
2   NaN  40.0   8   2.0
3  40.0   3.0   5   NaN
       A      B  C      D
0    5.0  100.0  4    5.0
1    3.0    2.0  3    4.0
2  100.0    4.0  8    2.0
3    4.0    3.0  5  100.0
       A      B    C      D
0    5.0    NaN    4    5.0
1  200.0  200.0  200    4.0
2    NaN    4.0    8  200.0
3    4.0  200.0    5    NaN
##### sort #####
     A    B  C    D
0  5.0  NaN  4  5.0
3  4.0  3.0  5  NaN
1  3.0  2.0  3  4.0
2  NaN  4.0  8  2.0
##### drop #####
##### swap #####
     0    1    2    3
A  5.0  3.0  NaN  4.0
B  NaN  2.0  4.0  3.0
C  4.0  3.0  8.0  5.0
D  5.0  4.0  2.0  NaN
     A    B    C    D
0  5.0  NaN  4.0  5.0
1  3.0  2.0  3.0  4.0
2  NaN  4.0  8.0  2.0
3  4.0  3.0  5.0  NaN

       one two three
first    a   b     c
second   d   e     f
first   one      a
        two      b
        three    c
second  one      d
        two      e
        three    f
dtype: object
one    first     a
       second    d
two    first     b
       second    e
three  first     c
       second    f
dtype: object
  level_0 level_1  0
0   first     one  a
1   first     two  b
2   first   three  c
3  second     one  d
4  second     two  e
5  second   three  f
```
* 通过列名，可以筛选出相应的列，如果是多个列，需要使用 list 指定列
* 可以通过列序号来筛选列，df.iloc[:, [0, 1]] , ":"表示所有行，第1，2列
* DataFrame.loc[] 可以用来行选择， 参数为行号
* 比较， 通过比较来筛选数据
* replace 替换。可以替换空值，单值，多值（list 指定被替换的值）。多对多替换使用字典
* 排序。sort_values， 通过“by” 来指定排序的参考列，ascending 来指定升序或降序。 还有sort_index ???
* drop 删除。可以通过列名或者行号删除，也可以指定条件删除
* 行列互换
* 数据透视表


## Pandas 基本操作

```
def pandas_operate_test():
    df = pd.DataFrame({"A": [5, 3, None, 4],
                 "B": [None, 2, 4, 3],
                 "C": [4, 3, 8, 5],
                 "D": [5, 4, 2, None]})
    print('#' * 20)
    print (df['A'] + df['C'])
    print('#' * 20)
    print (df["B"] + 7)
    print('#' * 20)
    print (df['A'] > 4)
    print('#' * 20)
    print (df.count())
```
```
####################
0    9.0
1    6.0
2    NaN
3    9.0
dtype: float64
####################
0     NaN
1     9.0
2    11.0
3    10.0
Name: B, dtype: float64
####################
0     True
1    False
2    False
3    False
Name: A, dtype: bool
####################
A    3
B    3
C    4
D    3
dtype: int64
```
可进行列与列，列与常数之间的运算， 比较.空值不参与运算。
更多内容参考[计算工具说明](https://pandas.pydata.org/docs/user_guide/computation.html#method-summary)

## Pandas 分组和聚合
数据集一般是列表嵌套字典的形式，如表格
|a|b|c|d|
|-|-|-|-|
|1|2|3|4|
|5|6|7|8|
|1|9|7|4|
对应的形式为 `[{'a': 1, 'b': 2, 'c': 3, 'd': 4,}, {'a': 5, 'b': 6, 'c': 7, 'd': 8,}, {'a': 1, 'b': 9, 'c': 7, 'd': 4, }]`


```
def group_test():
    data = [{'name': 'Jame', 'age': 9, 'class': 3, 'd': 4, },
            {'name': 'Tom', 'age': 17, 'class': 7, 'd': 7, },
            {'name': 'Dave', 'age': 9, 'class': 7, 'd': 4, }, ]

    df = pd.DataFrame(data)
    print (df)

    print ('#' * 20)
    ret = df.groupby('age')
    print (type(ret))
    print (ret.groups)

    print ("------------")
    print (ret.count())

    print (ret.aggregate({'class': 'count', 'd': 'sum'}))

    print ("*" * 20)
    print ("------  mean  ------")
    print (ret.agg("mean"))
    print ("------  mean to_dict ------")
    print (ret.mean().to_dict())
    print (ret.transform("mean"))
```
```
 name  age  class  d
0  Jame    9      3  4
1   Tom   17      7  7
2  Dave    9      7  4
####################
<class 'pandas.core.groupby.generic.DataFrameGroupBy'>
{9: Int64Index([0, 2], dtype='int64'), 17: Int64Index([1], dtype='int64')}
------------
     name  class  d
age                
9       2      2  2
17      1      1  1
     class  d
age          
9        2  8
17       1  7
********************
------  mean  ------
     class  d
age          
9        5  4
17       7  7
------  mean to_dict ------
{'class': {9: 5, 17: 7}, 'd': {9: 4, 17: 7}}
   class  d
0      5  4
1      7  7
2      5  4
```
* 通过groupby方法来进行分组，返回的是一个 pandas.core.groupby.generic.DataFrameGroupBy 对象， 通过属性 groups 来得到分组信息。对学生信息使用年龄分组，得到两组信息，9和17
* count 方法用来统计数量
* 分组后对某列进行求和、计数等操作  groupby().aggregate()
* 分组后求平均值 groupby().aggregate(“mean”) 或者 groupby().mean()
* 将处理结果转化为 dict  , to_dict()
* transform 和 agg 的区别。在结果上， transform 不会按组合并


### 数据透视表

## Pandas 多表拼接

```
def mutiple_test():
    group = ['x', 'y', 'z']
    data1 = pd.DataFrame({
        "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
        "age":np.random.randint(15,50,10)
        })
    
    data2 = pd.DataFrame({
        "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
        "salary":np.random.randint(5,50,10),
        })
    
    data3 = pd.DataFrame({
        "group": [group[x] for x in np.random.randint(0, len(group), 10)],
        "age": np.random.randint(15, 50, 10),
        "salary": np.random.randint(5, 50, 10),
    })

    print ("data1: \n", data1)
    print ("data2: \n", data2)
    print ("data3: \n", data3)

    print ("merge data1 and data2")
    print (pd.merge(data1, data2))
    
    print ("merge data2 and data3")
    print (pd.merge(data3, data2, on='group'))
    print('#' * 20)
    print (pd.merge(data3, data2))
    
    # 连接键类型，解决没有公共列问题
    print(pd.merge(data3, data2, left_on='age', right_on='salary'))

   
    # 连接方式
    # 内连接，不指明连接方式，默认都是内连接
    pd.merge(data3, data2, on= 'group', how='inner')
    # 左连接 left
    # 右连接 right
    # 外连接 outer
    
    # 纵向拼接
    pd.concat([data1, data2])
```
```
```
* 使用 merge 方法进行多表拼接.一对一拼接时自动使用公共列来做连接。多对一拼接时需要指定公共列。多对多， 不指定公共列，则查找所有相同的条目
* 没有公共列的情况，手动指定连接键
* 
## Pandas 输出和制图

### 输出
* pandas 可以将处理的数据输出为 dict ,交给 Python 处理。也可以输出到文件。比如 excel(to_excel()), 需要安装 pip install openpyxl
* 输出到excel 时可以指定 sheet 名
* 默认是添加索引的， 要去掉索引， 设置参数 `index=False`
* 要导出指定的列， 设置参数 columns
* 字符编码设置 encoding
* 缺失值处理 na_rep
* to_json(), to_csv(), to_hdf()......

```
def output_test():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, },
     {'a': 5, 'b': 6, 'c': 7, 'd': 8, },
     {'a': 1, 'b': 9, 'c': 7, 'd': 4, }, ]
    
    df = pd.DataFrame(data)
    df.to_excel(excel_writer="aaa.xlsx", sheet_name="xxxx",
                index=False, columns=['a', 'c'])
```

尽量使用内置函数

### 绘图
需要使用 matplotlib 库
使用 matplotlib.pyplot， 指定横纵坐标，即可绘图


<font color=#ff0000 size=5 face="黑体">导入库出错</font>


## jieba 分词与提取关键词


## snowNLP情感倾向分析

