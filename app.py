import streamlit as st
from streamlit_folium import folium_static
import folium

# Title and Introduction
st.title("Demographic and Socioeconomic Mapping Tool (MVP)")
st.write("This tool allows you to visualize demographic and socioeconomic data across the United States.")

# Initialize a map centered on the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Function to update map based on selected layers
def update_map(selected_layers):
    # Placeholder for layer logic (to be implemented)
    st.write(f"Selected Layers: {selected_layers}")

# Streamlit widgets for selecting layers
education_level = st.checkbox("Education Level")
age = st.checkbox("Age/Generational Cohort")
income_level = st.checkbox("Income Level")

selected_layers = []
if education_level:
    selected_layers.append("Education Level")
if age:
    selected_layers.append("Age/Generational Cohort")
if income_level:
    selected_layers.append("Income Level")

# Update the map based on selected layers
update_map(selected_layers)

# Display the map
folium_static(m)
