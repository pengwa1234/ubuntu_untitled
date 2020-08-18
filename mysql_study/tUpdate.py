import pymysql

try:
    # 创建一个数据库连接
    conn=pymysql.connect(host='localhost',database='ex01',user='root',password='password',charset='utf8')

    # 建立一个数据库游标
    cursor=conn.cursor()

    # 执行修改数据库的语句
    sql='update students set name="小红" WHERE id="1";'

    # 执行该sql语句
    cursor.execute(sql)

    # 提交
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭数据库
    conn.close()

except Exception as e:
    print(e)