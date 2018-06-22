#coding=utf-8
import sys
import os
import unittest
from appium import webdriver
import subprocess

def get_size(self):
    x = self.get_window_size()['width']
    y = self.get_window_size()['height']
    return(x,y)

#上滑操作就是从屏幕的下端点击一个坐标然后往上滑动，x坐标可以不变。Y的开始和结束坐标改进即可。
def swipe_up(self,t):
    screen = get_size(self)
    self.swipe(screen[0]*0.5,screen[1]*0.75,screen[0]*0.5,screen[1]*0.25,t)

#下滑就是从屏幕的上端点击一个坐标然后往下滑动到另外一个坐标，x坐标可以不变。Y的开始和结束坐标改变即可
def swipe_down(self,t):
    screen = self.get_size()
    self.swipe(screen[0]*0.5,screen[1]*0.25,screen[0]*0.5,screen[1]*0.75,t)

#左滑就是从屏幕的右端点击一个坐标点往左滑动到另外一个坐标点。Y坐标可以不改变。X的开始和结束坐标改变即可。
def swipe_left(self,t):
    screen = self.get_size()
    self.swipe(screen[0]*0.75,screen[1]*0.5,screen[0]*0.25,screen[1]*0.5,t)

#右滑就是从屏幕的左端点击一个坐标点然后往后滑动到另外一个坐标点.Y坐标可以不变。X的开始和结束坐标改变即可。
def swipe_right(self,t):
    screen = self.get_size()
    self.swipe(screen[0]*0.25,screen[1]*0.5,screen[0]*0.75,screen[1]*0.5,t)

