import streamlit as st 
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url : str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



with st.container():
    st.subheader(" Bienvenido a nuestro juego ! :wave: ")
    st.title(" Esto es Pytrivia 🕹️ 🎮 ")


with st.container():
    st.write("---")
    left_colum, right_colum = st.columns(2)
    with left_colum:
        st.header(" Integrantes del proyecto : ")
        st.write("""
                  - Candela Cáceres
                  - Camila Corbalán Saez
                  - Leandro Ezequiel Arrieta
                  - Lautaro Tomas Budini
                 """)
        #st.write(" Este trabajo consiste en el procesamiento y analisis de datos ...")
    with right_colum:
        lottie_url_coding = "https://lottie.host/b516970a-e00d-4829-b2f0-608ee6e10523/VicGANPQJy.json"
        lottie_url_download = load_lottieurl(lottie_url_coding)

        st_lottie(lottie_url_download)

with st.container():

    
    st.title ( " Información útil 🤓 ")
    st.write (" --- ")

    st.write( " **Descripción del juego** ")
    st.write ( """
                - Este es un juego interactivo que utiliza archivos CSV para su funcionamiento y obtención de información.
                Se muestran datos y dependiendo del nivel de dificultad que usted seleccione se le brindarán pistas (o no) para poder responder. 
                También podrá elegir entre 4 temáticas para jugar: Aeropuertos, Lagos, Conectividad y Censo 2022.
                Por cada respuesta correcta se irán sumando puntos que podrá utilizar para entrar en nuestro Ranking de 15 mejores jugadores.

              """)
    
    st.write( " **Datos necesarios** ")
    st.write ( """
                - Usted debe tener un nombre de usuario registrado previamente para poder comenzar a jugar, 
                  si aún no lo hizo puede hacerlo [aqui](http://localhost:8501/Formulario_de_registro). Una vez registrado, usted ya podrá jugar.
              
                - Se podrá seleccionar 3 niveles de dificultad, *Fácil* , *Medio*, o *Difícil*, dependiendo cual seleccione, habrá una variación en los puntos
                 que le servirá para tener la posibilidad de entrar en el Ranking.

              """)
    
    st.write( " **Instruccciones** ")
    st.write ( """
                - Deberá seleccionar la temática con la cual desea jugar: *Aeropuertos* , *Lagos*, *Conectividad*, *Censo 2022*,
                  y por último la dificultad.
              
                - Una vez comenzado el juego, se le aparecerán 5 preguntas que deberá responder correctamente para poder sumar puntos, 
                  las respuestas correctas tienen el valor de 1 punto por pregunta pero esto variará dependiendo del nivel de dificultad.

              """)
    
    st.write( " **Dificultad** ")
    st.write ( """
                Se podrán seleccionar 3 niveles diferentes de dificultad, cada uno le otorgará diferentes puntos:
              
                - *Fácil*: se obtiene la cantidad de puntos original (1 punto por respuesta correcta). Pista: se informan todas las vocales de la respuesta correcta.
              
                - *Medio*: se obtiene la cantidad de puntos original más el cincuenta por ciento de ese valor. Pista: Se informa la primer y última letra de la respuesta correcta.
              
                - *Difícil*: se obtiene el doble del puntaje original. No se brindan ayudas.

            
              """)     
