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


















