import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    data_json = response.json()
    data_restaurant = {}
    for item in data_json:
        restaurant_name = item['Company']
else:
    print(f'O erro foi {response.status_code}')