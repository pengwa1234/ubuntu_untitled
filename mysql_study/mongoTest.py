
from pymongo import *

# 获取客户端,建立连接
client=MongoClient('mongodb://localhost:27017/stu')

# 切换数据库
db=client.stu

# 获取集合
stu=db.stu

# 增加
# s1=stu.insert_one({'name':'张三丰'})

# 插入多条数据
# stu.insert_many([{'name':'张三丰','gender':1,'age':18},{'name':'张无忌','gender':1,'age':8},{'name':'路东北','gender':0,'age':38},
#                  {'name': '哈哈', 'gender': 0, 'age': 28},{'name':'东东','gender':1,'age':44}])

# 修改
# stu.update_one({'name':'养不会'},{'$set':{'name':'杨不悔'}})
# 修改多条数据
# stu.update_many({'name':'路东北'},{'$set':{'name':'养不会'}})

# 删除
# stu.delete_one({'name':'张督导'})

# 查询
cusor=stu.find({'name':'张三丰'})
for s in cusor:
    print(s['name'])

# cusor=stu.find({'age':{'$gt':20}}).sort('_id',DESCENDING)
cusor=stu.find({'age':{'$gt':20}}).sort('_id',-1)
for i in cusor:
    print(i)