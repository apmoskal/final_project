import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crops, Countries, and Cost of Living", layout="wide")

df = pd.read_csv('group_data.csv')

st.markdown("<h2 style='font-size:2rem; margin-bottom: 1rem;'>Crops, Countries, and Cost of Living 🌱</h2>", unsafe_allow_html=True)
st.image("crops-growing-in-thailand.jpg", width=600)

st.header("Basic Crop Information")
