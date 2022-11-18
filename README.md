# BCN_data

## Autora
Almudena Ramírez Haro

## Database
https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets (immigrants_by_nationality.csv, population.csv y unemployment.csv)

Adicionalmente, teniendo en mente el objetivo del proyecto, se creó una collection uniendo el número de personas migrantes, número de desempleados y total población de los distintos barrios de Barcelona en el año 2017. Esto se hizo empleando las funciones "$match", "$group" y "$merge".

## Descripción
Relación de gente inmigrante y de gente desempleada en los distintos barrios y distritos de Barcelona con respecto a la población total.

Teniendo en cuenta la población total por barrio y distrito, y dado un año determinado, representación de la población inmigrante (teniendo en cuenta su nacionalidad) y de la población desempleada.

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
* Tener en cuenta otras variables: utilizar otros años, poder filtrar por distritos...
* Utilizar webscrapping para actualizar el database con años posteriores
* Emplear geoqueries para mostrar las gráficas encima de los barrios (ejemplo: https://streamlit-demo-uber-nyc-pickups-streamlit-app-456wus.streamlit.app/)
* Subirlo a cloud services