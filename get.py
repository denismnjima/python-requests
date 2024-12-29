import requests

url = 'https://jsonplaceholder.typicode.com/todos'


response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("Error", response.status_code)