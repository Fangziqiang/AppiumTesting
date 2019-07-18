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


class testUsercenter(unittest.TestCase):
    # 添加setup进行初始化工作
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
#       夜神模拟器
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['platformVersion'] = '5.1.1'

#       OPPO R9s
#       desired_caps['platformVersion'] = '7.1.1'
#       desired_caps['deviceName'] = 'ba36aa7a'

#       小米 MIX2
#         desired_caps['platformVersion'] = '8.0.0'
#         desired_caps['deviceName'] ='e82b5f9d'
        
#       便签
#       desired_caps['appPackage'] = 'com.nearme.note'
#       desired_caps['appActivity'] = '.view.AllNoteActivity'
#       安卓pos客户端
        desired_caps['appPackage'] = 'com.hzcx.hzcxpospal'
        desired_caps['appActivity'] = 'com.hzcx.hzcxpospal.ui.actvity.NewShouYinActivity'

        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        # 初始化Appium 连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    #   测试用例使用test开头
    def login(self,username,password):
        usernameBtn = self.driver.find_element_by_id("com.hzcx.hzcxpospal:id/et_zhanghu")
        usernameBtn.send_keys("17610831883")
        passwordBtn = self.driver.find_element_by_id("com.hzcx.hzcxpospal:id/et_pwd")
        passwordBtn.send_keys("123456")
        signin = self.driver.find_element_by_id("com.hzcx.hzcxpospal:id/bt_login")
        signin.click()
        #签到成功弹窗
#       text = self.driver.find_element_by_id("com.oppo.usercenter:id/get_btn").text
#       print(text)
        else:
            print(is_signed)
       

        #   断言判断文本是否存在于页面中
#         self.assertIn("Web Browser Automation",text)

    #   添加teardown进行善后处理
    def tearDown(self):
        self.driver.quit()

#   添加测试集合
suit = unittest.TestSuite()
suit.addTest(testUsercenter("getintegral"))

if __name__ == '__main__':
    #  使用main()方法进行运行用例
    # unittest.main()
    #   使用 run放进行运行测试用例集
    run = unittest.TextTestRunner()
    run.run(suit)