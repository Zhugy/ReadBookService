#!/usr/bin/python
# -*- coding:utf-8 -*-

import redis, json

class ReadBookDB(object):

    def __init__(self):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379,decode_responses=True)
        self.rd = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


    def setData(self,bookCode,bookInfo):
        pipe = self.rd.pipeline()
        pipe.set(str(bookCode), str(bookInfo))
        pipe.execute()

    def getBookInfo(self,bookCode):
        str = self.rd.get(bookCode)
        jsonStr = json.loads(str,encoding='utf-8')
        return jsonStr


if __name__ == "__main__":
    # rd = ReadBookDB()
    # rd.setData("pp", '898988665556')
    # print(rd.getBookInfo('pp'))

    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
    # r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    # # r.set('name', 'runoob')  # 设置 name 对应的值
    # print(r.get('p'))  # 取出键 name 对应的值
