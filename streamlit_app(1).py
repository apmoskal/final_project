import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crop Yield Impact Through Climate Change and Pesticides", layout="wide")

df = pd.read_csv('group_data.csv')

# Sidebar for page selection
page = st.sidebar.selectbox("Select a page", ["Crop Info", "Country", "Yield by GDP"])

st.markdown("<h2 style='font-size:2rem; margin-bottom: 1rem;'>Impact of Climate Change and Pesticide Use on Global Crop Yields 🌱</h2>", unsafe_allow_html=True)
st.image("crops-growing-in-thailand.jpg", width=600)

if page == "Crop Info":
    st.header("Basic Crop Information")
    if 'Item' in df.columns:
        st.dataframe(df[['Item']].drop_duplicates().reset_index(drop=True), use_container_width=True)
    else:
        st.info("No crop information available.")
elif page == "Country":
    st.header("Country")
    st.write("Select a country from the data for details (customize as needed).")
elif page == "Yield by GDP":
    st.header("Yield by GDP")
    st.write("Analyze crop yield by GDP per capita here (customize as needed).")
