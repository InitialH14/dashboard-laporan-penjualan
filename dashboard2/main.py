import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime
from babel.numbers import format_currency

sns.set(style='dark')

def create_mean_review_items_df(df):
    sum_order_items_df = df.groupby(by="product_category_name")['review_score'].mean().sort_values(ascending=True).reset_index()
    return sum_order_items_df

def create_total_buying_items_df(df):
    sum_order_items_df = df.groupby(by="product_category_name")['order_id'].nunique().sort_values(ascending=False).reset_index()
    return sum_order_items_df

all_df = pd.read_csv("/mount/src/dashboard-laporan-penjualan/dashboard2/all_data.csv")

min_date = datetime.strptime(all_df["shipping_limit_date"].min(), '%Y-%m-%d %H:%M:%S').date()
max_date = datetime.strptime(all_df["shipping_limit_date"].max(), '%Y-%m-%d %H:%M:%S').date()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("/mount/src/dashboard-laporan-penjualan/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df["product_category_name"]

# st.dataframe(main_df)

# # Menyiapkan berbagai dataframe
mean_review_df = create_mean_review_items_df(all_df)
total_buying_product_df = create_total_buying_items_df(all_df)


# plot number of daily orders (2021)
st.header('Laporan Data Penjualan E-Commerce:sparkles:')

st.subheader("Rata-rata Ulasan Tiap Produk")

fig, ax = plt.subplots(figsize=(20, 50))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="review_score",  
    y="product_category_name", 
    data=mean_review_df, 
    palette=colors, 
    ax=ax
)

ax.set_xlabel("Rata-rata Ulasan", fontsize=30)
ax.set_ylabel("Nama Produk", fontsize=30)
ax.set_title("Rata-rata Ulasan Tiap Produk", loc="center", fontsize=50, weight="bold")

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

plt.tight_layout()

st.pyplot(fig)


# customer demographic
st.subheader("Total Pembelian Tiap Produk")

fig, ax = plt.subplots(figsize=(20, 50))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="order_id", 
    y="product_category_name",
    data=total_buying_product_df,
    palette=colors,
    ax=ax
)

ax.set_xlabel("Total Pembelian", fontsize=30)
ax.set_ylabel("Nama Produk", fontsize=30)
ax.set_title("Total Pembelian Tiap Produk", loc="center", fontsize=50, weight="bold")

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

plt.tight_layout()

st.pyplot(fig)

st.caption('Copyright © Hadid 2024')
