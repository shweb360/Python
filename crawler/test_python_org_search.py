import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Selenium测试,python.org 函数搜索功能的测试
# 测试用例类继承了unittest.TestCase类，这表明这个类是一个测试用例
class PythonOrgSearch(unittest.TestCase):
    #setUp函数进行了初始化
    def setUp(self):
        self.driver=webdriver.Chrome()

    # 测试用例的方法,它应该总是以字符'test'开始. 
    # 方法的第一行 本地引用了 setUp方法中创建的driver对象： 
    def test_search_in_python_org(self):
        driver=self.driver
        driver.get("https://www.python.org")
        #断言，确认页面标题里是否有'Python'这个单词
        self.assertIn("Pytho",driver.title)
        #寻找页面元素
        elem=driver.find_element_by_name("q")
        elem.send_keys("pycon")        
        #Keys.RETURN回车键
        elem.send_keys(Keys.RETURN)
        assert "No result found " not in driver.page_source

if __name__=="__main__":
    unittest.main()        
