
# JSON是一种轻量级的数据交换格式，易于阅读和编写，同时也易于机器解析和生成，能够有效提升信息的传输效率

# json.loads() 可以将json格式的字符串转换成python对象；（比如列表、字典、元组、整型以及浮点型），其中最常用的是转换为字典类型

import json

#JOSN字符串
website_info='{"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}'

py_dict = json.loads(website_info)
print("python字典数据格式：%s；数据类型：%s"% (py_dict,type(py_dict)))