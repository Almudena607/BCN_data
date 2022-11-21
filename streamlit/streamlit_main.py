import streamlit as st
from data.graphs import  total_barrio, sub_pl, desempl_barrio, inmi_barrio, distrito_inmigrantes, barrio_desempleo, barrio_inmigrantes, genero_desempleo


st.set_page_config(layout="wide")

def formato1(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)

def formato2(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:left;">{text}</h1>',unsafe_allow_html=True)




#### --------------------------------------------INTRO--------------------------------------------
formato1("Inmigración y desempleo en los barrios de Barcelona en 2017", 50, "white")
    
formato1("Este proyecto pretende mostrar la tasa de desempleo e inmigración en relación con la población total de Barcelona en el año 2017.", 20, "white")

formato1("Leyenda de distritos y barrios de Barcelona", 35, "white")  
col1, col2, col3 = st.columns(3)
with col1:
    st.text("1. Ciudad Vieja:\n 1.1. El Raval\n 1.2. Barrio Gótico\n 1.3. La Barceloneta\n 1.4. Sant Pere, Santa Caterina i la Ribera\n\n2. L'Eixample:\n 2.1. El Fort Pienc\n 2.2. Sagrada Familia\n 2.3. La Dreta de L'Eixample\n 2.4. Antiga Esquerra de l'Eixample\n 2.5. Nova Esquerra de l'Eixample\n 2.6. Sant Antoni\n\n3. Sants-Montjuïc:\n 3.1. El Poble Sec\n 3.2. La Marina del Prat Vermell\n 3.3. La Marina de Port\n 3.4. La Font de la Guatlla\n 3.5. Hostafrancs\n 3.6. La Bordeta\n 3.7. Sants-Badal\n 3.8. Sants\n 3.9. Parc de Montjuic\n 3.10. Zona Franca-Port\n\n4. Les Corts\n 4.1. Les Corts\n 4.2. La Maternitat i San Ramón\n 4.3. Pedralbes")
with col2:
    st.text("5. Sarrià-Sant Gervasi:\n 5.1. Vallvidrera, Tibidabo i les Planes\n 5.2. Sarrià\n 5.3. Las Tres Torres\n 5.4. Sant Gervasi-Bonanova\n 5.5. Sant Gervasi-Galvany\n 5.6. El Putget i Farró\n\n6. Gràcia:\n 6.1. Vallcarca i els Penitents\n 6.2. El Coll\n 6.3. La Salut\n 6.4. Vila de Gràcia\n 6.5. El Camp d’en Grassot i Gràcia Nova\n\n7. Horta-Guinardó:\n 7.1. Baix Guinardó\n 7.2. Can Baró\n 7.3. El Guinardó\n 7.4. La Font d’en Fargues\n 7.5. El Carmel\n 7.6. La Teixonera\n 7.7. Sant Genís dels Agudells\n 7.8. Montbau\n 7.9. La Vall d’Hebron\n 7.10. La Clota\n 7.11. Horta")
with col3:
    st.text("8. Nou Barris:\n 8.1. Vilapicina-Torre Llobeta\n 8.2. Porta\n 8.3. El Turó de la Peira\n 8.4. Can Peguera\n 8.5. La Guineueta\n 8.6. Canyelles\n 8.7. Les Roquetes\n 8.8. Verdun\n 8.9. La Prosperitat\n 8.10. La Trinitat Nova\n 8.11. Torre Baró\n 8.12. Ciudat Meridiana\n 8.13. Vallbona\n\n9. Sant Andreu:\n 9.1. La Trinitat Vella\n 9.2. Baró de Viver\n 9.3. El Bon Pastor\n 9.4. Sant Andreu\n 9.5. La Sagrera\n 9.6. El Congrés i els Indians\n 9.7. Navas\n\n10. Sant Martí:\n 10.1. El Camp de l’Arpa del Clot\n 10.2. El Clot\n 10.3. El Parc i la Llacuna del Poblenou\n 10.4. La Vila Olímpica del Poblenou\n 10.5. El Poble Nou\n 10.6. Diagonal Mar i Front Marítim del Poblenou\n 10.7. El Besòs i el Maresme\n 10.8. Provençals del Poblenou\n 10.9. Sant Martí de Provençals\n 10.10. La Verneda i la Pau")

#### --------------------------------------------INMIGRANTES--------------------------------------------
formato1("Análisis de inmigración", 35, "white")  
st.text("Para el análisis de datos de las personas inmigrantes se empleó el csv 'immigrants_by_nationality.csv' de la base de datos. Este está compuesto por siete columnas\n(año, distritos (código y nombre), barrios (código y nombre), nacionalidad y número de inmigrantes), de forma que la combinación de las primeras seis daba un\nnúmero diferente de personas inmigrantes.")

formato2("Datos de inmigración en función del barrio", 20, "grey")
st.text("Según el distrito seleccionado, se mostrarán en la gráfica sus barrios y la nacionalidad de las personas inmigrantes que estaban registradas en el 2017.")
barrio_inmigrantes()

formato2("Datos de inmigración en función de la nacionalidad", 20, "grey")
st.text("Al seleccionar una nacionalidad, se mostrarán los distritos y, dentro de cada uno, el números de inmigrantes de esa nacionalidad en cada barrio.")
distrito_inmigrantes()


#### --------------------------------------------DESEMPLEO--------------------------------------------
formato1("Análisis de desempleo", 35, "white")  
st.text("A continuación se muestran la visualización de los datos de desempleo, sacados de 'unemployment.csv'. El archivo tiene la misma estructura que los datos\nde inmigración, aunque sin datos de nacionalidad y con entradas para el mes el registro, el género y si es solamente desempleado o está en búsqueda activa de empleo.") 


formato2("Datos de demanda de empleo en función del barrio", 20, "grey")
st.text("Según el distrito seleccionado, se mostrarán en la gráfica sus barrios y si estaban registados en búsqueda activa de empleo o no en el 2017.")
barrio_desempleo() 

formato2("Datos de desempleo en función del género", 20, "grey") 
st.text("Según el distrito seleccionado, se mostrarán en la gráfica sus barrios y  el género de las personas desempleadas registradas en 2017.")
genero_desempleo()

#### --------------------------------------------CONCLUSIONES--------------------------------------------


formato1("Relación de los datos", 35, "white")       
st.text("Por último, estos datos partieron de la colección creada a partir de las tres originales.")
st.text("Para mostrar estos datos se tomó como variable dependiente los barrios de Barcelona. Las variables independientes fueron\nla cantidad de población pertenecientes al grupo de inmigrantes, desempleados o el total.")



formato2("Relación de los barrios con la tasa de inmigración, desempleo y población total", 20, "grey")
col1, col2, col3 = st.columns(3)
with col1:
    inmi_barrio()
with col2:
    desempl_barrio()
with col3:
    total_barrio()

sub_pl()
