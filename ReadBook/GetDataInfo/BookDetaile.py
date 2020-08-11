#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
from lxml import etree

class BookDetaile():
    '''
    :param bookCode: 文章Code
    :param chapterCode: 章节Code
    '''
    def __init__(self, bookCode, chapterCode):
        self.bookCode = bookCode
        self.chapterCode = chapterCode

    def requestChapter(self):
        localFile = r'/Users/zhugy781/zhugyProject/PythonProject/ReadBookService/ReadBook/localHtml/detail.htm'
        with open(localFile,'r',encoding='utf-8') as f:
            chart_soup = BeautifulSoup(f.read(), 'lxml')

        jsonData = {}
        contentDict = {}

        allDiv = chart_soup.find_all('div', class_='content')[0]
        contentStr = chart_soup.find_all('div', class_='showtxt')[0].text

        contentDict['title'] = allDiv.find('h1').string
        contentDict['txt'] = contentStr
        jsonData['data'] = contentDict
        return jsonData


    def texRequest(self):
        useragentPath = os.path.dirname(os.getcwd()) + '/UserAgent/fake_useragent.json'
        ua = UserAgent(path=useragentPath)

        heads = {'User-Agent': ua.random}
        reqFile = 'http://www.shuquge.com/txt/{}/{}'.format(str(self.bookCode), str(self.chapterCode))
        # reqData = requests.get(reqFile, headers = heads)
        reqData = requests.get(reqFile)
        reqData.encoding = 'utf-8'
        # sub_soup = BeautifulSoup(reqData.text, 'lxml')
        print(reqData.headers)
        print(reqData.text)



if __name__ == "__main__":
    book = BookDetaile("5809",'32857490.html')
    # book.requestChapter()
    book.texRequest()