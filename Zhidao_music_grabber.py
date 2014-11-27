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
import logging
import time
logging.basicConfig(filename='zhidao_buzhidao.log',level=logging.DEBUG)


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

        

for  url_index in xrange(0,60000,20):
        try:
                is_answerable=0
                is_used=0
                content_data=''
                title_data=''
                style_data=''

        	page_url='http://wapiknow.baidu.com/browse/99?lm=2&pn='+str(url_index)+'&mzl=browse_pp_'+str(url_index)
        	related_IP=random.choice(proxy_dict)   
                req=requests.get(page_url,proxies={"http": related_IP})
                req.encoding='utf-8'
                msg=req.text
                questions=re.findall('/question/(.*?)</a>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
                for question in questions:
                        qid=question.split('.html')[0]
                        print qid
                        title_data=question.split('">')[1]
                        print  title_data                                   
                        content_data=''  
                        style_data='音乐'      
                        is_used=0
                        is_answerable=1
                        
                        
                        dbV2.insert_music_data(qid, title_data, content_data, style_data, is_used,is_answerable,related_IP)

        except Exception, e:
                systime=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
                logging.debug(e)             
                #print 'title:',title[0],'content:',content[0],'used:',used[0]
	#time.sleep(2)
	#<span class="answer-title h2 grid">




