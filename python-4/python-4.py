# -*- coding:utf-8 -*-
from sklearn import datasets
import os
import pandas as pd


def sklearn_test():
    iris = datasets.load_iris()
    print (type(iris))
    print (iris)

    x, y = iris.data, iris.target

    # print (x)
    # print (y)
    
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
    
    emails = pd.Series(
        ['abc at aaa.com', 'admin@aa.com', 'aaa@mmm', 'ab@acb.com'])
    import re
    pattern = '[A-Za-z0-9._]+@[A-Za-z0-9._]+\\.[A-Za-z]{2,5}'
    mask = emails.map(lambda x: bool(re.match(pattern, x)))
    print (emails[mask])
    

def DateFrame_test():
    data = [['a','b','c'], ['d','e','f']]
    d = pd.DataFrame(data)
    print (d)
    
    d.columns = ['aa', 'bb', 'cc']
    d.index = ['A', 'B']
    print(d)

    print (type(d.values))


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
    

def snowNLP_test():
    from snownlp import SnowNLP
    text = '[  3] 10.0-11.0 sec   128 KBytes  1.05 Mbits/sec'
    s = SnowNLP(text)
    print (s.words)
    
if __name__ == "__main__":
    # sklearn_test()
    # file_path_test()
    # series_test()
    # DateFrame_test()
    # pre_proc_test()
    # pandas_adjust_test()
    # pandas_operate_test()
    # group_test()
    # mutiple_test()
    # output_test()
    # draw_test()
    # test()
    snowNLP_test()
    print ("===  end  ===")
    
