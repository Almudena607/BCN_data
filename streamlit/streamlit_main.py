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


#### --------------------------------------------INMIGRANTES--------------------------------------------
formato1("Análisis de inmigración", 35, "white")  
st.text("asfasfsbdvadc")

formato2("Datos de inmigración en función del barrio", 20, "grey")
st.text("Edkeihneirhutndwdbhfhdbwebewnshnbjwnhs")
barrio_inmigrantes()

formato2("Datos de inmigración en función de la nacionalidad", 20, "grey") #no hacer dropdown con la nacionalidad-> demasiado largo. Hacer input text
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")
distrito_inmigrantes()


#### --------------------------------------------DESEMPLEO--------------------------------------------
formato1("Análisis de desempleo", 35, "white")  
st.text("ADFFgsffsadxwe")

formato2("Datos de demanda de empleo en función del barrio", 20, "grey")
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")
barrio_desempleo() 

formato2("Datos de desempleo en función del género", 20, "grey") 
st.text("ldjfkjnsdlknsfln kaf jnñlwdxc asc kbñ\nñlsejcfamdñlakjdx ñalkfjnñalj\nñadkgnjvlalifneopr80`9rquw")
genero_desempleo()

#### --------------------------------------------CONCLUSIONES--------------------------------------------


formato1("Relación de los datos", 35, "white")       
st.text("Por último, se ha creado una nueva database partiendo del documento 'Number' de las tres originales y que todas tenían en común la clasificación por barrios.")
st.text("Para mostrar estos datos se tomó como variable dependiente los barrios de Barcelona. Las variables independientes fueron\nla cantidad de población pertenecientes al grupo de inmigrantes, desempleados o el total.")



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
