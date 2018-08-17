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
import sys
import os
import re



class HtmlContent(object):

	def __init__(self, html = None):
		self.content = etree.HTML(html)
		self.raw_html = html

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
		#abstract = self.content.xpath('//div[@class="container company-header-block "]//script[@id="company_base_info_detail"]/text()')

		p = re.compile(r'company_base_info_detail">(.+?)</script', re.S)
		abstract = p.search(self.raw_html)

		if abstract:
			res["简介"] = abstract.group(1).strip()
		else:
			res["简介"] = "暂无信息"
		
		return res 

	def getMarketInfo(self):

		pattern = '//div[@class="detail-list"]/div[@class="block-data-group"]/div[@id="nav-main-volatilityNum"]//table/tbody/tr/td'
		marketInfo = self.content.xpath(pattern)
		res = {}
		for i in xrange(0,len(marketInfo),2):
			(key, value) = marketInfo[i:i+2]
			key = key.xpath('string()')	
			res[key] = value.xpath('string()')
	
		
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
		
		return res
	
	def getLegalRisk(self):
		res = {}
		legalp1 = '//div[@id="nav-main-lawDangerous"]//div[@id="nav-main-announcementCount"]/span/text()'		
		l1 = self.content.xpath(legalp1)
		if l1:
			res["开庭公告数量"] = self.content.xpath(legalp1)[0]
		else:
			res["开庭公告数量"] = "0"
			
		legalp2 = '//div[@id="nav-main-lawDangerous"]//div[@id="nav-main-lawsuitCount"]/span/text()'		
		l2 = self.content.xpath(legalp2)
		if l2:
			res["法律诉讼数量"] = self.content.xpath(legalp2)[0]
		else:
			res["法律诉讼数量"] = "0"

		return res


	def getOperationalRisk(self):
		res = {}
		return res

	def getDevHistory(self):
		res = {}
		rongzi = '//div[@id="nav-main-develope"]//div[@id="nav-main-companyRongzi"]/span/text()'
		rong = self.content.xpath(rongzi)
		if rong:
			res["融资次数"] = rong[0]
		else:
			res["融资次数"] = "0"
	
		jingpin = '//div[@id="nav-main-develope"]//div[@id="nav-main-companyJingpin"]/span/text()'
		jing = self.content.xpath(jingpin)
		if jing:
			res["竞品数量"] = jing[0] 
		else:
			res["竞品数量"] = "0" 
	
		return res

	def getBusinessStatus(self):
		res = {}
		
		return res

	def getIntellectualProperty(self):
		res = {}	 
		ip = '//div[@id="nav-main-knowledgeProperty"]//div[@id="nav-main-patentCount"]/span/text()'
		ip = self.content.xpath(ip)
		if ip:
			res["专利数量"] = ip[0]
		else:
			res["专利数量"] = "0" 
		
		return res

	def getHistory(self):
		res = {}
		return res

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

def helper():
	for line in sys.stdin:
		filename = line.strip() + ".html"
		path = os.path.join("companies", filename)
		print path

if __name__ == "__main__":

	f = open('companies/四川本立建筑工程有限公司大邑钢结构分公司.html', 'r')
	html = f.read()
	f.close()
	##content = etree.HTML(html)
	Content = HtmlContent(html)
	#profile = Content.getProfile()
	#print profile
	#market = Content.getMarketInfo()
	#print market
	#back = Content.getBackgrounds()
	#print back
	#legal = Content.getLegalRisk()
	#print legal
	#history = Content.getDevHistory()
	#print history
	#ip = Content.getIntellectualProperty()
	#print ip
	info = Content.info()
	print info
	#for line in sys.stdin:
	#	filename = line.strip() + ".html"
	#	path = os.path.join("companies", filename)

	#	with open(path, "r") as f:
	#		html = f.read()
	#		content = HtmlContent(html)
	#		try:
	#			#info = content.info()
	#			#print info
	#			print content.html
	#		except:
	#			print sys.stderr
	#			pass
	#helper()	
