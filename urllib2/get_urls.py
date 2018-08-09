#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-06 10:40
# Email        : liyingxuan@sck2data.com.cn
# Filename     : get_urls.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

import re
import sys


'href="https://www.tianyancha.com/company/953838482" target="_blank"'
with open(sys.argv[1], 'r') as f:
	html = f.read()
	a = r'href="https://www.tianyancha.com/company/\d*'
	pattern = re.compile(a, re.S)
	url = pattern.search(html)
	print url.group()
