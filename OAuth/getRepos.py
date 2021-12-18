import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'
    
    headers = {'Authorization':'token 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'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()
        for proyect in payload:
            name = proyect['name']
            print(name)
    else:
        print(response.content)
