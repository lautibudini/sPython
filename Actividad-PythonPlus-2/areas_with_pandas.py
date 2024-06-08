import pandas as pd 

# Función para imprimir bonito : 
def print_report(title, res):
    """
    Lo que hace esta función es imprimir un reporte, recibiendo un titulo y 
    una estructura de tipo serie(Pandas).
    """
    print(f"{title.capitalize():-^40}")
    # Iteramos sobre los elementos de este tipo Serie.
    for f,c in res.items():  
        print(f"{f}: {c}")


# Configuramos la ruta del archivo.
file_route = "area_protegida.csv"

# Leemos el archivo csv con pandas: 
areas = pd.read_csv(file_route)
#print(areas)
#print(areas.shape) 

# Lo que hago es hacer un value count, de los elementos de la columna 6 (gna).
filtrado = areas.gna.value_counts().head(5)
#print(filtrado)
#print(filtrado.shape)

print_report("Super listado", filtrado.head(3))
