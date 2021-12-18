import json
import requests

#metodo GET

if __name__ == '__main__':
    url = 'https://httpbin.org/cookies'
    cookies = {'my-cookie': 'true'}
    
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        cookies = response.cookies
        print(cookies)
        
        print("El contenido es: ")
        print(response.content)