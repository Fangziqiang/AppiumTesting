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
#         OPPO R9s
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'ba36aa7a'
#       微信
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'

        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        # 初始化Appium 连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    #   测试用例使用test开头
    def testbaidu(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        text = self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").get_attribute("text")
        print(text)

        #   断言判断文本是否存在于页面中
        self.assertIn("Web Browser Automation",text)

    #   添加teardown进行善后处理
    def tearDown(self):
        self.driver.quit()

#   添加测试集合
suit = unittest.TestSuite()
suit.addTest(testUsercenter("testbaidu"))

if __name__ == '__main__':
    #  使用main()方法进行运行用例
    # unittest.main()

    #   使用 run放进行运行测试用例集
    run = unittest.TextTestRunner()
    run.run(suit)