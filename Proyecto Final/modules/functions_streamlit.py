import json
from pathlib import Path
from datetime import datetime

def verify(user, name, mail, gender, birth_date):
    """ 
    Este módulo verifica que todos los campos estén completos. 

    Args: 
      user: El username del usuario. 
      name: El nombre del usuario. 
      mail: El mail del usuario. 
      gender: El género del usuario.
      birth_date: La fecha de nacimiento del usuario.

    Returns: 
      Boolean: Retorna True si todos los campos están completos y False en el caso contrario.
    """
    if user.strip() and name.strip() and mail.strip() and gender.strip() and birth_date:
        return True
    return False

def verifymail(mail):
    """ 
    Este módulo verifica que el mail sea válido, comprobando si contiene un arroba. 
    
    Args: 
      mail: El mail del usuario. 

    Returns: 
      Boolean: Retorna True si en el mail hay un único arroba, False en el caso contrario. 
    """
    if mail.strip() and mail.strip().count('@') == 1:
        return True
    return False

def new_user(user, name, gender, birth_date):
    """ 
    Este módulo crea un nuevo usuario con la información proporcionada. 

    Args: 
      user: El username del usuario. 
      name: El nombre del usuario. 
      gender: El género del usuario.
      birth_date: La fecha de nacimiento del usuario.

    Returns:
      user_data: Un diccionario que contiene la información del usuario.
      Las claves son: "User", "Name", "Gender" y "BirthDate".
    """
    user_data = {
        'User': user,
        'Name': name,
        'Gender': gender,
        'BirthDate': birth_date.strftime('%Y-%m-%d')
    }
    return user_data 

def add_user(mail, new_user, user_data_path):
    """ 
    Módulo que añade los datos de un nuevo usuario a un archivo json o, si el mail 
    ya se encuentra en el archivo, actualiza sus datos. 

    Args: 
      mail: El mail del usuario. 
      new_user: Un diccionario con la información del usuario. Las claves son:
      "User", "Name", "Gender", "BirthDate".
      user_data_path: La ruta al archivo json.
    
    Returns: 
      None
    """
    users_data = {}

    # Verifico si el archivo existe
    if user_data_path.exists():
        # Cargo los datos existentes del archivo json
        with user_data_path.open("r") as file:
            try:
                users_data = json.load(file)
            except json.JSONDecodeError:
                # Manejo el caso de un archivo vacío
                pass

    # Agrego o actualizo el usuario en el diccionario
    users_data[mail] = new_user

    # Guardo los datos actualizados en el archivo
    with user_data_path.open("w") as file:
        json.dump(users_data, file, indent=4)