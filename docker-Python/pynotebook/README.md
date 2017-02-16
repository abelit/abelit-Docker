# Using python connect to oracle
## 1. Install driver to connect to oracle
> pip install cx_Oracle

## 2. Demo code
### Example 1. using cx_Oracle
```
import cx_Oracle
    if username == 'sys':
        conn = cx_Oracle.connect(username, password, host + ':' + str(port) + '/' + instance, cx_Oracle.SYSDBA)
    else:
        conn = cx_Oracle.connect(username, password, host + ':' + str(port) + '/' + instance)
```

# Using python connect to postgresql
## 1. Install driver to connect to postgresql
> pip install psycopg2

## 2. Demo code
### Example 1. using pyscopg2
```
import psycopg2

dbname = ""
username = ""
password = ""
host = "127.0.0.1"
port = "5432"

conn = psycopg2.connect(database=dbname, user=username, password=password, host=host, port=port)
cur = conn.cursor()
cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
cur.execute("SELECT * FROM product_category;")
rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()
```
### Example 2. using py-postgresql
```
from datetime import date, datetime, timedelta
import pymysql.cursors

#连接配置信息
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'zhyea.com',
          'db':'employees',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
# 创建连接
connection = pymysql.connect(**config)

# 获取明天的时间
tomorrow = datetime.now().date() + timedelta(days=1)

# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(sql, ('Robin', 'Zhyea', tomorrow, 'M', date(1989, 6, 14)));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close();
```

# Using python connect to mysql
## 1. Install driver to connect to mysql
> pip install PyMySQL

## 2. Demo code
### Example 1. using PyMySQL
```
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
```

```
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

# Using python connect to redis
## 1. Install driver to connect to redis
> pip install redis

## 2. Demo code
### Example 1. using redis
```
>>> import redis
>>> r = redis.StrictRedis(host='localhost', port=6379, db=0)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
'bar'
```

### Example 2. using redis
```
import time
from redis import Redis
from datetime import datetime
ONLINE_LAST_MINUTES = 5
redis = Redis()

def mark_online(user_id):         #将一个用户标记为online
    now = int(time.time())        #当前的UNIX时间戳
    expires = now + (app.config['ONLINE_LAST_MINUTES'] * 60) + 10    #过期的UNIX时间戳
    all_users_key = 'online-users/%d' % (now // 60)        #集合名，包含分钟信息
    user_key = 'user-activity/%s' % user_id                
    p = redis.pipeline()
    p.sadd(all_users_key, user_id)                         #将用户id插入到包含分钟信息的集合中
    p.set(user_key, now)                                   #记录用户的标记时间
    p.expireat(all_users_key, expires)                     #设定集合的过期时间为UNIX的时间戳
    p.expireat(user_key, expires)
    p.execute()

def get_user_last_activity(user_id):        #获得用户的最后活跃时间
    last_active = redis.get('user-activity/%s' % user_id)  #如果获取不到，则返回None
    if last_active is None:
        return None
    return datetime.utcfromtimestamp(int(last_active))

def get_online_users():                     #获得当前online用户的列表
    current = int(time.time()) // 60        
    minutes = xrange(app.config['ONLINE_LAST_MINUTES'])
    return redis.sunion(['online-users/%d' % (current - x)        #取ONLINE_LAST_MINUTES分钟对应集合的交集
                         for x in minutes])
```

# Using python connect to mongodb
## 1. Install driver to connect to mongodb
> pip install pymongo

## 2. Demo code
### Example 1. using pymongo
```
import pymongo
import datetime


def get_db():
    # 建立连接
    client = pymongo.MongoClient(host="10.244.25.180", port=27017)
    db = client['example']
    #或者 db = client.example
    return db


def get_collection(db):
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db['informations']
    print db.collection_names()
    return coll


def insert_one_doc(db):
    # 插入一个document
    coll = db['informations']
    information = {"name": "quyang", "age": "25"}
    information_id = coll.insert(information)
    print information_id


def insert_multi_docs(db):
    # 批量插入documents,插入一个数组
    coll = db['informations']
    information = [{"name": "xiaoming", "age": "25"}, {"name": "xiaoqiang", "age": "24"}]
    information_id = coll.insert(information)
    print information_id


def get_one_doc(db):
    # 有就返回一个，没有就返回None
    coll = db['informations']
    print coll.find_one()  # 返回第一条记录
    print coll.find_one({"name": "quyang"})
    print coll.find_one({"name": "none"})


def get_one_by_id(db):
    # 通过objectid来查找一个doc
    coll = db['informations']
    obj = coll.find_one()
    obj_id = obj["_id"]
    print "_id 为ObjectId类型，obj_id:" + str(obj_id)

    print coll.find_one({"_id": obj_id})
    # 需要注意这里的obj_id是一个对象，不是一个str，使用str类型作为_id的值无法找到记录
    print "_id 为str类型 "
    print coll.find_one({"_id": str(obj_id)})
    # 可以通过ObjectId方法把str转成ObjectId类型
    from bson.objectid import ObjectId

    print "_id 转换成ObjectId类型"
    print coll.find_one({"_id": ObjectId(str(obj_id))})


def get_many_docs(db):
    # mongo中提供了过滤查找的方法，可以通过各种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    coll = db['informations']
    #ASCENDING = 1 升序;DESCENDING = -1降序;default is ASCENDING
    for item in coll.find().sort("age", pymongo.DESCENDING):
        print item

    count = coll.count()
    print "集合中所有数据 %s个" % int(count)

    #条件查询
    count = coll.find({"name":"quyang"}).count()
    print "quyang: %s"%count

def clear_all_datas(db):
    #清空一个集合中的所有数据
    db["informations"].remove()

if __name__ == '__main__':
    db = get_db()
    my_collection = get_collection(db)
    post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    # 插入记录
    my_collection.insert(post)
    insert_one_doc(db)
    # 条件查询
    print my_collection.find_one({"x": "10"})
    # 查询表中所有的数据
    for iii in my_collection.find():
        print iii
    print my_collection.count()
    my_collection.update({"author": "Mike"},
                         {"author": "quyang", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
                          "date": datetime.datetime.utcnow()})
    for jjj in my_collection.find():
        print jjj
    get_one_doc(db)
    get_one_by_id(db)
    get_many_docs(db)
    # clear_all_datas(db)
```

# Using python connect to sqlite3
## 1. Install driver to connect to sqlite3
> pip install sqlite3

## 2. Demo code
### Example 1. using sqlite3
```
import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";

conn.close()
```
