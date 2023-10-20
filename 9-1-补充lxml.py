# 对Xpath表达式提供了良好的支持，因此能够高效地解析HTML/XML文档

# lxml提供了etree模块，该模块准men用来解析HTML/XML 文档

from lxml import etree

html = '''
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>测试bs4</title>
    </head>
    <body>
        <div>
            <p>百里守约</p>
        </div>
        <div class="song">
            <p>李清照</p>
            <p>王安石</p>
            <p>苏轼</p>
            <p>柳宗元</p>
            <a href="http://www.song.com/" title="赵匡胤" target="_self">
                <span>this is span</span>
                宋朝是最强大的王朝，不是军队的强大，而是经济很强大，国民都很有钱
            </a>
            <a href="" class="du">总为浮云能蔽日,长安不见使人愁</a>
            <img src="http://www.baidu.com/meinv.jpg" alt=""/>
        </div>
        <div class="tang">
            <ul>
                <li><a href="http://www.baidu.com" title="qing">清明时节雨纷纷,路上行人欲断魂,借问酒家何处有,牧童遥指杏花村</a></li>
                <li><a href="http://www.163.com" title="qin">秦时明月汉时关,万里长征人未还,但使龙城飞将在,不教胡马度阴山</a></li>
                <li><a href="http://www.126.com" alt="qi">岐王宅里寻常见,崔九堂前几度闻,正是江南好风景,落花时节又逢君</a></li>
                <li><a href="http://www.sina.com" class="du">杜甫</a></li>
                <li><a href="http://www.dudu.com" class="du">杜牧</a></li>
                <li><b>杜小月</b></li>
                <li><i>度蜜月</i></li>
                <li><a href="http://www.haha.com" id="feng">凤凰台上凤凰游,凤去台空江自流,吴宫花草埋幽径,晋代衣冠成古丘</a></li>
            </ul>
        </div>
    </body>
</html>

'''

tree = etree.HTML(html)

# 1、这三种方法实现的功能是一样的
r1 = tree.xpath('/html/body/div') #直接从上往下挨着找节点
r2 = tree.xpath('/html//div') #跳跃了一个节点来找到这个div节点的对象
r3 = tree.xpath('//div') #跳跃上面所有节点来寻找div节点的对象
# print(r1)
# print(r2)
# print(r3)

# 2、属性定位：只要div里面class是song的数据
r4 = tree.xpath('//div[@class="song"]')
# print(r4)

# 3、索引定位
r5 = tree.xpath('//div[@class="song"]/p')
# print(r5)
r6 = tree.xpath('//div[@class="song"]/p[3]')#单独返回的苏轼的p标签，要注意的是这里的索引不是从0开始的，而是1
# print(r6)

# 4、取文本
r7 = tree.xpath('//div[@class="tang"]//li[5]/a/text()')
# print(r7)
r8 = tree.xpath('//li//text()')
# print(r8)

# 5、取属性
r9 = tree.xpath('//div[@class="song"]/img/@src')
print(r9)
























