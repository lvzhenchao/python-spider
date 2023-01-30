# 网页解析方法有很多，正则解析只是其中之一，常见的还有BeautifulSoup 和 lxml
import re

# re模块常用方法

## 1、regex=re.compile(pattern,flags=0) 生成正则表达式对象

## 2、re.findall(pattern,string,flags=0) 根据正则表达式匹配目标字符串内容；返回值是匹配到的内容列表

## 3、regex.findall(string,pos,endpos) 根据正则表达式对象匹配目标字符串内容

## 4、re.split(pattern,string,flags = 0) 使用正则表达式匹配内容，切割目标字符串。返回值是切割后的内容列表

## 5、re.sub(pattern,replace,string,max,flags = 0) 使用一个字符串替换正则表达式匹配到的内容。返回值是替换后的字符串

## 6、re.search(pattern,string,flags=0) 匹配目标字符串第一个符合的内容，返回值为匹配的对象

# flags功能标志位
# 缩写元字符	   说明
# A	           元字符只能匹配 ASCII码。
# I	           匹配忽略字母大小写。
# S	           使得.元字符可以匹配换行符。
# M	           使 ^ $ 可以匹配每一行的开头和结尾位置

html="""
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""

# 1、贪婪匹配，re.S可以匹配换行符
# 创建正则表达式对象
pattern = re.compile('<div><p>.*</p></div>', re.S)
# 匹配html元素，提取信息
re_list = pattern.findall(html)
print(re_list)

# 2、非贪婪模式匹配
pattern2 = re.compile('<div><p>.*?</p></div>',re.S)
re_list2 = pattern2.findall(html)
print(re_list2)

# 2-1 非贪婪模式匹配 re.findall()
re_list3 = re.findall('<div><p>.*?</p></div>', html, re.S)
print(re_list3)


# 输出结果：非贪婪模式更适合提取html信息
['<div><p>www.biancheng.net</p></div>\n<div><p>编程帮</p></div>']
['<div><p>www.biancheng.net</p></div>', '<div><p>编程帮</p></div>']