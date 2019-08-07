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


class testCommunity(unittest.TestCase):
    # 添加setup进行初始化工作
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
#         解决无法输入中文
        desired_caps["unicodeKeyboard"] = "True"  
        desired_caps["resetKeyboard"] = "True" 
#         OPPO R9s
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'ba36aa7a'
#       微信
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
        
#         desired_caps['appActivity'] = 'com.oppo.community.MainActivity'
        # 当通过appPackage和appActivity启动失败时可替换下面这种，注意需要把上面的方式给注释掉
        # 'app':'E:\\weixin_1220.apk',

        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        # 初始化Appium 连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    #   测试用例使用test开头
    #定义快速输入方法，解决sendkeys方法输入速度慢的问题
    
    def getintegral2(self):
        sleep(2)
       
        lists = self.driver.find_elements_by_id("com.tencent.mobileqq:id/relativeItem")
        print (len(lists))
        lists[0].click()
        inputBox=self.driver.find_element_by_id("com.tencent.mobileqq:id/input")
        sendButton=self.driver.find_element_by_id("com.tencent.mobileqq:id/fun_btn")
        for i in range(10):
            testCommunity.fast_input2(u"小柯基",inputBox)
#             inputBox.send_keys(u"小柯基,来根烤肠")
            sendButton.click()
        
       

        #   断言判断文本是否存在于页面中
#         self.assertIn("Web Browser Automation",text)

    #   添加teardown进行善后处理
    def tearDown(self):
        self.driver.quit()

#   添加测试集合
suit = unittest.TestSuite()
suit.addTest(testCommunity("getintegral2"))

if __name__ == '__main__':
    #  使用main()方法进行运行用例
    # unittest.main()
    #   使用 run放进行运行测试用例集
    run = unittest.TextTestRunner()
    run.run(suit)