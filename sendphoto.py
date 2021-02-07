import requests
from pprint import pprint

token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def sendPhoto(ids):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload ={
        'chat_id':ids,
        'photo':'https://i.pinimg.com/564x/24/db/19/24db19c5a1a798e10bffc076e70313bb.jpg'
    }
    r=requests.get(url,params=payload)
    
    return r.json()


ids=1679454024
sendPhoto(ids)