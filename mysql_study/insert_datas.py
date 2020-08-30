from mysql_class import Mysql
import hashlib

while True:
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

    # 插入数据，插入sha1的密码,方式一：格式化的方式输入
    # sql = 'insert into students(name,password) values("%s","%s")' % (name, new_password1)

    # 方式二：利用excute_one()中的param输入
    sql = 'insert into students(name,password) values(%s,%s)'
    print(sql)
    mydb.excute_one(sql,(name,new_password1))
