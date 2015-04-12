from debug import *
from zoodb import *
import rpclib

def getBalance(username):
    ## Fill in code here.
    with rpclib.client_connect('/bank_svc/sock') as c:
        ret = c.call('getBalance', username=username)
        return ret

def setBalance(username, newBalance):
    with rpclib.client_connect('/bank_svc/sock') as c:
        ret = c.call('setBalance', username=username, newZoobars=newBalance)
        return ret

def createBalance(username):
    with rpclib.client_connect('/bank_svc/sock') as c:
        ret = c.call('createBalance',username=username)
        return ret
