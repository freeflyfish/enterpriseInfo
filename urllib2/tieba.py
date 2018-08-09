#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-03 00:05
# Email        : liyingxuan@sck2data.com.cn
# Filename     : tieba.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

import urllib
import urllib2

def loadPage(url):
	"""
	url: urls to be crawled

	"""
	headers = {'User-Agent': "Mozilla"}
	request = urllib2.Request(url, headers = headers)
	return urllib2.urlopen(request).read()
	

def writePage(html, filename):
	"""
	write html to local files
	"""
	with open(filename, 'w') as f:
		f.write(html)

def tiebaSpider(url, beginPage, endPage):
	for page in range(beginPage, endPage+1):
		pn = (page - 1) * 50	
		filename = "第" + str(page) + "页.html"
		fullurl = url + "&pn=" + str(pn)
		html = loadPage(fullurl)
		writePage(html, filename)

if __name__ == "__main__":
	kw = raw_input('请输入你要的贴吧名: ')
	startPage = int(raw_input('start page:'))
	endPage = int(raw_input('end page:'))
	url = "http://tieba.baidu.com/f?"
	kw = urllib.urlencode({"kw":kw})
	fullurl = url + kw 
	tiebaSpider(fullurl, startPage, endPage)
