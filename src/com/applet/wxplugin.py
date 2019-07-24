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
#         小米mix2
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] ='e82b5f9d'
#       微信
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        
        desired_caps['chromeOptions']= {'androidProcess': 'com.tencent.mm:appbrand0'}

        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        # 初始化Appium 连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        
        
    #   测试用例使用test开头
    def getintegral(self):
        sleep(7)
        def swipeDown(t):    
            x = self.driver.get_window_size()['width']    
            y = self.driver.get_window_size()['height']    
            x1 = int(x * 0.5)  # x坐标   
            y1 = int(y * 0.25)  # 起始y坐标    
            y2 = int(y * (0.25 + t))  # 终点y坐标    
            self.driver.swipe(x1, y1, x1, y2, 500)
        swipeDown(0.6) # 向下滑动屏幕的40%，准备从顶部进入小程序
        sleep(2)
        self.driver.find_element_by_android_uiautomator('text("汇智创享商家")').click() #点击顶部的图标进入小程序
        sleep(5)
        print self.driver.contexts
#         self.driver.switch_to.context('WEBVIEW_unknown')
        self.driver.find_element_by_xpath("//*[@resource-id=\"com.tencent.mm:id/v\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text=\"扫帚凳子\"]").click()
        sleep(3) 
#         signin = self.driver.find_element_by_xpath("//*[@resource-id="com.tencent.mm:id/v"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]")
#         signin.click()
        
#         if signinButton.is_enabled():
#             signinButton.click()
#         #签到成功弹窗
# #       text = self.driver.find_element_by_id("com.oppo.usercenter:id/get_btn").text
# #       print(text)
#         else:
#             print(is_signed)
#        

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