#coding=utf-8

#专门拿url什么的...

import urllib
import re



r = re.compile(r'href="(http://www\.cnpythoner\.com.+?)"')


def get_urls_from_url(url):
	try:
		opener = urllib.urlopen(url)
		contents = opener.read()
		g = r.finditer(contents)
		opener.close()
		return g
	except:
		return []



def get_url(url,data_cache,i):

	urls =  get_urls_from_url(url)
	for url in urls:
		url = url.groups()[0]
		if url not in data_cache :
			data_cache.append(url)
		else:
			continue
		i += 1
		print i
		print len(data_cache)
		print data_cache
		get_url(url,data_cache,i)

data_cache = []
i = 0
get_url("http://www.cnpythoner.com/",data_cache,i)


