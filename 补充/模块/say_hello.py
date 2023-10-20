import hello

hello.say()# 使用的语法格式为“模块名.函数”

# say.py文件使用了原本在hello.py文件中才有的say()函数；相对于say.py来说，hello.py就是一个自定义的模块

# 1、import 模块名...； 这种格式，会导入指定模块中所有成员（包括变量、函数、类等）
# 2、from  模块名 import 成员名； 只会导入模块中指定的成员，而不是全部成员