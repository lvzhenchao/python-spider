
# User-Agent 用户代理 网站服务器通过识别 “UA”来确定用户所使用的操作系统版本、CPU 类型、浏览器版本等信息

# #导入模块
# import urllib.request
# #向网站发送get请求
# response=urllib.request.urlopen('http://httpbin.org/get')
# html = response.read().decode()
# print(html)

# from urllib import request
# # 定义变量：URL 与 headers
# url = 'http://httpbin.org/get' #向测试网站发送请求
# #重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
# headers = {
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# # 1、创建请求对象，包装ua信息
# req = request.Request(url=url,headers=headers)
# # 2、发送请求，获取响应对象
# res = request.urlopen(req)
# # 3、提取响应内容
# html = res.read().decode('utf-8')
# print(html)

# 自建代理池，就是把多个浏览器的UA信息放进列表中，再随机选择
ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]

from urllib import parse
#构建查询字符串字典
query_string = {
'wd' : '爬虫'
}
#调用parse模块的urlencode()进行编码
result = parse.urlencode(query_string)

print(result)

#使用format函数格式化字符串，拼接url地址
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)

#quote()只能对字符串进行编码
# print(url.format(parse.quote("美女")))

# urllib.parse.urlencode({'key':'value'}) #字典
# urllib.parse.quote(string) #字符串

# 解码unquote(string)
string = '%E7%88%AC%E8%99%AB'
result = parse.unquote(string)
print(result)