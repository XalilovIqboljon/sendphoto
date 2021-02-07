import requests
from pprint import pprint

token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def sendContact(idx,number,name):
    url = f'https://api.telegram.org/bot{token}/sendContact'
    
    payload ={
        'chat_id':idx,
        'phone_number':number,
        'first_name':name
    }
    r=requests.post(url,params=payload)
    
    return r.json()


ids=1395234286
number = 998994443776
name="Xalilov Iqboljon"
pprint(sendContact(ids,number,name))