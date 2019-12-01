from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

# 断言“百度一下”出现在浏览器标题
assert '百度一下' in driver.title

input_text=driver.find_element_by_name("wd")
input_text.clear()
input_text.send_keys("selenium")
input_text.send_keys(Keys.RETURN)

assert '没有找到相关记录' in driver.page_source

# 关闭浏览器
driver.close()
