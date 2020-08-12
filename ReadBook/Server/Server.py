#!/usr/bin/python
# -*- coding:utf-8 -*-

from GetDataInfo.Home import loadHotList
from GetDataInfo.BookInfo import getBookHomeInfo
from GetDataInfo.BookDetaile import BookDetaile
from GetDataInfo.SearchBook import BookSearch

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return {"data":"hello word"}

# 热门排行
@app.route('/readbook/hot',methods=['GET'])
def hot():
    return loadHotList()

# 小说 基本信息
@app.route('/readbook/bookintroduce/<int:bookCode>', methods=["GET"])
def bookintroduce(bookCode):
    return getBookHomeInfo(bookCode)

# 章节信息
@app.route('/readbook/bookDetaile/<int:bookCode>/<int:textCode>', methods=["GET"])
def bookDetaile(bookCode, textCode):
    bookDet = BookDetaile(bookCode, textCode)
    return bookDet.requestChapter()

# 搜索
@app.route('/readbook/searchbook/<string:bookName>', methods=["GET"])
def searchBook(bookName):
    search = BookSearch()
    return search.search(bookName)

if __name__ == '__main__':
    isHome = True
    if isHome != True:
        app.run(host='192.168.0.103', port=9266, debug=True)
    else:
        app.run(host='10.24.48.100', port=9266, debug=True)
