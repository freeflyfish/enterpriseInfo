#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-02 22:26
# Email        : liyingxuan@sck2data.com.cn
# Filename     : test2.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

import urllib
import urllib2
import sys

url = "http://www.baidu.com/s"
keyword = raw_input("请输入要查询的字符串:")
#keyword = sys.argv[1]
headers = {"User-Agent" : "Mozilla"}
wd = {"wd" : keyword}
wd = urllib.urlencode(wd)
fullurl = url + "?" +  wd
#print fullurl
request = urllib2.Request(fullurl, headers = headers)
response = urllib2.urlopen(request)
print(response.read())
