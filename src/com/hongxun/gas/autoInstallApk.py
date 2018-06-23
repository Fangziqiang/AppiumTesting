#coding=utf-8

import os
from appium import webdriver
from time import sleep

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
# desired_caps['appPackage'] = 'com.jiaxun.management'
# desired_caps['appActivity'] = 'com.tencent.qcloud.timchat.ui.SplashActivity'
desired_caps['deviceName'] = '192.168.61.101:5555'
desired_caps['app'] = apk_path+'\\gas\\hongxutong.apk'

print apk_path

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
sleep(2)

print u"启动Activity"
driver.start_activity('com.jiaxun.management', 'com.tencent.qcloud.timchat.ui.SplashActivity')
#将APP放置后台 参数时间秒
# driver.background_app(5)

# print u"打开通知栏"
# driver.open_notifications()

#检查应用是否已经安装 参数包名
print u"检查应用是否已经安装 "
driver.is_app_installed('com.jiaxun.management')

# 删除应用
# driver.remove_app('com.jiaxun.management')

print "exit"