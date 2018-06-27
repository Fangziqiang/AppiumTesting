"""
Created on 2017/12/15

@author: manbu
"""
# coding:utf-8
import re
import requests
from bs4 import BeautifulSoup

filepath="F:/temp_xiaoshuo/";

class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')

    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()

tool=Tool()

# url="http://www.mx-xz.com/sc-zl/fenlei/";
url = "http://a.mp.uc.cn/media.html?mid=da9103ee5b5c459fbd65ef447c93b529&client=ucweb&uc_param_str=frdnsnpfvecpntnwprdsssnikt&uc_biz_str=S:custom%7CC:iflow_ncmt"
htmlr=requests.get(url);
bsObjHtml=BeautifulSoup(htmlr.text,"html.parser");

for titlelist in bsObjHtml.findAll("div",{"class":"title"}):
    if (titlelist.a != None):
        urltext=titlelist.a["href"];
        filename=titlelist.a["title"];

        fp=open(filepath+filename+".txt","w");

        rtext=requests.get(urltext);
        bsObjtext=BeautifulSoup(rtext.text);
        print "test"

        filetext=bsObjtext.find("div",{"id":"sdcms_content"});

        fp.write(tool.replace(filetext.__str__()));

        fp.close();