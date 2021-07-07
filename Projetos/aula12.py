import requests

response = requests.get('httsp://viacep.com.br/ws/01001000/json/')
print(response.status_code)
