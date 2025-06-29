import geopandas as gpd
import streamlit as st
import folium
from streamlit_folium import st_folium

# Display a basic map using Folium and Streamlit
def display_map(gdf):
    # Initialize a map centered on the US
    map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Add state boundaries to the map
    for _, row in gdf.iterrows():
        folium.GeoJson(
            row['geometry'],
            tooltip=row['NAME'],
            style_function=lambda x: {
                'fillColor': '#0080ff',
                'color': 'black',
                'weight': 2,
                'fillOpacity': 0.5
            }
        ).add_to(map)
    
    return map

# # Function to update map based on selected layers
# def update_map(selected_layers):
#     # Placeholder for layer logic (to be implemented)
#     st.write(f"Selected Layers: {selected_layers}")

# # Streamlit widgets for selecting layers
# education_level = st.checkbox("Education Level")
# age = st.checkbox("Age/Generational Cohort")
# income_level = st.checkbox("Income Level")

# selected_layers = []
# if education_level:
#     selected_layers.append("Education Level")
# if age:
#     selected_layers.append("Age/Generational Cohort")
# if income_level:
#     selected_layers.append("Income Level")

# # Update the map based on selected layers
# update_map(selected_layers)

# # Display the map
# folium_static(m)

# Main app execution
if __name__ == "__main__":
    # Load the GeoJSON file
    gdf = gpd.read_file('./data/boundaries/states.geojson')

    # Title and Introduction
    st.title("Demographic and Socioeconomic Mapping Tool (MVP)")
    st.write("This tool allows you to visualize demographic and socioeconomic data across the United States.")
    
    # Generate and display the map
    map = display_map(gdf)
    st_data = st_folium(map, width=725)
