import requests
import pandas as pd
import datetime

def main():
    protocols_list = ['beefy', 'exactly', 'mountain-protocol', 'kleros', 'rsk-bridge', 'balmy', 'contango-v2', 'contango-v1']
    all_data = []

    for protocol in protocols_list:
        url = f"https://api.llama.fi/protocol/{protocol}"
        response = requests.get(url)
        data = response.json()

        for entry in data['tvl']:
            timestamp = entry['date']
            tvl = entry['totalLiquidityUSD']
            date = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')
            # Renombrar protocolos
            if protocol in ['contango-v1', 'contango-v2']:
                protocol = 'contango'
            all_data.append([timestamp, date, tvl, protocol])

    df = pd.DataFrame(all_data, columns=['timestamp', 'date', 'tvl', 'protocol'])

    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

    df.set_index(['date', 'protocol'], inplace=True)
    df.sort_index(inplace=True)

    # Eliminar índices duplicados manteniendo el último valor
    df = df[~df.index.duplicated(keep='last')]

    full_date_range = pd.date_range(start=df.index.get_level_values('date').min(), end=df.index.get_level_values('date').max())

    new_index = pd.MultiIndex.from_product([full_date_range, df.index.get_level_values('protocol').unique()], names=['date', 'protocol'])

    df = df.reindex(new_index)

    # Propagar hacia adelante los datos y llenar NaN con 0
    df['tvl'] = df.groupby('protocol')['tvl'].ffill().fillna(0)

    df.reset_index(inplace=True)

    # Eliminar la columna 'timestamp'
    df.drop(columns=['timestamp'], inplace=True)

    # df.to_csv('nombre_del_archivo.csv', index=False)

    return df

if __name__ == "__main__":
    df = main()
    print(df)