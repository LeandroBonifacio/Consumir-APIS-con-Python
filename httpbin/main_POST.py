import json
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'name': 'Eduardo', 'curso':'Python', 'nivel': 'intermedio'}

# si enviamos los parametros adentro de json internamente post se encarga de serializarlos
# si enviamos los parametros adentro de data nosotros nos tenemos que encargar de serializarlos 
    response = requests.get(url, data=json.dumps(payload))
    print(response.url)
    
    if response.status_code == 200:
        print(response.content)