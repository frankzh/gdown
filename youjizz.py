#!/usr/bin/env python
# -*- coding: utf-8 -*-

from browser import browser
import datetime
import time
import re

def youjizz_geturl(link, login=None, passwd=None):
	opera = browser()
	content = opera.get(link)
	link = re.search('so.addVariable\("file","(.+)"\);', content).group(1)
	return opera.get(link, log=False, stream=True)
