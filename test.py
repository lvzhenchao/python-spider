def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")

# 调用next()内置函数
# num = intNum()
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(num.__next__())

# list() 和 tuple() 底层实现和 for 循环的遍历过程是类似的
num = intNum()
print(list(num))
num = intNum()
print(tuple(num))