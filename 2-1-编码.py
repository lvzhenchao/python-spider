import urllib.parse

# 当URL路径或者查询参数中，带有中文或者特殊字符的时候，就需要对URL进行编码（采用十六进制编码格式）
# URL编码的原则是使用安全字符去表示那些不安全的字符

# 1、URL组成：协议、域名、端口号、路径、查询参数等
url = "http://www.biancheng.net/index?param=10"

# 2、哪些参数需要编码
## 只允许使用ASCll字符集可以显示的字符

# 3、python实现编码和解码

## 解码：urllib.parse模块；分别是urlencode：编码 unquote：解码
### urlencode()和quote()：实现了对url地址的编码操作

word = input('请输入要搜索的内容：')

quote_encode = urllib.parse.quote(word) # quote() 只能对字符串编码

urlencode_encode = urllib.parse.urlencode({
    'wd': word
}) # urlencode() 可以直接对查询字符串字典进行编码

## 3-1 url地址拼接方式
### 1、字符串相加
baseurl1 = 'http://www.baidu.com/s?'
params1  ='wd=' + urllib.parse.quote(word)
url1     = baseurl1 + params1
print(url1)

### 2、字符串格式化
params2  ='wd=' + urllib.parse.quote(word)
url2 = 'http://www.baidu.com/s?%s'% params2
print(url2)

### 3、format()方法：常用
params3 ='wd=' + urllib.parse.quote(word)
url3    = 'http://www.baidu.com/s?{}'
url3 = url3.format(params3)
print(url3)