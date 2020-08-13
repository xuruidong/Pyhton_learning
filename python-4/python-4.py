# -*- coding:utf-8 -*-
#from sklearn import datasets
import os
import pandas as pd


def sklearn_test():
    iris = datasets.load_iris()
    print (type(iris))
    print (iris.feature_names)
    print (iris.target_names)


def file_path_test():
    print ("__file__ is ", __file__)
    print ("os.path.realpath(__file__) :", os.path.realpath(__file__))
    print ("os.path.dirname(os.path.realpath(__file__)): ",
           os.path.dirname(os.path.realpath(__file__)))
    #print ("new path: ", )
    

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
    

def DateFrame_test():
    data = [['a','b','c'], ['d','e','f']]
    d = pd.DataFrame(data)
    print (d)
    
    d.columns = ['aa', 'bb', 'cc']
    d.index = ['A', 'B']
    print(d)


def pd_read_test():
    data = pd.read_csv()
    data2 = pd.read_excel()
    data3 = pd.read_sql()


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
    
    
def pandas_adjust_test():
    df = pd.DataFrame({"A": [5, 3, None, 4],
                 "B": [None, 2, 4, 3],
                 "C": [4, 3, 8, 5],
                 "D": [5, 4, 2, None]})

    ndf = df[['A', 'C']]
    print (ndf)
    
    ndf = df.iloc[:, [0, 1]]
    print (ndf)
    
    ndf = df.loc[ [0, 2] ]
    print (ndf)
    ndf = df.loc[0:2]
    print (ndf)
    print ('*' * 10)
    
    ndf = df[df['A'] > 4]
    print (ndf)
    ndf = df[(df['A'] > 3) & (df['C'] > 4)]
    print (ndf)
    
    ndf = df.replace(4, 40)
    print (ndf)
    ndf = df.replace(np.nan, 100)
    print (ndf)
    ndf = df.replace([1, 2, 3], 200)
    print (ndf)
    # 多对多替换
    df.replace({4:400,5:500,8:800})    
    

    ndf = df.sort_values(by=['A'], ascending=False)
    print (ndf)
    # 多列排序
    df.sort_values(by=['A', 'C'], ascending=[True, False])

    
    # 删除
    # 删除列
    df.drop( 'A' ,axis = 1)
    
    # 删除行
    df.drop( 3 ,axis = 0)
    
    # 删除特定行
    df [  df['A'] < 4 ]
    
    
    # 行列互换
    df.T
    df.T.T    
    
    
def xxx():
    [{'a': 1, 'b': 2, 'c': 3, 'd': 4,}, {'a': 5, 'b': 6, 'c': 7, 'd': 8,}]
    
if __name__ == "__main__":
    # sklearn_test()
    # file_path_test()
    # series_test()
    # DateFrame_test()
    # pre_proc_test()
    pandas_adjust_test()
    print ("===  end  ===")
    
