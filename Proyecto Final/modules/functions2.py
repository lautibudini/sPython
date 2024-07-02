import re

def airport_types(airports_file): 
    """ 
    Módulo que recorre el archivo, lee el tipo de aeropuerto y, si este no está en la lista de tipos, 
    lo agrega.

    Args: 
      airport_file: Archivo csv de los aeropuertos. 
    
      Returns: 
        type_list: La lista actualizada de los tipos.
    """
    # Leo el encabezado
    airports_file.readline()
    # Declaro la lista de types 
    type_list= []
    # Itero sobre los aeropuertos 
    for airport in airports_file:
        # A la variable le asigno el tipo de aeropuerto
        airport_type = airport.strip().split(',')[2]
        # Si no se repitió el tipo, lo agrego a la lista
        if airport_type not in type_list:
            type_list.append(airport_type)
    return type_list

def airport_elevation (airports_file, elevation):
    """
    Módulo que recorre el archivo, compara el tipo de elevación del aeropuerto y, si es del tipo indicado, 
    agrega el nombre a la lista de aeropuertos de dicha elevación. 

    Args:
      airports_file: El archivo csv de los aeropuertos. 
      elevation: Elevación seleccionada ('bajo', 'medio', o 'alto')

    Returns: 
      airports_elevation: La lista actualizada con los nombres de los aeropuertos. 
    """
    # Pongo la elevación en minúscula y elimino los espacios en blanco para que haya coincidencia con el archivo
    elevation=elevation.lower().strip()
    # Declaro la lista de elevación de aeropuertos
    airports_elevation= []
    # Leo encabezado
    airports_file.readline()
    # Itero sobre los aeropuertos
    for airport in airports_file:
        # Asigno la elevación del aeropuerto a la variable
        airport_elevation= airport.strip().split(',')[23]
        # Si hay coincidencia, agrego el aeropuerto
        if airport_elevation == elevation:
            airport_name= airport.strip().split(',')[3]
            airports_elevation.append(airport_name)
    return airports_elevation

def airport_lower_or_higher(airports_file, elevation, elevation_choice):
    """ 
    Módulo que recorre el archivo, compara su elevación con el valor numérico seleccionado y agrega el nombre 
    del aeropuerto y su elevación a la lista de aeropuertos con menor o mayor elevación, según la que corresponda. 

    Args: 
      airports_file: El archivo csv de los aeropuertos. 
      elevation: Un valor numérico de la elevación. 
      elevation_choice: Un string con la elección del usuario, 'mayor' o 'menor'.

    Returns: 
      airports_elevation_list: La lista actualizada con el nombre y elevación de los aeropuertos que 
      cumplan con las condiciones dadas. 
    """
    # Declaro la lista 
    airports_elevation_list= []
    # Verifico si la elección es válida, debe ser "mayor" o "menor"
    if elevation_choice not in ['mayor', 'menor']:
        print("La elección de elevación debe ser 'mayor' o 'menor'.")
        return airports_elevation_list
    
    try:
        # Intento convertir la elevación ingresada a un número decimal
        elevation = float(elevation)
        # Si no puedo, informo que no es válido el número y retorno las listas vacías
    except ValueError:
        print("La elevación ingresada no es un número válido.")
        return airports_elevation_list  
    # Convierte la elevación ingresada a flotante
    elevation = float(elevation)
    
    # Leo el encabezado
    airports_file.readline()
    
    # Itero sobre los aeropuertos
    for airport in airports_file:
        # Antes de asignar el número de elevación en flotante, me fijo que sea un número válido
        if airport.strip().split(',')[6].isdigit():
          airport_elevation = float(airport.strip().split(',')[6])
          # Si la elección es menor, realizo lo siguiente 
          if elevation_choice == 'menor':
              # Si es menor, agrego el aeropuerto a la lista de elevaciones más bajas
              if airport_elevation < elevation:
                  airport_name = airport.strip().split(',')[3]
                  airports_elevation_list.append((airport_name, airport_elevation))
          # Si la elección es mayor
          elif elevation_choice == 'mayor':
              # Si es mayor, agrego el aeropuerto a la lista de elevaciones más altas
              if airport_elevation > elevation:
                  airport_name = airport.strip().split(',')[3]
                  airports_elevation_list.append((airport_name, airport_elevation))
    return airports_elevation_list



