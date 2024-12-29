import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "name":"test",
    "post":"post"
}
response = requests.post(url,json=data)

if response.status_code ==201:
    print(response.json)
else:
    print(response.status_code)