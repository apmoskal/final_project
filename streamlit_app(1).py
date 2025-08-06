import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crops, Countries, and Cost of Living", layout="wide")

df = pd.read_csv('group_data.csv')

st.markdown("<h2 style='font-size:2rem; margin-bottom: 1rem;'>Crops, Countries, and Cost of Living 🌱</h2>", unsafe_allow_html=True)
st.image("crops-growing-in-thailand.jpg", width=600)

st.header("Basic Crop Information")
columns_needed = ['Item', 'Plant Climate', 'Water Needs', 'Sunlight', 'Average Optimal Temp', 'Crop Type', 'Common Uses']
if all(col in df.columns for col in columns_needed):
    st.dataframe(df[columns_needed].drop_duplicates().reset_index(drop=True), use_container_width=True)
else:
    st.info("Some required columns are missing in the dataset.")
