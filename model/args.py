import optparse

def args():
    parse=optparse.OptionParser("input -h to show the options")
    parse.add_option('-u',dest='url',type="string",help='target url')
    parse.add_option('--url', dest='url', type="string", help='target url')
    parse.add_option('--host', dest='host', type="string", help='target host')
    parse.add_option('-m', dest='model', type="string", help='model')
    parse.add_option('--nm',dest='nmap_model',action='store',default='all',type='string',help='The nmap search model')
    parse.add_option('--code',dest='http_code',type="int",help="Tht HTTP code")
    (options, args) = parse.parse_args()
    tmp={}
    tmp['nmap_model']=options.nmap_model
    tmp['url']=options.url
    tmp['model']=options.model
    tmp['host']=options.host
    tmp['code']=options.http_code
    return tmp


