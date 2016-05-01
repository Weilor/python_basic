import urllib2

req = urllib2.Request("http://www.baidu.com")
rep = urllib2.urlopen(req)
content = rep.read()
print content