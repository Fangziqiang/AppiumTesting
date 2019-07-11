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

class HelloWorld(unittest.TestCase):
    def get_size(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return(x,y)
    
#     def swipe_left(self,t):
#         screen = get_size(self)
#         self.swipe(screen[0]*0.75,screen[1]*0.5,screen[0]*0.25,screen[1]*0.5,t)
        
        
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
        list = None
#         try:
        sleep(2)
            # 如果手机没有联系人，则通过create_contact_button 来创建。此处通过控件id 来查找
        list = driver.find_elements_by_id("com.tencent.mm:id/b93")
        print(len(list))
        for i in range(len(list)):
            list[i].click()
#           返回
            driver.keyevent(4)
            sleep(1)
#             swipe_left(driver,200)
            
#         except:
            # 否则通过底部的添加联系人菜单来添加
            # 单击创建按钮
#         print("找不到列表可点击项")
        
        # 稍等下，手机响应需要一点时间
        # 此处固定等待两秒方法不可取，由于不同的手机响应速度不同，脚本可能会失败
        # 此处仅是为了示例，在后面章节中会有更合理的等待方法
        sleep(2)
    
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
