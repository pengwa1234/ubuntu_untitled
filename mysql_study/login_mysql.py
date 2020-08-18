from mysql_class import Mysql
import hashlib

# 用户输入
name = input("请输入用户名:")
password = input("请输入密码:")

m = hashlib.sha1(password.encode('utf-8'))

# 将数据传入哈希对象中, hashlib.sha1(password.encode('utf-8'))等价于m=hashlib.sha1()和
#  m.update(password.encode('utf-8'))这两句;当内容太长的时候,可以使用update多次更新内容,等效更新一次长数据
# m.update(password.encode('utf-8'))

# 获取二进制
# new_password = m.digest()

# 获取16进制
new_password1 = m.hexdigest()

# print(new_password)
# print(new_password1)

# 连接数据库
mydb = Mysql('localhost', 'root', 'password', 'ex01')

# 查询用户名和密码
sql = 'select password from userinfo where name=%s'

result = mydb.get_many(sql, (name))
print(result)

if len(result) == 0:
    print("用户名错误")
else:
    if result[0][0] == new_password1:
        print("登陆成功")
    else:
        print("密码错误")
