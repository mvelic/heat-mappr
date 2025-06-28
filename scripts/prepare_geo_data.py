import geopandas as gpd
import os

def prepare_geographic_data(output_dir="data/boundaries"):
    """
    Fetches US state TIGER/Line shapefile, processes it, and saves it as a 
    GeoJSON file.

    The processing steps include:
    1. Filtering out territories to keep only the 50 states and DC.
    2. Selecting only the necessary columns for the application.
    3. Simplifying the geometry to reduce file size for better performance.
    """
    # URL for the 2024 US States TIGER/Line Shapefile
    # Note: The Census Bureau updates these URLs annually.
    raw_file = "./data/raw/tl_2024_us_state.zip"
    
    # print(f"Fetching state boundaries from: {url}")
    print(f"Fetching state boundaries from: {raw_file}")
    
    try:
        # Read the shapefile directly from the zipped URL
        gdf = gpd.read_file(raw_file)
    except Exception as e:
        print(f"Error fetching or reading the shapefile: {e}")
        return

    print("Filtering for the 50 states and DC...")
    # The 'STATEFP' column is the state FIPS code. Codes <= 56 are states/DC.
    # Territories like Puerto Rico (72), Guam (66), etc., have higher codes.
    # We convert to int for robust numerical comparison.
    gdf_states = gdf[gdf['STATEFP'].astype(int) <= 56].copy()

    print("Selecting relevant columns...")
    # Keep only columns needed for mapping and data joining
    columns_to_keep = ['STATEFP', 'STUSPS', 'NAME', 'geometry']
    gdf_states = gdf_states[columns_to_keep]

    print("Simplifying geometries for performance...")
    # Simplify geometry to reduce file size. The tolerance is in degrees.
    # A small tolerance like 0.005 provides a good balance of detail and size.
    # Note the use of `.copy()` to avoid SettingWithCopyWarning
    gdf_states['geometry'] = gdf_states.geometry.simplify(tolerance=0.005).copy()

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "states.geojson")
    print(f"Saving processed data to '{output_path}'...")
    
    # Save the final GeoDataFrame to a GeoJSON file
    gdf_states.to_file(output_path, driver='GeoJSON')

    print("Geographic data preparation complete.")

if __name__ == "__main__":
    prepare_geographic_data()