import streamlit as st
import pandas as pd
import sqlite3


conn = sqlite3.connect('data/mercadolivre.db')
df = pd.read_sql_query("Select * from laptop", conn)
conn.close()

#Dashboard definition
st.title('Marketing Analysis - Mercado Livre Laptops')
st.subheader('Main KPIS')
col1, col2, col3 = st.columns(3)

#Exploring KPI 1
items_amount = df.shape[0]
col1.metric(label="🖥️ Total de Notebooks", value=items_amount)

#Exploring KPI 2
common_brands = df['brand'].nunique()
col2.metric(label="🏷️ Common Brands", value=common_brands)

#Exploring KPI 3
average_br_currency = df['new_money'].mean()
col3.metric(label="💰 Average Price", value=f"{average_br_currency:.2f}")

#Brand Frequency
st.subheader('🏆 Related Frequency up to 10th page')
col1, col2 = st.columns([4, 2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

#Average Price per Brand
st.subheader('💵 Average price per brand')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_money'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_money'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

#Best reviews by brand
st.subheader('⭐ Brand best reviews')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)