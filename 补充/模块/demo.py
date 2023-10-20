
# 变量（name 和 add）
name = "Python教程"
add = "http://c.biancheng.net/python"


# 函数（ say() ）
def say():
    print("人生苦短，我学Python！")

# 一个 Clanguage 类
class CLanguage:
    def __init__(self,name,add):
        self.name = name
        self.add = add
    def say(self):
        print(self.name,self.add)

# say()
# clangs = CLanguage("C语言中文网","http://c.biancheng.net")
# clangs.say()

# 当【直接运行一个模块时】，name 变量的值为 __main__；
# 而将模块被导入其他程序中并运行该程序时，处于模块中的 __name__ 变量的值就变成了模块名

print("注意看我的名字是啥："+__name__)


if __name__ == '__main__': # if __name__ == '__main__': 的作用是确保只有单独运行该模块时，此表达式才成立
    print(name, add)
    say()
    clangs = CLanguage("C语言中文网","http://c.biancheng.net")
    clangs.say()