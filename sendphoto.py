import requests
from pprint import pprint

token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def sendPhoto(ids):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload ={
        'chat_id':ids,
        'photo':'AgACAgQAAxkDAAMQYB_WjPIennkmT1SxPc8oaFSooDkAAgGsMRt_XgRRWt0yqhJxhTskifkoXQADAQADAgADbQADLXQDAAEeBA',
        'caption':'TITLE'
    }
    r=requests.get(url,params=payload)
    
    return r.json()


ids=1395234286
pprint(sendPhoto(ids))