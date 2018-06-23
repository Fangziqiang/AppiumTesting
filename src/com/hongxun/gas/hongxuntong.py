# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import subprocess
from random import Random


class hongxuntong(unittest.TestCase):
        
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.jiaxun.management'
        desired_caps['appActivity'] = 'com.tencent.qcloud.timchat.ui.SplashActivity'
        desired_caps['deviceName'] = '192.168.61.101:5555'
        #解决无法输入中文
        desired_caps["unicodeKeyboard"] = "True"  
        desired_caps["resetKeyboard"] = "True" 
        desired_caps['noReset'] = 'False'
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
#         driver.install_app('hongxutong.apk')
#         driver.install_app(app_path)
        try:
            phoneNumber = driver.find_element_by_id("com.jiaxun.management:id/et_number")
#             phoneNumber.send_keys(u"test6测试")
#             phoneNumber.set_value("test6")
            fast_input(driver,u"test6",phoneNumber)

            sleep(2)            
            Button2 = driver.find_elements_by_class_name("android.widget.TextView")
            print u"找到确定按钮"
            Button2[2].click()
            driver.save_screenshot("add_page.png")
            #mineButton = driver.find_elements_by_class_name("android.widget.RelativeLayout")
            mineButton = driver.find_elements_by_id("com.jiaxun.management:id/tv_tab_title")
            mineButton[11].click()
            sleep(3)
            #清除程序数据
            driver.reset()
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
    
    