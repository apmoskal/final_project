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
    st.write("Maize, a member of the grains and grasses category, thrives in both tropical and temperate climates. It is well-suited to regions with low rainfall, typically ranging from 1 to 25 mm per week, and requires moderate light exposure of about 6 to 8 hours daily. The optimal temperature for maize growth is around 22.5°C, which supports healthy development and yield. Maize is a versatile crop with a wide range of uses, including human food, animal feed, and industrial applications, making it a crucial component in global agriculture and food systems.")
elif selected_crop == "Potatoes":
    st.write("Potatoes are temperate-climate tuber crops that grow best under moderate environmental conditions. They require a weekly rainfall of about 25 to 50 mm and benefit from moderate light exposure of 6 to 8 hours per day. The optimal temperature for potato growth is around 17.5°C, which promotes healthy tuber development. Classified as a root crop, potatoes are primarily used for human food and also have significant industrial applications, making them a vital staple in many regions around the world.")
elif selected_crop == "Rice, paddy":
    st.write("Rice is a staple crop widely grown in tropical regions, where it thrives under high rainfall conditions of 50 to 100 mm per week. It requires moderate sunlight, typically 6 to 8 hours per day, and grows optimally at a temperature of 27.5°C. As a member of the grains and grasses category, rice plays a crucial role in global food security. Its primary use is for human consumption, serving as a dietary cornerstone for billions of people around the world.")
elif selected_crop == "Sorghum":
    st.write("Sorghum is a resilient crop that thrives in tropical and desert climates, making it well-suited for regions with challenging growing conditions. It requires high rainfall levels, typically between 50 to 100 mm per week, and moderate sunlight exposure of 6 to 8 hours daily. The optimal temperature for sorghum growth is around 28.5°C. Belonging to the grains and grasses category, sorghum serves multiple purposes—ranging from human food and animal feed to various industrial uses. Its adaptability and versatility make it a valuable crop in both subsistence and commercial agriculture.")
elif selected_crop == "Soybeans":
    st.write("Soybeans are a versatile legume crop well-suited to temperate climates, where they grow effectively under low rainfall conditions ranging from 1 to 25 mm per week. They require moderate light exposure of 6 to 8 hours per day and perform best at an optimal temperature of 25°C. As members of the legume family, soybeans are rich in protein and serve a wide range of purposes. Their uses include human food products such as tofu and soy milk, animal feed, and various industrial applications, making them a crucial component of both agriculture and the global economy.")
elif selected_crop == "Wheat":
    st.write("Wheat is a major crop that thrives in temperate and Mediterranean climates, where it benefits from high rainfall levels ranging from 50 to 100 mm per week. It requires moderate sunlight, about 6 to 8 hours daily, and grows best at an optimal temperature of 20°C. Classified under the grains and grasses category, wheat is one of the most widely cultivated and consumed crops globally. Its primary uses include human food—such as bread, pasta, and flour—animal feed, and a variety of industrial applications, making it a foundational element in global food systems and economies.")
elif selected_crop == "Cassava":
    st.write("Cassava is a robust tuber crop ideally suited to tropical climates, where it flourishes under high rainfall conditions of 50 to 100 mm per week. Unlike many other crops, cassava requires high light exposure, typically 10 to 12 hours of sunlight daily, and grows optimally at a temperature of 27°C. Classified among tubers and root crops, cassava is a vital source of carbohydrates and plays a key role in food security for millions of people in tropical regions. Its uses extend beyond human food to include animal feed and industrial applications, highlighting its versatility and economic importance in agriculture.")
elif selected_crop == "Sweet Potatoes":
    st.write("Sweet potatoes are nutrient-rich tuber crops that grow well in both tropical and temperate climates. They thrive under moderate rainfall conditions, typically receiving 25 to 50 mm of water per week, and require moderate sunlight exposure of 6 to 8 hours daily. The optimal temperature for sweet potato cultivation is around 23.5°C, which supports healthy root development. As members of the tubers and root crops category, sweet potatoes are primarily used for human consumption, valued for their high nutritional content and versatility in a wide range of traditional and modern dishes.")
elif selected_crop == "Plaintains and others":
    st.write("Plantains are starchy fruits that thrive in tropical climates, where they grow best under moderate rainfall levels of 25 to 50 mm per week. They require moderate sunlight, around 6 to 8 hours daily, and perform optimally at a temperature of 27.5°C. As a key crop in many tropical regions, plantains are classified as starchy fruits and are primarily used for human food. They serve as a staple in many diets, offering a rich source of carbohydrates and playing an important role in food security and culinary traditions around the world.")
