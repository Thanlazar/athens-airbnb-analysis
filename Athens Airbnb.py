# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 13:04:16 2025

@author: thanl
"""
import pandas as pd

df= pd.read_csv(r"C:\Users\thanl\data\listings.csv")
df['price']=df['price'].str.replace('$','',regex=False).str.replace(',','',regex=False)
df['price']=pd.to_numeric(df['price'])

mean_price=df['price'].mean()
min_price=df['price'].min()
max_price=df['price'].max()
print(f"Ο μέσος όρος τιμών είναι: {mean_price} ευρώ,η μέγιστη τιμή είναι: {max_price} ευρώ,ενώ η ελάχιστη τιμή είναι: {min_price} ευρώ")
median_price=df['price'].median()
print(f"Η διάμεσος τιμών είναι: {median_price}")
unify_map = {'Athens, Αττική, Greece': 'Athens Center','Athina, 0, Greece': 'Athens Center','Athens, Acropolis, Greece': 'Acropolis, Athens, Greece', 
    'Αθηναίων, Αττική, Greece': 'ATHENS CENTER','Athens, 0, Greece': 'Athens Center',
    'Athens, ATTIKA, Greece': 'ATHENS CENTER',
    'Athens , Athens, Greece': 'ATHENS CENTER',
    'Athens, Attika, Greece': 'ATHENS CENTER',
    'Athina, Monastiraki, Greece': 'MONASTIRAKI,Athens,Greece',
    'Koukaki, athens, Greece': 'KOUKAKI,Athens, Greece',
    'Athens, Makrygianni, Greece': 'KOUKAKI/MAKRYGIANNI,Athens,Greece',
    'ΝΕΟ ΨΥΧΙΚΟ, ΑΤΤΙΚΗ, Greece': 'NEO PSYCHIKO,Athens,Greece',
    'Psichiko, Greece': 'NEO PSYCHIKO,Athens,Greece',
    'Filothei, Athens, Greece': 'FILOTHEI,Athens,Greece',
    'Kaisariani, Greece': 'KAISARIANI,Athens,Greece','Athina, Atiki, Greece':'Athens Center',
    'Αθηνα, Αττικης, Greece': 'ATHENS CENTER,Greece','Koukaki, Athens, Greece': 'Koukaki,Athens, Greece'}
df_normal=df[df['price']<=300]
df_normal['neighbourhood'] = df_normal['neighbourhood'].replace(unify_map).str.title()
#print(df_normal)
#print(f"Το αρχικό πλήθος:{len(df)}")
#print(f"Πλήθος μετά το φιλτράρισμα:{len(df_normal)}")
print(f"Νέα Μέση Τιμή:{df_normal['price'].mean()}")
neighborhood_stats = df_normal.groupby("neighbourhood")['price'].mean().sort_values(ascending=False)

neighbourhood_stats=df_normal.groupby("neighbourhood")['price'].mean().sort_values(ascending=False)
print(neighbourhood_stats.head(10))

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

neighbourhood_stats.head(10).plot(kind="bar")

plt.title("Top 10 Most Expensive Neighbourhoods in Athens (Avg Price < 300€)")
plt.xlabel("Neighbourhood")
plt.ylabel("Average Price (€)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("athens_airbnb_prices.png", dpi=300)

plt.show()

