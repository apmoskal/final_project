# Updated Streamlit App

import streamlit as st
import pandas as pd

# Sample DataFrame
# df = pd.DataFrame(...)  # Load your data here

year_min = 2000  # Example minimum year
year_max = 2023  # Example maximum year

# Replace the single year slider with a range slider
selected_year_range = st.slider("Select Year Range", year_min, year_max, (year_min, year_max))

# Update filtering to include all years in the selected range
filtered = df[(df['country'] == selected_country) & (years >= selected_year_range[0]) & (years <= selected_year_range[1])]

# Update chart and heading to reflect the selected year range
st.header(f"Data for years {selected_year_range[0]} to {selected_year_range[1]}")

# Your chart code here
