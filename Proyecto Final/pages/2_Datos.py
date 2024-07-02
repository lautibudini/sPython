import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
from pathlib import Path
import folium 
from streamlit_folium import st_folium 
from folium.plugins import MarkerCluster

tematica = st.selectbox('Selecciona un gráfico : ', ['Tipos de Lagos 🌊', 'Lagos por Provincia 🗺️', 'Mapa de Lagos en Argentina 🌐', 'Tipos de Aeropuertos 🛬', 'Aeropuertos por provincia ✈️', 'Mapa de Aeropuertos en Argentina 🗺️'])

match tematica:
    case 'Tipos de Lagos 🌊':
        # leo el dataset de lagos 
        ruta_lagos = Path('custom_dataset', 'lagos_arg.csv')
        lagos = pd.read_csv(ruta_lagos)

        # Acá me devuelve una serie donde están los tipos de lagos que hay y cuantas veces aparecen en la columna sup tamaño
        labels = lagos['sup tamaño'].value_counts()
        # Pongo otros colores a elección, ya que vienen otros por defecto
        colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
        
        # Creo el gráfico de torta
        fig, ax = plt.subplots()
        ax.pie(labels, labels=labels.index, autopct='%1.1f%%', colors=colors)
        ax.set_title('Porcentaje de tipos de lagos')

        # Muestro el gráfico
        st.write('Gráfico donde se muestran los tipos de lagos en Argentina y su porcentaje , clasificados según su superficie.')
        st.write('📍 Lago chico: Cuenta con una superficie menor o igual a 17km²')
        st.write('📍 Lago medio: Cuenta con una superficie mayor a 17km² y menor o igual a 59km²')
        st.write('📍 Lago grande: Cuenta con una superficie mayor a 59km²')
        st.pyplot(fig)

    case 'Tipos de Aeropuertos 🛬':
        # leo el dataset de aeropuertos. 
        ruta_aeropuertos = Path('custom_dataset', 'ar-airports.csv')
        aeropuertos = pd.read_csv(ruta_aeropuertos)

        # Acá me devuelve una serie donde están los tipos de aeropuertos que hay y cuantas veces aparecen en la columna
        aeropuertos = aeropuertos.elevation_name.dropna().value_counts() #filtramos los vacíos 
        # Cambio los colores que vienen por defecto
        colors = ['cyan', 'magenta', 'pink']
        # Creo el gráfico de torta
        fig2, ax2 = plt.subplots()
        ax2.pie(aeropuertos, labels=aeropuertos.index, autopct='%1.1f%%', colors=colors)
        ax2.set_title('Porcentaje de tipos de Aeropuertos ')

        # Muestro el gráfico
        st.write('Gráfico donde se muestran los tipos de Aeropuertos en Argentina, clasificados según su elevación:')
        st.write('📍 Aeropuerto bajo: Cuenta con una elevación menor a 131ft')
        st.write('📍 Aeropuerto medio: Cuenta con una elevación mayor a 131ft y menor o igual a 903ft')
        st.write('📍 Aeropuerto grande: Cuenta con una elevación mayor a 903ft')
        st.pyplot(fig2)

    case 'Aeropuertos por provincia ✈️':
        ruta_aeropuertos = Path('custom_dataset', 'ar-airports.csv')
        aeropuertos = pd.read_csv(ruta_aeropuertos)
        aeropuertos = aeropuertos.prov_name.dropna().value_counts() #filtramos los vacíos
        # Creo el gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(aeropuertos.index, aeropuertos.values, color='#7B68EE')  # Color lavanda

        # Configuro etiquetas y título
        ax.set_xlabel('Provincias')
        ax.set_ylabel('Cantidad de aeropuertos')
        ax.set_title('Cantidad de aeropuertos por provincia')

        # Roto las etiquetas del eje x para legibilidad
        plt.xticks(rotation=45, ha='right')

        # Ajusto el layout para evitar el recorte de las etiquetas
        plt.tight_layout()

        # Muestro el gráfico
        st.write('En este gráfico podemos apreciar la cantidad de aeropuertos por provincia que hay en Argentina. Ordenados de mayor a menor 📊')
        st.pyplot(fig)

    case 'Lagos por Provincia 🗺️':
        # leo el dataset de lagos 
        ruta_lagos = Path('custom_dataset', 'lagos_arg.csv')
        lagos = pd.read_csv(ruta_lagos)
        lagos= lagos.Ubicación.value_counts()
        fig, ax = plt.subplots()
        ax.bar(lagos.index, lagos.values, color='#3CB371')  # Color menta

        # Configuro etiquetas y título
        ax.set_xlabel('Provincias')
        ax.set_ylabel('Cantidad de lagos')
        ax.set_title('Cantidad de lagos por provincia')

        # Roto las etiquetas del eje x para mejorar la legibilidad
        plt.xticks(rotation=45, ha='right')

        # Ajusto el layout para evitar el recorte de las etiquetas
        plt.tight_layout()

        # Muestro el gráfico
        st.write('Este gráfico muestra la cantidad de lagos que hay en algunas Provincias de Argentina, ordenado de mayor a menor según su cantidad.🤓') 
        st.pyplot(fig)

    case 'Mapa de Lagos en Argentina 🌐':    
        ruta_lagos = Path('custom_dataset', 'lagos_arg.csv')
        lagos = pd.read_csv(ruta_lagos)
        df = lagos[['Nombre', 'latitud', 'longitud']]

        attr = (
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
            'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
        )
        tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'

        m = folium.Map(
            location=(-33.457606, -65.346857),
            control_scale=True,
            zoom_start=5,
            name='es',
            tiles=tiles,
            attr=attr
        )

        marker_cluster = MarkerCluster().add_to(m)

        for index, row in df.iterrows():
            folium.Marker(
                location=(row['latitud'], row['longitud']),
                popup=row['Nombre'],
                icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(marker_cluster)

        st.write('En este mapa podemos ver la ubicación exacta de los lagos en Argentina con su respectivo nombre.')
        st.write('🧐- A medida que se amplía el mapa podemos apreciar como surgen más puntos , ya que estos se agrupan para una mejor visualización cuando el mapa está con un determinado zoom.')
        st_folium(m, width=700, height=500)
    case 'Mapa de Aeropuertos en Argentina 🗺️':    
        ruta_aeropuertos = Path('custom_dataset', 'ar-airports.csv')
        aeropuertos = pd.read_csv(ruta_aeropuertos)
        df = aeropuertos[['name', 'latitude_deg', 'longitude_deg']].dropna()

        attr = (
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
            'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
        )
        tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'

        mapa = folium.Map(
            location=(-33.457606, -65.346857),
            control_scale=True,
            zoom_start=5,
            name='es',
            tiles=tiles,
            attr=attr
        )

        marker_cluster = MarkerCluster().add_to(mapa)

        for index, row in df.iterrows():
            folium.Marker(
                location=(row['latitude_deg'], row['longitude_deg']),
                popup=row['name'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)
        st.write('En este mapa podemos ver la ubicación exacta de los aeropuertos en Argentina con su respectivo nombre.')
        st.write('🧐- A medida que se amplía el mapa podemos apreciar como surgen más puntos , ya que estos se agrupan para una mejor visualización cuando el mapa está con un determinado zoom.')
        st_folium(mapa, width=700, height=500)