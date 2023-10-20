
#1、request库定义了7个常用的请求方法；
#requests.get() 与 requests.post() 方法最为常用；
#requests.request()构造一个请求对象，该方法是实现以下各个方法的基础；看参数列表

#2、SSL认证-verify参数；SSL证书是数字证书的一种；具有服务器身份验证和数据传输加密功能；
#verify参数的作用是检查 SSL 证书认证，参数的默认值为 True，如果设置为 False 则表示不检查 SSL证书

#3、代理IP-proxies参数；
# import requests
# url = 'http://httpbin.org/get'
# headers = {
#     'User-Agent':'Mozilla/5.0'
# }
# # 网上找的免费代理ip
# proxies = {
#     'http':'http://58.17.78.91:8085',
#     'https':'https://191.231.62.142:8000'
# }
# html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
# print(html)

# 4、用户认证-auth参数；
#持用户认证功能，也就是适合那些需要验证用户名、密码的网站，参数形式是一个元组
import requests
class xxxSpider(object):
  def __init__(self):
    self.url = 'http://code.tarena.com.cn/AIDCode/aid1906/13Redis/'
    # 网站使用的用户名，密码
    self.auth = ('c语言中文网','c.biancheng.net')

  def get_headers(self):
      headers = {'User-Agent':"Mozilla/5.0"}
      return headers

  def get_html(self,url):
      res = requests.get(url,headers=self.get_headers(),auth=self.auth)
      html = res.content
      print(html)
      return html

  def run(self):
      self.get_html(self.url)
if __name__ == '__main__':
    spider = xxxSpider()
    spider.run()