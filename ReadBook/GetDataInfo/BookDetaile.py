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
        url = 'http://www.shuquge.com/txt/{}/{}'.format(str(self.bookCode),str(self.chapterCode))
        print(url)
        print('http://www.shuquge.com/txt/5809/32857490.html')
        req = requests.get('http://www.shuquge.com/txt/514/31010531.html')
        req.encoding = 'utf-8'
        etree_html = etree.HTML(req.text)
        # 提取标题
        title = etree_html.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')
        print(title)
        # 提取内容
        content = etree_html.xpath('//*[@id="content"]//text()')  # 现在还是数组形式，文本，字符串
        text = "".join(content)  # \r和\n换行
        print(text)


        # chart_soup = BeautifulSoup(req.text, 'lxml')
        # print(chart_soup.find_all('div',class_='showtxt'))

    def download_text(self,url):
        # 导入包
        reponse = requests.get(url)
        # 解码
        reponse.encoding = reponse.apparent_encoding
        print(reponse.text)
        # 解析
        etree_html = etree.HTML(reponse.text)
        # 提取标题
        title = etree_html.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')
        print(title)
        # 提取内容
        content = etree_html.xpath('//*[@id="content"]//text()')  # 现在还是数组形式，文本，字符串
        text = "".join(content)  # \r和\n换行

        print(text)

        # 保存到txt文件，放到电脑桌面，绝对路径,r表示原意，\代表转义字符
        # with open(filePath + title[0] + '.txt', 'a', encoding='utf-8') as file:  # 创建并打开一个文件
        #     file.write(text)  # 放进去内容，写入
        #     file.close()  # 关闭


if __name__ == "__main__":
    book = BookDetaile("5809",'32857490.html')
    # book.requestChapter()
    book.download_text('http://www.shuquge.com/txt/514/31010531.html')