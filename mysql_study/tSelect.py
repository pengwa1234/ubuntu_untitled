import pymysql

try:
    # 创建数据库连接
    conn = pymysql.Connect(host='localhost', user='root', password='password', database='ex01', port=3306,
                           charset='utf8')

    # 创建cursor对象执行sql语句
    cursor = conn.cursor()

    # 插入语句到数据库
    # sql = 'insert into students(name) values("xiaoming11");'

    # 查询语句
    sql1 = 'select * from students;'

    # 执行单条sql语句
    # cursor.execute(sql)
    cursor.execute(sql1)

    # 执行多条sql语句
    # cursor.executemany(sql1)

    # 返回一条结果,fetchone()和fetchmany(),fetchall()需要和select一起搭配使用
    # data=cursor.fetchone()

    # 返回多条结果
    # data=cursor.fetchmany(10)

    # 返回全部
    data=cursor.fetchall()
    print(data)

    # 提交
    # conn.commit()

    cursor.close()
    conn.close()

except Exception as e:
    print(e)
