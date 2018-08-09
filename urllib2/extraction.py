#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-08 10:18
# Email        : liyingxuan@sck2data.com.cn
# Filename     : extraction.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

from lxml import etree
import json



class HtmlContent(object):
	def __init__(self, content = None):
		self.content = content

	def tester(self, pattern):
		return self.content.xpath(pattern)

	def getProfile(self):
		#pattern = '//div[@class="container company-header-block "][@id="company_web_top"]/div[@class="box"]/div[@class="content"]/div[@class="detail"]'
		pattern = '//div[@class="container company-header-block"][@id="company_web_top"]//div[@class="box"]//div[@class="content"]/div[@class="detial"]'
		profile = self.content.xpath(pattern)

		phone_number = profile[0].xpath('string(.)').encode('utf-8').strip()

		return phone_number

	def getMarketInfo(self):
		pass

	def getBackgrounds(self):
		pass
	
	def getLegalRisk(self):
		pass

	def getRunRisk(self):
		pass

	def getOperationalRisk(self):
		pass

	def getDevHistory(self):
		pass

	def getBusinessStatus(self):
		pass

	def getIntellectualProperty(self):
		pass 

	def getHistory(self):
		pass

	


if __name__ == "__main__":

	f = open('./dongfang.html', 'r')
	html = f.read()
	f.close()
	content = etree.HTML(html)
	#link_list = content.xpath("//div@[class="content"]/div/div/div/span)[]")
	content = HtmlContent(content)
	print content.tester('//div[@class="container company-header-block "]')[0].xpath('//div[@class="content"]/div[@class=detail]')	
	profile = content.getProfile()
	print profile
