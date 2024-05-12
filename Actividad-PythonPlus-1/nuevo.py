from collections import Counter
import csv

def my_function(file_name, n=None):
    """
    Esta funcion lo que hace es recibir un archivo, y con este 
    lo que hace es contar en el archivo dado de artistas cuantas veces
    estos aparecen y luego devuelve los mas comunes
    
    Args: 
      como primer parametro recibe un archivo, y puede recibir opcionalmente
      un segundo parametro para que retorne solo los artistas n mas comunes.
    Returns: 
      devuelve una lista de tuplas con los nombres de los artistas mas comunes, y cuantas
      veces aparecen estos en el archivo.
    """
    try:
        with open(file_name, encoding ='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            artists = Counter(map(lambda x: x[0], reader))
            if n is None:
                return artists.most_common(10)
            else:
                return artists.most_common(n)
    except FileNotFoundError:
        print(f'No fue posible abrir el archivo {file_name}, ya que no se encontro')

try:
    my_songs = my_function('songs_normalize.csv', 2)
except FileNotFoundError:
    print("Tenemos un problema!!")
finally:
    for song in my_songs:
        print(song)