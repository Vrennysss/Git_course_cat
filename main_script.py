import requests
from yandex_token import ya_token

url_cat = 'https://cataas.com/cat/cute/says'
url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
upload_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
group = 'PYAPI-142'
def cat_says(say):
    response = requests.get(f'{url_cat}/{say}')
    params_c_f = {'path': f'{group}/{say}'}
    headers_c_f = {'Authorization': f'OAuth {ya_token}'}
    # headers_c_f = {'Authorization': 'Oauth y0__xDjkd4pGNuWAyDe8qqzFjCchs2uCJmSakTYFqB7rEsiIGBXt7ZbxbcN'}
    print(headers_c_f)

    response_c_f = requests.put(f'{url_ya}', headers=headers_c_f, params=params_c_f)
    print(response_c_f)

    params_s_f = {'path':f'{group}/{say}/{say}','url':f'{url_cat}/{say}'}
    print(params_s_f)
    response_save_file = requests.post(f'{upload_ya}', headers=headers_c_f, params=params_s_f)
    print(response_save_file)

cat_says('hello')

