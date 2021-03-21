# MySQL

## 1 安装
yum install -y mariadb-server  
查看密码安全设置
show variables like 'validate_password%'  

修改密码策略  

## 2 字符集
查看字符集：  
show variables like '%character%';  
```
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
```
查看校对规则：  
show variables like 'collation_%';  
```
+----------------------+-------------------+
| Variable_name        | Value             |
+----------------------+-------------------+
| collation_connection | utf8_general_ci   |
| collation_database   | latin1_swedish_ci |
| collation_server     | latin1_swedish_ci |
+----------------------+-------------------+
```
MySQL 的utf8 和 UTF-8 不同。
设置字符集
修改配置文件 /etc/my.cnf 
设置MySQL 客户端字符集 
```

```

### utf8 与 utf8mb4 的区别

### MySQL 字符集之间的关系
character_set_client 客户端使用的字符集  
character_set_connection 连接层面的字符集 
character_set_database 当前选中的数据库字符集  
character_set_results 查询结果显示的字符集  
character_set_server 默认字符集  
character_set_system  

在创建数据库时，不指定字符集，使用默认的 character_set_server
```
MariaDB [(none)]> create database db1;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> show create database db1;
+----------+--------------------------------------------------------------------------------------------+
| Database | Create Database                                                                            |
+----------+--------------------------------------------------------------------------------------------+
| db1      | CREATE DATABASE `db1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ |
+----------+--------------------------------------------------------------------------------------------+
```
创建表时，根据数据库的字符集。

## 3 server 配置
interactive_timeout 针对交互式连接的超时设置  
wait_timeout 针对非交互式连接的超时设置  
max_connections 最大连接数  
character_set_server = utf8mb4 MySQL 字符集设置(默认字符集)  
init_connect = 'SET NAMES utf8mb4'  服务器为每一个连接的客户端执行的字符集  
chararcer_set_client_handshake = FALSE  ？？？报错
collation_server = utf8mb4_unicode_ci 
_ci 大小写敏感  _cs 大小写不敏感  

## 4 MySQL 连接
* MySQLdb 是 Python 2的包， 适用于 MySQL5.5 和Python 2.7  
* Python3 安装的MySQLdb 包叫做 mysqlclient, 加载的依然是MySQLdb   
pip install mysqlclient  
import MySQLdb  
* 其他DB-API: 
pymysql,  
mysql-connector-python (MySQL 官方)
* 使用 ORM 
pip install sqlalchemy

### pymysql 连接数据库
创建用户  
grant all privileges on db1.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';  

```
import pymysql

def pymysql_test():
    db = pymysql.connect("192.168.52.74", "testuser", "testpass", "db1")
    
    with db.cursor() as cursor:
        sql = 'select VERSION()'
        cursor.execute(sql)
        result = cursor.fetchone()
        print (result)
    db.commit()
    
    db.close()
```
输出 ('5.5.56-MariaDB',)  

### 使用 sqlalchemy
```
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
    
def sqlalchemy_core_test():
    # 打开数据库连接
    # mysql> create database testdb;
    # mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
    # echo=True 开启调试
    engine=create_engine("mysql+pymysql://testuser:testpass@192.168.52.74:3306/db1",echo=True)
     
    # 创建元数据
    metadata=MetaData(engine)
     
    book_table=Table('book',metadata,
        Column('id',Integer,primary_key=True),
        Column('name',String(20)),
        )
    author_table = Table('author', metadata,
        Column('id', Integer, primary_key=True),
        Column('book_id', None, ForeignKey('book.id')),
        Column('author_name', String(128), nullable=False)
        )
    
    try:
        metadata.create_all()
    except Exception as e:
        print(f"create error {e}")
```

```
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

def sqlalchemy_orm_test():
    # 打开数据库连接
    # mysql> create database testdb;
    # mysql> GRANT ALL PRIVILEGES ON db1.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
    
    Base = declarative_base()
    
    class Book_table(Base): 
        __tablename__ = 'bookorm' 
        book_id = Column(Integer(), primary_key=True) 
        book_name = Column(String(50), index=True) 
    
    
    # book_table=Table('book',metadata,
    #     Column('id',Integer,primary_key=True),
    #     Column('name',String(20)),
    #     )
    
    # 定义一个更多的列属性的类
    # 规范写法要记得写在最上面
    from datetime import datetime 
    from sqlalchemy import DateTime
    
    class Author_table(Base): 
        __tablename__ = 'authororm' 
        user_id = Column(Integer(), primary_key=True) 
        username = Column(String(15), nullable=False, unique=True)
        created_on = Column(DateTime(), default=datetime.now) 
        updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    
    # 实例一个引擎
    dburl="mysql+pymysql://testuser:testpass@192.168.52.74:3306/db1?charset=utf8mb4"
    engine=create_engine(dburl, echo=True, encoding="utf-8")
    
    Base.metadata.create_all(engine) 
