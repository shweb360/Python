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
    