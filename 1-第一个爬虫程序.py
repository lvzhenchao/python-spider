import urllib.request
from urllib import request
# 定义变量：URL 与 headers
url = 'http://httpbin.org/get' #向测试网站发送请求
#重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# 1、创建请求对象，包装ua信息
req = request.Request(url=url,headers=headers)
# 2、发送请求，获取响应对象
res = request.urlopen(req)
# 3、提取响应内容
html = res.read().decode('utf-8')
print(html)


# 常用方法
# 1、urllib.request.Request(url,headers)
# 创建请求对象、包装请求头。重构UA

# 2、urllib.request.urlopen(url,timeout)
# 发起请求并获取响应对象：一般这样用：urllib.request.urlopen(urllib.request.Request(url,headers),timeout)

# 3、html响应对象方法
# bytes = response.read() # read()返回结果为 bytes 数据类型
# string = response.read().decode() # decode()将字节串转换为 string 类型
# url = response.geturl() # 返回响应对象的URL地址
# code = response.getcode() # 返回请求时的HTTP响应码