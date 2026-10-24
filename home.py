import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import pydeck as pdk
import shapely

from joblib import load
from notebooks.src.config import DADOS_GEO_MEDIAN, DADOS_LIMPOS, MODELO_FINAL

@st.cache_data
def carregar_dados_limpos():
    return pd.read_parquet(DADOS_LIMPOS)

@st.cache_data
def carregar_dados_geo():

    return gpd.read_parquet(DADOS_GEO_MEDIAN)

@st.cache_data
def carregar_dados_geo():
    gdf_geo = gpd.read_parquet(DADOS_GEO_MEDIAN)

    # Explode MultiPolygons into individual polygons
    gdf_geo = gdf_geo.explode(ignore_index=True)

    # Function to check and fix invalid geometries
    def fix_and_orient_geometry(geometry):
        if not geometry.is_valid:
            geometry = geometry.buffer(0)  # Fix invalid geometry

        # Orient the polygon to be counter-clockwise if it's a Polygon or MultiPolygon
        if isinstance(
            geometry, (shapely.geometry.Polygon, shapely.geometry.MultiPolygon)
        ):
            geometry = shapely.geometry.polygon.orient(geometry, sign=1.0)

        return geometry

    # Apply the fix and orientation function to geometries
    gdf_geo["geometry"] = gdf_geo["geometry"].apply(fix_and_orient_geometry)


        # Extract polygon coordinates
    def get_polygon_coordinates(geometry):
        return (
            [[[x, y] for x, y in geometry.exterior.coords]]
            if isinstance(geometry, shapely.geometry.Polygon)
            else [
                [[x, y] for x, y in polygon.exterior.coords]
                for polygon in geometry.geoms
            ]
        )

    # Apply the coordinate conversion and store in a new column
    gdf_geo["geometry"] = gdf_geo["geometry"].apply(get_polygon_coordinates)

    return gdf_geo


@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)

df = carregar_dados_limpos()
dados_geo = carregar_dados_geo()
modelo = carregar_modelo()

st.title("Previsão de preços de imóveis")

condados = sorted(dados_geo["name"].unique())

coluna1, coluna2 = st.columns(2)

with coluna1:

    with st.form(key="formulario"):
        seleciona_condados = st.selectbox("Condado",condados)
        
        longitude = dados_geo.query("name == @seleciona_condados")["longitude"].values
        latitude = dados_geo.query("name == @seleciona_condados")["latitude"].values
        
        housing_median_age = st.number_input("Idade do imóvel", value=10)
        
        total_rooms = dados_geo.query("name == @seleciona_condados")["total_rooms"].values
        total_bedrooms = dados_geo.query("name == @seleciona_condados")["total_bedrooms"].values
        population = dados_geo.query("name == @seleciona_condados")["population"].values
        households = dados_geo.query("name == @seleciona_condados")["households"].values
        
        
        median_income = st.slider("Renda média (Em milhares de U$)", 5.0, 100.0, 45.0, 5.0)
        
        ocean_proximity = dados_geo.query("name == @seleciona_condados")['ocean_proximity'].values
    
        bins_income = [0,1.5,3,4.5,6, np.inf]
        median_income_cat = np.digitize(median_income/10, bins= bins_income)
    
    
    
    
        rooms_per_household = dados_geo.query("name == @seleciona_condados")["rooms_per_household"].values
        bedrooms_per_room = dados_geo.query("name == @seleciona_condados")["bedrooms_per_room"].values
        population_per_household = dados_geo.query("name == @seleciona_condados")["population_per_household"].values
        
            
        entrada_modelo = {
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income / 10,
            "ocean_proximity": ocean_proximity,
            "median_income_cat": median_income_cat,
            "rooms_per_household": rooms_per_household,
            "bedrooms_per_room": bedrooms_per_room,
            "population_per_household": population_per_household,
        }
        
        df_entrada_modelo = pd.DataFrame(entrada_modelo)
        
        botao_previsao = st.form_submit_button("Prever valor")
        
    if botao_previsao:
    
        valor = modelo.predict(df_entrada_modelo)
        st.metric(f"Preço previsto US$: ", value=f"{valor[0][0]:.2f}")

with coluna2:
    view_state = pdk.ViewState(
    latitude=float(latitude[0]),
    longitude=float(longitude[0]),
    zoom=5,
    min_zoom=5,
    max_zoom=15,
    )
    
    polygon_layer = pdk.Layer(
    "PolygonLayer",
    data=dados_geo[["name", "geometry"]],
    get_polygon="geometry",
    get_fill_color=[0, 0, 255, 100],
    get_line_color=[255, 255, 255],
    get_line_width=50,
    pickable=True,
    auto_highlight=True,
    )
    
    condado_selecionado = dados_geo.query("name == @seleciona_condados")
    
    highlight_layer = pdk.Layer(
    "PolygonLayer",
    data=condado_selecionado[["name", "geometry"]],
    get_polygon="geometry",
    get_fill_color=[255, 0, 0, 100],
    get_line_color=[0, 0, 0],
    get_line_width=500,
    pickable=True,
    auto_highlight=True,
    )
    
    tooltip = {
    "html": "<b>Condado:</b> {name}",
    "style": {"backgroundColor": "steelblue", "color": "white", "fontsize": "10px"},
    }
    
    mapa = pdk.Deck(
    initial_view_state=view_state,
    map_style="light",
    layers=[polygon_layer, highlight_layer],
    tooltip=tooltip,
    )
    
    st.pydeck_chart(mapa)



