# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import subprocess


class HelloWorld(unittest.TestCase):
        
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.nearme.note'
        desired_caps['appActivity'] = '.view.AllNoteActivity'
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
        
        # 查找创建新联系人按钮
#         createContactButton = None
        try:
            # 通过create_note_button 来创建note。此处通过控件id 来查找
            createNoteButton = driver.find_element_by_id("com.nearme.note:id/menu_new_note")
            createNoteButton.click()
            driver.save_screenshot("add_page.png")
        except:
            #找不到添加按钮
            print u"找不到添加按钮"
            
        edit = driver.find_element_by_id("com.nearme.note:id/text")
#         ss=u'我在测试'
#         fast_input(self,ss,edit)
        edit.send_keys(u"我在测试")
        # 保存一个屏幕截图
        driver.save_screenshot("afterinput.png")
        # 单击完成按钮
        completeButtom = driver.find_element_by_id("com.nearme.note:id/menu_edit_complete")
        completeButtom.click()
        #单机返回按钮
        backButtom=driver.find_element_by_id("com.nearme.note:id/support_up")
        backButtom.click()
        
        # 验证添加的联系人信息是否与预期输入一样com.nearme.note:id/text_content
        barTitle = driver.find_elements_by_id("com.nearme.note:id/text_content")
        self.assertEqual(barTitle[0].text, u"我在测试")
        barTitle[0].click()
        contactDatas = driver.find_element_by_id("com.nearme.note:id/text")
        self.assertEqual(contactDatas.text, u"我在测试")
        # 最后保存一个截图用于人工检查
        driver.save_screenshot("newContact.png")
        driver.quit()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    