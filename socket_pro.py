import urllib2
import urllib


url = 'http://www.baidu.com/cgi-bin/register.cgi'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'WHY',
          'location' : 'SDU',
          'language' : 'Python' }

headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()