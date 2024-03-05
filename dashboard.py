import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


# Page configuration
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded")
sns.set(style='dark')

df = pd.read_csv('day.csv')
df = pd.read_csv('hour.csv')
st.header('Dicoding Collection Dashboard')

# Hitung rata-rata penggunaan sepeda berdasarkan musim
season_counts = data_2011_2012.groupby('season')['cnt'].mean()

# Plot bar chart untuk menampilkan rata-rata penggunaan sepeda berdasarkan musim
plt.figure(figsize=(10, 6))
sns.barplot(x=season_counts.index, y=season_counts.values, color='darkblue')
plt.title('Average Bike Usage by Season (2011-2012)')
plt.xlabel('Season')
plt.ylabel('Average Bike Usage')
st.pyplot()

# Tampilkan jumlah pengguna sepeda di setiap musim
st.write("Spring Bike Usage:", spring_bike_usage)
st.write("Summer Bike Usage:", summer_bike_usage)
st.write("Fall Bike Usage:", fall_bike_usage)
st.write("Winter Bike Usage:", winter_bike_usage)

# Plot line chart untuk menampilkan rata-rata penggunaan sepeda berdasarkan jam hari
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_usage.index, y=hourly_usage.values, marker='o')
plt.title('Average Bike Usage by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Bike Usage')
plt.grid(True)
st.pyplot()

# Analisis Perbedaan Antara Jam Sibuk dan Jam Sepi
# Mengelompokkan data berdasarkan jam operasional harian (hour) dan menghitung rata-rata jumlah penyewaan sepeda (cnt)
# Kemudian membagi menjadi jam sibuk (misalnya, jam 7-10 pagi dan jam 4-7 sore) dan jam sepi (sisanya)
busy_hours = hourly_usage[(hourly_usage.index.isin(range(7, 11)) | hourly_usage.index.isin(range(16, 20)))].mean().mean()
non_busy_hours = hourly_usage[~((hourly_usage.index.isin(range(7, 11))) | (hourly_usage.index.isin(range(16, 20))))].mean().mean()

# Tampilkan perbedaan tingkat penggunaan sepeda antara jam sibuk dan jam sepi
st.write("Rata-rata Penggunaan Sepeda pada Jam Sibuk:", busy_hours)
st.write("Rata-rata Penggunaan Sepeda pada Jam Sepi:", non_busy_hours)
