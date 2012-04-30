#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import re
from config import *

def geturl(link, login, passwd):
	opera = requests.session(headers=headers)
	values = { 'txtuser':login, 'txtpass':passwd, 'txtcheck':'login', 'txtlogin':'' }
	opera.post('http://netload.in/index.php', values)
	return opera.get(link).url	# return connection
	
def status(login, passwd):
	opera = requests.session(headers=headers)
	values = { 'txtuser':login, 'txtpass':passwd, 'txtcheck':'login', 'txtlogin':'Login' }
	opera.post('http://netload.in/index.php', values)
	content = opera.get('http://netload.in/index.php?id=15').content
	if 'This account was locked' in content or 'not found in our records!' in content or 'Invald Password' in content or 'Invalid User ID!' in content:
		return -1
	elif 'Sorry, please activate first your account.' in content:	# account not activated
		return time.time()
	elif 'Please wait a moment before tryingto log in again!' in content:	# ip blocked
		print 'ip blocked'
		asd
		return -2
	content = opera.get('http://netload.in/index.php?id=2').content
	if 'No Bonus' in content or 'Kein Premium' in content:
		return time.time()
	else:
		return time.time() + int(re.search('<div style="float: left; width: 150px; color: #FFFFFF;"><span style="color: green">([0-9]+) Tage?.+</span></div>', content).group(1))*60*60*24
	print content

def upload(login, passwd, filename):
	opera = requests.session(headers=headers)
	host = opera.get('http://api.netload.in/getserver.php').content
	content = opera.post(host, {'user_id':login, 'user_password':passwd, 'modus':'file_upload'}, files={'file':open(filename, 'rb')}).content
	return re.search('UPLOAD_OK;.+;[0-9]+;(.+);.+', content).group(1)
