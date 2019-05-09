# -*- coding:utf-8 -*-
import cx_Oracle
import traceback
# import time
# from tkinter import messagebox


class db_connect():
    username = 'MES'
    password = 'MES'
    ip = '10.2.0.25:1521/MES08'
    # conn = None
    # cr = None

    def db_conn(self):
        try:
            conn = cx_Oracle.connect(db_connect.username, db_connect.password, db_connect.ip, encoding="UTF-8",
                                     nencoding="UTF-8")
            db_connect.conn = conn
            print('connect success')
            # return True
        except Exception:
            traceback.print_exc()
            # messagebox.showerror('警告', '数据库连接失败，请检查网络连接！')
            # exit()
            return False
        return True

    def db_close(self):
        try:
            db_connect.conn.close()
            print('connect close')
        except Exception:
            traceback.print_exc()

    def create_cursor(self):
        db_connect.cr = db_connect.conn.cursor()

    def sql_search(self):
        sql = 'select * from line where rownum<25'
        db_connect.cr.execute(sql)
        # global xs
        xs = db_connect.cr.fetchall()
        return xs


# if __name__ == '__main__':
#     # conn = cx_Oracle.connect(db_connect.username, db_connect.password, db_connect.ip)
#     db = db_connect()
#     db.db_conn()
#     # print('db connect')
#     db.create_cursor()
#     db.sql_search()
#
#     time.sleep(2)
#     db.db_close()
#     exit()

