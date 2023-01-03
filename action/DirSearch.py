import threading
import time
from threading import Thread
import re
import requests
from queue import Queue
import codecs
from concurrent.futures import ThreadPoolExecutor
import model.globals as globals
resulte=[]
class Dirsearch(threading.Thread):
    def __init__(self,queue,total):
        threading.Thread.__init__(self)
        self.header={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.0; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51'
        }
        self._queue = queue
        self._total = total
        self.count=10
    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            code = globals.get_value('args')['code']
            try:
                r = requests.get(url=url,headers=self.header,timeout=5)
                if r.status_code == code:
                    resulte.append(url)
                    print(url + "------>status:{0}".format(r.status_code))
            except:
                pass
    def check(self):
        if re.match("^http*[s]://.*/",self.url):
            pass
        else:
            self.url=self.url+'/'

def start():
        url=globals.get_value('args')['url']
        queue =Queue()
        with open('dicc.txt','r') as f:
            for i in f.readlines():
                queue.put(url+"/"+i.rstrip('\n'))
                total = queue.qsize()
                threads = []
                thread_count = int(10)
                for i in range(thread_count):
                    threads.append(Dirsearch(queue,total))
                for thread in threads:
                        thread.start()
                for thread in threads:
                    thread.join()
        globals.set_value('dir', resulte)
