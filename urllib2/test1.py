#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-02 15:24
# Email        : liyingxuan@sck2data.com.cn
# Filename     : test1.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

import urllib2
import sys

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
html = response.read()
print(html)
#sys.stdout.write(html)

