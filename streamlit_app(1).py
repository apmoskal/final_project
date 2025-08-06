import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crops, Countries, and Cost of Living", layout="wide")

df = pd.read_csv('group_data.csv')

st.markdown("<h2 style='font-size:2rem; margin-bottom: 1rem;'>Crops, Countries, and Cost of Living 🌱</h2>", unsafe_allow_html=True)
st.image("crops-growing-in-thailand.jpg", width=600)

st.header("Basic Crop Information")

# Dropdown for crop selection
crops = [
    "Maize",
    "Potatoes",
    "Rice, paddy",
    "Sorghum",
    "Soybeans",
    "Wheat",
    "Cassava",
    "Sweet potatoes",
    "Plantains and others",
    "Yams"
]
selected_crop = st.selectbox("Select a crop:", crops)
st.write(f"You selected: {selected_crop}")
if selected_crop == "Maize, a member of the grains and grasses category, thrives in both tropical and temperate climates. It is well-suited to regions with low rainfall, typically ranging from 1 to 25 mm per week, and requires moderate light exposure of about 6 to 8 hours daily. The optimal temperature for maize growth is around 22.5°C, which supports healthy development and yield. Maize is a versatile crop with a wide range of uses, including human food, animal feed, and industrial applications, making it a crucial component in global agriculture and food systems.":
    st.write("Maize is a plant that thrives")
elif selected_crop == "Wheat":
    st.write("HELLO")
