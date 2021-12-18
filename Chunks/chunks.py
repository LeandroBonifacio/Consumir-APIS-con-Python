
import json
import requests


if __name__ == '__main__':
    url = 'https://assets.afcdn.com/story/20161017/989289_w378h270c1cx511cy250.jpg'

    response = requests.get(url, stream=True)#realiza la peticion sin descargar el contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content():#descarga el contenido poco a poco
            file.write(chunk)
        
    response.close();

        
        
