import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set visual style for seaborn
sns.set(style='dark')

# Page configuration
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Function corrections
def avg_bike_usage_by_weather(hour_df, weather_mapping):
    avg_bike_weather = hour_df.groupby('weathersit')['cnt'].mean().reset_index()
    avg_bike_weather['weather_condition'] = avg_bike_weather['weathersit'].map(weather_mapping)
    return avg_bike_weather

def avg_bike_usage_by_hour(hour_df):
    hourly_usage = hour_df.groupby(hour_df['todaysdate'].dt.hour)['cnt'].mean()
    return hourly_usage

# Read data
day_dataframe = pd.read_csv("newday_df.csv")
hour_dataframe = pd.read_csv("newhour_df.csv")

datetime_columns = ["todaysdate"]
hour_dataframe.sort_values(by="todaysdate", inplace=True)
hour_dataframe.reset_index(inplace=True)
 
for column in datetime_columns:
    hour_dataframe[column] = pd.to_datetime(hour_dataframe[column])

min_date = hour_dataframe["todaysdate"].min()
max_date = hour_dataframe["todaysdate"].max()



with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
 
main_df = hour_dataframe[(hour_dataframe["todaysdate"] >= str(start_date)) & 
                (hour_dataframe["todaysdate"] <= str(end_date))]


avg_bike_weather = avg_bike_usage_by_weather(main_df, weather_mapping={1: 'Clear', 2: 'Cloudy', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'})
hourly_usage = avg_bike_usage_by_hour(main_df)

st.header('Bike Sharing Dashboard')

calculate_sharing = hour_dataframe['cnt'].sum()
st.metric("Total Bike Sharing", f"{calculate_sharing:,}")


# Menghitung rata-rata penggunaan sepeda berdasarkan musim
season_counts = main_df.groupby('season')['cnt'].mean()

# Warna untuk setiap batang
colors = ['blue', 'green', 'orange', 'red']

# Membuat objek Figure
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat diagram batang dengan warna yang berbeda
ax.bar(season_counts.index, season_counts.values, color=colors)
ax.set_title('Average Bike Usage by Season (2011-2012)')
ax.set_xlabel('Season')
ax.set_ylabel('Average Bike Usage')

# Menampilkan plot Average Bike Usage by Hour of the Day menggunakan st.pyplot(fig)
st.pyplot(fig)

# Membuat objek Figure dan Axes
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat line plot
sns.lineplot(x=hourly_usage.index, y=hourly_usage.values, marker='o', ax=ax)

# Mengatur judul dan label
ax.set_title('Average Bike Usage by Hour of the Day')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Bike Usage')

# Menambahkan grid
ax.grid(True)

# Menampilkan plot di Streamlit menggunakan st.pyplot(fig)
st.pyplot(fig)

