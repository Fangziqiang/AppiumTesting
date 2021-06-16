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
from selenium.common.exceptions import  NoSuchElementException,WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class testAPPstore(unittest.TestCase):
    # 添加setup进行初始化工作
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #OPPO R9s
        #desired_caps['platformVersion'] = '7.1.1'
        #desired_caps['deviceName'] = 'ba36aa7a'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = '763d6ade'
#       软件商店
        desired_caps['appPackage'] = 'com.heytap.market'
        desired_caps['appActivity'] = '.activity.MainActivity'
        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        # 初始化Appium 连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        

    #   测试用例使用test开头
#     @unittest.skip("ceshi")
    def test_getintegral(self):
        self.driver.implicitly_wait(10)
        try:
        #sleep(5)
            meButon = self.driver.find_element_by_xpath('//*[@resource-id="com.heytap.market:id/navi_menu_tab"]/android.view.ViewGroup[1]/android.widget.FrameLayout[5]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
            meButon.click()
        except NoSuchElementException:
            print ("找不到我的按钮")
        try:
            signin = self.driver.find_element_by_id("com.heytap.market:id/nearx_btn_sign_in")
            signin.click()
        except NoSuchElementException:
            print("找不到签到按钮")
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.alert_is_present())
        self.driver.switch_to.alert().accept()
    #   添加teardown进行善后处理
    def tearDown(self):
        self.driver.quit()

#   添加测试集合
suit = unittest.TestSuite()
suit.addTest(testAPPstore("test_getintegral"))

if __name__ == '__main__':
    #  使用main()方法进行运行用例
    # unittest.main()
    #   使用 run放进行运行测试用例集
    run = unittest.TextTestRunner()
    run.run(suit)