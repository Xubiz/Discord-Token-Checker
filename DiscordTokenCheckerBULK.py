import requests
import time

with open('tokens.txt', 'r') as f:
    for line in f:
        time.sleep(1)
        token = line.rstrip("\n")
        headers = {
            'Authorization': f'{token}'  
        }
        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

        try:
            if src.status_code == 200:
                print('Token Works! >' + token)
            else:
                print('Invalid Token. >' + token)
        except Exception:
            print("Yeah we can't contact discordapp.com")
print('end')
