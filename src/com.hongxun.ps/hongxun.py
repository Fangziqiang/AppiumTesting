# -*- coding: utf-8 -*-
import sys
import os
import unittest

from time import sleep
from appium import webdriver
import subprocess
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common import desired_capabilities
from swipeMethod import swipe_up
from swipeMethod import swipe_left
from swipeMethod import swipe_right
# from swipeMethod import get_size

class HelloWorld(unittest.TestCase):
        
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.hongxun.ps'
#         com.tencent.qcloud.timchat.ui.SplashActivity
        desired_caps['appActivity'] = 'com.tencent.qcloud.timchat.ui.SplashActivity'
        desired_caps['deviceName'] = '192.168.61.101:5555'
        #解决无法输入中文
        desired_caps["unicodeKeyboard"] = "True"  
        desired_caps["resetKeyboard"] = "True" 
        #desired_caps["automationName"] = "uiautomator2"
        pass
        #定义快速输入方法，解决sendkeys方法输入速度慢的问题
        def fast_input(self,str,element):
            x = subprocess.check_output('adb devices', shell=True).split('\n')[1][:-7]
            element.click()
            sleep(0.3)
            subprocess.Popen('adb -s %s shell input text %s'%(x,str), shell=True)
            sleep(0.5)
        
        # 初始化Appium 连接Appium服务器地址
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        
        #操作启动页
        sleep(3)
        print u"等待3秒"
        swipe_left(driver,200)
        print u"第一屏"
        sleep(1)
        swipe_left(driver,200)
        print u"第2屏"
        sleep(1)
        swipe_left(driver,200)
        print u"第3屏"
        sleep(1)
        print u"向左滑动页面"
            
        try:    
            # 查找取消按钮
            negativeButton = driver.find_element_by_id("com.hongxun.ps:id/md_buttonDefaultNegative")
            negativeButton.click()
            driver.save_screenshot("add_page.png")             
        except:
            print u"未找到取消按钮，无需登录"
        #向上滑动
        swipe_up(driver,200)
        #锁定及唤醒屏幕
#         driver.lock(5)#5位时间秒
#         driver.keyevent(26)   
        
        guanjiaButton2 = driver.find_elements_by_class_name("android.widget.TextView")
        #判断标签名称是否为管家
        self.assertEqual(guanjiaButton2[5].text, u"管家")
        guanjiaButton2[5].click()
        print len(guanjiaButton2)
        
        #切换到政讯页
        #self.assertEqual(guanjiaButton2[4].text, u"政讯")
        #判断政讯标签名称是否正确
        if guanjiaButton2[4].text==u"政讯":
            print u"中间标签名称为政讯"
            guanjiaButton2[4].click()
        else:
            print u"中间标签名称为"+guanjiaButton2[4].text
        
        #使用uiautomator方法定位社区标签
        zhengWuButton = driver.find_element_by_android_uiautomator("text(\"社区\")")
        self.assertEqual(zhengWuButton.text, u"社区")
        zhengWuButton.click()
        
        
        #实现列表滚动查找
#         driver.scroll(origin_el, destination_el)
        
        
        
        driver.quit()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    