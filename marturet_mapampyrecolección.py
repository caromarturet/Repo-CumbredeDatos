import folium
import pandas as pd
import json

# URL de los archivos CSV en línea
url_data1 = 'https://raw.githubusercontent.com/caromarturet/Repo-CumbredeDatos/main/Odata.xslm%20-%20Puntos%20Verdes.csv'
url_data2 = 'https://raw.githubusercontent.com/caromarturet/Repo-CumbredeDatos/main/Odata.xlsm%20-%20Recoleccion%20diferenciada.csv'

# Leer los datos del primer CSV desde la URL
data1 = pd.read_csv(url_data1)

# Leer los datos del segundo CSV desde la URL
data2 = pd.read_csv(url_data2)

# Crear un mapa de Folium
my_map = folium.Map(location=[-27.4698, -58.8304], zoom_start=13)

# Iterar los datos del primer CSV
for _, row in data1.iterrows():
    lat, lon = row['lat'], row['lng']
    folium.Marker(
        location=[lat, lon],
        tooltip=row['ubicacion'],
        icon=folium.Icon(color='green')  # En este caso es verde para Puntos Verdes
    ).add_to(my_map)

# Iterar los datos del segundo CSV
for _, row in data2.iterrows():
    coordinates = json.loads(row['st_asgeojson'])
    lat, lon = coordinates['coordinates'][0][0][1], coordinates['coordinates'][0][0][0]
    folium.Marker(
        location=[lat, lon],
        tooltip=row['nombre_barrio'],
        icon=folium.Icon(color='red')  # En este caso es rojo para Recolección Diferenciada
    ).add_to(my_map)

my_map.save('map.html')

my_map # Muestra el mapa