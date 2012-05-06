#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
import time
import re
import os
from config import *

def getApikey(login, passwd):
	opera = requests.session(headers=headers)
	return re.search('<content type="text">(.+)</content>', opera.post('http://api.crocko.com/apikeys', {'login':login, 'password':passwd}).content).group(1)

def status(login, passwd):
	# get apikey
	apikey = getApikey(login, passwd)
	opera = requests.session(headers=headers)
	content = opera.get('http://api.crocko.com/account', headers={'Authorization':apikey}).content
	premium_end = re.search('<ed:premium_end>(.*?)</ed:premium_end>', content).group(1)
	if not premium_end:
		return 0
	else:
		return premium_end	# convert to timestamp

def upload(login, passwd, filename):
	# get apikey
	apikey = getApikey(login, passwd)
	opera = requests.session(headers=headers)
	content = opera.post('http://api.crocko.com/files', headers={'Authorization':apikey}, files={'file':open(filename, 'rb')}).content	# upload
	return re.search('<link title="download_link" href="(.+)"', content).group(1)
	