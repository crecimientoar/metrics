import requests
from datetime import datetime
import csv
from io import StringIO
headers = {"X-DUNE-API-KEY": "d7Pw3Li6P9khAbqpZXGmVOOJ6AKN4XFx"}

# # Execution ID
# url = f"https://api.dune.com/api/v1/query/{query_id}/execute"

# response = requests.request("POST", url, headers=headers)

# print(response.text)

# the_response = response.text

# # State
# url = f"https://api.dune.com/api/v1/execution/{the_response}/status"

# response = requests.request("GET", url, headers=headers)

# print(response.text)

##################
### Poap Holders
query_id = 2448239
url = f"https://api.dune.com/api/v1/query/{query_id}/results"

response = requests.request("GET", url, headers=headers)
# print(response.text)

data = response.json()
poap_holders = data['result']['rows'][0]['poap_holders']
print(poap_holders)

##################
### Poap Collections
query_id = 2448223
url = f"https://api.dune.com/api/v1/query/{query_id}/results"

response = requests.request("GET", url, headers=headers)
# print(response.text)

data = response.json()
# print(data)
poap_collections = data['result']['rows'][0]['paop_collections']
print(poap_collections)

##################
### Poap Minted
query_id = 2448176
url = f"https://api.dune.com/api/v1/query/{query_id}/results"

response = requests.request("GET", url, headers=headers)
# print(response.text)

data = response.json()
# print(data)
poap_minted = data['result']['rows'][0]['poaps_minted']
print(poap_minted)

##################
### Poap Historic Minters
query_id = 2998884
url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
response = requests.request("GET", url, headers=headers)
# print(response.text)

csv_file = StringIO(response.text)

# Leer el CSV en una lista de diccionarios
reader = csv.DictReader(csv_file)
data_list = list(reader)

# Convertir la columna 'time' a datetime para poder ordenar
for item in data_list:
    item['time'] = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f UTC')

# Ordenar la lista por la fecha
data_list.sort(key=lambda x: x['time'])

# Mostrar resultados
# for item in data_list:
#     print(item['time'], item['minters'])

##################
### Poap Historic Minted
query_id = 2448201
url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
response = requests.request("GET", url, headers=headers)
# print(response.text)

csv_file = StringIO(response.text)

# Leer el CSV en una lista de diccionarios
reader = csv.DictReader(csv_file)
data_list = list(reader)

# Convertir la columna 'time' a datetime para poder ordenar
for item in data_list:
    item['time'] = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f UTC')

# Ordenar la lista por la fecha
data_list.sort(key=lambda x: x['time'])

# # Mostrar resultados
# for item in data_list:
#     print(item['time'], item['amount'])

##################
### Poap Historic Collections
query_id = 2448195
url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
response = requests.request("GET", url, headers=headers)
# print(response.text)

csv_file = StringIO(response.text)

# Leer el CSV en una lista de diccionarios
reader = csv.DictReader(csv_file)
data_list = list(reader)

# Convertir la columna 'time' a datetime para poder ordenar
for item in data_list:
    item['time'] = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f UTC')

# Ordenar la lista por la fecha
data_list.sort(key=lambda x: x['time'])

# # Mostrar resultados
# for item in data_list:
#     print(item['time'], item['amount'])