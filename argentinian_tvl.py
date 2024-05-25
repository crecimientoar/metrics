import requests, pandas as pd, datetime, dotenv
from web3 import Web3
dotenv.load_dotenv()

protocols_list = ['exactly']
all_data = []

for protocol in protocols_list:
    url = f"https://api.llama.fi/protocol/{protocol}"
    response = requests.get(url)
    data = response.json()
    
    for entry in data['tvl']:
        timestamp = entry['date']
        tvl = entry['totalLiquidityUSD']
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')
        
        all_data.append([timestamp, date, tvl, protocol])

df = pd.DataFrame(all_data, columns=['timestamp', 'date', 'tvl', 'protocol'])

df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df.set_index('date', inplace=True) # date as index
full_date_range = pd.date_range(start=df.index.min(), end=df.index.max())
df = df.reindex(full_date_range, method='ffill')
df.reset_index(inplace=True) # index as a column
df.rename(columns={'index': 'date'}, inplace=True)
df['tvl'] = df['tvl'] / 1e6
df['tvl'] = df['tvl'].map('${:,.2f}M'.format)
df['date'] = df['date'].dt.strftime('%d/%m/%Y')

print(df)