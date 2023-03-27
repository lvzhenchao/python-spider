# coding:utf8
import requests
from lxml import etree
from ua_info import ua_list
import random

# <dl class="board-wrapper">
# 	<dd>
# 		<i class="board-index board-index-1">1</i>
# 		<a href="/films/1200486" title="我不是药神" class="image-link" data-act="boarditem-click" data-val="{movieId:1200486}">
# 		  <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default">
# 		  <img alt="我不是药神" class="board-img" src="https://p0.pipi.cn/mmdb/d2dad59253751bd236338fa5bd5a27c710413.jpg?imageView2/1/w/160/h/220">
# 		</a>
# 		<div class="board-item-main">
# 			  <div class="board-item-content">
# 				  <div class="movie-item-info">
# 					<p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
# 					<p class="star">
# 							主演：徐峥,周一围,王传君
# 					</p>
# 					<p class="releasetime">上映时间：2018-07-05</p>
# 				  </div>
# 				  <div class="movie-item-number score-num">
# 					<p class="score">
# 						<i class="integer">9.</i>
# 						<i class="fraction">6</i>
# 					</p>
# 				  </div>
# 			  </div>
# 		</div>
# 	</dd>
# 	<dd>...</dd>
# 	<dd>...</dd>
# 	<dd>...</dd>
# </dl>

# 1、确定信息元素结构:
## 所采集的信息【电影名称、主演演员、上映时间】都包含在<dd>标签中，而<dd>标签又包含在<dl>标签中，dl是父辈节点
# 2、基准表达式：针对每一个dd提取信息，比较繁琐；
## 将10个<dd>节点放入一个列表，使用for循环遍历每一个节点对象：匹配10个<dd>节点的Xpath表达式称为【基准表达式】
## xpath_bds='//dl[@class="board-wrapper"]/dd'


class MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset=50'
        self.headers={'User-Agent':random.choice(ua_list)}
    def save_html(self):
        html=requests.get(url=self.url,headers=self.headers).text
        #jiexi
        parse_html=etree.HTML(html)
        # 基准 xpath 表达式，匹配10个<dd>节点对象
        dd_list=parse_html.xpath('//dl[@class="board-wrapper"]/dd') #列表放10个dd
        print(dd_list)
        # .// 表示dd节点的所有子节点后代节点
        # 构建item空字典将提取的数据放入其中
        item={}
        for dd in dd_list:
            # 处理字典数据，注意xpath表达式匹配结果是一个列表，因此需要索引[0]提取数据
            item['name']=dd.xpath('.//p[@class="name"]/a/text()')[0].strip()
            item['star']=dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time']=dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            #输出数据
            print(item)
    def run(self):
        self.save_html()
if __name__ == '__main__':
    spider=MaoyanSpider()
    spider.run()