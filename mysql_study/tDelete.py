import pymysql
try:
    # 创建一个数据库连接
    conn=pymysql.connect(host='localhost',database='ex01',user='root',password='password',charset='utf8')

    # 创建一个游标
    cursor=conn.cursor()

    # 删除名字包含xiaoming的语句
    sql='delete from students where name like"%xiaoming%"; '

    # 执行sql语句
    cursor.execute(sql)

    # 提交语句
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭数据库连接
    conn.close()

except Exception as e:
    print(e)