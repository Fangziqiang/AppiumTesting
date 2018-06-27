#coding=utf-8

import requests
payload1 = {'username': 'fzq', 'return': 'index.php'}
payload2 = {'username': 'fzq', 'return': 'index.php','password': '159753ai'}
payload2 = {'tl_login': 'admin', 'tl_password': 'admin','password': '159753ai'}

#requests允许使用params关键字参数
# r = requests.get("http://192.168.10.5/mantisbt/login_password_page.php/post",params=payload1)
r2 = requests.get("http://192.168.10.5/mantisbt/login.php/post",params=payload2)

print r2.status_code
# print r.headers['content-type']
# print r.encoding
# print r.text
# print r.json()
#通过打印输出该 URL，你能看到 URL 已被正确编码
# print r2.url
print r2.content
print r2.text