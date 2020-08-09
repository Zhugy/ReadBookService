#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests, os, re
from bs4 import BeautifulSoup
import lxml
from uuid import uuid1
from random import choice
import json

def loadHotList():
    req = requests.get('http://www.shuquge.com/top.html')
    chart_soup = BeautifulSoup(req.text,'lxml')
    hotList = chart_soup.body.find_all('div',class_='block bd')
    jsonData = {}
    countArr = []
    for div in hotList:
        subDic = {}
        subDic["title"] = div.find('h2').string
        content = []
        for subHt in div.find_all('li'):
            disDir = {}
            disDir["typename"] = subHt('span')[0].string
            disDir["name"] = subHt('a')[0].string
            disDir["url"] = subHt.find('a')['href']
            content.append(disDir)

        subDic["content"] = content
        countArr.append(subDic)
        # print('---------------\n\n\n----------------------')

    jsonData["data"] = {"hotArr": countArr}

    # print(json.dumps(jsonData,ensure_ascii=False))
    return jsonData

if __name__ == "__main__":
    print('书趣阁 首页')
    loadHotList()