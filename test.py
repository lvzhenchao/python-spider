import os

print(os.getcwd())
print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.relpath('E:\python_code\python-spider'))
print(os.path.relpath('E:\python_code\python-spider', 'E:\python_code'))

path = "E:\python_code\python-spider\demo.txt"
print(os.path.dirname(path))