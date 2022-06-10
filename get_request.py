import requests
import json


def get_info(url):
    #Codigo extra por si la request no existe (page not found)
    response = requests.get(url)
    status = response.status_code
    if status == 404:
        pass
    else:
        return json.loads(response.text)


if __name__ == '__main__':
    url = f'https://api.gael.cloud/general/public/sismos'
    print(get_info(url))