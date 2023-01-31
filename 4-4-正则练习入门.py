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