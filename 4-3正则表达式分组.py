import re

# 正则表达式：能够将子表达式做成子集，使用（）进行分组，方便对字符串进行划分

## 使用场景：
### 1、对子表达式进行重复(对多个字符进行重复的话)
###：(ab){3} 表示 ab 字符重复3次

### 2、获取到子表达式匹配到的内容

## 分组的使用方法：正则中通过小括号“()”来指定需要重复的子表达式，然后再加上限定符对这个子表达式进行重复
###：例如：(abc)? 表示0个或1个abc；一组括号里面的表达式就表示一个分组

### 捕获组：捕获组和非捕获组
### 区别：捕获组表示的分组会捕获文本（即:匹配字符），而非捕获组表示的分组不会捕获文本
#### 捕获组可以通过从左到右计算其开括号来编号

### 表达式 (A)(B(C))
# 分组编号	分组编号对应的子表达式
# 0	        (A)(B(C))
# 1	        (A)
# 2	        (B(C))
# 3	        (C)

## 补充
### 如果想匹配3个数字：\d{3}
### 重复多个字符：(ab){3},3次ab

# 正则表达式分组示例 : 正则表达式分组可以从匹配的信息中提取出想要的信息
# 当需要哪个特定信息的时候，就可以通过分组（也就是加括号）的方式获得
website="编程帮 www.biancheng.net"

# 提取所有信息， 转义"."
pattern_1 = re.compile('\w+\s+\w+\.\w+\.\w+')
print(pattern_1.findall(website))

# 提取匹配信息的第一项
pattern_2 = re.compile('(\w+)\s+\w+\.\w+\.\w+')
print(pattern_2.findall(website))

#有两个及以上的()则以元组形式显示
pattern_3 = re.compile('(\w+)\s+(\w+\.\w+\.\w+)')
print(pattern_3.findall(website))

# ['编程帮 www.biancheng.net']
# ['编程帮']
# [('编程帮', 'www.biancheng.net')]

# 网页信息提取：取出两部影片的名称和主演信息
html="""
    <div class="movie-item-info">
        <p class="name">
        <a title="你好，李焕英">你好，李焕英</a>
        </p>
        <p class="star">
        主演：贾玲,张小斐,沈腾
        </p>    
    </div>
    <div class="movie-item-info">
        <p class="name">
        <a title="刺杀，小说家">刺杀，小说家</a>
        </p>
        <p class="star">
        主演：雷佳音,杨幂,董子健,于和伟
        </p>    
    </div> 
"""
pattern = re.compile(r'<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>', re.S)
r_list  = pattern.findall(html)
print(r_list)

if r_list:
    for r_info in r_list:
        print("影片名称：", r_info[0])
        print("影片主演：", r_info[1].strip())
        print(20*"*")



















