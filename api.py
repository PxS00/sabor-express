import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    data_json = response.json()
    data_restaurant = {}
    for item in data_json:
        restaurant_name = item['Company']
        if restaurant_name not in data_restaurant:
            data_restaurant[restaurant_name] = []
        
        data_restaurant[restaurant_name].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

print(data_restaurant['McDonald’s'])