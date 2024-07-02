# Proyecto grupo 21 💻

## integrantes :
- Candela Cáceres
- Camila Corbalán Saez
- Leandro Ezequiel Arrieta
- Lautaro Tomas Budini

### Sobre nuestro proyecto: 

Nuestro proyecto es un juego de trivia que utiliza diversos datasets como fuente de preguntas. Los jugadores pueden elegir una temática específica y su nivel de dificultad antes de comenzar. Cada cuestionario consta de 5 preguntas, donde los jugadores deben responder basándose en los primeros 4 datos proporcionados para cada pregunta.

Al finalizar el juego, los jugadores pueden revisar sus respuestas y explorar un ranking histórico que muestra a los mejores jugadores.

Además, el juego cuenta con una sección dedicada a datos en la página 2, que incluye gráficos informativos sobre aeropuertos y lagos, así como mapas que permiten a los jugadores explorar y conocer estos datos antes de participar en la trivia. La página 6 ofrece una sección de estadísticas, donde se analizan los resultados de las partidas según diferentes criterios como el género de los jugadores y la dificultad de las temáticas,  proporcionando análisis adicionales basados en los datos recopilados.

# Pasos a seguir para poder ejecutar el  proyecto

### Debemos crear un entorno virtual en nuestros archivos  🗂️.

#### - Creación del entorno para windows y linux : 
- Como primer paso debemos crear una carpeta nueva.
- Una vez ya creada la carpeta debemos hacer uso de la herramienta GitBash , posicionandonos con el comando: 
```bash
    cd nombre-carpeta-creada
```
- Ahora crearemos un directorio virtual llamado 'venv' para poder instalar todas las extenciones necesarias, Con el comando: 
```bash
    python -m venv venv
```

#### - Activacion del Entorno Virtual en Windows: 
- Para activarlo debemos ejecutar este comando parados en la    carpeta:
```bash
    source venv/Scripts/activate
```
- Cuando ya no lo usemos mas, lo desactivamos con el comando : 
```bash
    deactivate
```

#### - Activacion del Entorno Virtual en Linux:
- Para activarlo debemos ejecutar este comando parados en la carpeta : 
```bash
    source venv/bin/activate
```
- Cuando ya no lo usemos mas, lo desactivamos con el comando :
```bash
    deactivate
```

### Una vez que tenemos el entorno virtal debemos clonar  a nuestra carpeta donde esta nuestro entorno virtual, el proyecto asi podemos ejecutarlo.

- Como primer paso debemos tener la url del repositorio, entrando a gitlab para ubicarla.
- Luego con Bash parados en nuestra carpeta donde tenemos el entorno virtual, debemos ejecutar el comando :
```bash
    git clone https://gitlab.catedras.linti.unlp.edu.ar/python2024/code/grupo21.git
```
 En este caso esa seria la url, luego de esto vamos a tener el proyecto en nuestra carpeta.
- Si en algun futuro hay alguna actualizacion debemos ejecutar en comando :
```bash
    git pull
```

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
- Antes de la ejecución de la apliación debemos instalarnos las librerias necesarias para su ejecución con el siguiente comando :
```bash
    pip install requirements.txt
```
- Para poder abrir la aplicacion debemos, en este caso explicado con vscode abrir su terminal y poner el comando:
```bash
    streamlit run 1_inicio.py
```
donde '1_Inicio.py' es el nombre de la pagina principal.

