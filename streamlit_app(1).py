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
if selected_crop == "Maize":
    st.write("Maize is a plant that thrives in 'Tropical/Temperate' conditions. Low (1-25 mm/week)	Moderate (6–8hrs)	22.5	Grains/Grasses	Human Food, Animal Feed, Industrial
")
elif selected_crop == "Wheat":
    st.write("HELLO")
