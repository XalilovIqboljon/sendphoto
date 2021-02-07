import requests
from pprint import pprint

token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def sendDice(idx):
    url = f'https://api.telegram.org/bot{token}/sendDice'
    
    payload ={
        'chat_id':idx,
        # 'emoji':emoji,
    }
    r=requests.post(url,params=payload)
    
    return r.json()


ids=1395234286
# emoji='🤟'
pprint(sendDice(ids))