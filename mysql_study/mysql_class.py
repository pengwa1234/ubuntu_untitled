import pymysql


class Mysql(object):
    def __init__(self, host, user, password, database, charset='utf8', port='3306'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def myconnet(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def excute_one(self, sql, param=()):
        try:
            self.myconnet()
            self.cursor.execute(sql, param)
        except Exception as e:
            print(e)
            self.db.rollback()
        else:
            self.db.commit()
        finally:
            self.close()

    def excute_many(self, sql, param):
        try:
            self.myconnet()
            self.cursor.executemany(sql, param)
        except Exception as e:
            print(e)
            self.db.rollback()
        else:
            self.db.commit()
        finally:
            self.close()

    def get_one(self, sql, param=()):
        try:
            self.myconnet()
            self.cursor.execute(sql, param)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(e)

    def get_many(self, sql, param=()):
        try:
            self.myconnet()
            self.cursor.execute(sql, param)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


if __name__ == '__main__':
    mydb = Mysql('localhost', 'root', 'password', 'py3')
    sql1='insert into students(name) VALUES (%s);'
    mydb.excute_many(sql1,['小花1','小明1','小兔子1','小猪猪1'])
    sql = 'select * from students;'
    res=mydb.get_many(sql)
    print(res)