```

在类中， 使用`__tablename__` 来指定表名称， 变量名就是字段名，  

## SQL 知识
SQL 语言功能划分：  
DQL: Data Query Language, 数据查询语言（不仅仅是 select ），开发工程师学习的重点  
DDL: Data Definition Language, 数据定义语言，操作库和表结构  
DML：Data Manipulation Language, 数据操作语言，操作表中记录  
DCL: Data Control Language, 数据控制语言，安全和访问权限控制  


外键和级联， 影响性能  
SELECT 查询关键字的顺序：  
SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT  
执行顺序 FROM  WHERE 
* 生产环境因为列数相对较多，一般禁用 SELECT *  
* WHERE 字段为避免全表扫描，一般需要增加索引  

## SQL 聚合函数
SQL 中有算数函数，字符串函数，日期函数，转换函数，聚合函数。 聚合函数一般用于汇总表的数据。
常见的聚合函数：  
* COUNT()   行数
* MAX()     最大值
* MIN()     最小值
* SUM()     求和
* AVG()     平均值

聚合函数忽略空行  
SELECT COUNT(*) FROM table1;  
SELECT COUNT(*), AVG(n_star),MAX(n_star) FROM table1 WHERE id < 10;  
SELECT COUNT(*), n_star FROM table1 GROUP BY n_star;  

## 多表操作
### 子查询
什么是子查询： 需要从查询结果中再次进行查询，才能得到想要的结果。 

子查询需要注意的问题：  
* 关联子查询与非关联子查询的区别
* 何时使用 IN, 何时使用 EXISTS

非关联子查询：
SELECT COUNT(*), n_star FROM table1 GROUP BY n_star HAVING n_star > (SELECT AVG(n_star) FROM table1) ORDER BY n_star DESC;  

小表驱动大表
table1 > table2  
SELECT * FROM table1 WHERE condition IN (SELECT condition FROM table2);  
table1 < table2  
SELECT * from table1 WHERE EXIST (SELECT condition FROM table2 WHERE table2.condition=table1.condition)

### join
搜图 SQL JOINS ![]()
自然连接  

## 事务
概念：  
事务的特性 ACID: 
* A 原子性 atomic
* C 一致性 Consistency
* I 隔离性 isolation
* D 持久性 durability

如何保证事务的特性？
事务的隔离级别  
* 读未提交： 允许读到为提交的数据
* 读已提交：只能读到已经提交的内容
* 可重复读：同一事务在相同查询条件下两次查询得到的数据结果一致
* 可串行化：事务进行串行化，但是牺牲了并发性能

在 MySQL 中，数据是默认提交的(隐式提交)，可以自行关闭，查询状态：
show variables like 'autocommit';  
关闭自动提交：
set autocommit=0;  
使用 BEGIN 关键字，开始一个事务，之后的sql 不会被自动提交，直到遇到 COMMIT,. ROLLBACK 回滚，ROLLBACK TO, 

## pymysql

```
items = [('name', 'xxx'), ('passwd', 'dddd')]
dict(items)
```

## sqlalchemy

### 使用 sqlalchemy 

`__repr__()` 魔术方法的作用  

ORM 分层结构  
业务逻辑层  -> 类
持久层    ->  ORM
数据库层  ->  数据库

```
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey,desc,func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

