from mysql_class import Mysql

import hashlib

# 用户输入
user = input("请输入名字:")
password = input("请输入密码:")

m = hashlib.sha1()
m.update(password.encode('utf-8'))
new_password = m.hexdigest()

param=[user,new_password]

mydb = Mysql('localhost', 'root', 'password', 'ex01')
sql = 'select name from userinfo'
names = mydb.get_many(sql)
# print(names)
for name in names:
    if name[0] == user:
        print(type(name[0]))
        print(user)
        print("该用户已经存在")
        break
else:
    sql1 = 'insert into userinfo(name,password) values(%s,%s)'
    mydb.excute_one(sql1, param)
    print("注册成功")