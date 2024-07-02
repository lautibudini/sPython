import random 
import pandas as pd 
import streamlit as st
from pathlib import Path
from modules import functions_statistics  as ranking
    
  
# ----------------------------------------------------------------------
# Procedimientos para pasar la informacion al juego dependiendo la tematica : 

def lagos_option(dificultad):
    """
    Esta función es la encargada de preparar el dataframe de lagos con las 4 columnas 
    seleccionadas para las preguntas del juego.

    Args: 
      recibe como parametro el nivel de dificultad. 
    """
    ruta = Path('custom_dataset', 'lagos_arg.csv')
    name = ['Nombre','Ubicación','Superficie (km²)','sup tamaño']
    frame = pd.read_csv(ruta)      
    frame = frame[name] #Le aplicamos una mascara con las columnas que queremos
    game(frame,dificultad,name, frame.shape[0])


def censo_option(dificultad):
    """
    Esta función es la encargada de preparar el dataframe de Censo con las 4 columnas 
    seleccionadas para las preguntas del juego.

    Args: 
      recibe como parametro el nivel de dificultad. 
    """
    ruta = Path('custom_dataset', 'c2022_tp_c_resumen_adaptado.csv')
    name = ['Jurisdicción','Total de población','Población en viviendas particulares','Población en situación de calle(²)']
    frame = pd.read_csv(ruta)
    frame = frame[name]
    game(frame,dificultad,name,frame.shape[0])
 
def airports_option(dificultad):
    """
    Esta función es la encargada de preparar el dataframe de Aeropuertos con las 4 columnas 
    seleccionadas para las preguntas del juego.

    Args: 
      recibe como parametro el nivel de dificultad. 
    """
    ruta = Path('custom_dataset', 'ar-airports.csv')
    frame = pd.read_csv(ruta)
    names = ['tipo ','nombre', 'elevacion', 'nombre de provincia']                             
    frame = frame[['type','name', 'elevation_name', 'prov_name']].dropna() # filtramos los nulos                
    game(frame,dificultad,names, frame.shape[0] )

    
def conectividad_option(dificultad):
    """
    Esta función es la encargada de preparar el dataframe de Conectividad con las 4 columnas 
    seleccionadas para las preguntas del juego.

    Args: 
      recibe como parametro el nivel de dificultad. 
    """
    ruta = Path('custom_dataset', 'Conectividad_Internet.csv')
    frame = pd.read_csv(ruta)
    names = ['Provincia','Partido', 'Localidad', 'posee conectividad']                           
    frame = frame[names]                                 
    game(frame,dificultad,names, frame.shape[0])

# ------------------------------------------------------------------------
# Estructura del juego para los diferentes datasets.
def crear_dataframe():
    """"
      Esta función es la encargada de generar el dataset de la session state, a partir
      de las preguntas generadas y las respuestas del jugador para luego ser usado.
      
      Returns: 
        retorna el dataframe creado con las columnas (Pregunta-Respuesta_jugador-Respuesta_correcta)
    """
    respuestas_jugador= st.session_state.game_state['respuestas']
    datos_pregunta_respuesta = st.session_state.game_state['preguntas'][:5]
    # Creamos el DataFrame
    data = {
       'Pregunta': [pregunta for pregunta, _ in datos_pregunta_respuesta],
       'Respuesta_jugador': respuestas_jugador,
       'Respuesta_correcta': [respuesta_correcta for _, respuesta_correcta in datos_pregunta_respuesta]}
    return pd.DataFrame(data)

def game(frame,dificultad,names, filas):
    """
      Esta funcion es la que genera la pregunta a partir de un dataset y una dificultad, utilizando
      un formulario, genera la pregunta selecciónando una fila random del dataset y una columna la cual
      sera el atributo a adivinar.

      Args: 
        recibe el dataframe del dataset, la dificultad, los nombres de las categorias, y la cant de filas.
    """
    with st.form('key_lagos_facil'):
        number = random.randint(0,3)                 # El numero del atributo que se adivinara         
        row = frame.iloc[random.randint(1,filas-1)]  # El numero de fila al azar que usaremos
        st.subheader(f'Pregunta : ')
        #Crea el formulario con las 4 categorias
        for i in range(4): #0 a 3
            print(i,number, row[i])
            if number != i:                   
             st.write(f'{names[i]} : {row[i]}')
            else :  
                # Me guardo en una lista de tuplas la categoria a adivinar y su respuesta
                st.session_state.game_state['preguntas'].append((names[i] , row[i]))               
                adivinar_indice = i
        # Muestra lo que se debe adivinar como la ultima opcion.
        # Filtra el atributo a ganar dependiendo de la dificultad para ver que tipo de pistas se brindan.
        st.text(f'{names[adivinar_indice]} : {filtrado(dificultad, row[adivinar_indice])}')
        res = st.text_input('Ingrese su respuesta')
        btn_res = st.form_submit_button('responder') 
        if btn_res:
            # Guarda en una lista las respuestas del jugador en la partida.
            st.session_state.game_state['respuestas'].append(res)
            st.session_state.game_state['cant_preguntas'] += 1

            

