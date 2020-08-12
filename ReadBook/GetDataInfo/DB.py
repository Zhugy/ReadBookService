#!/usr/bin/python
# -*- coding:utf-8 -*-

import redis, json

class ReadBookDB(object):

    def __init__(self):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379,decode_responses=True)
        self.rd = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


    def setData(self,bookCode,bookInfo):
        pipe = self.rd.pipeline()
        pipe.set(str(bookCode), json.dumps(bookInfo))
        # 12小时过期
        pipe.expire(str(bookCode), 60*60*12)
        pipe.execute()

    def getBookInfo(self,bookCode):
        val = self.rd.get(str(bookCode))
        if type(val) == str:
            if len(val) == 0:
                return None
            p = json.loads(val)
            return p
        return None



if __name__ == "__main__":
    rd = ReadBookDB()
    # rd.setData("119292", '898988665556')
    print(rd.getBookInfo("119292"))


    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
    # r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    # # r.set('name', 'runoob')  # 设置 name 对应的值
    # print(r.get('119292'))  # 取出键 name 对应的值
