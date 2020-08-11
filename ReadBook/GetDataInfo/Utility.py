#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

# 获取资源文件 目录
def localHtmlPath(fileName):
    file = os.path.dirname(os.getcwd()) + '/localHtml'
    if len(fileName) == 0:
        return file
    return file + '/{}'.format(str(fileName))















if __name__ == "__main__":
    f = localHtmlPath('detail.htm')
    print(f)