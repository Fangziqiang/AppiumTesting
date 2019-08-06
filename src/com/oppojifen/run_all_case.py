#coding=utf-8

import unittest
import os

class RunCase(unittest.TestCase):
    def test01(self):
#         os.getcwd()获取当前目录，方法一
        case_path=os.path.join((os.getcwd()),'')
#         方法二
#         case_path=os.path.dirname(os.path.abspath(__file__))
        print (case_path)
        suite=unittest.defaultTestLoader.discover(case_path,'test*.py')
        print(suite)
        unittest.TextTestRunner().run(suite)
    
if __name__=="__main__":
    unittest.main()
    