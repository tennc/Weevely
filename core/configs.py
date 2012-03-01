import os

dirpath = '~/.weevely/'
rcfile = 'weevelyrc'
historyfile = 'weevely_history'

class Configs:
    
    def __init__(self):
        
        self.dirpath = os.path.expanduser( dirpath )
        
        if not os.path.exists(self.dirpath):
            os.mkdir(self.dirpath)
            
        self.rc_commands = self.__load_rc()
        self.historyfile = self.__historyfile()
            
    def __load_rc(self):
        
        rcpath = self.dirpath + historyfile
        
        if not os.path.exists(rcpath):
            return []
        
        try:
            rcfile = open(rcpath, 'r')
        except Exception, e:
            print "[!] Error opening rc file."
        else:
            return [c for c in rcfile.read().split('\n') if c and c[0] != '#']

    def __historyfile(self):
        return self.dirpath + historyfile
            