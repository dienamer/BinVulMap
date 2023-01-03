import nmap
import re
import model.globals as globals
class Nmap:
    nm= nmap.PortScanner()
    result={}
    def __init__(self):

        self.model = globals.get_value('args')['nmap_model']
        self.host = globals.get_value('args')['host']
        print(self.host)
    def allScanner(self):
        args="-A"
        tmp={}
        self.nm.scan(hosts=self.host,arguments=args)
        for port in self.nm[self.host]['tcp']:
            tmp[port]=self.nm[self.host]['tcp'][port]
        self.result['port']=tmp
    def vulScanner(self):
        args="--script=vuln"
        self.nm.scan(hosts=self.host,arguments=args)
        self.result['vul'] = ''
        str_tmp=''
        for port in self.nm[self.host]['tcp']:
            key = dict()
            key = self.nm[self.host]['tcp'][port]
            key = dict(key)
            if 'script' in key.keys():
                script_key = dict(key['script']).keys()
                for key_tmp in script_key:
                    str_tmp = str_tmp + key['script'][key_tmp]
        self.result['vul']=str_tmp
    def sysScanner(self):
        pass
    def run(self):
        if self.model == 'all':
            self.allScanner()
        elif self.model == 'vul':
            self.vulScanner()
        globals.set_value('nmap',self.result)

