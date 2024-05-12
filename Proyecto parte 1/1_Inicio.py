import streamlit as st 
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url : str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



with st.container():
    st.subheader(" Bienvenido a nuestro trabajo! :wave: ")
    st.title(" Trabajo integrador Primera parte - Grupo 21 -")


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
        st.write(" Este trabajo consiste en el procesamiento y analisis de datos ...")
    with right_colum:
        lottie_url_coding = "https://lottie.host/1d7534a1-efd3-4fca-935b-1d0ea05f6f6f/ILDjE1uz5q.json"
        lottie_url_download = load_lottieurl(lottie_url_coding)

        st_lottie(lottie_url_download)




     
