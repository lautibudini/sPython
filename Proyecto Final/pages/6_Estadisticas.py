import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
from pathlib import Path
from modules import functions_statistics

path_users_sessions = Path('users_info', 'users_sessions.csv')
users = pd.read_csv(path_users_sessions)

with st.container():

    st.title(" Estadísticas del juego ")
    st.write (" ---- ")


grafico = st.selectbox('Selecciona un gráfico : ', ['Géneros', 'Mayores al Promedio', 'Promedio preguntas mensuales', 'Partidas por día de semana', 'Top 10 usuarios por fecha', 'Dificultad datasets', 'Comparar dos usuarios', 'Temática de mayor conocimiento por género', 'Promedio de dificultades y cantidad de veces elegida', 'Usuarios en racha'])

match grafico:
    case 'Géneros':
        users = pd.read_csv(path_users_sessions)
                
        genders = users['genero'].value_counts()
        # Pongo otros colores a elección, ya que vienen otros por defecto
        colors = ['aqua','yellow']
        # Creo el gráfico de torta
        fig, ax = plt.subplots()
        ax.pie(genders, labels=genders.index, autopct='%1.1f%%', colors=colors)
        ax.set_title('Usuarios que hayan jugado alguna vez el juego agrupados por género')
        # Muestro el gráfico
        st.write('Jugadores agrupados por género')
        st.pyplot(fig)
    case 'Mayores al Promedio':
        # Leo los datos 
        users = pd.read_csv(path_users_sessions)
       
        #Calculo el promedio de puntaje total
        prom = functions_statistics.promedio(users)
    
        # cuento usuarios con puntajes superiores e inferiores al promedio
        mayores_al_promedio = users['puntaje'] > prom
        mayores = mayores_al_promedio.sum()
        menores = (~mayores_al_promedio).sum()
        
        # creo datos para el gráfico de torta
        labels = ['Mayor al promedio', 'Menor o igual al promedio']
        sizes = [mayores, menores]
        colors = ['lime', 'pink']
        
        # creo el gráfico de torta
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
        ax.set_title('Proporción de usuarios con puntaje mayor al promedio')
        # muestro el gráfico en Streamlit
        st.write('Usuarios con puntaje mayor al promedio')
        st.pyplot(fig)
    case 'Promedio preguntas mensuales':
        # leo los datos
        users = pd.read_csv(path_users_sessions)
        # fechas de inicio y fin
        fecha_inicio = st.date_input('Seleccione la fecha de inicio del rango')
        fecha_fin = st.date_input('Seleccione la fecha de fin del rango')

        if fecha_inicio and fecha_fin:
            # convierto fechas a tipo datetime
            fecha_inicio = pd.to_datetime(fecha_inicio)
            fecha_fin = pd.to_datetime(fecha_fin)
            
            users['fecha'] = pd.to_datetime(users['fecha'], format='%Y-%m-%d %H:%M:%S')
            
            # filtro los datos para incluir solo las filas entre las fechas ingresadas por el usuario
            users_filtrado = users[(users['fecha'] >= fecha_inicio) & (users['fecha'] <= fecha_fin)]
            
            # agrego una columna de mes para agrupar
            users_filtrado['mes'] = users_filtrado['fecha'].dt.month
            
            # agrupo por usuario y mes, y calculo el promedio de preguntas acertadas
            preguntas_acertadas_mensuales = users_filtrado.groupby(['usuario', 'mes'])['respuestas_correctas'].mean().reset_index()
            
            # agrupo por usuario y calculo el promedio mensual de preguntas acertadas
            promedio_mensual_por_usuario = preguntas_acertadas_mensuales.groupby('usuario')['respuestas_correctas'].mean().reset_index()
            
            # muestro los resultados
            st.subheader('Promedio de preguntas acertadas mensuales en un rango de fechas')
            st.write(promedio_mensual_por_usuario)
    case 'Dificultad datasets':
        # leo los datos 
        users=pd.read_csv(path_users_sessions)
        # calculo los errores (5 - respuestas_correctas)
        users['errores'] = 5 - users['respuestas_correctas']

        # agrupo por tematica y calculo el total de errores por temática
        errores_por_tematica = users.groupby('tematica')['errores'].sum().reset_index()

        # ordeno las temáticas por el número de errores de mayor a menor
        errores_por_tematica_ordenado = errores_por_tematica.sort_values(by='errores', ascending=False)

        # muestro los resultados
        st.subheader('Temáticas ordenadas por mayor cantidad de errores.')
        st.write(errores_por_tematica_ordenado)
    case 'Partidas por día de semana':
        # leo los datos 
        users = pd.read_csv(path_users_sessions)
        # convierto la columna 'fecha' a datetime
        users['fecha'] = pd.to_datetime(users['fecha'], format='%Y-%m-%d %H:%M:%S')
        # obtengo días de la semana (0: lunes, 1: martes, ..., 6: domingo)
        users['dia_semana'] = users['fecha'].dt.dayofweek
        # cuento la cantidad de partidas por cada día de la semana
        partidas_por_dia = users['dia_semana'].value_counts().sort_index()
        # añado todos los días en el df
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        partidas_por_dia = partidas_por_dia.reindex(range(7), fill_value=0)
        # mapeo los números de los días a nombres de los días
        partidas_por_dia.index = [dias_semana[dia] for dia in partidas_por_dia.index]
        # creo el gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(partidas_por_dia.index, partidas_por_dia.values, color='purple')
        ax.set_title('Cantidad de partidas realizadas por día de la semana')
        ax.set_xlabel('Día de la semana')
        ax.set_ylabel('Cantidad de partidas')
        # muestro el gráfico en Streamlit
        st.write('Partidas por día de la semana')
        st.pyplot(fig)
    case 'Top 10 usuarios por fecha':
        # leo los datos 
        users = pd.read_csv(path_users_sessions)
        fecha_inicio = st.date_input('Seleccione la fecha de inicio del rango')
        fecha_fin = st.date_input('Seleccione la fecha de fin del rango')
        if fecha_inicio and fecha_fin:
            # convierto fecha a tipo datetime
            fecha_inicio = pd.to_datetime(fecha_inicio)
            fecha_fin = pd.to_datetime(fecha_fin)
            #me fijo que esté en el rango
            users['fecha'] = pd.to_datetime(users['fecha'], format='%Y-%m-%d %H:%M:%S')
            users_filtrado = users[(users['fecha'] >= fecha_inicio) & (users['fecha'] <= fecha_fin)]
            # agrupo por usuario, realizo la sumatoria y solo muestro los primeros 10
            top_10_usuarios = users_filtrado.groupby('usuario')['puntaje'].sum().nlargest(10).reset_index()
            # muestro el gráfico
            st.subheader('Top 10 Usuarios por fecha')
            st.write(top_10_usuarios)
    case 'Comparar dos usuarios':
        # leo los datos 
        users = pd.read_csv(path_users_sessions)
        users['fecha'] = pd.to_datetime(users['fecha'], format='%Y-%m-%d %H:%M:%S')
        #lista de usuarios
        lista_usuarios = users['usuario'].unique()
        # selección de usuarios
        usuario1 = st.selectbox('Seleccione el primer usuario', lista_usuarios)
        usuario2 = st.selectbox('Seleccione el segundo usuario', lista_usuarios)

        if usuario1 and usuario2:
            # filtro los datos para los usuarios seleccionados
            users_filtrado = users[(users['usuario'] == usuario1) | (users['usuario'] == usuario2)]

            # creo gráfico
            plt.figure(figsize=(10, 6))
            
            for usuario in [usuario1, usuario2]:
                datos_usuario = users_filtrado[users_filtrado['usuario'] == usuario]
                plt.plot(datos_usuario['fecha'], datos_usuario['puntaje'], label=usuario)

        plt.xlabel('Fecha')
        plt.ylabel('Puntaje')
        plt.title('Evolución del puntaje a lo largo del tiempo')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
    case 'Temática de mayor conocimiento por género':
        # leo los datos 
        users = pd.read_csv(path_users_sessions)
        # selección de género
        genero_elegido = st.selectbox('Seleccione el género', ['Femenino', 'Masculino', 'Otro'])

        # filtro los datos según el género seleccionado
        datos_genero = users[users['genero'] == genero_elegido]

        # verifico si hay datos para el género seleccionado
        if datos_genero.empty:
            st.write(f"No hay datos disponibles para el género {genero_elegido}.")
        else:
            # calculo el promedio de respuestas correctas por temática
            promedio_respuestas_por_tematica = datos_genero.groupby('tematica')['respuestas_correctas'].mean().reset_index()

            # encuentro la temática con mayor conocimiento
            mejor_tematica = promedio_respuestas_por_tematica.loc[promedio_respuestas_por_tematica['respuestas_correctas'].idxmax()]

            # muestro resultado
            st.subheader(f"Para el género {genero_elegido}, la temática con mayor conocimiento es '{mejor_tematica['tematica']}'")
    case 'Promedio de dificultades y cantidad de veces elegida':

        users = pd.read_csv(path_users_sessions) #dataframe del csv

        frecuencia_dificultad = users.groupby('dificultad').size() #cantidad de veces que aparece una dificultad

        promedio_puntaje = users.groupby('dificultad')['puntaje'].mean() #se calcula el promedio

        df_frecuencia = frecuencia_dificultad.reset_index()
        df_frecuencia.columns = ['dificultad', 'frecuencia']

        df_promedio = promedio_puntaje.reset_index()
        df_promedio.columns = ['dificultad', 'promedio puntaje']

        
        resultado = pd.merge(df_frecuencia, df_promedio, on='dificultad')

        st.subheader('Promedio por dificultad y cantidad de veces que fue elegida ')
        st.write(resultado)
    case 'Usuarios en racha':
        # leo los datos 
        users = pd.read_csv(path_users_sessions)
        users['fecha'] = pd.to_datetime(users['fecha'])
        # Filtrar los datos para incluir solo puntajes mayores a cero
        users = users[users['puntaje'] > 0]

        # fecha más reciente en los datos
        fecha_mas_reciente = users['fecha'].max()

        # calculo la fecha hace 7 días desde la fecha más reciente
        fecha_inicio = fecha_mas_reciente - pd.DateOffset(days=6)

        # filtro los datos para los últimos 7 días
        datos_ultimos_siete_dias = users[users['fecha'] >= fecha_inicio]

        # usuarios únicos
        todos_los_usuarios = users['usuario'].unique()

        # lista para almacenar usuarios en racha
        usuarios_en_racha = []

        # itero sobre cada usuario y verifico la racha 
        for usuario in todos_los_usuarios:
            # filtro datos del usuario actual
            datos_usuario = datos_ultimos_siete_dias[datos_ultimos_siete_dias['usuario'] == usuario]
            
            # cuento días con puntaje mayor a 0
            dias_con_puntaje = datos_usuario['fecha'].dt.date.nunique()
            
            # si el usuario tiene puntaje mayor a cero en todos los días de los últimos 7 días, agrego a la lista
            if dias_con_puntaje == 7:
                usuarios_en_racha.append(usuario)

        # creo un df con los usuarios en racha
        df_usuarios_en_racha = pd.DataFrame(usuarios_en_racha, columns=['Usuario'])

        # muestro el df
        st.subheader("Usuarios en racha: ")
        if len(df_usuarios_en_racha) > 0:
            st.dataframe(df_usuarios_en_racha)
        else:
            st.write("No hay usuarios en racha.")