def lake_size(option,reader):
    """
    Recorre el iterador , comparando el valor en la columna 'sup_tamaño' viendo si coincide
    con el valor ingresado, y asi filtrando y agregando el nombre a una lista que luego retorna

    Args: 
      Recibe la opcion de tamaño del lago y el iterador del archivo.

    Returns: 
      Una lista de los nombres de los lagos que tienen ese tamaño.
    """

    name = 0    # indices de las columnas del archivo
    size = 8
    lakes =[]
    for row in reader :
        if (row[size] == option):
            lakes.append(row[name])
    return lakes


def max_five_percent (data):
     
      """
       A partir de la lista 'data' se guarda los porcentajes de poblacion en situacion de calle
       y las jurisdicciones.

       Args:
          Recibe como parametro una lista con datos del csv censo 2022.

       Returns:
          Retorna una lista ordenada de mayor a menor con porcentaje de poblacion 
          en situacion de calle y jurisdicciones.   
      """
      max_percent= []
      jurisdiction = 0
      poverty = 13
      aux = list(map(lambda x: [x[jurisdiction], x[poverty]], data))[2:] #solo tomo nombres y porcentajes en una lista
      max_percent.extend(aux) 
      percent = 1
      max_percent.sort(key=lambda x: x[percent], reverse=True)

      return max_percent

def max_gender_jurisdiction (data):
     
     """
       A partir de la lista 'data' se guarda los porcentajes de población en situación de calle
       y las jurisdicciones.

       Args:
          Recibe como parametro una lista con datos del csv censo 2022 

       Returns:
          Retorna una lista con 2 valores, un máximo (brecha) y un nombre (jurisdicción)  
      """
     
     jurisdiction = 0
     men = 5
     women = 9
     maxim= []
     
     aux = list(map(lambda x: [x[jurisdiction], x[men] ,x[women]], data))[2:] # con [:2] omito el header y el total
     men = 1 #actualizo
     women = 2 #idem
     aux2 = list(map(lambda x: [x[jurisdiction], abs(int(x[men]) - int(x[women]))], aux)) #uso funcion valor absoluto para que siempre me de positivo
     maxim.extend (max(aux2, key = lambda x: x[1]))  #calculo el max

     return maxim



def capitals_list(reader):
    """
    Esta funcion lo que hace es recibir un archivo donde relaciona las provincias con sus respectivas capitales,
    teniendo en cuenta la columna 'CAPITAL' donde si posee el valor 'primary' o 'admin' significa que en la 
    columna 0  encontramos el nombre de una capital y en columna 1 el nombre de la provincia.

    Args:
      Recibe como parametro un iterador de un archivo.
    
    Returns: 
      Retorna una lista con las capitales de cada provincia.
    """

    num_capital = 6   #numero de columnas a usar
    name_capital = 0
    capitals  = []
    for row in reader: 
        capitals.append(row[name_capital])  if (row[num_capital] == 'admin' ) or (row[num_capital] == 'primary') else None
    return capitals


def biggest_poblation(reader,number):
    """
    Lo que hace esta funcion es procesar las provincias en el archivo pasado como parametro
    para tener en una lista, las provincias con mayor poblacion que la ingresada

    Args: 
      recibe un iterador de un archivo y un numero de poblacion
    Returns: 
      retorna una lista de provincias
    """
    res = []
    prov = 0
    poblation = 1
    for row in reader:
        if int(row[poblation]) > int(number) :
            res.append(row[prov].lower()) # se agrega el nombre de la provincia que cumple con lo pedido de cant. poblacion.
    return res 

def smallest_poblation(reader,number):
    """
    Lo que hace esta funcion es procesar las provincias en el archivo pasado como parametro
    para tener en una lista, las provincias con menor poblacion que la ingresada

    Args: 
      recibe un iterador de un archivo y un numero de poblacion
    Returns: 
      retorna una lista de provincias
    """
    res = []
    prov = 0
    poblation = 1
    for row in reader:
        if int(row[poblation]) < int(number) :
            res.append(row[prov].lower()) # se agrega el nombre de la provincia que cumple con lo pedido de cant. poblacion.
    return res

