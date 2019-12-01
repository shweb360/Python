'''实战要求：
用例一：
打开移动端网站 http://a.4399en.com/
登录,账号/密码为是： gfc@qq.com/123456
登录后，断言是否已经处于登录状态
关闭浏览器
https://www.kancloud.cn/guanfuchang/python_selenium/714651
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建Chrome驱动实例,这里创建driver时，传入chrome_options参数，告诉服务器，我是用移动端浏览器访问的
options=webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')

driver=webdriver.Chrome(chrome_options=options)
# 设置浏览器大小，让它看起来跟手机的样式差不多。
driver.set_window_size("380","680")

# 设置一个全局的等待超时时间 10s
driver.implicitly_wait(10)

# 打开首页
driver.get("http://a.4399en.com/")
driver.find_element_by_class_name("CNlogin").click()

# 在用户名输入框中输入正确的用户名
wait=WebDriverWait(driver,20,0.5)

account = wait.until(EC.visibility_of_element_located((By.ID,"modify-account")))
# account = driver.find_element_by_id("modify-account")
account.clear()
account.send_keys("gfc@qq.com")

password = driver.find_element_by_id("modify-password")
password.clear()
password.send_keys("123456")

driver.find_element_by_xpath("//input[@type='submit'][@value='Login']").click()

# 休息3s
time.sleep(3)
assert 'gfc@qq.com' in driver.page_source
driver.find_element_by_class_name("CNreg").click()
# 关闭浏览器
# driver.quit()
