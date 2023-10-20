import pymysql

# 1、链接数据库
db = pymysql.connect(host = '192.168.33.10', user = 'root', password = 'root', database = 'maoyandb')

# 2、创建对象句柄
cursor = db.cursor()

# 3、执行sql
# 占位符插入
sql = "insert into filmtab values('%s','%s','%s')" % ('刺杀小说家','雷佳音','2021')
cursor.execute(sql)
# 列表传参方式
sql = 'insert into filmtab values(%s,%s,%s)'
cursor.execute(sql,['刺杀,小说家','雷佳音','2021'])

# 4、提交数据
db.commit()

# 5、关闭数据库
cursor.close()
db.close()