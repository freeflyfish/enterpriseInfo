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
		pattern = '//div[@class="container company-header-block "]//div[@class="content"]//div[@class="in-block"]'
		profile = self.content.xpath(pattern)
		res = {}
		for item in profile:
			(key, value)  = item.xpath("string()").split(u'\uff1a')
			#print key.encode('utf8')
			key = key.encode('utf8')
			value = value.strip(u'\u67e5\u770b\u66f4\u591a')
			res[key] = value.encode('utf8')
		abstract = self.content.xpath('//div[@class="container company-header-block "]//script[@id="company_base_info_detail"]/text()')
		res["简介"] = abstract[0].strip()
		res = json.dumps(res)
		
		return res 

	def getMarketInfo(self):

		pattern = '//div[@class="detail-list"]/div[@class="block-data-group"]/div[@id="nav-main-volatilityNum"]//table/tbody/tr/td/text()'
		marketInfo = self.content.xpath(pattern)
		res = {}
		for i in xrange(0,len(marketInfo),2):
			(key, value) = marketInfo[i:i+2]
			key = key.xpath('string()')	
			res[key] = value.xpath('string()')
	
		res = json.dumps(res)
		
		return res

	def getBackgrounds(self):

		#table = '//div[@class="detail-list"]//div[@class="data-content"][@id="_container_baseInfo"]/table'
		table = '//div[@class="detail-list"]//div[@id="_container_baseInfo"]/table[@class="table -striped-col -border-top-none"]//tr/td/text()'
		backgrounds = self.content.xpath(table)
		#print len(backgrounds)
		res = {}
		#for i in xrange(len(backgrouds)): 
		#	b = backgrouds[i]
		#	data = b.xpath('//td')
		#	for j in xrange(0,len(data),2):
		#		key, value = data[j:j+2]
		#		key = key.xpath('string()')[0]
		#		value = value.xpath('string')
		#		print type(key),type(value)
		#		res[key] = value	
		m, n = divmod(len(backgrounds),2)
		for i in xrange(0, m, 2):
			key, val = backgrounds[i:i+2]
			res[key] = val
			
		if n == 1:
			res[backgrounds[-1]] = self.content.xpath('//div[@class="detail-list"]//div[@id="_container_baseInfo"]/table[@class="table -striped-col -border-top-none"]//tr/td[@colspan="4"]/span//text/text()')
		res["score"] = self.content.xpath('//div[@class="detail-list"]//div[@id="_container_baseInfo"]/table[@class="table -striped-col -border-top-none"]//tr/td/img/@alt')[0]
		res["注册资本"] = self.content.xpath('//div[@class="detail-list"]//div[@id="_container_baseInfo"]/table[@class="table"]//tr/td//text/text()')[0]
		res = json.dumps(res)
		
		return res
	
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

	def info(self):
		info = {}
		info["公司简介"] = self.getProfile()	
		info["上市信息"] = self.getMarketInfo()	
		info["公司背景"] = self.getBackgrounds()	
		info["司法风险"] = self.getLegalRisk()	
		info["经营风险"] = self.getOperationalRisk()	
		info["公司发展"] = self.getDevHistory()	
		info["经营状况"] = self.getBusinessStatus()	
		info["知识产权"] = self.getIntellectualProperty()	
		info["历史信息"] = self.getHistory()	
		
		return json.dumps(info)


if __name__ == "__main__":

	f = open('./dongfang.html', 'r')
	html = f.read()
	f.close()
	content = etree.HTML(html)
	Content = HtmlContent(content)
	#profile = Content.getProfile()
	#print profile
	#market = Content.getMarketInfo()
	#print market
	back = Content.getBackgrounds()
	print back
