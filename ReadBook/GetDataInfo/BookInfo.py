#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests, os, re
from bs4 import BeautifulSoup


def getBookHomeInfo(bookCode):
    # 网络请求

    bookFile = 'http://www.shuquge.com/txt/{}/index.html'.format(str(bookCode))
    req = requests.get("http://www.shuquge.com/txt/5809/index.html")
    req.encoding = 'utf-8'
    chart_soup = BeautifulSoup(req.text, 'lxml')
    # 加载本地数据
    # # localFile = '/Users/zhugy781/zhugyProject/PythonProject/ReadBookService/ReadBook/localHtml/bookHome.html'
    # #
    # localFile = "/Users/zhugy781/zhugyProject/ReadBookService/ReadBook/localHtml/bookHome.html"
    # with open(localFile, 'r', encoding="utf-8") as f:
    #     chart_soup = BeautifulSoup(f.read(), 'lxml')

    jsonData = {}

    # 解析小说基本信息
    div = chart_soup.find_all('div', class_='info')[0]
    bookInfo = analysisBookHead(jsonData, div)

    # 解析小说 章节
    catalogMap = chart_soup.find_all('div', class_='listmain')[0]
    listMain = analysisCatalog(jsonData, catalogMap)

    jsonData['data'] = {'bookInfo': bookInfo, "listmain": listMain}


    return jsonData



# 解析头部信息
"""
    :param jsonData: 返回的整个数据
    :param div :解析书本头部信息

"""


def analysisBookHead(jsonData, div):
    bookInfo = {}

    # 查找封面图
    cover = div.find('img')
    bookInfo["bookFileName"] = cover['alt']
    bookInfo['cover'] = {"bookCover": cover['src']}

    # 查找 small
    smallInfo = div.find('div', class_='small')
    smallSpanArr = smallInfo.find_all('span')
    smallDict = {}
    for index in range(0, len(smallSpanArr)):
        if index == 0:
            smallDict['author'] = smallSpanArr[index].get_text()
        elif index == 1:
            smallDict['type'] = smallSpanArr[index].get_text()
        elif index == 2:
            smallDict['mark'] = smallSpanArr[index].get_text()
        elif index == 3:
            smallDict['size'] = smallSpanArr[index].get_text()
        elif index == 4:
            smallDict['lastUpdateDate'] = smallSpanArr[index].get_text()
        elif index == 5:
            smallDict['lastUpdateInfo'] = {
                "title": smallSpanArr[index].get_text(),
                "defaultName": smallSpanArr[index].contents[0],
                "key": smallSpanArr[index].contents[1]['href']
            }
    bookInfo['small'] = smallDict

    # 查找intro
    introInfo = div.find('div', class_='intro')
    introDict = {}
    introDict['headName'] = introInfo.get_text()
    # TODO:  暂未找到取值的最优解决方案
    """
        <div class="intro">
            <span>
                简介：
            </span>
            吾有一口玄黄气，可吞天地日月星。天蚕土豆最新鼎力大作，2017年度必看玄幻小说。
            <br/>
                作者：天蚕土豆所写的《元尊》无弹窗免费全文阅读为转载作品,章节由网友发布。
            <br/>
            推荐地址：http://www.shuquge.com/txt/5809/index.html
        </div>
    """
    # htmlStr = str(introInfo)
    # print('如下html 还没有解析--------->\n😢😢😢😢😢😢\n{} \n😢😢😢😢😢😢😢😢'.format(str(htmlStr)))
    bookInfo['intro'] = introDict

    # link 数据解析
    linkMap = div.find('div', class_='link')
    linkDict = {}
    linkDict['linkName'] = linkMap.find('span').contents[0]
    linkSubArr = []
    for href in linkMap.find_all('a'):
        linkSubArr.append({"name": href.get_text(), "key": href['href']})
    linkDict['linkArr'] = linkSubArr
    bookInfo['link'] = linkDict

    return bookInfo


# 解析章节
def analysisCatalog(jsonData, divMap):
    listMain = []
    itemDict = {}
    itemList = []

    for div in divMap.find('dl').contents:
        # 过滤空值
        if div.name == None:
            continue
        # 段落的分割
        if div.name == 'dt':
            # 已经存过数值
            if len(itemDict.values()) > 0:
                itemDict['list'] = itemList
                listMain.append(itemDict.copy())
                # 清空数据
                itemList = []
                itemDict = {}

            itemDict['name'] = div.string
            continue
        # 每一章节
        if div.name == 'dd':
            aTag = div.find('a')
            itemList.append({"title": aTag.string, "keyValue":aTag['href']})

    # 结束的时候重新赋值
    if len(itemDict.values()) > 0:
        itemDict['list'] = itemList
        listMain.append(itemDict.copy())

    return listMain



if __name__ == "__main__":
    getBookHomeInfo(5809)
