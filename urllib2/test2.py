#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-02 22:26
# Email        : liyingxuan@sck2data.com.cn
# Filename     : test2.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

import sys
import re

with open("dongfang.html", 'r') as f:
	html = f.read()
	pattern = re.compile(r'company_base_info_detail">(.+?)</script', re.S)
	res = pattern.search(html)
	if res:
		print "res is ", res.group(1)
	

