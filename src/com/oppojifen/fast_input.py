#coding=utf-8
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import subprocess

class fastInput():
    def fast_input2(self,str,element):
        x = subprocess.check_output('adb devices', shell=True).split('\n')[1][:-7]
        element.click()
        sleep(0.3)
        subprocess.Popen('adb -s %s shell input text %s'%(x,str), shell=True)
        sleep(0.5)
    fast_input2