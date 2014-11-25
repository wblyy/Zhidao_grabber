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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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

for  url_index in xrange(85998341,0,-1):
	page_url='http://zhidao.baidu.com/question/'+str(url_index)
	related_IP=random.choice(proxy_dict)
	    req=requests.get(page_url,proxies={"http": related_IP})
        req.encoding='gbk'
        msg=req.text
	#msg.encoding ='utf-8'
        title=re.findall('<title>(.*?)</title>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
	content=re.findall('accuse="qContent">(.*?)</pre>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)#accuse="qContent">
	used=re.findall('<span class="answer-title h2 grid">(.*?)</span>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
	answerable=re.findall('id="answer-bar">(.*?)<i class="i-arrow-down">'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
	style=re.findall('<a class="f-aid" alog-alias="qb-class-info" href="(.*?)</a>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
	#<a class="f-aid" alog-alias="qb-class-info" href="  #</a>
	#id="answer-bar"> #<i class="i-arrow-down">
        print 'title:',title[0]
        if content:
                print 'content:',content[0]
        if used:
                print 'used:',used[0]
        if answerable:
        		print 'answerable',answerable[0]
        qid=url_index
        dbV2.insertdata(qid, title[0], content[0], style[0], used[0],answerable[0],related_IP)
                
	#print 'title:',title[0],'content:',content[0],'used:',used[0]
	#time.sleep(2)
	#<span class="answer-title h2 grid">




