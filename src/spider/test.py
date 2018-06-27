#coding=utf-8

import requests 

html = requests.get("http://a.mp.uc.cn/media.html?mid=da9103ee5b5c459fbd65ef447c93b529&client=ucweb&uc_param_str=frdnsnpfvecpntnwprdsssnikt&uc_biz_str=S:custom%7CC:iflow_ncmt")

print html.text