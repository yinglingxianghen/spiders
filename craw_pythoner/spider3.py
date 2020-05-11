#coding=utf-8

#拿url，顺便拿拿数据什么的...
#尼玛，看起来还是有点慢...
#传说中的多线程呢！！？？

import urllib
import re
import threading
import Queue


q = Queue.Queue()
mylock = threading.RLock()  


r = re.compile(r'href="(http://www\.cnpythoner\.com.+?)"')


urls = []

def save_contents_from_url(url,contents):

    filename = url.replace("http://","")
    filename = filename.replace(".","_")
    filename = filename.replace("/","|")

    opene = open("/tmp/c/%s"%filename,"w")
    opene.write(contents)
    opene.close()
    return 

def set_urls_from_contents(contents):
    g = r.finditer(contents)
    mylock.acquire()  
    for url in g :
        url = url.groups()[0]
        print url
        if url in urls:
            continue
        else:
            urls.append(url)
            q.put(url)
    mylock.release()  




def save_contents():
    while True:
        url = q.get()
        try:
            opener = urllib.urlopen(url)
            contents = opener.read()
            opener.close()
            set_urls_from_contents(contents)
            save_contents_from_url(url,contents)
        except:
            continue



#加个线程玩一玩
#多线程本质是并行
#并行是各自做自己的事
#a做a的事，b做b的事
#各做各的
#偶尔牵扯到数据共享，就很容易傻了



q.put("http://www.cnpythoner.com")

ts = []
for i in range(1,100):
    t = threading.Thread(target=save_contents)
    t.start()
    ts.append(t)

for t in ts:
    t.join()
    








