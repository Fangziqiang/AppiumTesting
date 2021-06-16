# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#coding=utf-8

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "sanxingA9"
caps["appPackage"] = "com.me.fzw.dashanonline"
caps["appActivity"] = "com.me.fzw.dashanonline.activity.GuidePageActivity"
caps["noReset"] = "True"

driver = webdriver.Remote("http://192.168.1.186:4723/wd/hub", caps)

#el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ListView/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.ImageView")
try:
	img_close = driver.find_element_by_id("com.me.fzw.dashanonline:id/img_close")
	img_close.click()
except:
	print (u"没有弹窗")
#driver.switch_to.alert.accept()
#el1 = driver.find_element_by_id("com.me.fzw.dashanonline:id/iv_item")
#el1.click()

#面授课分享
#//*[@resource-id="com.me.fzw.dashanonline:id/rv_quick_access"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]
courseButton = driver.find_element_by_xpath('//*[@resource-id="com.me.fzw.dashanonline:id/rv_quick_access"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]')
courseButton.click()
try:
	bk_detail = driver.find_element_by_id("com.me.fzw.dashanonline:id/rl_content")
	bk_detail[0].click()
except:
	print (u"控件定位失败")
driver.close()

