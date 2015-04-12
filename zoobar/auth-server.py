#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *
from zoodb import *
import hashlib
import random
import pbkdf2
import os
import struct
import bank_client

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def decode_salt(salt):
    return struct.pack('I', int(salt))

class AuthRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    def rpc_login(self, username, password):
        db = cred_setup()
        cred = db.query(Cred).get(username)
        if not cred:
            return None
        if cred.password == pbkdf2.PBKDF2(password, decode_salt(cred.salt)).hexread(32):
            return newtoken(db, cred)
        else:
            return None

    def rpc_register(self, username, password):
        db = person_setup()
        person = db.query(Person).get(username)
        if person:
            return None
        newperson = Person()
        newperson.username = username
        db.add(newperson)
        db.commit()
        db = cred_setup()
        newcred = Cred()
        newcred.username = username
        newcred.salt = str(struct.unpack('I',self.get_salt(4))[0])
        newcred.password = pbkdf2.PBKDF2(password, decode_salt(newcred.salt)).hexread(32)
        db.add(newcred)
        db.commit()
        if bank_client.createBalance(username) is None:
            return None
        return newtoken(db, newcred)
        
    def rpc_check_token(self, username, token):
        db = cred_setup()
        cred = db.query(Cred).get(username)
        if cred and cred.token == token:
            return True
        else:
            return False
    
    def get_salt(self, num_bytes):
        return os.urandom(num_bytes)
    
(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
