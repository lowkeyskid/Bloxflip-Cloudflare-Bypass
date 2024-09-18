from classes.useragent import ua
from classes.requests  import requests

ua = ua()
requests = requests()

response = requests.get('https://api.bloxflip.com/user', headers={
    'User-Agent': ua.generate(),
    'Accept': 'application/json',
    'Connection': 'close',
    'X-Auth-Token': '' # users auth token, this is just a demo request
})

print(response.json())