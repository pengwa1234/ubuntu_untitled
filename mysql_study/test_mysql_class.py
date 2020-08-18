from mysql_class import Mysql

mysql=Mysql('localhost','root','password','ex01')

# param=str(input("情输入一个名字:"))

sql='insert into students(name) values(%s);'

# sql='update students set name=%s where id=1'

# sql1='delete from students where id=1'
# mysql.excute_one(sql,param)
# mysql.excute_one(sql1)

# sql='select name from students where id<6'
# result=mysql.get_one(sql)
result=mysql.excute_many(sql,['xiaohua','xiama'])
print(result)




