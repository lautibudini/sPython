# Proyecto grupo 21 💻

## integrantes :
- Candela Cáceres
- Camila Corbalán Saez
- Leandro Ezequiel Arrieta
- Lautaro Tomas Budini

### Sobre nuestro proyecto: 
Nuestro proyecto se enfoca en el análisis de diversos conjuntos de datos proporcionados previamente, cada uno con nombre y contenido distintivo. A partir de estos conjuntos de datos originales, creamos archivos nuevos en los que modificamos la información según las necesidades de nuestro análisis. Incorporamos nuevas categorías a los encabezados acompañadas de valores calculados durante el procesamiento de los datos originales. 

Una vez que los archivos nuevos se crean, nuestro proyecto ofrece la posibilidad de realizar consultas sobre ellos. Algunas de estas consultas requieren la interacción del usuario, quien proporcionará ciertos valores necesarios para el correcto funcionamiento de la consulta. 

Estos nuevos archivos serán implementados en un juego que estamos desarrollando. Este último fue creado utilizando el framework "Streamlit", presenta un menú que ofrece cuatro opciones. Sin embargo, por el momento, solo dos de estas opciones están funcionando, la pantalla de inicio y un formulario interactivo.

El formulario permite al usuario ingresar su información personal, la cual se almacena en un nuevo archivo JSON que creamos con dicho propósito. En caso de que el mail del usuario ya esté registrado, los datos anteriores se sobreescriben con la nueva información proporcionada. Si el mail no fue usado anteriormente, se agrega como un nuevo usuario.

# Pasos a seguir para poder ejecutar el  proyecto

### Debemos crear un entorno virtual en nuestros archivos  🗂️.

#### - Creación del entorno para windows y linux : 
- Como primer paso debemos crear una carpeta nueva.
- Una vez ya creada la carpeta debemos hacer uso de la herramienta GitBash , posicionandonos con el comando    cd ...nombre de carpeta... .
- Ahora crearemos un directorio virtual llamado 'venv' para poder instalar todas las extenciones necesarias, Con el comando python -m venv venv.

#### - Activacion del Entorno Virtual en Windows: 
- Para activarlo debemos ejecutar este comando parados en la    carpeta: source venv/Scripts/activate .
- Cuando ya no lo usemos mas, lo desactivamos con el comando : deactivate  .


#### - Activacion del Entorno Virtual en Linux:
- Para activarlo debemos ejecutar este comando parados en la carpeta : source venv/bin/activate .
- Cuando ya no lo usemos mas, lo desactivamos con el comando : deactivate

### Una vez que tenemos el entorno virtal debemos clonar  a nuestra carpeta donde esta nuestro entorno virtual, el proyecto asi podemos ejecutarlo.

- Como primer paso debemos tener la url del repositorio, entrando a gitlab para ubicarla.
- Luego con Bash parados en nuestra carpeta donde tenemos el entorno virtual, debemos ejecutar el comando : git clone ..url.. , luego de esto vamos a tener el proyecto en nuestra carpeta.
- Si en algun futuro hay alguna actualizacion debemos ejecutar en comando : git pull .

## Ya teniendo el proyecto lo que queda es elegir nuestro editor de codigo favorito, en este caso explicaremos con VSCODE 🖥️.




### Cómo funcionan los archivos Jupyter Notebook : 
- Los archivos jupyter son los que terminan con la extencion '.ipynb' , estos se caracterizan por tener celdas 'MarkDown' donde es posible poner un bloque de texto, utilizado para poder explicar pasos importantes en nuestro algoritmo, sobre que trata el siguente bloque de codigo y/o demas cosas. 
- Tambien tenemos celdas o bloques de codigo donde ahi se ejecutan los codigos en lenguaje 'python' en este caso.
- Por cada bloque de markdown y bloque de codigo va a haber distintos procedimientos los cuales representan un inciso. 

### Extensiones de VSCode para estos archivos : 
- Para poder ejecutar nuestros archivos de jupyter y de python, debemos tener instaladas extensiones en vscode que nos ayudaran a esto. Al querer ejecutarlos, vsCode nos recomienda extensiones necesarias y basicas, si es que no las tenemos instaladas. Aquí dejamos algunas: 

- Para Jupyter : Jupyter - Jupyter Cell Tags - Jupyter Keymap - Jupyter Slide Show- Jupyter Notebook Renderers. 
- Para python  :  Python - Python Debugger - Pylance.

### Ejecucion del los jupyter : 

- Primero debemos ejecutar las primeras celdas de los dos archivos jupyter , que son : 
-  LIBRERIAS :  las librerias poseen funciones ya predefinidas que nos serviran a lo largo del proyecto para facilitar el desarrollo del mismo. 
- RUTAS : las rutas nos sirven para poder trabajar con los archivos y poder ubicarlos, en este caso modificamos las rutas para que en cualquier sistema operativo se encuentre el archivo del proyecto, ya que dependiendo el SO pueden llegar a cambiar algunos comandos.

- Una vez ya ejecutadas estas celdas mencionadas anteriormente, podemos ejecutar el primer archivo 'Procesamiento.ipynb' lo que hace es trabajar en cada inciso con distintos archivos proporcionados, agregando nueva informacion importante para luego poder trabajar con estos en el segundo jupyter 'Consultas.ipynb' en el cual, como el nombre lo indica hay varios inicisos que filtran el contenido de estos archivos para así informar distintos datos de estos.

### Ejecucion de la aplicacion web : 
- Para poder abrir la aplicacion lo que debemos hacer es, En este caso explicado con vscode podemos abrir su terminal y poner el comando [streamlit run 1_Inicio.py] donde 1_Inicio.py es el nombre de la aplicación.

