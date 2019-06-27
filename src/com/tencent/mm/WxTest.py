# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver


class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
#       夜神模拟器
#       desired_caps['deviceName'] = '127.0.0.1:62001'
#       desired_caps['platformVersion'] = '5.1.1'

#       OPPO R9s
#       desired_caps['platformVersion'] = '7.1.1'
#       desired_caps['deviceName'] = 'ba36aa7a'

#       小米 MIX2
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] ='e82b5f9d'
        
#       便签
#       desired_caps['appPackage'] = 'com.nearme.note'
#       desired_caps['appActivity'] = '.view.AllNoteActivity'
#       微信
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'

        #设置每次启动不清除程序原始数据
        desired_caps['noReset'] = 'True'
        pass
        
        # 初始化Appium 连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        
        # 查找登录按钮
        LoginButton = None
        try:
            # 如果手机没有联系人，则通过create_contact_button 来创建。此处通过控件id 来查找
            LoginButton = driver.find_element_by_id("com.tencent.mm:id/b6e")
        except:
            # 否则通过底部的添加联系人菜单来添加
            LoginButton = driver.find_element_by_id("com.android.contacts:id/menu_add_contact")
            # 单击创建按钮
            LoginButton.click()
        
        # 稍等下，手机响应需要一点时间
        # 此处固定等待两秒方法不可取，由于不同的手机响应速度不同，脚本可能会失败
        # 此处仅是为了示例，在后面章节中会有更合理的等待方法
        sleep(2)
        # 查看Dialog 的显示是否显示
        try:
            dialog = driver.find_element_by_id("android:id/content")
            # 找到“本地保存”按钮并点击
            saveLocal = driver.find_element_by_id("com.tencent.mm:id/b6e")
            saveLocal.click()
            sleep(2)
        except:
            # 如果找不到Dialog 或者button, 就会跳转到这里
            print("no dialog found")
        
        sleep(2)
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
