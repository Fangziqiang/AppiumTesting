#coding=utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "模拟器"
caps["appPackage"] = "com.oppo.usercenter"
caps["appActivity"] = ".vip.UCVIPMainActivity"
caps["noReset"] = "True"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.oppo.usercenter:id/cb_sign_in")
el1.click()
el2 = driver.find_element_by_id("com.oppo.usercenter:id/tv_sign")
el2.click()

driver.quit()