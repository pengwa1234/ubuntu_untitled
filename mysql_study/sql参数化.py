import pymysql

# 创建一个数据库连接
conn = pymysql.connect(host='localhost', user='root', password='password', database='ex01', charset='utf8')

# 创建一个游标
cursor = conn.cursor()

param = '笑话'

# 参数化sql
sql = 'insert into students(NAME) values(%s);'

try:
    # 执行sql语句
    cursor.execute(sql, param)

except Exception as e:
    print(e)
    conn.rollback()

else:
    conn.commit()

finally:
    cursor.close()
    conn.close()
