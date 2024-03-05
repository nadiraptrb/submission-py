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

# Load the CSV file into a DataFrame
df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

st.header('Dicoding Collection Dashboard')

# Hitung rata-rata penggunaan sepeda berdasarkan musim
season_counts_day = df_day.groupby('season')['cnt'].mean()
season_counts_hour = df_hour.groupby('season')['cnt'].mean()

# Plot bar chart untuk menampilkan rata-rata penggunaan sepeda berdasarkan musim
plt.figure(figsize=(10, 6))
sns.barplot(x=season_counts_day.index, y=season_counts_day.values, color='darkblue')
plt.title('Average Bike Usage by Season (Day)')
plt.xlabel('Season')
plt.ylabel('Average Bike Usage (Day)')
fig_day = plt.gcf()  # Get the current figure
st.pyplot(fig_day)

plt.figure(figsize=(10, 6))
sns.barplot(x=season_counts_hour.index, y=season_counts_hour.values, color='darkblue')
plt.title('Average Bike Usage by Season (Hour)')
plt.xlabel('Season')
plt.ylabel('Average Bike Usage (Hour)')
fig_hour = plt.gcf()  # Get the current figure
st.pyplot(fig_hour)

