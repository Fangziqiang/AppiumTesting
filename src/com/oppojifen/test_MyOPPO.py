# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import subprocess
from swipeMethod import swipe_up
from swipeMethod import swipe_left
from swipeMethod import swipe_right
from _ast import TryExcept

# https://cloud.tencent.com/developer/article/1467203  安装定位工具

class testUsercenter(unittest.TestCase):
    # 添加setup进行初始化工作
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
#         OPPO R9s
<<<<<<< HEAD:src/com/oppojifen/test_Usercenter.py
        #desired_caps['platformVersion'] = '7.1.1'
        #desired_caps['deviceName'] = 'ba36aa7a'
        #desired_caps['deviceName'] = '305f8735'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = '763d6ade'
=======
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'ba36aa7a'

>>>>>>> a6ab878977fedb75f0b20164b05ee2c95514714b:src/com/oppojifen/test_MyOPPO.py
        desired_caps['appPackage'] = 'com.oppo.usercenter'
        desired_caps['appActivity'] = 'com.oppo.usercenter.vip.UCVIPMainActivity'

        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        # 初始化Appium 连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    #   测试用例使用test开头
    def test_getintegral(self):
<<<<<<< HEAD:src/com/oppojifen/test_Usercenter.py
        try:
            self.driver.implicitly_wait(10)
            signin = self.driver.find_element_by_xpath('//*[@text="已签"]')
            signin.click()
            print("签到成功")
            #self.driver.switch_to.alert.accept()
        except:
            print("已签到")

        #断言判断文本是否存在于页面中
        #self.assertIn("Web Browser Automation",text)

    #添加teardown进行善后处理
=======
        #隐式等待10s
        self.driver.implicitly_wait(10)
        
        signin = self.driver.find_element_by_id("com.oppo.usercenter:id/cb_sign_in")
        signin.click()
        signinButton = self.driver.find_element_by_id("com.oppo.usercenter:id/sign_btn")
        is_signed = signinButton.text
        if signinButton.is_enabled():
            signinButton.click()
#             self.driver.switch_to.alert.accept()
        #签到成功弹窗
#       text = self.driver.find_element_by_id("com.oppo.usercenter:id/get_btn").text
#       print(text)
        else:
            print(is_signed)
       

        #   断言判断文本是否存在于页面中
#         self.assertIn("Web Browser Automation",text)

    #   添加teardown进行善后处理
>>>>>>> a6ab878977fedb75f0b20164b05ee2c95514714b:src/com/oppojifen/test_MyOPPO.py
    def tearDown(self):
        self.driver.quit()
#   添加测试集合
suit = unittest.TestSuite()
suit.addTest(testUsercenter("test_getintegral"))

if __name__ == '__main__':
    #  使用main()方法进行运行用例
    # unittest.main()
    #   使用 run放进行运行测试用例集
    run = unittest.TextTestRunner()
    run.run(suit)