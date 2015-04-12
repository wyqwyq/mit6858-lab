from zoodb import *
from debug import *
import bank_client
import auth_client
import time

def transfer(sender, recipient, zoobars, token):
    # persondb = person_setup()
    # bankdb = bank_setup()
    # senderp = bankdb.query(Bank).get(sender)
    # recipientp = bankdb.query(Bank).get(recipient)
    if token and not auth_client.check_token(sender, token):
        raise ValueError()

    sender_old_balance = bank_client.getBalance(sender)
    recipient_old_balance = bank_client.getBalance(recipient)
    if sender_old_balance is None or recipient_old_balance is None:
        raise ValueError("sender: "+ str(sender_old_balance) + "recipient: "+ str(recipient_old_balance))

    sender_balance = sender_old_balance - zoobars
    recipient_balance = recipient_old_balance  + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    bank_client.setBalance(sender, sender_balance)
    bank_client.setBalance(recipient, recipient_balance)

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    return bank_client.getBalance(username)

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

