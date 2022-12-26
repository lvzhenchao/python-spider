# 爬虫程序分三个部分

# 1、拼接url地址
# 2、发送请求
# 3、保存

# 所需模块
from urllib import request
from urllib import parse

# 1、拼接url地址
url = 'http://www.baidu.com/s?wd={}'
word = input("请输入搜索内容")
params = parse.quote(word) #quote()只能对字符串进行编码
full_url = url.format(params)# 格式化字符串；使用format函数格式化字符串，拼接url地址；有三种url拼接方法 http://c.biancheng.net/python_spider/url-coding.html
print(params)
print(full_url)

# 2、发送请求
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}# 重构请求头
req = request.Request(url = full_url, headers = headers) #2-1创建请求对应-Request
res = request.urlopen(req) #2-2获取响应对象-urlopen
html = res.read().decode("utf-8") #2-3获取响应内容-read

# 3、保存为本地文件
filename = word + '.html'
with open(filename,'w', encoding='utf-8') as f:
    f.write(html)

