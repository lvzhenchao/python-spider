# 分组机制；实现分组很简单，使用（）即可
# 分组非常重要的功能：捕获数据[捕获分组]；当从匹配好的数据中，提取【关键数据】的时候可以使用分组
# 示例：
import re

s = """
    张三：0731-8825951
"""
print(re.findall('(\d{4})-(\d{7})', s))#(\d{4}) 和 (\d{7})就分别捕获了两段数据：0731、8825951

ss = """
    <div>hi</div>
"""
print(re.findall('<div>.*?</div>', ss))   #['<div>hi</div>']
print(re.findall('<div>(.*?)</div>', ss)) #['hi']

#1、提取学号
s1 = """
    需要匹配的
    2019-5013-08
    2020 5013 08
    2021501308
    
"""
# 需要提取的
# 2019 5013 08
# 2020 5013 08
# 2021 5013 08

print(re.findall('(\d{4})[\s-]?(\d{4})[\s-]?(\d{2})', s1))

#2、提取年月日
s2 = """
    需要匹配的
    2020-1-2
    2020-2-2
    2020-01-02
    2020/01/20
"""
# 需要提取的
# 2020 1 2
# 2020 2 2
# 2020 01 02
# 2020 01 20
print(re.findall('(\d{4})[-\/]?(\d{1,2})[-\/]?(\d{1,2})', s2))

#3、或者条件 or；加上 |符号；提取所有视频文件
s3 = """
    需要匹配的
    1.avi
    abc.mp4
    chapter1.wmv
    chapter2.rmvb
"""
# 需要提取的
# .avi
# .mp4
# .wmv
# .rmvb
print(re.findall('(.avi|.mp4|.wmv|.rmvb)', s3))

#4、非捕获分组：不会把匹配到的内容保存到分组里面，就是不需要分组里面的数据
## https://www.cnblogs.com/piperck/p/15878834.html
## 有时候，并不需要捕获某个分组的内容，但是又想使用分组的特性；
## 可以使用非捕获组(?:表达式)，从而不捕获数据，还能使用分组的功能
s4 = """
    需要匹配的
    01-75855
    0731-75855
    12345-75855
    tel:75855
"""
# 需要提取的
# 75855
# 75855
# 75855
# 75855
print(re.findall('(?:\w+)[\-:](\d+)', s4))

#4-1提取所有电话号码
s4_1 = """
    需要匹配的
    2118673676
    (211)8673676
    211.867.3676
    (211)867-3676
    211-867-3676
"""
# 需要提取的
# 211 867 3676
# 211 867 3676
# 211 867 3676
# 211 867 3676
# 211 867 3676
print(re.findall('\(?(\d{3})\)?[-.]?(\d{3})[.-]?(\d{4})', s4_1))

# 分组回溯引用：引用之前匹配分组的机制，子匹配，该匹配接下来会再次出现；使用\N可以引用编号为N的分组
#5、回溯引用：匹配单词(匹配符合 ab ba 这种关系)
s_5 = """
    需要匹配的
    abccba
    allagmatic
    otto
    abba
    asffs
    maam
    warrandice
"""
print(re.findall('.*(\w)(\w)\2\1.*', s_5))## 没出来结果

#5-1、回溯引用实践
s_5_1 = """
    需要匹配的
    mama
    baba
    froufrou
    barbar
    haha
    hehe
    ohhohh
"""
print(re.findall('(\w).*(\w).*\1\2.*', s_5_1))

# 6 先行断言：环视，也叫预搜索

# 6-1 正向先行断言：(?=表达式)指在某个位置向右看，所在位置右侧必须匹配【表达式】；密码强度验证：至少一个大写字母、至少一个小写字母、至少一个数字、至少8个字符
s_6 = """
需要匹配的
Admin123456
pZUJLUpTL2
Tnut2eWPN1
wJxpVhVYi3
UySRo49ps
Ig7AHzZ0J
oYHMDdHCK9
yiyWKQnWo2
gTZEEkVrj1
8Ij12340as
wdfqe#wefDdf444
Codejiaonang123
CodeJiaonang@qq1
111111abc11ABc
CodeJiaonang123

不能匹配的
qwe
8848
123456
asd123
Adm123
Asd123
wjleif932
admin123
123admin
123asd123
ADMIN123()
编号89757
888888888info
masterxiao123
888888888A
"""
print(re.findall('(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d).{8,}', s_6))

# 6-2 反向先行断言：(?!表达式)的作用是保证右边不能出现某字符
s_6_2 = """
需要匹配的
abc@sina.com
qq@163.com
a@google.com
qq@123.com

不能匹配的
test@qq.com
qq@qq.com
gc@qq.com
163@qq.com
"""
print(re.findall('.*@(?!qq)\w*\.com', s_6_2))





















