
# JSON是一种轻量级的数据交换格式，易于阅读和编写，同时也易于机器解析和生成，能够有效提升信息的传输效率

# json.loads() 可以将json格式的字符串转换成python对象；（比如列表、字典、元组、整型以及浮点型），其中最常用的是转换为字典类型

import json

#JOSN字符串
website_info='{"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}'

# 1、将字符串转换为Python对象
py_dict = json.loads(website_info)
print("python字典数据格式：%s；数据类型：%s"% (py_dict,type(py_dict)))
## json字符串看上去和python字典非常相似，但是本质不同；JSON是字符串类型，而Python字典是dict类型

# 2、将python对象转换为json字符串，并将转换后的数据写入到json格式文件中，因此该方法必须操作文件流对象
## json.dump(object,f,inden=0，ensure_ascii=False)
## 参数说明如下：
## object：Python 数据对象，比如字典，列表等
## f：文件流对象，即文件句柄。
## indent：格式化存储数据，使 JSON 字符串更易阅读。
## ensure_ascii：是否使用 ascii 编码，当数据中出现中文的时候，需要将其设置为 False。
ditc_info = {"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}
with open("web.json", "a") as f:
    json.dump(ditc_info, f, ensure_ascii=False)