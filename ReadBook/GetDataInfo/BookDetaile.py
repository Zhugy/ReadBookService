#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
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
        reqFile = 'http://www.shuquge.com/txt/{}/{}'.format(str(self.bookCode), str(self.chapterCode))
        reqData = requests.get(reqFile)
        reqData.encoding = reqData.apparent_encoding
        sub_soup = BeautifulSoup(reqData.text, 'lxml')
        print(sub_soup)



if __name__ == "__main__":
    book = BookDetaile("5809",'32857490.html')
    # book.requestChapter()
    book.texRequest()