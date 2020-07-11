import requests
token = input('Token: ')
headers={
    'Authorization': f'{token}'
}
src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
try:
    if src.status_code == 200:
        print(f'Token Works! {token}')
    else:
        print(f'Invalid Token. {token}')
except Exception:
    print("Somethink goes wrong! (Probably discord shut down...)")    
