# python-4 Pandas

## pandas 简介

[Pandas 中文](https://www.pypandas.cn/)

### 测试数据来源
sklearn 提供了机器学习的数据集，暂时免去数据清洗的过程

* 引入数据集 `from sklearn import dateset`
* 加载鸢尾花数据 `iris = datasets.load_iris()`, 其他数据集如 load_Boston 波士顿房价 回归， load_digits 手写体 分类
* 返回的数据类型是 sklearn.utils.Bunch， 继承 dict 的类。使用 `x, y = iris.data, iris.target` 将数据和目标分离， x是花瓣特征（长短宽窄），y是特征对应的花的种类。
* 使用`iris.feature_names` 可以获得特征名， `iris.target_names` 获得种类名称
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
    print (dir(ret))
    
    s1 = pd.Series(['a', 'b', 'c'], index=['A', 'B', 'C'])
    print(s1)
    s2 = pd.Series({'A': 'a', 'B': 'b', 'C': 'c'})
    print (s2)

    print (s1.index)
    print (s1.values)
    
    print (s1.values.tolist())
```
* 可以使用 list 创建
* 创建时可以自定义索引，其中有两种方法，字典或指定index
* 取所有索引 `s.index`, 所有值 `s.values`
* 将值转为 Python 的 list `s.values.tolist()`

### DataFrame
```
def DateFrame_test():
    data = [['a','b','c'], ['d','e','f']]
    d = pd.DataFrame(data)
    print (d)
    
    d.columns = ['aa', 'bb', 'cc']
    d.index = ['A', 'B']
    print(d)
```
* 可以使用二维 list 创建 DataFrame
* 同样可以设置索引

## Pandas 数据导入
通过 `read_xxx()` 方法来从不同类型数据源中导入数据。
```
def pd_read_test():
    data = pd.read_csv()
    data2 = pd.read_excel()
    data3 = pd.read_sql()
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


## Pandas 分组聚合
数据集一般是列表嵌套字典的形式，如表格
|a|b|c|d|
|-|-|-|-|
|1|2|3|4|
|5|6|7|8|
对应的形式为 `[{'a': 1, 'b': 2, 'c': 3, 'd': 4,}, {'a': 5, 'b': 6, 'c': 7, 'd': 8,}]`
