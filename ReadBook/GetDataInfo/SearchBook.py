#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests, os
from bs4 import BeautifulSoup
from GetDataInfo.Utility import user_egentDict

class BookSearch(object):

    def search(self,bookName):
        return self.__requestData(bookName)

    def __requestData(self, bookName):
        reqFile = 'http://www.shuquge.com/search.php'
        parmat = {"searchkey": str(bookName), "submit":""}
        reqData = requests.post(reqFile,data=parmat,headers=user_egentDict())
        reqData.encoding = 'utf-8'
        chart_soup = BeautifulSoup(reqData.text, 'lxml')

        bookBoxMap = chart_soup.find_all('div', class_ = 'bookinfo')

        searchList = []
        for book in bookBoxMap:
            bookInfo = {}
            bookInfo['bookName'] = book.a.text
            bookInfo['bookCode'] = book.a['href'].split('/').pop(-2)
            bookInfo['cat'] = book.find_all('div', class_="cat")[0].text
            bookInfo['author'] = book.find_all('div', class_="author")[0].text

            for update in book.find_all('div', class_="update"):
                updateDict = {}
                updateDict['defaultName'] = update.find('span').text
                updateDict['updateNama'] = update.a.text
                updateDict['chapterCode'] = update.a['href'].split('/').pop(-1).split('.')[0]
                bookInfo['update'] = updateDict

            searchList.append(bookInfo)

        jsonData = {}

        jsonData["data"] = {"searchList": searchList}
        return jsonData




if __name__ == "__main__":
    search = BookSearch()
    search.search('古龙')