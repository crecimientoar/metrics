import requests, csv
from datetime import datetime
from io import StringIO
import streamlit as st

dune_key = st.secrets["DUNE_API_KEY"]

headers = {"X-DUNE-API-KEY": dune_key}
# https://dune.com/KARTOD/decentraland-dashboard

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
### Holders y supply
def main_stats():
    query_id = 373477
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    combined_holders = data['result']['rows'][0]['combined_holders']
    combined_supply = data['result']['rows'][0]['combined_supply']
    return combined_holders, combined_supply

##################
### Volume and sales
def timeline_stats():
    query_id = 373489
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"

    response = requests.request("GET", url, headers=headers)
    # print(response.text)

    data = response.json()
    
    volume_7_days = data['result']['rows'][0]['Volume_7_Days']
    volume_all_time = data['result']['rows'][0]['Volume_All_Time']
    sales_7_days = data['result']['rows'][0]['Sales_7_Days']
    sales_all_time = data['result']['rows'][0]['Sales_All_Time']
    return volume_7_days, volume_all_time, sales_7_days, sales_all_time

##################
### Historic floors and volumes
def historic_floor_and_volumes():
    query_id = 373537
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