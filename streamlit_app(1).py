import streamlit as st
from PIL import Image
import os
import pandas as pd
import altair as alt
import numpy as np
import pydeck as pdk

# Set page config at the top (must be before any Streamlit component)
st.set_page_config(page_title="Crop Yield Impact Through Climate Change and Pesticides", layout="wide")

# read in data
df = pd.read_csv('group_data.csv')

st.title("Impact of Climate Change and Pesticide Use on Global Crop Yields 🌱")

# Filters on Sidebar
st.sidebar.header("Filters")  # Move filters to the sidebar

# Slider: Filter by Year
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

# Selectbox: Filter by Country
country_options = ["All"] + sorted(df["country"].dropna().unique())
country = st.sidebar.selectbox("Filter by Country", options=country_options)

# Filter the DataFrame based on selected country and year range
if country == "All":
    filtered_df = df[df["Year"].between(*time_range)]
else:
    filtered_df = df[(df["country"] == country) & (df["Year"].between(*time_range))]

x_axis_options = ['pesticides_tonnes', 'avg_temp', 'GDP_per_capita_clean', 'food_supply']
x_axis_choice = st.selectbox("Select Variable", options=x_axis_options)

x_axis_title = {
    'pesticides_tonnes': 'Pesticides (tonnes)',
    'avg_temp': 'Avg Temp (°C)',
    'GDP_per_capita_clean': 'GDP per Capita',
    'food_supply': 'Food Supply'
}.get(x_axis_choice, x_axis_choice)

selection = alt.selection_point(
    fields=['country'],
    empty='all',
    bind='legend',
    on='click'
)

# Scatter plot with legend
scatter = alt.Chart(filtered_df).mark_circle().encode(
    x=alt.X(f'{x_axis_choice}:Q', title=x_axis_title),
    y=alt.Y('hg/ha_yield:Q', title='Yield (hg/ha)'),
    color=alt.condition(
        selection,
        alt.Color('country:N', legend=alt.Legend(title="Country", columns=3)),
        alt.value('lightgray')),
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    tooltip=['country:N', f'{x_axis_choice}:Q', 'hg/ha_yield:Q', 'Item:N', 'food_supply:Q']
).add_params(
    selection
).properties(
    width=500,
    height=400
).interactive()

# Box plot that responds to selection
boxplot = alt.Chart(filtered_df).mark_boxplot().encode(
    x=alt.X('Item:N', title='Crop', axis=alt.Axis(labelAngle=-45)),
    y=alt.Y(f'{x_axis_choice}:Q', title=x_axis_title)
).transform_filter(
    selection
).properties(
    width=500,
    height=400
)

# Line chart: Yield over time by Crop (filtered by country selection)
line_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x=alt.X('Year:O', title='Year'),
    y=alt.Y('sum(hg/ha_yield):Q', title='Total Yield (hg/ha)'),
    color=alt.Color('Item:N', title='Crop'),
    tooltip=['Year:O', 'Item:N', 'hg/ha_yield:Q', 'country:N']
).transform_filter(
    selection
).properties(
    width=1000,
    height=400,
    title='Crop Yield Over Time by Crop (Filtered by Country)'
).interactive()

# Arrange plots: scatter above, boxplot next to it, and line chart below both
top_row = scatter & boxplot
final_chart = alt.vconcat(
    top_row,
    line_chart
).properties(
    title='Interactive Exploration of Crop Yield'
).configure_view(
    strokeWidth=0
).configure_legend(
    labelFontSize=12,
    titleFontSize=13
).resolve_scale(color='independent')

st.altair_chart(final_chart, use_container_width=True)
