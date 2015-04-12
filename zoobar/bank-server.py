#!/usr/bin/python
#
# Insert bank server code here.
#
import sys
from debug import *
from zoodb import *
import rpclib

class BankRpcServer(rpclib.RpcServer):
    def rpc_getBalance(self, username):
        db = bank_setup()
        balance = db.query(Bank).get(username)
        if balance:
            return balance.zoobars
        return None
    
    def rpc_setBalance(self, username, newZoobars):
        db = bank_setup()
        balance = db.query(Bank).get(username)
        if not balance:
            return None
        balance.zoobars = newZoobars
        db.add(balance)
        db.commit()
        return balance.zoobars        

    def rpc_createBalance(self, username):
        db = bank_setup()
        balance = db.query(Bank).get(username)
        if balance:
            return None 
        new_balance = Bank()
        new_balance.username = username
        new_balance.zoobars = 10
        db.add(new_balance)
        db.commit()
        return new_balance.zoobars

(_, dummy_zookld_fd, sockpath) = sys.argv
s = BankRpcServer()
s.run_sockpath_fork(sockpath)
