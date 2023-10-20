# CSV文件又称为逗号分隔值文件，是一种通用的、相对简单的文件格式，用以存储表格数据，包括数字或者字符
import csv

# 1、csv.reader()
# CSV模块的reader类可用于读写序列化的数据 reader(csvfile, dialect='excel', **fmtparams)
# 参数说明：
# csvfile：必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象。
# dialect：编码风格，默认为 excel 的风格，也就是使用逗号,分隔。
# fmtparam：格式化参数，用来覆盖之前 dialect 对象指定的编码风格。

with open('eggs.csv', 'r', newline="") as csvfile:
    # delimiter 指定分隔符，默认为逗号，这里指定为空格
    # quotechar 表示引用符  quotechar 是引用符，当一段话中出现分隔符的时候，用引用符将这句话括起来，以能排除歧义
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(','.join(row))

# 2、csv.DictReader()
with open('names.csv', newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        print(row['first_name'], row['last_name'])