
# Beautiful Soup简称BS4[4是版本号]，是一个Python第三方库。可以从HTML和XML文档快速地提取指定的数据；
# 优势：简单、使用方便，并且容易理解

html_doc = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>

"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser') #html.parser 表示解析文档时所用的解析器；此处的解析器也可以是 'lxml' 或者 'html5lib'
# soup = BeautifulSoup(open('html_doc.html', encoding='utf8'), 'lxml')

#prettify()用于格式化输出html/xml文档
print(soup.prettify())

# BS4常用语法
## bs4将HTML文档转换成一个树形结构，该结构有利于快速地遍历和搜索HTML文档






















