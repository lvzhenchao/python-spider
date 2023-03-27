# 对Xpath表达式提供了良好的支持，因此能够高效地解析HTML/XML文档

# lxml提供了etree模块，该模块准men用来解析HTML/XML 文档

#1、导入模块
from lxml import etree

#2、创建解析对象
html_str = '''
<div>
    <ul>
         <li class="item1"><a href="link1.html">Python</a></li>
         <li class="item2"><a href="link2.html">Java</a></li>
         <li class="site1"><a href="c.biancheng.net">C语言中文网</a>
         <li class="site2"><a href="www.baidu.com">百度</a></li>
         <li class="site3"><a href="www.jd.com">京东</a></li>
    </ul>
</div>
'''
parse_html = etree.HTML(html_str)#html()方法会转换为符合规范的HTML文档格式
# tostring()将标签元素转换为字符串输出，注意：result为字节类型
# result = etree.tostring(parse_html)
# print(result)
# print(result.decode('utf-8'))

#3、 调用xpath表达式
##获取a标签的文本信息
r_list = parse_html.xpath('//a/text()')
print(r_list)
##获取所有href的属性值
r_list1 = parse_html.xpath('//a/@href')
print(r_list1)
