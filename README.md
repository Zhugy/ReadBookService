# ReadBookService
使用Python 爬取 书趣阁 的信息，通过自己搭建的 服务器 把数据以 json 的形式 返回

```
@app.route('/', methods=['GET'])
def hello():
    return {"data":"hello word"}

# 热门排行
@app.route('/readbook/hot',methods=['GET'])
def hot():
    return loadHotList()

# 小说 基本信息
@app.route('/readbook/bookintroduce/<int:bookCode>', methods=["GET"])
def bookintroduce(bookCode):
    return getBookHomeInfo(bookCode)

# 章节信息
@app.route('/readbook/bookDetaile/<int:bookCode>/<int:textCode>', methods=["GET"])
def bookDetaile(bookCode, textCode):
    bookDet = BookDetaile(bookCode, textCode)
    return bookDet.requestChapter()

# 搜索
@app.route('/readbook/searchbook/<string:bookName>', methods=["GET"])
def searchBook(bookName):
    search = BookSearch()
    return search.search(bookName)
        
        ```
