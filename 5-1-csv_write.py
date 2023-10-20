# CSV文件又称为逗号分隔值文件，是一种通用的、相对简单的文件格式，用以存储表格数据，包括数字或者字符
import csv

# CSV模块的writer类可用于读写序列化的数据 writer(csvfile, dialect='excel', **fmtparams)
# 参数说明：
# csvfile：必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象。
# dialect：编码风格，默认为 excel 的风格，也就是使用逗号,分隔。
# fmtparam：格式化参数，用来覆盖之前 dialect 对象指定的编码风格。

# 1> csv.writer()
# 单行写入
with open('eggs.csv', 'w', newline='') as csvfile:
    # delimiter 指定分隔符，默认为逗号，这里指定为空格【一个单字符】
    # quotechar 表示引用符  quotechar 是引用符，当一段话中出现分隔符的时候，用引用符将这句话括起来，以能排除歧义【一个单字符】
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|')
    # writerow 单行写入，列表格式传入数据
    spamwriter.writerow(['www.biancheng.net'] * 5 + ['how are you'])
    spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])

# 多行写入
with open('aggs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 注意传入数据的格式为列表元组格式
    writer.writerows([('hello','world'), ('I','love','you')])

# 2> csv.DictWriter() 类似字典的形式读写数据
with open('names.csv', 'w', newline='') as csvfile:
    #构建字段名称，也就是key，表头
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 写入字段名，当做表头
    writer.writeheader()
    # 多行写入
    writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'},{'first_name': 'Lovely', 'last_name': 'Spam'}])
    # 单行写入
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})