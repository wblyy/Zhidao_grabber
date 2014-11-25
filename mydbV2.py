# -*- coding: utf-8 -*-
import MySQLdb

class BaseDB(object):
    def __init__(self, database=None, user=None, passwd=None, host=None):
        self.database = database if database else 'mysql'
        self.user = user if user else 'root'
        self.passwd = passwd if passwd else '654321'
        #self.host = host if host else '114.243.222.166'#不需要输端口号
        self.host = host if host else 'soniegg.oicp.net'

    @property
    def db(self):
        return MySQLdb.connect(self.host, self.user, self.passwd, self.database, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        insert_id = cur.lastrowid
        conn.commit()
        return insert_id
        
    def _query_rows(self, *args):
        cur = self.db.cursor()
        cur.execute(*args)
        return cur.fetchall()

    def test_db(self):
        return self._query_rows('show tables')

class MydbV2(BaseDB):
    def __init__(self):
        BaseDB.__init__(self, database='zhidao_whole')

    def insert_data(self, qid, title, content, style, is_used,is_answerable,related_IP):
        self._execute(r'insert ignore zhidao_lib(qid, title, content, style, is_used,is_answerable,related_IP) '
                      r'values (%s, %s, %s, %s, %s, %s, %s)', (qid, title, content, style, is_used,is_answerable,related_IP))
    
