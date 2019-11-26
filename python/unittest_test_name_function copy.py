#导入模块和要测试的函数get_formatted_name()
import unittest
from unittest_name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formated_name=get_formatted_name('W','sh')
        #断言方法用来核实得到的结果和期望的结果是否一致
        self.assertEqual(formated_name,'W Sh')
    

unittest.main()        
