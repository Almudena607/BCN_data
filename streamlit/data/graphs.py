import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from data.st_data import all_neigh, get_neighborhoods, get_immigrants_nationality
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as pe
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

#--------------------------------------------GRÁFICOS INMIGRACIÓN------------------------------- 
def graph_inmigrantes():
    nationality = st.text_input('Write the name of the country in English (e.g.: Spain)')
    df = pd.DataFrame.from_dict(get_immigrants_nationality(nationality))                ###### !!!! ValueError: If using all scalar values, you must pass an index
    distritos = []
    inmigrantes = []
    nacionalidad = []
    barrio = []
    for d in df["results"]:
        for v in d:
            for i in v:
                if "Nationality" == i:
                    distritos.append(v["District Name"])
                elif "Number" == i:
                    inmigrantes.append(v["Number"])
                elif "Neighborhood Name" == i:
                    barrio.append(v["Neighborhood Name"])
                elif "Nationality" == i:
                    nacionalidad.append(v["Nationality"])

    fig = pe.line(x=nacionalidad, y=inmigrantes)

    st.write(fig)
    


#--------------------------------------------GRÁFICOS RELACIÓN VARIABLES-------------------------------

# poner tres columnas con tablas?

def inmi_barrio():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver los datos de inmigrantes según el barrio:", pag_lines)

    #getting the data
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

    #drawing the line plot
    fig = pe.line(x=barrios, y=inmigrantes, labels={'x':'', 'y':'Inmigrantes'})

    st.write(fig)

def desempl_barrio():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver los datos de desempleados según el barrio:", pag_lines)

    #getting the data
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

    #drawing the line plot
    fig = pe.line(x=barrios, y=desempleados, labels={'x':'', 'y':'Desempleados'})

    st.write(fig)


def total_barrio():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver los datos de población total según el barrio:", pag_lines)

    #getting the data
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

    #drawing the line plot
    fig = pe.line(x=barrios, y=poblacion, labels={'x':'', 'y':'Población'})

    st.write(fig)


# aquí pone cómo hacer este gráfico mejor -> https://plotly.com/python/line-and-scatter/
def sub_pl():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Ir a la gág.", pag_lines)

    #getting the data
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



    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=barrios, y=inmigrantes, name="Datos inmigración"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=barrios, y=desempleados, name="Datos desempleo"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text="Double Y Axis Example"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Barrios")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Inmigración</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Desempleo</b>", secondary_y=True)

    st.write(fig)