def province_lakes(reader, res):
    """
    Lo que hace esta funcion es procesar el archivo de lagos, agregando en una lista los nombre de los 
    lagos de las provincias que estan en la lista pasada como parametro.
    Comparando si la columna numero 1 -ubicacion- , que es el nombre de provinvia esta en la lista pasada como parametro, asi 
    sabiendo si agregar o no el nombre del lago a la lista.

    Args: 
      recibe un iterador del archivo de lagos y una lista con provincias
    Returns: 
      retorna una lista de nombres de lagos que cumplen con lo pedido
    """
    lakes = []
    name = 0
    prov = 1
    for row in reader:
        if row[prov].lower() in res:
            lakes.append(row[name])
    return lakes

def province_airports(reader,res):
    """
    Lo que hace esta funcion es procesar las provincias en el archivo de aeropuerto pasado
    como parametro , así viendo que se guarden en una lista los nombres de aeropuertos de las distintas provincias
    que hay en la lista pasada como parametro 

    Args: 
      recibe un iterador del archivo de aeropuertos y una lista de provincias
    Returns: 
      retorna una lista del nombre de los aeropuertos que cumplen con lo pedido
    """
    name = 3
    prov = 24
    airports = []
    for row in reader:
        if row[prov].lower() in res:
            airports.append(row[name])
    return airports


def province_conectivity(reader,res,header): 
    """
    Lo que hace esta funcion es crear un diccionario ,donde las claves son los distintos tipos de provincias 
    pasados como lista y su valor son los tipos de conectividad que se inicializan en cero.
    Una vez ya creado, procesa el archivo de conectividad, vinculando el nombre de la provincia viendo
    si esta en el diccionario, si esta y posee algun tipo de conectividad lo que hace es agregarlo a la  clave de 
    esa provincia si no estaba antes. 

    Args: 
      recibe un iterador de un archivo , una lista de provincias, y una lista con tipos de conectividad. 
    Returns: 
      retorna un diccionario donde la clave es una provincia , y el valor es una lista de los distintos tipos 
      de conectividad de esa provincia 
    """
    conectividad = 16 # aca dice si posee conectividad o no, en caso de no poseer ya que se que todos sus campos son no.
    
    conectivity = {}
    # recorro cada provincia que cumple y le agrego esta lista
    for elem in res: 
        value = elem.replace('ó','o').replace('á','a').replace('é','e').replace('í','i').replace('ú','u')
        conectivity[value] = []
    # una vez que ya tengo la estructura recorro el archivo
    for row in reader:
        if row[conectividad] != 'NO' and row[0].lower() in conectivity:
            tipos = row[4:14]
            index = 0
            for elem in tipos:
                if elem =='SI':
                    if header[index] not in conectivity[row[0].lower()]:
                        conectivity[row[0].lower()].append(header[index])
                index = index + 1 
    return conectivity


def get_connectivities(header):
    """
       A partir del encabezado del archivo csv el cual es una lista
       guarda en una variable los valores desde la posicion 4 a la -4.
       Tales valores son los tipos de conectividad.

       Args:
          Recibe como parametro una lista.

       Returns:
          Retorna una lista con los diferentes tipos de conectividad.   
    """
    connectivities = header[4:-4]
    return connectivities


def cant_connectivities(header,reader):
    """
    -Usa otra funcion para obtener las conectividades.
    -Crea una diccionario con los diferentes tipos de conectividades como
     clave y inicializa todos sus valores en 0.
    -Recorre el iterador dado en cada columna. En cada columna recorre
     la lista de conectividades para evaluar cada conectividad de la
     columna:
        si esta es 'SI' significaria que la localidad en la que se
        encuentra iterando tiene esta conectividad, por lo tanto se le suma
        1 al valor de la conectividad en el diccionario.

    Args:
      Recibe las claves del encabezado de un diccionario y un iterador
      de un archivo como parametros.

    Returns:
      Retorna un diccionario con los diferentes tipos de conectividad
      como claves y la cantidad de localidades que tienes esa conectividad
      como valor.       
    """
    connectivities = get_connectivities(list(header.keys())) #Convertimos las claves del header en una lista y la paso como parametro a la funcion get_connectivities
    
    dict_connectivities = {connection: 0 for connection in connectivities} #Creamos el diccionario con la conectividad como clave y valor 0 en c/u

    for row in reader:
        for connection in connectivities:
            if row[connection] == 'SI':
                dict_connectivities[connection] += 1 # Aumenta en 1 el valor de la conectividad en el diccionario
    return dict_connectivities



