import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('data/data.json')
pd.options.display.max_columns = None

#Source column added
#Datetime column added
df['_source'] = "https://lista.mercadolivre.com.br/notebook"
df['_datetime'] = datetime.now()


#Data treatment
df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')


#Ensuring it's a string
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace(r'[\(\)]', '', regex=True)


#Change type to float
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)

#Price as floats and total amount
#Set products price range 1000 < x < 5000
df = df[
    (df['old_money'] >= 1000) & (df['old_money'] <= 10000) &
    (df['new_money'] >= 1000) & (df['new_money'] <= 10000)
]

conn = sqlite3.connect('data/mercadolivre.db')
df.to_sql('laptop', conn, if_exists='replace', index=False)
conn.close()

