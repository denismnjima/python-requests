import requests

url = 'https://jsonplaceholder.typicode.com/todos'


try:

    response = requests.get(url)
    if response.status_code == 200:
        for i in response.json():
            print(i['title'])
    else:
        print(response.status_code)

except requests.exceptions.RequestException as e:
    print('request failed', e)