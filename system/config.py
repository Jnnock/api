#encoding=utf-8

dsn = None
user = None
pwd = None
database = None
redisDsn = None
redisPort = None
redisPwd = None
apiLink = None
url = None

def getDatabaseDSN():
    global dsn
    if dsn == None:
        dsn = "127.0.0.1"
    return dsn

def getDatabaseUser():
    global user
    if user == None:
        user = "root"
    return user

def getDatabasePwd():
    global pwd
    if pwd == None:
        pwd = "1234"
    return pwd

def getDatabase():
    global database
    if database == None:
        database = "api_port"
    return database

def getRedisDsn():
    global redisDsn
    if redisDsn == None:
        redisDsn = "127.0.0.1"
    return redisDsn

def getRedisPort():
    global redisPort
    if redisPort == None:
        redisPort = "6379"
    return redisPort

def getRedisPwd():
    global redisPwd
    if redisPwd == None:
        redisPwd = None
    return redisPwd

def getApiLink():
    global apiLink
    if apiLink == None:
        apiLink = "http://crm.hechuangedu.com/"
    return apiLink

def getUrl():
    global url
    if url == None:
        url = 'http://api.com'
    return url
