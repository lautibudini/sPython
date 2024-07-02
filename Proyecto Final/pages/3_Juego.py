import streamlit as st
import pandas as pd
from pathlib import Path
from modules import functions_st_game as game
import json
import datetime

# NO_CREADO -> GENERAR_PREGUNTAS -> MOSTRAR_PUNTAJE
#        ^---------------------------v

# 1. El juego tiene estados.
# 2. Los datos que quiero persistir los guardo en el session_state.
# 3. Cada vez que cambio de estado ejecuto rerun() para volver a ejecutar el script.
# Si es nuevo se crea la session  


if "game_state" not in st.session_state: 
    st.session_state["game_state"] = {
        'estado' : 'no_creado',
        'email': '',
        'usuario' : None,
        'puntaje' : 0,
        'genero': '',
        'tematica': '',
        'dificultad': '',
        'preguntas':[],
        'respuestas':[],
        'dataframe': None ,
        'cant_preguntas' :0,
        'cant_res_correctas':0,
        'fecha': None 
    }

reader_users = Path('users_info', 'users_data.json')

# Leemos el archivo JSON de los registros
if reader_users.exists() and reader_users.stat().st_size > 0:
    try:
        with reader_users.open() as file:
            users_data = json.load(file)
    except json.JSONDecodeError:
        users_data = {}  # En caso de error de decodificación, inicializamos users_data como un diccionario vacío
else:
    users_data = {}  # Si el archivo no existe o está vacío, inicializamos users_data como un diccionario vacío

# Extraemos los usuarios
usernames = [data['User'] for data in users_data.values()]

if not usernames:
    st.warning("No hay usuarios registrados. Por favor, regístrese primero en 'Formulario de registro'.")
else:
    # Registramos al usuario
    if st.session_state.game_state['estado'] == 'no_creado': 
        with st.form('formulario'):
            nombre = st.selectbox('Ingrese su nombre de usuario : ', usernames)
            tematica = st.selectbox('Seleccione un dataset para jugar : ', ['Lagos', 'Aeropuertos', 'Conectividad','Censo'])
            dificultad = st.selectbox('Seleccione el nivel de dificultad del juego : ', ['facil', 'medio', 'dificil'])
            registro = st.form_submit_button('jugar')
        # Cuando apriete jugar debemos guardar los datos que seleccionó
        if registro: 
            st.session_state.game_state["estado"] = "generar_preguntas"
            st.session_state.game_state["usuario"] = nombre
            for email, user_data in users_data.items():
                if user_data['User'] == nombre:
                    st.session_state.game_state["genero"] = user_data['Gender']
                    st.session_state.game_state["email"] = email
                    break
            st.session_state.game_state['tematica'] = tematica
            st.session_state.game_state['dificultad'] = dificultad
            st.rerun()

    
    
    # Estado para generar pregunta 
    elif st.session_state.game_state['estado'] == 'generar_preguntas':  
        game.tematica(st.session_state.game_state['dificultad'], st.session_state.game_state['tematica'])
        
        
        if st.session_state.game_state['cant_preguntas'] == 5:  # fin del juego
            # Llamamos a una funcion que cree el dataFrame de las preguntas y respuestas generadas
            st.session_state.game_state['dataframe'] = game.crear_dataframe()
            st.session_state.game_state['puntaje'] = game.calcular_puntaje(st.session_state.game_state['dataframe'],st.session_state.game_state['dificultad'])
            st.session_state.game_state["fecha"] = datetime.datetime.now()
            st.session_state.game_state["estado"] = "mostrar_puntaje"
            st.rerun()
    elif st.session_state.game_state['estado'] == 'mostrar_puntaje':
        path_users_sessions = Path('users_info', 'users_sessions.csv')
        users = pd.read_csv(path_users_sessions)
        users.loc[len(users)] = [
            st.session_state.game_state["usuario"],
            st.session_state.game_state["dificultad"],
            st.session_state.game_state["tematica"],
            st.session_state.game_state["cant_res_correctas"],
            st.session_state.game_state["puntaje"],
            st.session_state.game_state["genero"],
            st.session_state.game_state["fecha"].strftime("%Y-%m-%d %H:%M:%S"),
            st.session_state.game_state["email"]
        ]
        users.to_csv(path_users_sessions, index=False)
        game.fin_de_juego(st.session_state.game_state['puntaje'],
                          st.session_state.game_state['cant_res_correctas'],
                         st.session_state.game_state['cant_preguntas'])
        
        # Ya guardada la información en el csv, entonces reseteamos los datos para volver a jugar con otro usuario.
        st.session_state.game_state["usuario"] = None
        st.session_state.game_state["dificultad"] = None
        st.session_state.game_state["tematica"]= None
        st.session_state.game_state["cant_preguntas"] = 0
        st.session_state.game_state["cant_res_correctas"] = 0
        st.session_state.game_state["puntaje"] = 0
        st.session_state.game_state["genero"] = None
        st.session_state.game_state["fecha"] = None
        st.session_state.game_state["email"] = None
        st.session_state.game_state["preguntas"] = []
        st.session_state.game_state["respuestas"] = []
        st.session_state.game_state["dataframe"] = None

        # Cambiamos el estado a no creado para que pueda volver a jugar.
        st.session_state.game_state["estado"] = "no_creado"
        