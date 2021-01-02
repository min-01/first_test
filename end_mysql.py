import pymysql
import datetime

connect = pymysql.connect(host='localhost',
                          database='test',
                          charset='utf8',
                          user='root',
                          password='12116szh'
                          )


class Thing:
    def __init__(self, thing, time, status):
        self.thing = thing
        self.time = time
        self.status = status

    @staticmethod
    def add_todo(thing):
        connect.ping(reconnect=True)
        cur = connect.cursor()
        try:
            insert_sql = "insert into todo value('%s','%s','%s','%s','%s')" % (thing, datetime.datetime.now(), 0, getuser.account, getuser.password)
            cur.execute(insert_sql)
        except Exception as e:
            print("待办添加失败", e)
        else:
            connect.commit()
            print("添加成功！")
        cur.close()
        connect.close()

    @staticmethod
    def query_thing():
        connect.ping(reconnect=True)
        cur = connect.cursor()
        sql = "select thing,time,status from todo where account='%s' and password='%s'" % (getuser.account, getuser.password)
        cur.execute(sql)
        rows = cur.fetchall()
        things = []
        for r in rows:
            thing = Thing(r[0], r[1], r[2])
            things.append(thing)
        cur.close()
        connect.close()
        return things


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # def create_namelist(self):
    #     cur = connect.cursor()
    #     try:
    #         create_sql = "create table student (id int(10), name varchar(30), sex varchar(5), grade varchar(100), tel varchar(12), email varchar(50), choose_location varchar(20), introduce_yourself varchar(800)) ENGINE=InnoDB DEFAULT CHARSET=utf8"
    #         cur.execute(create_sql)
    #     except Exception as e:
    #         print("表已经存在或创建失败", e)
    #     else:
    #         print("表创建成功;")
    #     connect.commit()
    #     cur.close()
    #     connect.close()

    def add_one(id, name, sex, grade, tel, email, choose_location, introduce_yourself):
        connect.ping(reconnect=True)
        cur = connect.cursor()
        try:
            insert_sql = "insert into student value('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                id, name, sex, grade, tel, email, choose_location, introduce_yourself)
            cur.execute(insert_sql)
        except Exception as e:
            print("报名失败", e)
        else:
            connect.commit()
            print("报名成功！")
        cur.close()
        connect.close()

    @staticmethod
    def query_all():
        connect.ping(reconnect=True)
        cur = connect.cursor()
        sql = "select name,id from student"
        cur.execute(sql)
        rows = cur.fetchall()
        users = []
        for r in rows:
            user = User(r[1], r[0])
            users.append(user)
        connect.commit()
        cur.close()
        connect.close()
        return users


class getuser:
    account = '1@123'
    password = '123'

    @staticmethod
    def set(account, password):
        getuser.account = account
        getuser.password = password
