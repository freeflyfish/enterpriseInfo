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
	"Cookie": "aliyungf_tc=AQAAAOdXlGrVrwUAveXdq1ATouOdQ714; csrfToken=Fm6IlH95wS65M6KiIVpwDt3p; jsid=SEM-BAIDU-CG-SY-001952; TYCID=7718cbb096b911e8878daf25e77eca07; undefined=7718cbb096b911e8878daf25e77eca07; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1533258360; ssuid=3479097461; _ga=GA1.2.934726892.1533258362; _gid=GA1.2.818450949.1533258362; RTYCID=d7e20bf5af5e42b18bf2509620e88270; token=de01ff16652145d8bc9f68eff92e1d01; _utm=d81e8ecc717b4cfb93c9fceac535929f; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzMzI1ODgwMCwiZXhwIjoxNTQ4ODEwODAwfQ.aQkBny7_XypBopn4ZwDWPoIpSdayFOd1J6hUSdPblSkKTNpePiYw8gMhbO-SePcMXX_Di_mU9eV9GWL9xBwsiw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218911313670%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzMzI1ODgwMCwiZXhwIjoxNTQ4ODEwODAwfQ.aQkBny7_XypBopn4ZwDWPoIpSdayFOd1J6hUSdPblSkKTNpePiYw8gMhbO-SePcMXX_Di_mU9eV9GWL9xBwsiw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1533259292",
	"Upgrade-Insecure-Requests" : "1", 
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
	}
	print company_real_url
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
	"Cookie": "aliyungf_tc=AQAAAOdXlGrVrwUAveXdq1ATouOdQ714; csrfToken=Fm6IlH95wS65M6KiIVpwDt3p; jsid=SEM-BAIDU-CG-SY-001952; TYCID=7718cbb096b911e8878daf25e77eca07; undefined=7718cbb096b911e8878daf25e77eca07; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1533258360; ssuid=3479097461; _ga=GA1.2.934726892.1533258362; _gid=GA1.2.818450949.1533258362; RTYCID=d7e20bf5af5e42b18bf2509620e88270; token=de01ff16652145d8bc9f68eff92e1d01; _utm=d81e8ecc717b4cfb93c9fceac535929f; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzMzI1ODgwMCwiZXhwIjoxNTQ4ODEwODAwfQ.aQkBny7_XypBopn4ZwDWPoIpSdayFOd1J6hUSdPblSkKTNpePiYw8gMhbO-SePcMXX_Di_mU9eV9GWL9xBwsiw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218911313670%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxMTMxMzY3MCIsImlhdCI6MTUzMzI1ODgwMCwiZXhwIjoxNTQ4ODEwODAwfQ.aQkBny7_XypBopn4ZwDWPoIpSdayFOd1J6hUSdPblSkKTNpePiYw8gMhbO-SePcMXX_Di_mU9eV9GWL9xBwsiw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1533259292",
	"Upgrade-Insecure-Requests" : "1", 
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
	}
	
	for page in tqdm(crawl_list):
		filename = page + ".html"
		key = {"key" : page}
		query = urllib.urlencode(key)
		full_url = origin_url + query
		html = loadPage(full_url, headers = headers)
		info = getCompanyInfo(html)
		savePage(info, filename)

def main():

	pagelist = genPagelist(sys.argv[1])

	crawlPage(pagelist)

if __name__ == "__main__":
	main()	
