#锁定屏幕时间秒
driver.lock(5)
#解锁屏幕
driver.keyevent(26)
#将APP放置后台 参数时间秒
driver.background_app(5)
#收起键盘
driver.hide_keyboard()
#启动Activity 
driver.start_activity('包名', 'activity名')
#打开通知栏
driver.open_notifications()
#检查应用是否已经安装 参数包名
driver.is_app_installed('xxxxxx')
#安装应用 参数 路径
driver.install_app('path/my.apk')
#删除应用
driver.remove_app('xxxxxx')
#摇晃（Shake）
driver.shake()
#关闭应用
driver.close_app()
#重置（等于卸载后重装）放在程序最后一步执行
driver.reset()
#获取应用的字符串
driver.app_strings
#按键事件
driver.keyevent(KeyboardInterrupt)
#获取当前Activity
driver.current_activity
#触摸动作(TouchAction) / 多点触摸动作(MultiTouchAction)
action = TouchAction(driver)
action.press(element=el, x=10, y=10).release().perform()
#滑动(Swipe) 参数 开始x,y坐标   滑动到的X,y坐标， 持续时间ms
driver.swipe(start=75, starty=500, endx=75, endy=0, duration=800)
#双指向内移动缩小屏幕
driver.pinch(element=el)
#放大 
driver.zoom(ele)

#坐标点击
driver.tap([(x,y)],time)

#滚动
driver.scroll(ele1,ele2)

#按住element并拖动到另外一个element上
driver.drag_and_drop(ele1,ele2)

#滑动
driver.swipe(x1,y1,x2,y2,time)
driver.flick(x1,y1,x2,y2)

#滑动到某个元素。
#todo: xxxx

#拉出文件 (Pull File)从设备中拉出文件
driver.pull_file('Library/xxx/xxx.plist')


#推送文件(Push file) 把文件放到设备中
data = "test is good"
path = "/data/local/tmp/test.txt"
driver.push_file(path, data.encode('base64'))

# appium扩展提供了pressKeyCode()方法。该方法Android特有。

# 方法：pressKeyCode()
# 发送一个键码的操作。需要一个入参。
driver.pressKeyCode(29); 
电话键

KEYCODE_CALL 拨号键 5

KEYCODE_ENDCALL 挂机键 6

KEYCODE_HOME 按键Home 3

KEYCODE_MENU 菜单键 82

KEYCODE_BACK 返回键 4

KEYCODE_SEARCH 搜索键 84

KEYCODE_CAMERA 拍照键 27

KEYCODE_FOCUS 拍照对焦键 80

KEYCODE_POWER 电源键 26

KEYCODE_NOTIFICATION 通知键 83

KEYCODE_MUTE 话筒静音键 91

KEYCODE_VOLUME_MUTE 扬声器静音键 164

KEYCODE_VOLUME_UP 音量增加键 24

KEYCODE_VOLUME_DOWN 音量减小键 25
