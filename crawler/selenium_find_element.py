# 通过本节，我们需要数量掌握以下几种元素定位方法
# 通过id定位
# 通过class定位
# 通过name属性定位
# 通过标签名定位
# 通过链接文本定位
# 通过xpath定位
# 通过css选择器定位
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
driver=webdriver.Chrome()

file_path='file:///F:/03%E5%AD%A6%E4%B9%A0%E5%8C%BA/13Python/02Demo/crawler/selenium_test_hello.html'

driver.get(file_path)

#元素定位
# 通过class定位
head_title=driver.find_element_by_class_name("head_title")
print("head_title:"+head_title.text)

# 通过id定位
world=driver.find_element_by_id("world")
print("world:"+world.text)

# 通过name属性定位
username=driver.find_element_by_name("username")
print(username.get_attribute("value"))

# 通过标签名定位
# 定位标签为<button>的元素
submit_btn =driver.find_element_by_tag_name("button");
print(submit_btn.text)

# 通过链接文本定位
# 定位链接文本完全匹配“我的看云首页”的元素
linktext=driver.find_element_by_link_text("我的看云首页")
print(linktext.get_attribute("href"))
# 定位链接文本部分匹配“看云首页”的元素
partial_linktext=driver.find_element_by_partial_link_text("看云首页")
print(partial_linktext.get_attribute("href"))

# 通过xpath定位
# xpath定位，相对路径定位用户名输入框
username=driver.find_element_by_xpath("//body/div/input")
print(username.get_attribute("value"))
# xpath定位，相对路径与属性结合 定位密码输入框
password=driver.find_element_by_xpath("//input[@name='password']")
print(password.get_attribute("value"))
# xpath定位，多个属性结合 定位密码输入框
password=driver.find_element_by_xpath("//input[@name='password'][@type='text']")
print(password.get_attribute("value"))


# 通过css选择器定位
# css选择器，标签+属性 定位用户名输入框
username=driver.find_element_by_css_selector("input[name='username']")
print(username.get_attribute("value"))
# css选择器，标签+class类名 定位用户名输入框
username=driver.find_element_by_css_selector("input.user_name")
print(username.get_attribute("value"))
# css选择器，标签+多个class类名，定位密码输入框，注意不要空格，空格代表下一级子元素
password=driver.find_element_by_css_selector("input.ptqa.pwd")
print(password.get_attribute("value"))
# css选择器，id+多个class类名，定位密码输入框
password=driver.find_element_by_css_selector("#login_form .ptqa.pwd")
print(password.get_attribute("value"))
# css选择器，多级class类名，定位密码输入框
password=driver.find_element_by_css_selector(".login .ptqa.pwd")
print(password.get_attribute("value"))
# css选择器，class类名+属性，定位密码输入框
password=driver.find_element_by_css_selector(".login .ptqa[name='password']")
print(password.get_attribute("value"))
# css 选择器，根据父子关系，定位密码输入框
password=driver.find_element_by_css_selector("div[id='login_form']>input[name='password']")
print(password.get_attribute("value"))
# css 选择器，根据兄弟关系，定位密码输入框
password = driver.find_element_by_css_selector("input[name='username']+input")
print(password.get_attribute("value"))

# 用find_element_by_css_selector 获取的是单个元素
# 用find_elements_by_css_selector获取的是元素组列表

# 通用的终极定位语法
# 上面的所有元素定位 find_element_by_xxx和find_elements_by_xxx调用的结果，
# 实际上都是在调用以下两种方法，我们也可以直接调用一下两种方法即可。
# find_element(self, by=By.ID, value=None):
# find_elements(self, by=By.ID, value=None):

# 根据id,定位id为“world”的元素
world=driver.find_element(by=By.ID,value="world")
print(world.text)
# xpath定位，相对路径与属性结合 定位密码输入框
password = driver.find_element(By.XPATH,"//input[@name='password']")
print(password.get_attribute("value"))
# css选择器，标签+属性 定位用户名输入框
username = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
print(username.get_attribute("value"))