def calcular_puntaje(dataframe,dificultad):
    """
      Función encargada de calcular el puntaje del jugador, dependiendo de la dificultad elegida.

      Args:
        Recibe el dataframe donde se encuentra la respuesta correcta y la respuesta del jugador, junto
        con la dificultad elegida en la partida.
      Returns: 
        Retorna el puntaje final del jugador.
    """
    puntaje_tot = 0
    for _, row in dataframe.iterrows():
        respuesta_jugador = row['Respuesta_jugador']
        respuesta_correcta = row['Respuesta_correcta']
        if respuesta_jugador is not None and len(respuesta_jugador) > 0:
                if isinstance(respuesta_jugador,str) and isinstance(respuesta_correcta,str):
                    respuesta_jugador = respuesta_jugador.strip().lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
                    respuesta_correcta = respuesta_correcta.strip().lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
                    if respuesta_correcta == respuesta_jugador:
                        puntaje_tot+= 1
                        st.session_state.game_state['cant_res_correctas'] += 1
                else :
                    if int(respuesta_jugador) == int(respuesta_correcta):
                        puntaje_tot+= 1
                        st.session_state.game_state['cant_res_correctas'] += 1
    return calculo_final_puntos(dificultad,puntaje_tot)

def calculo_final_puntos(dificultad, puntos):
    """
      Función auxiliar que recibe una dificultad y puntos del jugador y dependiendo la dificultad, calcula
      el puntaje que debe tener.
      Args: 
        Dificultad y el puntaje sin modificaciones.
      Returns: 
        Retorna el puntaje modificado segun la dificutad.
    """
    if (puntos>0):
        match dificultad:
            case 'facil':
                return puntos
            case 'medio':
                return puntos + puntos / 2
            case 'dificil':
                return puntos * 2
    else : 
        return 0 



def fin_de_juego(puntaje,res_correctas,cant_preg):
    """
      Función donde se muestra el final de una partida, mostrando con ella el puntaje del jugador,
      la cantidad de respuestas correctas de la partida, lo que respondio el jugador y por ultimo el 
      ranking de los mejores jugadores.
      Args: 
        Recibe el puntaje, la cant de respuestas corretas, cantidad de preguntas.
    """
    st.title(' ✨🎊 ¡Terminaste de responder las preguntas! 🎊✨')
    st.subheader(f'Tu puntaje total fue de : {puntaje} puntos ')
    st.subheader(f'Respondiste bien {res_correctas} preguntas de {cant_preg}')
    st.title(' 📝 Respuestas del jugador : ')
    st.dataframe(st.session_state.game_state['dataframe'])
    ruta = Path('users_info','users_sessions.csv')
    ranking.mostrar_ranking_historico_puntaje(ruta)
    st.subheader('Toque [aqui](http://localhost:8501/Ranking) para ir a la pagina del ranking 📊')



# ------------------------------------------------------------------------
# Funciones para filtrar el juego segun la dificultad y tematica seleccionada.

def tematica(dificultad, tematica):
    """
        Esta función es la encargada de filtrar el juego segun la tematica seleccionada.
    Args: 
         Se recibe la tematica y la dificultad seleccionada. 
    """
    if tematica == 'Lagos':
        lagos_option(dificultad)
    elif tematica == 'Conectividad':
        conectividad_option(dificultad)
    elif tematica == 'Censo':
        censo_option(dificultad)
    else: 
        airports_option(dificultad)


def filtrado(dificultad, cadena):
    """
    Esta funcion solo se fija que nivel de dificultad es para saber como retornar la ayuda
    que se le brinda para responder, segun la dificultad seleccionada.

    Args: 
      la dificultad y la respuesta.
    Returns:
      Devuelve una cadena de texto.
    """
    print(cadena)
    if dificultad == 'facil': 
        return facil(cadena)
    elif dificultad == 'medio':
        return medio(cadena)
    else: 
        return ''
    

def facil(cadena):
    """
    Esta funcion lo que hace es recibir una cadena y devuelve otra donde solo aparecen
    las vocales y las que no son vocales las deja con el caracter '_'.
    En caso de ser un numero y no un string, devuelve un string donde especifica entre que rango
    esta ese numero dado.
    Args:
      Recibe una cadena.
    Return: 
      Devuelve la cadena modificada.
    """
    res = cadena
    # Aca debo verificar si es un numero para mostrar una opcion.
    if str(res).isdigit():
        mas_cinco = res + 5
        menos_cinco = res - 5
        res = (f'Esta entre : {menos_cinco} y {mas_cinco}')
        return res
    else:
        vowels = ['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú','Á','É','Í','Ó','Ú',' ']
        for letra in cadena:
            if letra not in vowels:
                res = res.replace(letra, '_')   
        return res


def medio(cadena):
    """
    Esta funcion lo que hace es recibir una cadena y devuelve otra donde solo aparecen
    la primer y ultima letra, las demas las deja con el caracter '_'.
    En caso de ser un numero, devuelve un string donde aclara que ese numero es menor que ... como pista.
    Args:
      Recibe una cadena String.
    Return: 
      Devuelve la cadena modificada.
    """
    res = cadena
    # Aca debo verificar si es un numero para mostrar una opcion.
    if str(res).isdigit():
        mas_cinco = res + 5
        res = (f' Es mas chico que : {mas_cinco}')
        return res
    # En el caso de conectividad debo verificar si no es (si-no) para mostrar solo la primer letra.
    else:
        if len(cadena) == 2: 
            res = (f'{cadena[0]}_')
        else: 
            res =''
            for i,letra in enumerate(cadena): 
                if  i == 0 or i == len(cadena) - 1:
                    res+= letra
                elif letra == ' ': 
                    res+= ' '
                else: 
                    res+='_'
        return res