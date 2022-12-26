import demo

print(demo.name, demo.add)
demo.say()
clangs = demo.CLanguage("C语言中文网","http://c.biancheng.net")
clangs.say()

print(dir(demo))# 通过 dir() 函数，我们可以查看某指定模块包含的全部成员（包括变量、函数和类）