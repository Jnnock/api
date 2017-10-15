# encoding = utf-8

import MySQLdb,sys,config
reload(sys)
sys.setdefaultencoding('utf-8')

class selectDB():
    def __init__(self,table):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()
        self.table = table
        self.limit = ''
        self.mode = ''
        self.column = ''

    def limit(self,num):
        self.limit = num

    def setColumn(self,desc):
        self.column = desc

    def calcuate(self,desc):
        self.mode = desc

    def select(self,data):
        print self
        term = []
        for condition in data:
            term.append("%s%s%s"(condition,method,data[condition]))
        cond = ' and '.join(term)
        sql = "select %s from %s where %s"%(self.column,self.table,cond)
        print sql
