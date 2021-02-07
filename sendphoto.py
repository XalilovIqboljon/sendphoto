import requests
from pprint import pprint

token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def sendPhoto(idx):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    photo=open('photo.jpg','rb')
    payload ={
        'chat_id':idx,
        # 'photo':'AgACAgQAAxkDAAMQYB_WjPIennkmT1SxPc8oaFSooDkAAgGsMRt_XgRRWt0yqhJxhTskifkoXQADAQADAgADbQADLXQDAAEeBA',
        'caption':"Oq ko'ylak"
    }
    r=requests.post(url,params=payload,files={'photo':photo})
    
    return r.json()


ids=1395234286
pprint(sendPhoto(ids))