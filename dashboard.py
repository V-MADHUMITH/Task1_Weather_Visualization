 
import streamlit as st
import pandas as pd
weather_data = [
    {"City": "London", "Temperature": 15, "Humidity": 80, "Weather": "Cloudy"},
    {"City": "New York", "Temperature": 22, "Humidity": 60, "Weather": "Sunny"},
    {"City": "Tokyo", "Temperature": 18, "Humidity": 75, "Weather": "Rainy"},
    {"City": "Paris", "Temperature": 16, "Humidity": 70, "Weather": "Cloudy"},
    {"City": "Mumbai", "Temperature": 30, "Humidity": 85, "Weather": "Humid"}
]

st.title("Weather Data Visualization 🌍")
df = pd.DataFrame(weather_data)
st.write("### Weather Data Table")
st.dataframe(df)
st.write("### Temperature Comparison")
st.bar_chart(df.set_index("City")["Temperature"])
st.write("### Humidity Comparison")
st.bar_chart(df.set_index("City")["Humidity"])
