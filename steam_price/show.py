import webbrowser
import pandas as pd
import requests
import time

df10 = pd.read_csv('data.csv')


df = df10.sort_values(by=['Price'], ascending=False)

wallet = int(input())
con_rate = 73.6
wallet_in_dollars = wallet/con_rate

df['Name'] = df[df['Price'] < wallet_in_dollars]['Name']
df = df.dropna()
df1 = df.head(15)
# print(df1)
name = list(df1['Name'])
# print(name)
for i in name:
	link = 'https://steamcommunity.com/market/listings/730/'+i
	webbrowser.open(link, new=2)
	time.sleep(1)
