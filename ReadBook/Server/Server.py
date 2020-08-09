#!/usr/bin/python
# -*- coding:utf-8 -*-

from Home.Home import loadHotList
from flask import Flask, request

app = Flask(__name__)

@app.route('/readbook/hot',methods=['GET'])
def hot():
    return loadHotList()


if __name__ == '__main__':
    app.run(host='192.168.0.102',port=9266, debug=True)
