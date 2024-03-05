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


