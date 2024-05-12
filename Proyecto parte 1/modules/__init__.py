import re

def add_elevation_airport (data_airports):
  """
  Módulo que procesa los datos de los aeropuertos, agrega la nueva categoría 
  'elevation_name' y evalúa si su contenido debe ser 'bajo', 'medio' o 'alto' según 
  su elevación.
  
  Args: 
    data_airports: Un archivo csv con los aeropuertos.

  Returns: 
    El archivo csv actualizado. 
  """
  for airport in data_airports:
    elevation_str = airport[6]  # Obtengo en la variable el dato que necesito evaluar
    if elevation_str.strip() and elevation_str.isdigit():  # Evalúo que no esté vacío el dato y que su contenido sea un número. Si lo es, lo transformo en flotante y comparo
        elevation_ft = float(elevation_str)
        elevation_name = (
            'bajo' if elevation_ft <= 131 else
            'medio' if elevation_ft <= 903 else
            'alto'
        )
    else:
        elevation_name = ''

    # Agrego 'elevation_name' al aeropuerto actual
    airport.append(elevation_name)
  return data_airports

def add_province_airport(data_airports, data_airports_prov):
  """
  Módulo que procesa los datos del aeropuerto y de las provincias. Busca el nombre de la ciudad del aeropuerto en el archivo 
  de las provincias, y si hay coincidencia, agrega al archivo de los aeropuertos la provincia en la nueva categoría, 'prov_name'.

  Args: 
    data_airports: Un archivo csv con los aeropuertos. 
    data_airports_prov: Un archivo csv con especificaciones de ciudades y provincias de Argentina.

  Returns: 
    El archivo de los aeropuertos actualizado
  """
# Itero sobre los aeropuertos en data_airports 
  for airport in data_airports:
    # Transformo en una lista de strings las ciudades, pongo todo en minúscula y reemplazo ciertos caracteres
      airport_municipality = airport[13].lower().replace('/', '').replace('(', '').replace(')', '').split()
      prov_name = ''  # Inicializo el nombre de la provincia como vacío para cada aeropuerto
    
    # Busco la ciudad actual del aeropuerto en data_airports_prov
      for province in data_airports_prov:
        # Transformo el nombre de la ciudad en una lista de strings y pongo todo en minúscula
          city_list = province[0].lower().replace('ó','o').replace('í','i').replace('ú','u').replace('é','e').replace('á','a').split()
        
        # Verifico si cada palabra en airport_municipality está presente en alguna de las sublistas en city_list. Primero utilizo el any para saber si hay alguna coincidencia
        #y después el all para especificar que deben estar todas sí o sí.
          if all(any(word in subcity for subcity in city_list) for word in airport_municipality):
              prov_name = province[5]  # Asigno el nombre de la provincia correspondiente
              break  # Salgo del loop si hay coincidencia
    
    # Agrego 'prov_name' al aeropuerto actual
      airport.append(prov_name)
  return data_airports
  

def match_surface(valor, fila): 
        """
        Matchea el valor ingresado de la profundidad del lago y decide si es chico-medio-grande
        y agrega ese valor a la columna correspondiente. 

        Args : 
          Recibe como parametro la profundidad  del lago y la fila del iterador. 

        """  
        match valor:
            case valor if valor<=17: 
                fila.append('chico')
            case valor if valor>= 18 and valor<=59:
                fila.append('medio')
            case valor if valor >59: 
                fila.append('grande')



def conversion(grados,minutos,segundos):
    """
    Lo que hace es calcular la latitud y/o longitud recibiendo como parametros 
    (grados- minutos - segundos).

    GD = grados +(mintutos / 60) + (segundos/3600)  y al ser (O y S) el res va en negativo por convencion. 
    
    Args: 
      recibe los grados, minutos y segundos.
    
    Returns: 
      el resultado del calculo de GD.
    """
    return float((grados +(minutos /60) + (segundos/3600))*-1)


def process(reader,writer):
    """
    Modulo que realiza el proceso de completar las nuevas columnas , procesando las filas del archivo 
    y completando  asi estos nuevos valores realiazando los calculos necesarios.

    Args: 
      el iterador del archivo de lagos, el nuevo archivo para escribir en el.
    """

    coordenadas = 5
    superficie = 2

    for row in reader:
        # En valor tomo las coordenadas
        valor = row[coordenadas]
        
        # En res tengo una lista de los numeros como str.
        res = re.findall(r'\d+',valor)
        
        la = conversion(float(res[0]),float(res[1]),float(res[2]))
        lo = conversion(float(res[3]),float(res[4]),float(res[5]))
        
        # una vez que calculo agrego
        row.append(la)
        row.append(lo) 


        # Ahora llenamos segun los criterios de superficie :
        # En valor guardo la superficie y la convierto en entero
        valor = int(row[superficie])
        
        match_surface(valor,row)
    
        # Una vez que terminamos de completar todo escribimos el renglon: 
        writer.writerow(row)

def process_conectividad(reader,writer):
    
    for row in reader:

        #Reemplazo los '--' por 'NO' para asi agregarlos modificados en el writer. 
        """Creo una lista, que, por comprension, tomara los valores por defecto de la linea que se esta iterando. Salvo
           que esta tenga como valor '--', en ese caso reemplazara ese valor por 'NO'.

        Recibiendo como parametros el iterador de conectividad y el nuevo archivo para escribirlo.
        
        """
        write_line = ['NO' if valor == '--' else valor for valor in row] 

        #En la nueva columna (posee conectividad) se agregara 'SI' o 'NO' dependiendo del caso
        if 'SI' not in row:
            write_line.append('NO')
        else:
            write_line.append('SI')

        #Agrego la nueva linea ya modificada en el writer.
        writer.writerow(write_line)


def percent (new_row,writer,street,tot):
        
    """
       A partir de la fila actualizada (sin '///' o '-') trabajo para calcular el porcentaje
       de población en situación de calle para cada jurisdicción.

       Args:
          Recibe una fila actualizada que es una lista, writer para agregar el porcentaje
          y street/tot que son los indices que representan el total de poblacion
          y la poblacion en situacion de calle que necesito para calcular.

       Returns:
          Retorna el writer actualizado con los porcentajes.   
     """    

    if int(new_row[tot])!= 0: #verifico NO estar dividiendo por 0
       tot_por = int(new_row[street])/int(new_row[tot])*100 #utilizo fila actualizada porque es la que tiene los valores reemplazados
       new_row.append(tot_por) #añado el porcentaje 
            
    else:
       None # no existe el caso de que una poblacion tenga 0 habitantes  


def poblation_process (reader, writer):
    
    """
       Trabajo a partir de los archivos reader y writer;
       a medida que voy leyendo del reader, modifico en el writer, intercambio en los campos que haya '///' o 
       '-' por 0. Luego añado una columna al archivo que es el porcentaje de poblacion en situación de calle.

       Args:
          Recibe como parametro un reader y un writer del csv.

       Returns:
          Retorna un nuevo archivo csv modificado con el original.   
     """    
    
    street = 4 # me guardo los indices
    tot = 1
    
    for row in reader: 
         
         new_row = [value.replace('///', '0').replace('-', '0') for value in row] #reemplazo los valores en caso de que sean /// o -, caso contrario se deja el que esta
         percent(new_row, writer, street, tot) 
         writer.writerow(new_row) #se añade la fila actualizada

