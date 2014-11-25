 # encoding: UTF-8
import ConfigParser
import re
import urllib2
import urllib
import time
from mydbV2 import MydbV2
from random import choice
import random
import requests
from IPdb import IPdb

dbV2 = MydbV2()
myIPdb=IPdb()
proxy_dict=['http://113.11.198.163:2223/',
			#r'http://113.11.198.164:2223/',
			#r'http://113.11.198.165:2223/',
			#r'http://113.11.198.166:2223/',
			'http://113.11.198.167:2223/',
			'http://113.11.198.168:2223/',
			'http://113.11.198.169:2223/',
			]

for  url_index in xrange(919637438114007139,0,-1):
	page_url='http://zhidao.baidu.com/question/'+str(url_index)
	msg=requests.get(page_url,proxies={"http": random.choice(proxy_dict)}).text
	title=re.findall('<title>(.*?)</title>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
	content=re.findall('accuse="qContent">(.*?)</pre>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)#accuse="qContent">
	used=re.findall('<span class="answer-title h2 grid">(.*?)</span>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
	print 'title:',title[0].decode('utf-8'),'content:',content[0].decode('utf-8'),'used:',used[0].decode('utf-8')
	#time.sleep(2)
	#<span class="answer-title h2 grid">




