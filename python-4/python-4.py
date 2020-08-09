# -*- coding:utf-8 -*-
from sklearn import datasets

def sklearn_test():
    iris = datasets.load_iris()
    print (type(iris))
    print (iris.feature_names)
    print (iris.target_names)


if __name__ == "__main__":
    sklearn_test()
    print ("===  end  ===")
    
