# 1、匹配特定的某些数据 code
import re

s = """
    codejiaonang
    code
    codeinfo
"""
pattern = re.compile('code')
print(pattern.findall(s))

print(re.findall('code',s))

# 2、字符组（[]）：匹配一组可能出现的字符 python | Python
s2 = """
    I like Python3 and I like python2.7
    人生苦短我用Python
    python
"""

print(re.findall('[Pp]ython', s2))

# 3、匹配多个单词 Ruby、Rube、ruby、rube
s3 = """
Ruby、Rube、ruby、rube
"""
print(re.findall('[Rr]ub[ey]', s3))


# 4、区间 连字符(-)代表区间；匹配数据所有的数字、小写字母和大写字母
s4 = """
    abcdefg
    012345678
    987654321
    ABCDEFG
    
    +_)*^$%
    <>?:"{}
    （）。，/
    ?><,.>()
"""
print(re.findall('[0-9|a-z|A-Z]', s4))

# 5、匹配特殊字符；对特殊符号进行转义 \;常见的特殊字符如下： * + ? ^ $ [] () {} | \
s5 = """
    []
    -----
    --
    ()
    
    123456789
    Abcdefg
    code123
    0codejn
"""
print(re.findall('[(\[\])|(\-)|(\(\))]+', s5))
print(re.findall('[\[\]|\-|\(\)]+', s5))

# 6、匹配字母，[]字符组可以放多个条件
s6 = """
    a
    b
    y
    z
    B
    A
    F
    
    0
    01
    012
    []()\
    Q0123456789---
    0123456789
    .-/*130.
"""

print(re.findall('[a-z|A-F]', s6))

# 7、取反，匹配不包含数字的字符组；通过字符组开头使用[^]字符实现取反操作
s7 = """
    爱吗
    爱哦
    爱我自己
    爱了
    我爱我
    
    我爱你
    爱你
    爱你爱你
    不爱你
    爱你一万年
"""
print(re.findall('[我]*[爱][^你].*', s7))

# 匹配不包含小写字母的数据
s7_1 = """
    01234
    1234567890
    ABCDEFG
    CODEJIAONANG123
    []
    +_)(91283)
    -*/124566ABV
    
    ab
    abc
    abcd
    www
    codejiaonang
    com
    pythonregext

"""
print(re.findall('[(\S)*,^(a-z)].+', s7_1))

# 8、快捷匹配数字和字母
s8 = """
    master
    code
    jiaonang
    123456789
    987654321
    0123
    CODE
    JIAONANG
    hello world
    python
    
    //\
    =-
    /*-
    `
    !!!
    $#$%
    /*-+
    <>()
    {}
    ||
"""
print(re.findall('[\w].+', s8))

# 9、匹配空白分隔的单词
s9 = """
    code
    code jiaonang
    code jiaonang
    code www
    code jiaonang
    
    CODEINFO
    codeasd/
    codejiaonangA$
    JIAONANG-MASTER
    CO DEJIAONANG! 

"""
print(re.findall('code\s[\w]*', s9))

# 10、单词边界
s10 = """
    code
    code jiaonang
    code.jiaonang
    www.code
    code-jiaonang
    
    CODEINFO
    codeasd/
    codejiaonangA$
    JIAONANG-MASTER
    CODEJIAONANG!
"""
print(re.findall('.*\bcode\b.*', s10))

























