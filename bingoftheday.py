#!/usr/bin/python

import urllib2, json
from os.path import expanduser
import os

req = urllib2.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
res = json.load(req)
urlbase = (res['images'][0]['urlbase'])
name = (res['images'][0]['fullstartdate'])
url = 'http://www.bing.com'+ urlbase + '_1920x1080.jpg'
home = expanduser('~')
basepath = home + '/Pictures/bing-wallpapers/'
path = basepath + name + '.jpg'
if not os.path.exists(basepath):
    os.mkdir(basepath)

print("Downloading %s to %s" % (url, path))
with open(path, 'w') as f:
    pic = urllib2.urlopen(url)
    f.write(pic.read())
