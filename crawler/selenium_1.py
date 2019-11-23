
# 下载python的selenium安装包
# pip install selenium

# 简单的使用

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
#给定的URL的页面，WebDriver会等待页面完全加载完(就是onload函数被触发了)
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Python")
#driver.find_element_by_id("kw").send_keys(Keys.RETURN)
#等待5秒
driver.implicitly_wait(5)
#点击按钮
driver.find_element_by_id("su").click()
# quit退出整个浏览器
# driver.quit()
# close只会关闭一个标签
# driver.close()



# selenium-python中文文档
# https://python-selenium-zh.readthedocs.io/zh_CN/latest/2.%E5%BC%80%E5%A7%8B/