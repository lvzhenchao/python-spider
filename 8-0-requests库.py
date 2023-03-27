import requests

# 除了urllib库，还有一个很重的Requests库，“让HTTP服务于人类”
# 是第三方库

# 1、常用请求方法 requests.get(url,headers=headers,params,timeout)
data = {
    'name': '编程帮',
    'url': "www.biancheng.net"
}
url = 'http://httpbin.org/get'
res = requests.get(url,params = data)
# print(res.text)

# 2、requests.post(url,data={请求体的字典})
url = 'https://fanyi.baidu.com'
data1 = {
    'from': 'zh',
    'to': 'en',
    'query': '编程帮www.biancheng.net你好'
}
response = requests.post(url, data=data)
# print(response)
# print(response.encoding)
# response.encoding="utf-8"    #更改为utf-8编码
# print(response.status_code)  # 打印状态码
# print(response.url)          # 打印请求url
# print(response.headers)      # 打印头信息
# print(response.cookies)      # 打印cookie信息
# print(response.text)  #以字符串形式打印网页源码
# print(response.content) #以字节流形式打印

url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=38785274,1357847304&fm=26&gp=0.jpg'
#简单定义浏览器ua信息
headers = {'User-Agent':'Mozilla/4.0'}
#读取图片需要使用content属性
html = requests.get(url=url,headers=headers).content
#以二进制的方式下载图片
# with open('C:/Users/13701/Pictures/python_logo.jpg','wb') as f:
    # f.write(html)

# 3、HttpResponse响应对象
#百度翻译
url = 'https://fanyi.baidu.com'
#post请求体携带的参数，可通过开发者调试工具查看
#查看步骤：NetWork选项->Headers选项->Form Data
data = {'from': 'zh',
        'to': 'en',
        'query': '编程帮www.biancheng.net你好'
        }
response = requests.post(url, data=data)
print(response)

response1 = requests.get('http://www.baidu.com')
print(response1.encoding)
response1.encoding="utf-8"    #更改为utf-8编码
print(response1.status_code)  # 打印状态码
# print(response1.url)          # 打印请求url
print(response1.headers)      # 打印头信息
# print(response1.cookies)      # 打印cookie信息
# print(response1.text)  #以字符串形式打印网页源码
# print(response1.content) #以字节流形式打印