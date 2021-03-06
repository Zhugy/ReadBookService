#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests, os, re
from bs4 import BeautifulSoup
from GetDataInfo.Utility import localHtmlPath
from GetDataInfo.Utility import AllData

def loadHotList():
    if AllData().isLoadLocalData():# 加载本地数据
        fileName = localHtmlPath('hotlist.html')
        with open(fileName, 'r', encoding='utf-8') as f:
            chart_soup = BeautifulSoup(f.read(), 'lxml')
    else:
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
            bookCode = subHt.find('a')['href'].split('/')[-2]
            disDir["bookCode"] = bookCode
            content.append(disDir)

        subDic["content"] = content
        countArr.append(subDic)
        # print('---------------\n\n\n----------------------')

    jsonData["data"] = {"hotArr": countArr}

    return jsonData

if __name__ == "__main__":
    print('书趣阁 首页')
    loadHotList()