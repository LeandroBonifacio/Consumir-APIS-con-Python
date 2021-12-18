import json
import requests

#metodo GET

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args = { 'name': 'Eduardo', 'curso':'Python', 'nivel': 'intermedio'}
    headers = {'Content-Type': 'aplication/json'}

    response = requests.get(url, params=args, headers=headers)
    print(response.url)

    if response.status_code == 200:
        print(response.content)
        print(response.headers)
        
        
