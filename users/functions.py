import datetime
import random

def  get_payment_id(item):

    ctime = datetime.datetime.now()
    mtime = str(ctime.today())
    newtime = ''.join(ch for ch in mtime if ch.isalnum())
    year = newtime[0:4]
    month_day = newtime[5:14]
   
    my_id = f'{item}-{year}-{str(month_day)}'
  
    return my_id

def get_album_cent(amount):
    percent = 0.7
    try:
        amount = float(amount)
        price = amount* percent
        return price
    except:
        return None

def get_event_cent(amount):
    percent = 0.7
    try:
        amount = float(amount)
        price = amount* percent
        return price
    except:
        return None


def  get_event_code():

    ctime = datetime.datetime.now()
    mtime = str(ctime.today())
    newtime = ''.join(ch for ch in mtime if ch.isalnum())
    year = newtime[0:4]
    month_day = newtime[5:14]
   
    my_id = f'{year}{str(month_day)}'
  
    return my_id
