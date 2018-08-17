#!/usr/bin/env python
#coding=utf-8
# ******************************************************
# Author       : lyn1x
# Last modified: 2018-08-03 09:15
# Email        : liyingxuan@sck2data.com.cn
# Filename     : tianyancha.py
# Description  : copyright sichuankunlun reserved 2018!
# ******************************************************

import urllib
import urllib2
import re
import sys
import os
import time
from tqdm import *

headers = {

}

url = "https://www.tianyancha.com/company/953838482"



request = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(request)

#print(response.read())

def genPagelist(fin):
	"""
	fin: company name file, one company per line;	
	return : a list of companies;
	"""
	with open(fin, 'r') as f:
		pagelist = [ page.strip('\n') for page in f.readlines()]
	print("page list generated!")
	print("*" * 30)
	return pagelist

def savePage(html, filename):
	"""
	html : html file to be saved;
	filename : directory and filename to save the html files;
	"""
	if not os.path.exists("./companies"):
		os.mkdir("./companies")	
	else:
		pass

	with open("./companies/" + filename , 'w') as f:
		f.write(html)	
	


def loadPage(url, headers):
	"""
	url : web addresses of companies;
	headers : head of post;
	return : html file of websites;
	"""
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)

	return response.read()

def getCompanyInfo(html):
	
	pattern = re.compile('href="https://www.tianyancha.com/company/\d*"',re.S)
	page = pattern.search(html)
	company_real_url = page.group()[6:-1]
	headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.9",
	"Cache-Control" : "max-age=0",
	"Connectioni": "keep-alive",
	"Cookie": "aliyungf_tc=AQAAAOdXlGrVrwUAveXdq1ATouOdQ714; csrfToken=Fm6IlH95wS65M6KiIVpwDt3p; jsid=SEM-BAIDU-CG-SY-001952; TYCID=7718cbb096b911e8878daf25e77eca07; undefined=7718cbb096b911e8878daf25e77eca07; ssuid=3479097461; _ga=GA1.2.934726892.1533258362; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1533258360,1533696238,1533793210,1534432738; _gid=GA1.2.1057220902.1534432738; token=88e2e80c640542bbbaa7a5197e5825b1; _utm=ca34583a9a69403c958a710b4a070588; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzNDQzNDU3MywiZXhwIjoxNTQ5OTg2NTczfQ.7BktFYquNWU2XlpNqoAM6DEC8fWDusSnCvRFRmwqV66_6Qqb7EeV_ow0OZZefduAsz6d-ErnbyMwVrQv0rjldw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218911313670%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzNDQzNDU3MywiZXhwIjoxNTQ5OTg2NTczfQ.7BktFYquNWU2XlpNqoAM6DEC8fWDusSnCvRFRmwqV66_6Qqb7EeV_ow0OZZefduAsz6d-ErnbyMwVrQv0rjldw; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1534434576",
	"Upgrade-Insecure-Requests" : "1", 
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
	}
	#print company_real_url
	request = urllib2.Request(company_real_url, headers = headers)
	response = urllib2.urlopen(request)

	return response.read() 
	

def crawlPage(crawl_list):
	"""
	crawl_lsit: list, contains the companies we are going to get info;

	"""
	
	origin_url = "https://www.tianyancha.com/search?"
	headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.9",
	"Cache-Control" : "max-age=0",
	"Connectioni": "keep-alive",
	"Cookie": "aliyungf_tc=AQAAAOdXlGrVrwUAveXdq1ATouOdQ714; csrfToken=Fm6IlH95wS65M6KiIVpwDt3p; jsid=SEM-BAIDU-CG-SY-001952; TYCID=7718cbb096b911e8878daf25e77eca07; undefined=7718cbb096b911e8878daf25e77eca07; ssuid=3479097461; _ga=GA1.2.934726892.1533258362; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1533258360,1533696238,1533793210,1534432738; _gid=GA1.2.1057220902.1534432738; token=88e2e80c640542bbbaa7a5197e5825b1; _utm=ca34583a9a69403c958a710b4a070588; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzNDQzNDU3MywiZXhwIjoxNTQ5OTg2NTczfQ.7BktFYquNWU2XlpNqoAM6DEC8fWDusSnCvRFRmwqV66_6Qqb7EeV_ow0OZZefduAsz6d-ErnbyMwVrQv0rjldw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218911313670%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzNDQzNDU3MywiZXhwIjoxNTQ5OTg2NTczfQ.7BktFYquNWU2XlpNqoAM6DEC8fWDusSnCvRFRmwqV66_6Qqb7EeV_ow0OZZefduAsz6d-ErnbyMwVrQv0rjldw; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1534434576",
	"Upgrade-Insecure-Requests" : "1", 
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
	}
	
	cnt = 0
	for page in tqdm(crawl_list):
		cnt += 1
		if cnt % 10 == 0:	
			time.sleep(10)
		filename = page + ".html"
		key = {"key" : page}
		query = urllib.urlencode(key)
		full_url = origin_url + query
		#print full_url
		html = loadPage(full_url, headers = headers)
		try:
			info = getCompanyInfo(html)
			savePage(info, filename)
		except:
			pass



def main():

	pagelist = genPagelist(sys.argv[1])

	crawlPage(pagelist)

if __name__ == "__main__":
	main()	
