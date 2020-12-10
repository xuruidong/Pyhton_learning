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
* 通过列名，可以筛选出相应的列，需要使用 list 指定列
* 可以通过列序号来筛选列， 
* DataFrame.loc[] 可以用来行选择， 参数为 
* 比较
* replace 替换。可以替换空值，单值，多值（list 指定被替换的值）
* 排序。sort_values， 通过“by” 来指定排序的参考列，ascending 来指定升序或降序。 还有sort_index ???
* drop 删除。

<font color=#ff0000 size=5 face="黑体">未完成， 再看</font>

## Pandas 基本操作
[计算工具说明](https://pandas.pydata.org/docs/user_guide/computation.html#method-summary)


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
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, },
     {'a': 5, 'b': 6, 'c': 7, 'd': 8, },
     {'a': 1, 'b': 9, 'c': 7, 'd': 4, }, ]

    df = pd.DataFrame(data)
    print (data)
    
    ret = df.groupby('a')
    print (type(ret))
    print (ret.groups)

    print ("------------")
    print (ret.count())

    print (ret.aggregate({'a': 'count', 'b': 'sum'}))

    print ("*" * 20)
    print (ret.agg("mean"))
    print (ret.mean().to_dict())
    print (ret.transform("mean"))
```

* 通过groupby方法来进行分组，返回的是一个 pandas.core.groupby.generic.DataFrameGroupBy 对象， 通过属性 groups 来得到分组信息
* count 方法用来统计数量
* 分组后对某列进行求和  groupby().aggregate()
* 分组后求平均值 groupby().aggregate(“mean”) 或者 groupby().mean()
* 将处理结果转化为 dict  , to_dict()
* transform 和 agg 的区别。在结果上， transform 不会按组合并


### 数据透视表

## Pandas 多表拼接

## Pandas 输出和制图

### 输出
* pandas 可以将处理的数据输出为 dict ,交给 Python 处理。也可以输出到文件。比如 excel(to_exvel()), 需要安装 pip install openpyxl
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