def get_provincias_with_fibra(reader):
    """
       -Recorre el iterador guardando en un diccionario las provicias como
        claves del mismo y como valor una lista donde se guardaran tuplas las cuales tendran 2 valore:
          -El primer valor es el nombre de la ciudad.
          -El segundo valor es 'SI' o 'NO'. Esto depender de si la ciudad 
           tiene fibra optica o no. 
       -Luego recorrera el diccionario de provincias iterando en todas
        las ciudades de la provincia evaluando si las mismas tienen TODAS
        fibra optica. Si todas las ciudades de la pronvincia tienen fibra
        el nombre de la misma se guardara en una lista.

        Args:
          Recibe como parametro el iterador de un archivo.

        Returns:
          Retorna una lista con los nombres de las pronvias que cumplen
          con la condicion:
             Todas sus ciudades tienen fibra optica.
    """
    provincias_with_fibra_optica = [] # Lista donde se guardaran los nombres de las pronvincias que cumplan la condicion.

    provincias = {} # Diccionario donde se guardaran las pronvicias con sus ciudades y si tienen fibra optica.

    for row in reader:
        provincia = row[0] # Nombre de la provincia.
        city = row[2] # Nombre de la ciudad.
        fibra_optica = row[7] # Valor que tenga fibra optica (si/no).
        
        if provincia not in provincias: 
            provincias[provincia] = [] # Si la provincia en la que estoy iterando no se encuentra en el diccionario, la agrego y como valor le asignamos una lista vacia.

        provincias[provincia].append((city,fibra_optica)) # Agregamos (la ciudad y si la misma tiene fibra optica) como tupla en la lista de valores de la provincia. 
        
 
    for provincia, city in provincias.items():
       
       all_with_fibra_optica = all(fibra == 'SI' for _,fibra in city) # Evaluamos (en todas las ciudades de la provincia que se esta iterando) si cada ciudad tiene fibra optica .
       if all_with_fibra_optica:  
            provincias_with_fibra_optica.append(provincia) #Si se cumple la condicion se agrega la provincia a la lista de provincias que cumplen la condicion.
    return provincias_with_fibra_optica

def capitals_province_list(reader, capital_index, capital_name, capital_connectivity):
      
      """
       uso el archivo reader 'ar' para guardar y acomodar los 
       datos que necesito parra luego usarlos.

       se hace un arreglo/acomodacion con replace, lower y split 
       en las capitales para no tener errores y replace lower tambien en
       las provincias para obtener coincidencias y resultados mas precisos

       Args:
          Recibe como parametros el archivo de lectura 'ar', indices 
          y la lista donde voy a almacenar las capitales/provincias

       Returns:
          Retorna una lista que contiene listas de provincias y capitales
      """
     
      for i in reader:
        if i[capital_index] == 'admin' or i[capital_index] == 'primary':
            # transformo el nombre de la capital en una lista de strings
            list_capital = i[capital_name].lower().replace('ó', 'o').replace('á', 'a').replace('í', 'i').replace('é', 'e').replace('ú', 'u').split()
            # guardo provincia y capital en una lista
            capital_connectivity.append([i[5].lower().replace('ó', 'o').replace('á', 'a').replace('í', 'i').replace('é', 'e').replace('ú', 'u'), list_capital])
       
      return capital_connectivity

def capitals_connectivity (capital_connectivity,reader, province, local, connection):
     

     """
       uso el archivo reader 'ar' y mi lista de capitales/provincias
       para verificar el estado de conectividad de las capitales y luego informar
       en otra lista que contenga ya todos los datos.
       
       Args:
          Recibe como parametros el archivo de lectura 'conectividad', indices 

       Returns:
          Retorna una lista que contiene listas de provincia, capital y conectividad   
      """
     list_capitals_connectivity= []
     for row in reader:
        province_1 = row[province].lower().replace('ó', 'o').replace('á', 'a').replace('í', 'i').replace('é', 'e').replace('ú', 'u')  # guardo provincia
        capital_list = row[local].lower().replace('ó', 'o').replace('á', 'a').replace('í', 'i').replace('é', 'e').replace('ú', 'u').split()  # guardo capital como lista de strings

        for list in capital_connectivity:
        
            if province_1 == list[0] and all(word in capital_list for word in list[1]): # verifica si coincide la provincia de mi lista y si coinciden las palabras de mi lista con la capital del archivo 'conectividad'
               list_capitals_connectivity.append([list[0], list[1], row[connection]]) # agrego todos los datos a mi lista

     return list_capitals_connectivity