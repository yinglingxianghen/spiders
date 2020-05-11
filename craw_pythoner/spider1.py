#coding=utf-8

#拿url，顺便拿拿数据什么的...

import urllib
import re



r = re.compile(r'href="(http://www\.cnpythoner\.com.+?)"')


def get_urls_from_contents(url):
	try:
		opener = urllib.urlopen(url)
		contents = opener.read()
		g = r.finditer(contents)
		opener.close()
		return g
	except:
		return []

def save_contents_from_url(url):
	opener = urllib.urlopen(url)
	contents = opener.read()
	opener.close()

	filename = url.replace("http://","")
	filename = filename.replace(".","_")
	filename = filename.replace("/","|")

	opene = open("/tmp/c/%s"%filename,"w")
	opene.write(contents)
	opene.close()
	return 

def get_and_save_url(url,data_cache,i):

	save_contents_from_url(url) #这里只加了一行

	urls =  get_urls_from_contents(url)
	for url in urls:
		url = url.groups()[0]
		if url not in data_cache :
			data_cache.append(url)
		else:
			continue
		i += 1
		get_and_save_url(url,data_cache,i)

data_cache = []
i = 0
get_and_save_url("http://www.cnpythoner.com/",data_cache,i)