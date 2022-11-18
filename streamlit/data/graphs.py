import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from data.st_data import all_neigh, get_neighborhoods



def data_fr():
    pag = [1,2,3,4,5,6,7]
    n = st.selectbox("See page:", pag)
    df = pd.DataFrame.from_dict(get_neighborhoods(n))
    barrios = []
    inmigrantes = []
    desempleados = []
    poblacion = []
    for d in df["results"]:
        for v in d:
            for i in v:
                if "_id" == i:
                    barrios.append(v["_id"])
                elif "Total Immigrants" == i:
                    inmigrantes.append(v["Total Immigrants"])
                elif "Total Population" == i:
                    poblacion.append(v["Total Population"])
                elif "Total Unemployed" == i:
                    desempleados.append(v["Total Unemployed"])
    
    fig = go.Figure(
                data=[go.Bar(x=barrios, y=inmigrantes)],
                layout_title_text="Barrios - inmigrantes")
    st.write(fig)




#prueba
def graphs_concl():
    df = pd.DataFrame(get_neighborhoods())
    x = all_neigh()
    y = df["Total Population"]
    st.line_chart(df, x, y , width=0, height=0, use_container_width=True)