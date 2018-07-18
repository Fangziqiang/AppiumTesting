#coding=utf8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

if __name__=="__main__":
    ffdriver = "D:\\Program Files\\Mozilla Firefox\\firefox.exe"
    os.environ["webdriver.firefox.driver"] =ffdriver
    print "1"
    driver=webdriver.Firefox(ffdriver)
    #隐形等待和显性等待可以同时用，要注意的是：最大等待时间取决两者之间的大值
    driver.implicitly_wait(10)
    driver.get("http://www.testingunion.com")
    locator=(By.LINK_TEXT,u'webdriver')
    try:
        #在最长20秒内，每个0.5秒去检查locator是否存在，如果存在则进入下一步
        WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
        #提取该文本对应的url,并打印出来
        print driver.find_element_by_link_text(u'webdriver').get_attribute('href')
    finally:
        print u"异常了"
    driver.quit()