def sqlalchemy_insert():
    # 打开数据库连接
    # mysql> create database testdb;
    # mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
    Base = declarative_base()
    
    class Book_table(Base):
        __tablename__ = 'bookorm'
        book_id = Column(Integer(), primary_key=True)
        book_name = Column(String(50), index=True)
    
        def __repr__(self):
            return "Book_table(book_id='{self.book_id}', " \
                "book_name={self.book_name})".format(self=self)
    
    
    class Author_table(Base):
        __tablename__ = 'authororm'
        user_id = Column(Integer(), primary_key=True)
        username = Column(String(15), nullable=False, unique=True)
        created_on = Column(DateTime(), default=datetime.now)
        updated_on = Column(DateTime(), default=datetime.now,
                            onupdate=datetime.now)    
    
    # 实例一个引擎
    dburl="mysql+pymysql://testuser:testpass@192.168.52.74:3306/db1?charset=utf8mb4"
    engine=create_engine(dburl, echo=True, encoding="utf-8")
    
    # 创建session
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()
    
    # 增加数据
    book_demo = Book_table(book_name='肖申克的救赎')
    book_demo2 = Book_table(book_name='活着')
    book_demo3 = Book_table(book_name='水浒传')    
    
    # 增加多条数据
    '''
    session.add(book_demo)
    session.add(book_demo2)
    session.add(book_demo3)
    session.flush() 
    session.commit() 
    '''
    print (book_demo)
    # session.add(book_demo)
    
    result = session.query(Book_table).all()
    print (result)
    print ('*1'*30)
    for result in session.query(Book_table):
        print(result)   
        
    print ('*2'*20)
    result = session.query(Book_table).first()
    print ("result: ", result)
    
    # print ('*3'*20)
    # result = session.query(Book_table).scalar()
    # print ("result: ", result)    
    
    # 指定列数
    print ('*4'*20)
    result = session.query(Book_table.book_name).first()  
    print ("result: ", result)
    
    print ('*5'*20)
    for result in session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)):
        print(result)
    
    print ('*6'*20)    
    query = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(3)
    print([result.book_name for result in query])  
    
    print ('*7'*20)   
    result = session.query(func.count(Book_table.book_name)).first()
    print(result)
    
    result = session.query(Book_table).filter(Book_table.book_id > 2, Book_table.book_id < 20).all()
    print( result )
    
    # 连接词
    # from sqlalchemy import and_, or_, not_
    # filter(
    #     or_(
    #         Book_table.xxx.between(100, 1000),
    #         Book_table.yyy.contains('book')
    #     )
    # )  
    
    # update
    '''
    res = session.query(Book_table)
    res = res.filter(Book_table.book_id == 1)
    res.update({Book_table.book_name: 'xxx'})
    print (res.first())
    print (type(Book_table.book_name))
    session.commit() 
    '''
    
    # delete
    res = session.query(Book_table)
    res = res.filter(Book_table.book_id == 2)
    # res.delete()
    session.delete(res.one())
    session.commit()
```

* 在类中， 使用`__tablename__` 来指定表名称， 变量名就是字段名
* SQL datatypes， 有 Integer， String， Decimal， Float, Boolean, Text ， DateTime等等
* 指定约束， 如是否是主键 primary_key=True， 是否唯一 unique=True，是否为空 nullable=False，是否自增 autoincrement 等等
* 通过 create_engine 创建引擎
* 创建 session, session 维护了一个事务， 完成会话提交，会话回滚等操作。 sessionmaker 使用了工厂模式， 创建了一个session 类，
* session.add     INSERT
* session.flush() 如果只使用flush , 不使用 commit, 不会结束事务
* session.commit  COMMIT
* session.query   查询
* query().all()  所有结果。 建议迭代获取结果 for result in session.query(Book_table)
* query().first() 获取第一个值
* query().one() 获取一条记录。只有一条记录时可以使用，否则会抛出异常
* query().scalar() 获取一条记录的第一个值。只有一条记录时可以使用，否则会抛出异常
* 筛选查询列时，在query 传入对于的变量
* order_by 排序， 默认时升序，可以使用desc 进行降序
* limit() 限制条数
* from sqlalchemy import func 后可以使用聚合函数
* 使用 filter 可以进行过滤

## 连接池

```
import pymysql
# pip3 install DBUtils
from dbutils.pooled_db import PooledDB
db_config = {
  "host": "server1",
  "port": 3306,
  "user": "testuser",
  "passwd": "testpass",
  "db": "testdb",
  "charset": "utf8mb4",
  "maxconnections":0,   # 连接池允许的最大连接数
  "mincached":4,        # 初始化时连接池中至少创建的空闲的链接,0表示不创建
  "maxcached":0,        # 连接池中最多闲置的链接,0不限制
  "maxusage" :5,        # 每个连接最多被重复使用的次数,None表示无限制
  "blocking":True       # 连接池中如果没有可用连接后是否阻塞等待
                        #  True 等待; False 不等待然后报错
}
 
spool = PooledDB(pymysql, **db_config) 

conn = spool.connection()
cur = conn.cursor()
SQL = "select * from bookorm;"
cur.execute(SQL)
f = cur.fetchall()
print(f)
cur.close()
conn.close()
```