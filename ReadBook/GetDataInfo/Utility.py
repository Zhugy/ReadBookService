#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from fake_useragent import UserAgent

# 获取资源文件 目录
def localHtmlPath(fileName):
    file = os.path.dirname(os.getcwd()) + '/localHtml'
    if len(fileName) == 0:
        return file
    return file + '/{}'.format(str(fileName))

# UserAgent
def user_egentDict():
    useragentPath = os.path.dirname(os.getcwd()) + '/UserAgent/fake_useragent.json'
    ua = UserAgent(path=useragentPath)
    headers = {'User-Agent': ua.random}
    return headers













if __name__ == "__main__":
    f = localHtmlPath('detail.htm')
    print(f)