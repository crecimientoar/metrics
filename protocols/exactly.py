import requests, csv
from datetime import datetime
from io import StringIO
import streamlit as st

dune_key = st.secrets["DUNE_API_KEY"]

headers = {"X-DUNE-API-KEY": dune_key}
# https://dune.com/exactly/exactly

##################
### Daily active users
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def daily_active_users():
    query_id = 1848503
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        item['day'] = datetime.strptime(item['day'], '%Y-%m-%d %H:%M:%S.%f UTC')

    data_list.sort(key=lambda x: x['day'])
    return data_list

##################
### Daily active users
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def total_users():
    query_id = 2180940
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        item['day'] = datetime.strptime(item['day'], '%Y-%m-%d %H:%M:%S.%f UTC')

    data_list.sort(key=lambda x: x['day'])

    # Obtener el último elemento de la lista ordenada
    last_entry = data_list[-1]

    # Extraer el valor de 'users' del último elemento
    latest_users_count = last_entry['users']
    return data_list #, latest_users_count

##################
### Daily active users
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def total_tx():
    query_id = 2260290
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        item['day'] = datetime.strptime(item['day'], '%Y-%m-%d %H:%M:%S.%f UTC')

    data_list.sort(key=lambda x: x['day'])
    return data_list

##################
### The total amount of tx
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def total_transactions():
    query_id = 2260433
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    poap_holders = data['result']['rows'][0]['tx']
    return poap_holders

##################
### Depositors at this moment
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def active_depositors():
    query_id = 2969689
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    poap_holders = data['result']['rows'][0]['users']
    return poap_holders

##################
### Borrowers at this moment
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def active_borrowers():
    query_id = 2974644
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    poap_holders = data['result']['rows'][0]['users']
    return poap_holders

##################
### Historic depositors
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def historic_depositors():
    query_id = 2983679
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        # Ajustar el formato aquí para coincidir con el de tus datos
        item['day'] = datetime.strptime(item['day'], '%Y-%m-%d %H:%M:%S')

    data_list.sort(key=lambda x: x['day'])
    return data_list

##################
### Historic borrowers
@st.cache_data(ttl=86400)  # Cache por 24 horas (86400 segundos)
def historic_borrowers():
    query_id = 2983449
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    csv_file = StringIO(response.text)

    reader = csv.DictReader(csv_file)
    data_list = list(reader)

    for item in data_list:
        # Ajustar el formato aquí para coincidir con el de tus datos
        item['day'] = datetime.strptime(item['day'], '%Y-%m-%d %H:%M:%S')

    data_list.sort(key=lambda x: x['day'])
    return data_list