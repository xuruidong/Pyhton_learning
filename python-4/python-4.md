# python-4 Pandas

## pandas 简介

### 测试数据来源
sklearn 提供了机器学习的数据集，暂时免去数据清洗的过程

* 引入数据集 `from sklearn import dateset`
* 加载鸢尾花数据 `iris = datasets.load_iris()`, 其他数据集如 load_Boston 波士顿房价 回归， load_digits 手写体 分类
* 返回的数据类型是 sklearn.utils.Bunch， 继承 dict 的类。使用 `x, y = iris.data, iris.target` 将数据和目标分离， x是花瓣特征（长短宽窄），y是特征对应的花的种类。
* 使用`iris.feature_names` 可以获得特征名， `iris.target_names` 获得种类名称
* 使用训练集和测试集分类功能， 可以把x y按照一定的比例来划分，

