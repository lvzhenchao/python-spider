
from urllib import request
from urllib import parse

# 拼接url地址
def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    # 此处使用urlencode()进行编码，可对字典类型编码
    params = parse.urlencode({'wd': word})
    # 格式化
    url = url.format(params)
    return url

# 发送请求
def request_url(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    ## 请求对象 + 响应对象 + 提取内容
    req  = request.Request(url=url,headers=headers)
    res  = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件至本地
    # 使用 with as 操作已经打开的文件对象（本身就是上下文管理器），无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件
    # with 表达式[ as target]：
    #      代码块
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

# 主程序入口
if __name__ == "__main__":
    word = input("请输入搜索内容：")
    url  = get_url(word)
    filename = word + '.html'
    request_url(url, filename)