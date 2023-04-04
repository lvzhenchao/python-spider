
# JSON是一种轻量级的数据交换格式，易于阅读和编写，同时也易于机器解析和生成，能够有效提升信息的传输效率

# json.loads() 可以将json格式的字符串转换成python对象；（比如列表、字典、元组、整型以及浮点型），其中最常用的是转换为字典类型
# json.load() 该方法用于操作文件流对象，不过它与 dump() 恰好相反，它表示从json 文件中读取 JSON 字符串，并将读取内容转换为 Python 对象

# json.dump() 可以将 Python 对象（字典、列表等）转换为 json 字符串，并将转换后的数据写入到 json 格式的文件中 ，因此该方法必须操作文件流对象
# json.dumps() 方法可以将 Python 对象转换成 JSON 字符串

import json

#JOSN字符串
website_info='{"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}'

# 1、json.loads()
py_dict = json.loads(website_info)
print("python字典数据格式：%s；数据类型：%s"% (py_dict,type(py_dict)))
## json字符串看上去和python字典非常相似，但是本质不同；JSON是字符串类型，而Python字典是dict类型

# 2、json.dump()
## json.dump(object,f,inden=0，ensure_ascii=False)
## 参数说明如下：
## object：Python 数据对象，比如字典，列表等
## f：文件流对象，即文件句柄。
## indent：格式化存储数据，使 JSON 字符串更易阅读。
## ensure_ascii：是否使用 ascii 编码，当数据中出现中文的时候，需要将其设置为 False。
ditc_info = {"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}
with open("web.json", "a") as f:
    json.dump(ditc_info, f, ensure_ascii=False)


## 2-1 将列表转换成json
item_list = []
item = {'website': 'C语言中文网', 'url': "c.biancheng.net"}
for k,v in item.items():
    item_list.append(v)
with open('info_web.json', 'a') as f:
    json.dump(item_list, f, ensure_ascii=False)

# 3、json.load();
site = {'name':'c语言中文网',"url":"c.biancheng.net"}
filename = 'website.json'
with open (filename,'w') as f:
    json.dump(site,f,ensure_ascii=False)
with open (filename,'r') as f:
    print(json.load(f))


# 4、json.dumps()
items = json.dumps(item,ensure_ascii=False)
print('转换之后的数据类型为：',type(items))
print(item)





