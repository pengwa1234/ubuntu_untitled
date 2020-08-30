from redisHelper import redisHelper

from mysql_class import Mysql

from hashlib import sha1

import hashlib

# 接受输入
name = input("请输入用户名：")
pwd1 = input("请输入密码:")

# 加密
s1 = sha1()
s1.update(pwd1.encode('utf-8'))
pwd2 = s1.hexdigest()

# 查询redis中是否存在此用户
r = redisHelper('localhost', 6379)
# print(r.get(name)) 如果不存在返回的是None

mydb = Mysql('localhost', 'root', 'password', 'ex01')
if r.get(name) == None:
    sql = 'select password from students where name=%s;'
    result = mydb.get_one(sql, name)
    if result == None:
        print("用户不存在")
    else:
        print(result)
        if pwd2 == result[0]:
            print('登陆成功')
            r.set(name, pwd2)
            print('123')
        else:
            print('密码不正确')
else:
    print(r.get(name))
    # 这里需要转码一下，返回的是b'fc19318dd13128ce14344d066510a982269c241b'(byte类型)，与pwd2类型不一致
    if r.get(name).decode('utf-8') == pwd2:
        print('登陆成功')
    else:
        print('密码输入错误')
