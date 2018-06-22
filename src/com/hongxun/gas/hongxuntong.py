# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import subprocess


class hongxuntong(unittest.TestCase):
        
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.jiaxun.management'
        desired_caps['appActivity'] = 'com.tencent.qcloud.timchat.ui.SplashActivity'
        desired_caps['deviceName'] = 'ba36aa7a'
        #解决无法输入中文
        desired_caps["unicodeKeyboard"] = "True"  
        desired_caps["resetKeyboard"] = "True" 
        pass
        def fast_input(self,str,element):
#             str=str.encode(gbk)
            x = subprocess.check_output('adb devices', shell=True).split('\n')[1][:-7]
            element.click()
            sleep(0.3)
            subprocess.Popen('adb -s %s shell input text %s'%(x,str), shell=True)
            sleep(0.5)
        
        # 初始化Appium 连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        
        try:
            driver.save_screenshot("add_page.png")
        except:
            #找不到添加按钮
            print u"找不到添加按钮"
        # 保存一个屏幕截图
        driver.save_screenshot("afterinput.png")
        
        # 最后保存一个截图用于人工检查
        driver.save_screenshot("newContact.png")
        driver.quit()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(hongxuntong)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    