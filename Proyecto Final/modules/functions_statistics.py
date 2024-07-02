import pandas as pd 
import streamlit as st
import requests


def total_puntos(dificultad, puntos):
    """
      Función encargada de modificar y calcular el puntaje final dependiendo la dificultad
      seleccionada.
      Args: 
        dificultad y puntaje actual.
    """
    match dificultad:
        case 'facil':
            return puntos
        case 'medio':
            return puntos + puntos / 2
        case 'dificil':
            return puntos * 2


def load_lottieurl(url):
    """
      Función encargada de corroborar y generar la imagen/gif lottie.
      Args: 
        la url del gif.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def promedio(usuarios):
    return usuarios['puntaje'].mean() 

def mostrar_ranking_historico_puntaje(archivo):
    """
      Función encargada de mostar el ranking historico de los jugadores, recibiendo el archivo csv, y 
      convirtiendolo en un dataset para poder usar mejor su información y poder generar el nuevo dataset.
      Args: 
        la ruta del archivo csv.
    """
    df = pd.read_csv(archivo)
    df_puntaje = df.groupby('email')['puntaje'].sum().reset_index()

    # Ordenamos por puntaje total de manera descendente para que se pueda mostrar de manera ordenada
    df_puntaje = df_puntaje.sort_values(by='puntaje', ascending=False).reset_index(drop=True)

    # Agregamos el puesto del jugador en la columna 'puesto'
    df_puntaje['puesto'] = df_puntaje.index + 1

    st.title('Ranking historico de puntajes 🙀')
    st.write('A continuación se muestra el ranking de los mejores puntajes acumulados por los jugadores.')
    # Mostramos primero el puesto, usuario y puntaje, solo los primeros 15.
    st.write(df_puntaje[['puesto', 'puntaje','email']].head(15))
