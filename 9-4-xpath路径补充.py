## 很多个相同下面的div：
# <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
#     <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
#     <span>by <small class="author" itemprop="author">Albert Einstein</small>
#     <a href="/author/Albert-Einstein">(about)</a>
#     </span>
#     <div class="tags">
#         Tags:
#         <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /    >
#         <a class="tag" href="/tag/change/page/1/">change</a>
#         <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
#         <a class="tag" href="/tag/thinking/page/1/">thinking</a>
#         <a class="tag" href="/tag/world/page/1/">world</a>
#     </div>
# </div>

html = """
<div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
    <span class="text" itemprop="text">“The first world.”</span>
    <span>
        by 
        <small class="author" itemprop="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /    >
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>
<div class="quote" itemscope itemtype="http://schema.org">
    <span class="text" itemprop="text">“The second world.”</span>
    <span>
        by 
        <small class="author" itemprop="author">Einstein</small>
        <a href="/author/Albert-Einstein">(about1)</a>
    </span>
    <div class="tags">
        Tags:
        <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /    >
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>
"""
from lxml import etree

response = etree.HTML(html)

quotes_lists = response.xpath('//div[@class = "quote"]')

print(quotes_lists)
# [<Element div at 0x1e6efeda200>, <Element div at 0x1e6efeda100>]

quote_0_0 = quotes_lists[0].xpath('//span[1]/text()') # 会把所有标签的文本给提取出来，并不是想要的第一个标签下面额某个文本
# print(quote_0_0)
# ['“The first world.”', '“The second world.”']

quote_0_1 = quotes_lists[0].xpath('./span[1]/text()')
# print(quote_0_1)
# ['“The first world.”']

quote_0_2 = quotes_lists[0].xpath('.//span[1]/text()')
# print(quote_0_2)
# ['“The first world.”']

for p in quotes_lists:
    print(p.xpath('./span[1]/text()'))
    print(p.xpath('.//span[1]/text()'))
































