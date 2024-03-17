import pprint

import requests
token = '6522302180:AAE1liTMwfnmBNhqy7ZAxjZgeL0iXoR-OFM'
main_url = f'https://api.telegram.org/bot{token}'
#url = f'{main_url}/getMe'
#result = requests.get(url)
#print(result.json())

url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())
messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id':chat_id,
        'text': 'Приветствую!'
    }
    result = requests.post(url, params=params)