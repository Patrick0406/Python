# !/usr/bin/python
# coding:utf-8
import urllib, urllib2, sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=d26b5ea5e8b5478a9efa105a5bd1c192 &client_secret=6df02a909eee471897dbbec9127da86e'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)