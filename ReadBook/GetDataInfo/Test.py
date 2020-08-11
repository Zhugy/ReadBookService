#!/usr/bin/python
# -*- coding:utf-8 -*-

# 导入包
import requests

url = "http://www.shuquge.com/txt/514/363448.html"
reponse = requests.get(url)
# 解码
reponse.encoding = reponse.apparent_encoding
reponse.text

# 提取信息
from lxml import etree

# 解析
etree_html = etree.HTML(reponse.text)
# 提取标题
title = etree_html.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')
print(title)
# 提取内容
content = etree_html.xpath('//*[@id="content"]//text()')  # 现在还是数组形式，文本，字符串
text = "".join(content)  # \r和\n换行

# 保存到txt文件

with open('./第一章 若得来生重倚剑，屠尽奸邪笑苍天.txt', 'a', encoding='utf-8') as file:  # 创建并打开一个文件
    file.write(text)  # 放进去内容，写入
    file.close()  # 关闭

# 导入包
import requests
# 提取信息
from lxml import etree

filePath = r"/Users/zhugy781/zhugyProject/PythonProject/ReadBookService/ReadBook/Book"


def download_text(url):
    # 导入包
    reponse = requests.get(url)
    # 解码
    reponse.encoding = reponse.apparent_encoding
    # 解析
    etree_html = etree.HTML(reponse.text)
    # 提取标题
    title = etree_html.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')
    print(title)
    # 提取内容
    content = etree_html.xpath('//*[@id="content"]//text()')  # 现在还是数组形式，文本，字符串
    text = "".join(content)  # \r和\n换行

    # 保存到txt文件，放到电脑桌面，绝对路径,r表示原意，\代表转义字符
    with open(filePath + title[0] + '.txt', 'a', encoding='utf-8') as file:  # 创建并打开一个文件
        file.write(text)  # 放进去内容，写入
        file.close()  # 关闭


# 取到所有文章的链接
def get_link(index_url):
    index_html = requests.get(index_url).text
    index_etree = etree.HTML(index_html)
    dd = index_etree.xpath('/html/body/div[5]/dl/dd')
    link_list = []  # 打包所有的练接
    for item in dd:
        href = "http://www.shuquge.com/txt/514/" + item.xpath('./a/@href')[0]
        print(href)
        link_list.append(href)
    return link_list  # 返回的东西，我要带走的


if __name__ == '__main__':
    index_url = "http://www.shuquge.com/txt/514/index.html"  # 文章首页链接
    links = get_link(index_url)
    for link in links:
        target_url = link
        print("这在爬取：", target_url)
        download_text(target_url)  # 带进去的东西

# 取到所有文章的链接
index_url = "http://www.shuquge.com/txt/514/index.html"  # 文章首页链接

index_html = requests.get(index_url)
index_etree = etree.HTML(index_html)
dd = index_etree.xpath('/html/body/div[5]/dl/dd')
link_list = []  # 打包所有的练接
for item in dd:
    href = "http://www.shuquge.com/txt/514/" + item.xpath('./a/@href')[0]
    link_list.append(href)
    print(href)

print(len(link_list))
