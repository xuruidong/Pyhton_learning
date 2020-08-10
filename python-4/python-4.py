# -*- coding:utf-8 -*-
from sklearn import datasets
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
    
if __name__ == "__main__":
    # sklearn_test()
    # file_path_test()
    # series_test()
    DateFrame_test()
    print ("===  end  ===")
    
