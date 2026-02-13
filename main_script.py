import requests
import json
from yandex_token import ya_token

url_cat = 'https://cataas.com/cat/cute/says'
url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
upload_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
group = 'PYAPI-142'
headers_c_f = {'Authorization': f'OAuth {ya_token}'}

def up_json(say):
    params_upload_json = {
        'path':f'{group}/{say}/{say}.json',
        'overwrite':'true'
    }
    print(params_upload_json)
    temp_link = requests.get(f'{upload_ya}', headers=headers_c_f, params=params_upload_json)
    href_link = temp_link.json()['href']
    print(href_link)
    with open('temp.json', 'rb') as f:
        response_upload_json = requests.put(href_link, data=f)




def cat_says(say):
    response = requests.get(f'{url_cat}/{say}')
    params_c_f = {'path': f'{group}/{say}'}
    # headers_c_f = {'Authorization': f'OAuth {ya_token}'}
    # headers_c_f = {'Authorization': 'Oauth y0__xDjkd4pGNuWAyDe8qqzFjCchs2uCJmSakTYFqB7rEsiIGBXt7ZbxbcN'}
    # print(headers_c_f)

    response_c_f = requests.put(f'{url_ya}', headers=headers_c_f, params=params_c_f)
    print(response_c_f)

    params_s_f = {'path':f'{group}/{say}/{say}','url':f'{url_cat}/{say}'}
    print(params_s_f)

    response_save_file = requests.post(f'{upload_ya}', headers=headers_c_f, params=params_s_f)
    print(response_save_file)

    params_j_fs = {
        'path':f'{group}/{say}/{say}',
        'fields': ['size']
    }
    response_fs = (requests.get(f'{url_ya}', headers=headers_c_f, params=params_j_fs))
    print(response_fs.json())

    with open('temp.json', 'w', encoding='utf-8') as f:
        json.dump(response_fs.json(), f, ensure_ascii=True, indent=4)

    up_json(say)

cat_says('hello')


