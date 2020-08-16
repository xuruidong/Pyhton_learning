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
    

def output_test():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, },
     {'a': 5, 'b': 6, 'c': 7, 'd': 8, },
     {'a': 1, 'b': 9, 'c': 7, 'd': 4, }, ]
    
    df = pd.DataFrame(data)
    df.to_excel(excel_writer="aaa.xlsx", sheet_name="xxxx",
                index=False, columns=['a', 'c'])
    
#import matplotlib.pyplot as plt
def draw_test():
    dates = pd.date_range('20200101', periods=12)
    df = pd.DataFrame(np.random.randn(12, 4),
                      index=dates, columns=list('ABCD'))
    print (df)

    plt.plot(df.index, df['A'])
    plt.show()
    

def test():
    group = ['x', 'y', 'z']
    data = pd.DataFrame({
        "group": [group[x] for x in np.random.randint(0, len(group), 15)],
        "salary": np.random.randint(5, 50, 15),
        "age": np.random.randint(15, 50, 15),
        "id": [995 + i for i in range(15)],
        # "order_id": np.random.randint(2005, 2010, 15),
    })
    table1 = data
    table2 = None
    
    # select * from data
    print (data.values)

    # select * from data limit 10
    print (data[0:10])
    
    # select id from data
    print (data["id"])

    # select count(id) from data
    print (data["id"].count())
    
    # select * from data where id < 1000 and age > 30
    print (data[(data["id"] < 1000) & ((data["age"] > 30))])

    # =====================
    print ("\n=====================")
    table1 = pd.DataFrame({
        "id": np.random.randint(995, 1005, 15),
        "order_id": np.random.randint(2005, 2010, 15),
    })
    print (table1)
    
    # 6. select id,count(DISTINCT order_id) from table1 groupby id
    tb = table1.drop_duplicates(['order_id'])
    print (tb)
    
    grp = tb.groupby('id')
    ret = grp.aggregate({'order_id': 'count'})
    print (ret)

    print ("\n7. =====================")
    # 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    print(pd.merge(table1, data, on="id", how="inner"))

    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    pd.concat([table1, table2])

    # 9. DELETE FROM table1 WHERE id=10;
    res = table1[table1["id"] != 10]
    print(res)
    

    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    del table1['id']
    print (table1)
    
    
    
if __name__ == "__main__":
    # sklearn_test()
    # file_path_test()
    # series_test()
    # DateFrame_test()
    # pre_proc_test()
    # pandas_adjust_test()
    #group_test()
    # output_test()
    # draw_test()
    test()
    print ("===  end  ===")
    
