import streamlit as st
from data.st_data import get_total_immigrants, get_total_unemployed, get_total, all_neigh, immigrants_nationality, get_neighborhoods
from data.graphs import  total_barrio, sub_pl, desempl_barrio, inmi_barrio, graph_inmigrantes
import pandas as pd
import time

st.set_page_config(layout="wide")

def formato1(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)

def formato2(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:left;">{text}</h1>',unsafe_allow_html=True)

def header(text):
        st.markdown(f"<p style='color:white;'>{text}</p>",unsafe_allow_html=True)



#### --------------------------------------------INTRO--------------------------------------------
formato1("Inmigración y desempleo en los barrios de Barcelona en 2017", 50, "white")
    
st.text("Este proyecto pretende mostrar la tasa de desempleo e inmigración en relación con\nla población total de Barcelona en el año 2017.")
st.text("Para ello se toman como variables independientes los barrios o distritos de\nBarcelona, y como variables independientes, la cantidad de población pertenecientes\nal grupo de inmigrantes, desempleados o el total.\nTambién se tendrá en cuenta el año de recogida de datos.")


#### --------------------------------------------INMIGRANTES--------------------------------------------
formato1("Análisis de inmigración", 35, "white")  
st.text("asfasfsbdvadc")

formato2("Datos de inmigración en función del barrio", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

#barrio = st.selectbox("Select one neigborhood to search", all_neigh())
#data = immigrants_nationality(barrio)
#st.write(data)

formato2("Datos de desempleo en función del distrito", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

formato2("Datos de inmigración en función de la nacionalidad", 20, "grey") #no hacer dropdown con la nacionalidad-> demasiado largo. Hacer input text
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

graph_inmigrantes()


#### --------------------------------------------DESEMPLEO--------------------------------------------
formato1("Análisis de desempleo", 35, "white")  
st.text("ADFFgsffsadxwe")

formato2("Datos de desempleo en función del barrio", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

formato2("Datos de desempleo en función del distrito", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

formato2("Datos de desempleo en función del género", 20, "grey") 
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

formato2("Datos de desempleo en función del mes", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")


#### --------------------------------------------POBLACIÓN--------------------------------------------
formato1("Análisis de la población", 35, "white")  
st.text("ajklceinhksmxz")

formato2("Datos de población en función del barrio", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")


formato2("Datos de población en función del distrito", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

formato2("Datos de población en función del género", 20, "grey") 
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")

formato2("Datos de población en función del rango de edad", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")


#### --------------------------------------------CONCLUSIONES--------------------------------------------


formato1("Relación de los datos", 35, "white")       
st.text("blah blah blah")


#presentación datos en gráficos

formato2("Relación de los barrios con la tasa de inmigración, desempleo y población total", 20, "grey")
col1, col2, col3 = st.columns(3)
with col1:
    inmi_barrio()
with col2:
    desempl_barrio()
with col3:
    total_barrio()

sub_pl()
