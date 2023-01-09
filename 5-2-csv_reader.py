# CSV文件又称为逗号分隔值文件，是一种通用的、相对简单的文件格式，用以存储表格数据，包括数字或者字符
import csv

# 1、csv.reader()
with open('eggs.csv', 'r', newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(','.join(row))