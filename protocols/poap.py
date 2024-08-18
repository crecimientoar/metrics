import requests, csv
from datetime import datetime
from io import StringIO
import streamlit as st

dune_key = st.secrets["DUNE_API_KEY"]

headers = {"X-DUNE-API-KEY": dune_key}
# https://dune.com/hildobby/poap

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
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def poap_holders():
    query_id = 2448239
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    poap_holders = data['result']['rows'][0]['poap_holders']
    return poap_holders

##################
### Poap Collections
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def poap_collections():
    query_id = 2448223
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    
    poap_collections = data['result']['rows'][0]['paop_collections']
    return poap_collections
    

##################
### Poap Minted
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def poap_minted():
    query_id = 2448176
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    
    poap_minted = data['result']['rows'][0]['poaps_minted']
    return poap_minted
    # print(poap_minted)

##################
### Poap Historic Minters
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def poap_historic_minters():
    query_id = 2998884
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        item['time'] = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f UTC')

    data_list.sort(key=lambda x: x['time'])
    return data_list

# Mostrar resultados
# for item in data_list:
#     print(item['time'], item['minters'])

##################
### Poap Historic Minted
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def poap_historic_minted():
    query_id = 2448201
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        item['time'] = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f UTC')

    data_list.sort(key=lambda x: x['time'])
    return data_list

# # Mostrar resultados
# for item in data_list:
#     print(item['time'], item['amount'])

##################
### Poap Historic Collections
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def poap_historic_collections():
    query_id = 2448195
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        item['time'] = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f UTC')

    data_list.sort(key=lambda x: x['time'])
    return data_list

# # Mostrar resultados
# for item in data_list:
#     print(item['time'], item['amount'])