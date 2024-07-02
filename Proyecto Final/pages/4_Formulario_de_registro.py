import streamlit as st 
from datetime import datetime, timedelta
from pathlib import Path
import json 
from modules import functions_streamlit

# Declaro la ruta para el archivo de los datos de usuario
path_user_data = Path('users_info', 'users_data.json')

with st.container():
    with st.form(key='form1'):
        st.write("Ingrese sus datos para poder registrarse:")
        text_name = st.text_input("Ingrese su nombre de usuario")
        text_real_name = st.text_input('Ingrese su nombre completo')
        text_mail = st.text_input('Ingrese su mail')
        actual_date = datetime.now()
        minim_date = datetime(actual_date.year - 100, actual_date.month, actual_date.day)
        date_birth = st.date_input("Fecha de nacimiento", min_value=minim_date, max_value=actual_date, value=minim_date)
        text_gender = st.selectbox('Ingrese su género', ['Femenino', 'Masculino', 'Otro'])
        
        # Verificar si el formulario ha sido enviado
        if st.form_submit_button('Enviar'): 
            # Verificar si todos los campos están completos
            aux = functions_streamlit.verify(text_name, text_real_name, text_mail, text_gender, date_birth)
            if aux:
                # Verificar si el correo electrónico es válido
                mail = functions_streamlit.verifymail(text_mail)
                if mail:
                    # Crear datos del nuevo usuario
                    new_user_data = functions_streamlit.new_user(text_name, text_real_name, text_gender, date_birth)
                    # Agregar el usuario a los datos existentes
                    functions_streamlit.add_user(text_mail, new_user_data, path_user_data)
                    st.write('Se agregó el usuario correctamente')
                else:
                    st.write('No es un mail válido.')
            else:
                st.write('No completaste todos los campos.')