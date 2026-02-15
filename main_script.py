import requests
import json
import os
import time
from yandex_token import ya_token

url_cat = 'https://cataas.com/cat/cute/says'
url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
upload_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
group = 'Group_PYAPI-142'
headers_c_f = {'Authorization': f'OAuth {ya_token}'}

def up_json(say):
    params_upload_json = {
        'path':f'disk:/{say}/{say}.json',
        'overwrite':'true'
    }
    # print(params_upload_json)
    temp_link = requests.get(f'{upload_ya}', headers=headers_c_f, params=params_upload_json)
    href_link = temp_link.json()['href']

    if temp_link.status_code == 200:
        print('Ссылка для загрузки JSON получена')
    else:
        print(f'Ошибка: {temp_link.status_code}')


    with open('temp.json', 'rb') as f:
        response_upload_json = requests.put(href_link, data=f)
    if response_upload_json.status_code == 201:
        print('JSON загружен в папку с изображением')
    else:
        print(f'Ошибка: {response_upload_json.status_code}')

    try:
        os.remove('temp.json')
        print('Временный файл TEMP удален')
    except:
        print('Файл TEMP не найден')


def cat_says(say):
    response = requests.get(f'{url_cat}/{say}')

    if 300 > response.status_code >= 200:
        print(f'Кот говорит: {say} (ответ от API получен)')
    else:
        print(f'Кот молчит но в его взгляде читается: {response.status_code}')

    params_c_f = {'path': f'disk:/{say}'}
    headers_c_f = {'Authorization': f'OAuth {ya_token}'}
    # headers_c_f = {'Authorization': 'Oauth y0__xDjkd4pGNuWAyDe8qqzFjCchs2uCJmSakTYFqB7rEsiIGBXt7ZbxbcN'}
    # print(params_c_f)

    response_c_f = requests.put(f'{url_ya}', headers=headers_c_f, params=params_c_f)

    if response_c_f.status_code == 201:
        print('Ответ на запрос получен (папка создана)')
    elif response_c_f.status_code == 409:
        print('Ответ на запрос получен (папка уже существует)')
    else:
        print(f'Ошибка: {response_c_f.status_code}')

    # print(response_c_f.status_code)

    params_s_f = {'path':f'disk:/{say}/{say}','url':f'{url_cat}/{say}'}

    # print(params_s_f)

    response_save_file = requests.post(f'{upload_ya}', headers=headers_c_f, params=params_s_f)
    # print(response_save_file.status_code)
    while True:
        response_save_file.status_code == 202
        time.sleep(2)
        print('Загрузка...')
        break

    params_j_fs = {
        'path':f'disk:/{say}/{say}',
        'fields': ['size']
    }
    response_fs = (requests.get(f'{url_ya}', headers=headers_c_f, params=params_j_fs))

    if response_fs.status_code == 200:
        print(f'Размер сгенерированного изображения: {response_fs.json()['size']} байт')
    else:
        print(f'Ошибка получения JSON: {response_fs.status_code}')

    with open('temp.json', 'w', encoding='utf-8') as f:
        json.dump(response_fs.json(), f, ensure_ascii=True, indent=4)

    up_json(say)

say = str(input("Что скажет кот: "))
cat_says(say)
