import streamlit as st 
from modules import functions_statistics as fs
from pathlib import Path
from streamlit_lottie import st_lottie



with st.container():
    st.title(" Ranking de puntajes 💯💯 ")
    st.write (" ---- ")
    left_colum, right_colum = st.columns(2)
    with left_colum:
        ruta = Path('users_info','users_sessions.csv')
        fs.mostrar_ranking_historico_puntaje(ruta)
    with right_colum:
        lottie_url_coding = "https://lottie.host/44d47111-68fa-4ed2-b124-bdaef1bf71c1/FCSgDJttWo.json"
        lottie_url_download = fs.load_lottieurl(lottie_url_coding)
        st_lottie(lottie_url_download)