import requests, pandas as pd, datetime
from web3 import Web3
# dotenv.load_dotenv()
import pandas as pd
import numpy as np

protocols_list = ['beefy', 'exactly', 'mountain-protocol', 'kleros', 'rsk-bridge', 'balmy', 'contango-v2', 'contango-v1']
# protocols_list = ['rsk-bridge']
all_data = []

for protocol in protocols_list:
    url = f"https://api.llama.fi/protocol/{protocol}"
    response = requests.get(url)
    data = response.json()

    # Procesar cada entrada de datos y añadirla a all_data
    for entry in data['tvl']:
        timestamp = entry['date']
        tvl = entry['totalLiquidityUSD']
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')

        all_data.append([timestamp, date, tvl, protocol])

# Crear un DataFrame con los datos recopilados
df = pd.DataFrame(all_data, columns=['timestamp', 'date', 'tvl', 'protocol'])

# Convertir 'date' a tipo datetime para manipulación de fechas
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Establecer un índice múltiple con 'date' y 'protocol'
df.set_index(['date', 'protocol'], inplace=True)
df.sort_index(inplace=True)

# Crear un rango completo de fechas
full_date_range = pd.date_range(start=df.index.get_level_values('date').min(), end=df.index.get_level_values('date').max())

# Crear un nuevo MultiIndex que incluya todas las combinaciones de fechas y protocolos
new_index = pd.MultiIndex.from_product([full_date_range, df.index.get_level_values('protocol').unique()], names=['date', 'protocol'])

# Reindexar con método 'ffill' para propagar hacia adelante los datos
df = df.reindex(new_index, method='ffill')

# Restablecer el índice para volver a tener 'date' y 'protocol' como columnas
df.reset_index(inplace=True)

# Formatear la columna 'tvl' dividiendo por 1 millón y formateando como cadena de texto
df['tvl'] = df['tvl'] / 1e6
df['tvl'] = df['tvl'].map('${:,.2f}M'.format)

# Convertir la fecha de vuelta a formato día/mes/año
df['date'] = df['date'].dt.strftime('%d/%m/%Y')

# Imprimir el DataFrame resultante
print(df)