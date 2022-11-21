# Relación entre la tasa de inmigración y la de desempleo en los barrios de Barcelona en 2017
<b>Autora:</b> Almudena Ramírez Haro

![Barrios y distritos de Barcelona](./imagen/barcelona.png?raw=true "Barrios y distritos de Barcelona")


## Database
https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets (immigrants_by_nationality.csv, population.csv y unemployment.csv)

Adicionalmente, teniendo en mente el objetivo del proyecto, se creó una collection uniendo el número de personas migrantes, número de desempleados y total población de los distintos barrios de Barcelona en el año 2017. Esto se hizo empleando las funciones "$match", "$group" y "$merge".


## Descripción
Teniendo en cuenta la población total por barrio y distrito en el 2017, se realiza una representación visual de la población inmigrante y de la población desempleada de Barcelona.


## Flujo de trabajo seguido para crear el proyecto
1. Se descargaron los tres csv de kaggle.com y se subieron a Mongodb.
2. Desde Mongodb establecí conexión con un jupyter notebook para hacer un análisis exploratorio de los datos y comprobar que estaban bien. En este caso, la base de datos está muy bien hecha, así que no hizo falta tocarlos.
3. Creé la API y los routers (estos se fueron añadiendo o eliminando a lo largo del proyecto en función de la necesidad), y los conecté con la base de datos de mongo.
4. A continuación, con una idea de cómo iba a orientar el proyecto, creé otra colección en Mongodb a partir de las tres anteriores. Para esto tomé una serie de decisiones, como utilizar solamente un año, ya que en la colección de inmigrantes había menos años registrados que en el resto y por cuestión de tiempo. Agrupé las colecciones en función de lo que tenían en común: los barrios de Barcelona, y, utilizando un '$merge', agrupé el número total de inmigrantes, desempleados y población de cada barrio. Por cuestiones de tiempo tampoco tomé variables como nacionalidad, género o demanda de empleo específicas de cada una de las colecciones originales.
5. Empecé el streamlit creando gráficas para filtrar según variables propias de los datos de inmigración y desempleo, pudiendo observar la nacionalidad de la gente inmigrante o la cantidad de personas demandando empleo activamente en función de los barrios. Por último, tomando la colección hecha por mí, realicé unas gráficas donde se pudiera visualizar una comparativa de inmigración-desempleo-población total según el barrio. 


## Elementos del proyecto
Este proyecto contiene tres carpetas principales: api, data y streamlit. La de data contiene todos los archivos csv así como el jupyter notebook que se empleó para el análisis exploratorio de los datos. Por otra parte, en "api" se encuentran, principalmente, la conexión con la base de datos en mongo (subcarpeta database), la subcarpeta con distintos routers separados en ficheros según la collección a la que acceda y el fichero principal. En streamlit están las conexiones con la API y el programa para generar las gráficas (subcarpeta data), y el fichero principal que contiene la estructura del dashboard.


## Cómo se ejecuta el proyecto
En el documento "requirements.txt" están los programas y sus versiones utilizados para crear el proyecto.

### Ejecutar API
Abrir terminal y ejecutar el fichero `run_api.sh`

```bash
./run_api.sh
```

### Ejecutar streamlit
En el terminal, ejecutar el fichero `streamlit_main.py`

```bash
streamlit run 'streamlit_main.py'
```

## Ideas para un futuro
* Tener en cuenta otras variables (por ejemplo el año)
* Separar los datos en páginas: 'Home', 'Inmigración', 'Desempleo', 'Relación por barrios'
* Utilizar webscrapping para actualizar el database con años posteriores
* Emplear geoqueries para mostrar las gráficas encima de los barrios (ejemplo: https://streamlit-demo-uber-nyc-pickups-streamlit-app-456wus.streamlit.app/)
* Subirlo a cloud services