
# 使用 Python 爬虫抓取猫眼电影网 TOP100 排行榜（https://maoyan.com/board/4）影片信息，包括电影名称、上映时间、主演信息

from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list

# 定义一个爬虫类
class MaoyanSpider(object):
    # 初始化
    # 定义初始化页面url
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"

    # 请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url = url, headers = headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)