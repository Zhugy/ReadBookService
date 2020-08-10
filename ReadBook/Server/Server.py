#!/usr/bin/python
# -*- coding:utf-8 -*-

from GetDataInfo.Home import loadHotList
from GetDataInfo.BookInfo import getBookHomeInfo

from flask import Flask, request

app = Flask(__name__)

@app.route('/readbook/hot',methods=['GET'])
def hot():
    return loadHotList()

@app.route('/readbook/bookintroduce/<int:bookCode>', methods=["GET"])
def bookintroduce(bookCode):
    return getBookHomeInfo(bookCode)


if __name__ == '__main__':
    app.run(host='10.24.48.100',port=9266, debug=True)
