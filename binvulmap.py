from model import globals
from model import args
from action.NmapSearch import Nmap
from action.DirSearch import Dirsearch, start

if __name__=='__main__':
    globals.init()
    globals.set_value('args',args.args())
    print(globals.get_value('args')['url'])
    start()
    print(globals.get_value('dir'))