# Selenium WebDriver提供了两类waits- 隐式和显式。
# 显式的waits会让WebDriver在更深一步的执行前等待一个确定的条件触发，
# 隐式的waits则会让WebDriver试图定位元素的时候对DOM进行指定次数的轮询。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
try:
    # 这段代码会等待10秒，如果10秒内找到元素则立即返回，否则会抛出TimeoutException异常，
    # WebDriverWait默认每500毫秒调用一下ExpectedCondition直到它返回成功为止。
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,"kw"))
finally:    
    driver.quit()
    



#1、selenium只是模拟浏览器的行为，而浏览器解析页面是需要时间的（执行css，js），一些元素可能需要过一段时间才能加载出来，为了保证能查找到元素，必须等待

#2、等待的方式分两种：
browser=webdriver.Chrome()
wait1=WebDriverWait(browser,10)
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

wait=WebDriverWait(browser,10) #显式等待
wait1=browser.implicitly_wait(10)    #隐式等待
wait.until(EC.presence_of_element_located((By.CLASS_NAME,'tH0')))
'''
显式等待：指定等待某个标签加载完毕
隐式等待：等待所有标签加载完毕

'''