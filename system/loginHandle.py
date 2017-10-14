#encoding=utf-8

import sys,config,dbHandle
reload(sys)
sys.setdefaultencoding('utf-8')

def authenticate(email,passwd):
    identityInfo = {
    'email':email,
    'passwd':passwd
    }
    staffSelect = dbHandle.selectDB('user_info')
    staffSelect.mode('=')
    staffSelect.mode('*')
    staffSelect.select(identityInfo)
