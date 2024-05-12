import json 

def verify(user, name, mail, gender):
    """ 
    Este módulo verifica que todos los campos estén completos. 

    Args: 
      user: El username del usuario. 
      name: El nombre del usuario. 
      mail: El mail del usuario. 
      gender: El género del usuario. 
    
    Returns: 
      Boolean: Retorna True si todos los campos están completos y False en el caso contrario.
    """
    if user.strip() and name.strip() and mail.strip() and gender.strip():
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

def new_user(user, name, mail, gender):
  """ 
  Este módulo crea un nuevo usuario con la información proporcionada. 

  Args: 
    user: El username del usuario. 
    name: El nombre del usuario. 
    mail: El mail del usuario. 
    gender: El género del usuario. 

  Returns
    user_data: Un diccionario que contiene la información del usuario.
    Las claves son: "User", "Name", "Mail" y "Gender".
  """
  user_data = {
      'User': user,
      'Name': name,
      'Mail': mail,
      'Gender': gender, }
  return user_data 


def add_user(new_user, user_data):
    """ 
    Módulo que añade los datos de un nuevo usuario a un archivo json o, si el mail 
    ya se encuentra en el archivo, actualiza sus datos. 

    Args: 
      new_user: Un diccionario con la información del usuario. Las claves son:
      "Mail", "Name", "Birth", "Gender". 
      user_data: El archivo json.
    
    Returns: 
      None
    """
    email_exists = False
    users_data = []

    # Verifico si el archivo existe
    if user_data.exists():
        # Cargo los datos existentes del archivo json
        with user_data.open("r") as file:
            try:
                users_data = json.load(file)
            except json.JSONDecodeError:
                # Manejo el caso de un archivo vacío
                pass
        # Verifico si el correo electrónico ya está en los datos del archivo
        for i in range(len(users_data)):
            user=users_data[i]
            if user.get("Mail") == new_user.get('Mail'):
                users_data[i]=new_user # Actualizo datos del archivo existente
                email_exists= True 
                break     

    # Si el correo electrónico no está presente, agrego el nuevo usuario
    if not email_exists:
        users_data.append(new_user)

    # Guardo los datos actualizados en el archivo
    with user_data.open("w") as file:
        json.dump(users_data, file, indent=4)
