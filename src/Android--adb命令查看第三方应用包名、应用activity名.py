（adb shell am start -n 包名/包名＋类名）

adb shell am start -n com.android.fcc.espressif/com.android.fcc_app.MainActivity

查看activity名：

（1）启动要查看的程序；

（2）命令行输入：adb shell dumpsys window w |findstr \/ |findstr name=


补充：使用adb shell dumpsys window | findstr mCurrentFocus  命令查看当前运行的包名和Activity更清晰一些。

com.tencent.mm/com.tencent.mm.plugin.appbrand.ui.AppBrandUI

二 、从电脑端向手机复制文件

输入: adb pull 电脑路径  手机存储路径  
 adb push  /Users/xxxx/xxx.txt   /sdcard/xxx
 
 
 
 https://blog.csdn.net/csh86277516/article/details/52382214