
# 是一个用于测试web应用的自动化测试工具，直接运行在浏览器中，实现了对浏览器的自动化操作
## 比如软件自动化测试，检测软件与浏览器兼容性，自动录制、生成不同语言的测试脚本，以及自动化爬虫等

## 1、自动访问百度
# 导入seleinum webdriver接口
from selenium import webdriver
import time
# 创建Chrome浏览器对象
browser = webdriver.Chrome()
#访问百度网站
browser.get('http://www.baidu.com/')
#阻塞3秒
time.sleep(3)
# 自动退出浏览器
browser.quit()