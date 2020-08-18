import pymysql

# 创建数据库连接
conn=pymysql.connect(host='localhost',user='root',password='password',database='ex01',charset='utf8')

# 创建游标
cursor=conn.cursor()


# 多个参数
# param=[("小兔子"),("小牛"),("小猪")]
param=(("小兔子1"),("小牛1"),("小猪1"))

# sql语句
sql='insert into students(name) values(%s);'


try:
    # 执行sql语句
    cursor.executemany(sql,param)

except Exception as e:
    print(e)
    conn.rollback()

else:
    conn.commit()

finally:
    cursor.close()
    conn.close()
