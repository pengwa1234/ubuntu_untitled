import pymysql

try:
    # 创建数据库连接
    conn = pymysql.Connect(host='localhost', user='root', password='password', database='ex01', port=3306,
                           charset='utf8')

    # 创建cursor对象执行sql语句
    cursor = conn.cursor()

    # 插入语句到数据库
    sql = 'insert into students(name) values("xiaoming11");'


    # 执行单条sql语句
    cursor.execute(sql)



    # 提交
    conn.commit()

    cursor.close()
    conn.close()

except Exception as e:
    print(e)
