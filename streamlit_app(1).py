import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crops, Countries, and Cost of Living", layout="wide")

df = pd.read_csv('group_data.csv')

# Sidebar for page selection using radio buttons (always visible)
page = st.sidebar.radio("Select a page", ["Crop Info", "Country", "Yield by GDP"])

st.markdown("<h2 style='font-size:2rem; margin-bottom: 1rem;'>Crops, Countries, and Cost of Living 🌱</h2>", unsafe_allow_html=True)
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

    # Use 'country' and 'Year' columns from your CSV
    if 'country' in df.columns and 'Year' in df.columns and 'hg/ha_yield' in df.columns:
        country_options = sorted(df['country'].dropna().unique())
        selected_country = st.selectbox("Select Country", country_options)

        # Parse years to integers for slider
        df["Year"] = pd.to_datetime(df["Year"], errors='coerce')
        min_year = int(df["Year"].dt.year.min())
        max_year = int(df["Year"].dt.year.max())
        time_range = st.sidebar.slider(
            "Select Years",
                min_year,
                max_year,
                (min_year, max_year)
        )

        df['Year'] = df['Year'].dt.year

        # Filter data
        filtered = df[(df['country'] == selected_country) & (years == selected_year)]

        if not filtered.empty:
            st.subheader(f"Crop Yield in {selected_country} for {selected_year}")
            # Sum yields for each crop and sort descending
            yield_by_crop = filtered.groupby('Item')['hg/ha_yield'].sum().sort_values(ascending=False)
            st.bar_chart(yield_by_crop)
        else:
            st.info("No data available for the selected country and year.")
    else:
        st.info("Required columns are missing in the dataset.")
elif page == "Yield by GDP":
    st.header("Yield by GDP")
    st.write("Analyze crop yield by GDP per capita here (customize as needed).")
