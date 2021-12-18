import json
import requests

#metodo GET

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args = { 'name': 'Eduardo', 'curso':'Python', 'nivel': 'intermedio'}

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        '''
        response_json = response.json() #dict
        origin = response_json['origin']
        print(origin)
        '''
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
        
        
