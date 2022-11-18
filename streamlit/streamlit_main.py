import streamlit as st
from data.st_data import get_total_immigrants, get_total_unemployed, get_total, all_neigh, immigrants_nationality
from data.graphs import total_immigrants, graphs_concl
from data.tables import tablas_conclusiones
from pages.pag_conclusion import conclus_page
import pandas as pd
import time

pf = pd.DataFrame()




def title(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)

def header(text):
    st.markdown(f"<p style='color:white;'>{text}</p>",unsafe_allow_html=True)


#pagina Home-> explicación del dashboard, cómo funciona y los datos
title("Inmigración y desempleo en los barrios de Barcelona en 2017", 50, "white")
   
st.text("Este proyecto pretende mostrar la tasa de desempleo e inmigración en relación con\nla población total de Barcelona en el año 2017.")
st.text("Para ello se toman como variables independientes los barrios o distritos de\nBarcelona, y como variables independientes, la cantidad de población pertenecientes\nal grupo de inmigrantes, desempleados o el total.\nTambién se tendrá en cuenta el año de recogida de datos.")


#pagina inmigrantes-> pequeña introducción, data visualitation
st.text("asfasfsbdvadc")

st.header("Datos de inmigración en función del barrio")

#barrio = st.selectbox("Select one neigborhood to search", all_neigh())
#data = immigrants_nationality(barrio)
#st.write(data)

st.header("Datos de inmigración en función del distrito")

st.header("Datos de inmigración en función de la nacionalidad") #no hacer dropdown con la nacionalidad-> demasiado largo. Hacer input text

st.header("Datos de inmigración en función del año")


#pagina desempleados-> pequeña introducción, data visualitation
st.text("ADFFgsffsadxwe")

st.header("Datos de desempleo en función del barrio")

st.header("Datos de desempleo en función del distrito")

st.header("Datos de desempleo en función del género") 

st.header("Datos de desempleo en función de la fecha")


#pagina población-> pequeña intro y data
st.text("ajklceinhksmxz")

st.header("Datos de población en función del barrio")

st.header("Datos de población en función del distrito")

st.header("Datos de población en función del género") 

st.header("Datos de población en función del rango de edad")

st.header("Datos de población en función del año")

#### --------------------------------------------CONCLUSIONES--------------------------------------------

title("Conclusiones", 35, "white")
st.text("blah blah blah")

#presentación datos en tablas
tablas_conclusiones()

graphs_concl()


