
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
soup1 = BeautifulSoup(html_doc, 'html.parser') #html.parser 表示解析文档时所用的解析器；此处的解析器也可以是 'lxml' 或者 'html5lib'
# soup = BeautifulSoup(open('html_doc.html', encoding='utf8'), 'lxml')

#prettify()用于格式化输出html/xml文档
# print(soup1.prettify())

# BS4常用语法
## bs4将HTML文档转换成一个树形结构，该结构有利于快速地遍历和搜索HTML文档

# 1、Tag节点
soup2 = BeautifulSoup('<p class="Web site url"><b>c.biancheng.net</b></p>', 'html.parser')
#获取整个p标签的html代码
print(soup2.p)
#获取b标签
print(soup2.p.b)
#获取p标签内容，使用NavigableString类中的string、text、get_text()
print(soup2.p.text)
#返回一个字典，里面是多有属性和值
print(soup2.p.attrs)
#查看返回的数据类型
print(type(soup2.p))
#根据属性，获取标签的属性值，返回值为列表
print(soup2.p['class'])
#给class属性赋值,此时属性值由列表转换为字符串
soup2.p['class']=['Web','Site']
print(soup2.p)

# 2、遍历节点

# 3、find_all()与find()是解析HTML文档的常用方法，可以在HTML文档中按照一定的条件（相当于过滤器）查找所需内容
## find_all();  find_all( name , attrs , recursive , text , limit )
### 简化代码：soup.find_all("a") == soup("a")
html_doc3 = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站</p>
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
<a href="http://c.biancheng.net/django/" id="link3">django教程</a>
<p class="vip">加入我们阅读所有教程</p>
<a href="http://vip.biancheng.net/?from=index" id="link4">成为vip</a>
"""
#创建soup解析对象
soup3 = BeautifulSoup(html_doc3, 'html.parser')
#查找所有a标签并返回
print(soup3.find_all("a"))
#查找前两条a标签并返回
print(soup3.find_all("a",limit=2))
#只返回两条a标签

## find()方法类似，但是仅返回一个符合条件的结果，所以方法没有limit参数

# 4、CSS选择器：BS4支持大部分的 CSS 选择器，比如常见的标签选择器、类选择器、id 选择器，以及层级选择器
## select() 方法，通过向该方法中添加选择器
html_doc4 = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站</p>
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
<a href="http://c.biancheng.net/django/" id="link3">django教程</a>
<p class="vip">加入我们阅读所有教程</p>
<a href="http://vip.biancheng.net/?from=index" id="link4">成为vip</a>
<p class="introduce">介绍:
<a href="http://c.biancheng.net/view/8066.html" id="link5">关于网站</a>
<a href="http://c.biancheng.net/view/8092.html" id="link6">关于站长</a>
</p>
"""
soup = BeautifulSoup(html_doc4, 'html.parser')
print("-----------------")
#根据元素标签查找
print(soup.select('title'))
#根据属性选择器查找
print(soup.select('a[href]'))
#根据类查找
print(soup.select('.vip'))
#后代节点查找
print(soup.select('html head title'))
#查找兄弟节点
print(soup.select('p + a'))
#根据id选择p标签的兄弟节点
print(soup.select('p ~ #link3'))
#nth-of-type(n)选择器，用于匹配同类型中的第n个同级兄弟元素
print(soup.select('p ~ a:nth-of-type(1)'))
#查找子节点
print(soup.select('p > a'))
print(soup.select('.introduce > #link5'))




















