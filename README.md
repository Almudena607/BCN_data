# BCN_data

![Barrios y distritos de Barcelona](./imagen/barcelona.png?raw=true "Barrios y distritos de Barcelona")

<b>Autora:</b> Almudena Ramírez Haro


## Database
https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets (immigrants_by_nationality.csv, population.csv y unemployment.csv)

Adicionalmente, teniendo en mente el objetivo del proyecto, se creó una collection uniendo el número de personas migrantes, número de desempleados y total población de los distintos barrios de Barcelona en el año 2017. Esto se hizo empleando las funciones "$match", "$group" y "$merge".


## Descripción
Relación de gente inmigrante y de gente desempleada en los distintos barrios y distritos de Barcelona con respecto a la población total.

Teniendo en cuenta la población total por barrio y distrito, y dado un año determinado, representación de la población inmigrante (teniendo en cuenta su nacionalidad) y de la población desempleada.


## Flujo de trabajo seguido para crear el proyecto
1. Se descargaron los tres csv de kaggle.com y se subieron a Mongodb.
2. Creé la API y los routers (estos se fueron añadiendo o eliminando a lo largo del proyecto en función de la necesidad).
3. Desde Mongodb establecí conexión con la API y con un jupyter notebook para hacer un análisis exploratorio de los datos y comprobar que estaban bien. En este caso, la base de datos está muy bien hecha, así que no hizo falta tocarlos.
4. A continuación, con una idea de cómo iba a orientar el proyecto, creé otra colección en Mongodb a partir de las tres anteriores. Para esto tomé una serie de decisiones, como utilizar solamente un año, ya que en la colección de inmigrantes había menos años registrados que en el resto y por cuestión de tiempo. Agrupé las colecciones en función de lo que tenían en común: los barrios de Barcelona, y, utilizando un '$merge', agrupé el número total de inmigrantes, desempleados y población de cada barrio. Por cuestiones de tiempo tampoco tomé variables como nacionalidad, género o demanda de empleo específicas de cada una de las colecciones originales.
5. Empecé el streamlit creando gráficas para filtrar según variables propias de los datos de inmigración y desempleo, pudiendo observar la nacionalidad de la gente inmigrante o la cantidad de personas demandando empleo activamente en función de los barrios. Por último, tomando la colección hecha por mí, realicé unas gráficas donde se pudiera visualizar una comparativa de inmigración-desempleo-población total según el barrio. 


## Cómo se ejecuta el proyecto
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