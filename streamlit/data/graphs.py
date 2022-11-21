import pandas as pd
import streamlit as st
from data.st_data import get_neighborhoods, get_immigrants_nationality, all_nationality, get_immigrants_neighborhood, all_district, get_unemployed_neighborhood
import plotly.graph_objs as go
import plotly.express as pe
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#--------------------------------------------GRÁFICOS INMIGRACIÓN------------------------------- 
def barrio_inmigrantes():

    #boxes to select the district and the page
    distrito = st.selectbox("Selecciona un distrito para ver las nacionalidades de cada barrio:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos barrios y distintas nacionalidades:", pag_lines)


    #getting the data
    a = get_immigrants_neighborhood(distrito, n)
    df = pd.DataFrame(a)
    distritos = []
    inmigrantes = []
    nacionalidad = []
    barrio = []
    for _, data in df.iterrows():
        for dicc in df["results"]:
            for c in dicc:
                if "Number" == c:
                    inmigrantes.append(dicc["Number"])
                elif "Neighborhood Name" == c:
                    barrio.append(dicc["Neighborhood Name"])
                elif "Nationality" == c:
                    nacionalidad.append(dicc["Nationality"])
                elif "District Name" == c:
                    distritos.append(dicc["District Name"])

    #drawing the graphs
    
    fig = pe.bar(df, x=barrio, y=inmigrantes, color=nacionalidad, labels={'x':'Barrios', 'y':'Tasa inmigración'})   
    st.write(fig)



def distrito_inmigrantes():

    #boxes to select the nationality and the page
    nationality = st.selectbox("Selecciona el país para ver los datos de esa nacionalidad en cada barrio:", all_nationality())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos distritos y la nacionalidad de los inmigrantes registrados en cada barrio:", pag_lines)

    #getting the data
    a = get_immigrants_nationality(nationality, n)
    df = pd.DataFrame(a)
    distritos = []
    inmigrantes = []
    barrio = []
    nacionalidad = []
    for _, data in df.iterrows():
        for dicc in df["results"]:
            for c in dicc:
                if c == "District Name":
                    distritos.append(dicc["District Name"])
                elif "Number" == c:
                    inmigrantes.append(dicc["Number"])
                elif "Neighborhood Name" == c:
                    barrio.append(dicc["Neighborhood Name"])
                elif "Nationality" == c:
                    nacionalidad.append(dicc["Nationality"])

    #drawing the graphs
    
    fig = pe.bar(df, x=distritos, y=inmigrantes, color=barrio, labels={'x':'Distrito', 'y':'Tasa inmigración'})
    st.write(fig)


#--------------------------------------------GRÁFICOS DESEMPLEO-------------------------------

def barrio_desempleo():

    distrito = st.selectbox("Selecciona un distrito para ver los datos de desempleo de cada barrio:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos barrios y los datos de desempleo de cada uno:", pag_lines)

    a = get_unemployed_neighborhood(distrito, n)
    df = pd.DataFrame(a)
    distritos = []
    barrio = []
    genero = []
    desempleados = []
    demanda_empleo = []
    for _, data in df.iterrows():
        for dicc in df["results"]:
            for c in dicc:
                if c == "District Name":
                    distritos.append(dicc["District Name"])
                elif "Number" == c:
                    desempleados.append(dicc["Number"])
                elif "Neighborhood Name" == c:
                    barrio.append(dicc["Neighborhood Name"])
                elif "Gender" == c:
                    genero.append(dicc["Gender"])     
                elif "Demand_occupation" == c:
                    demanda_empleo.append(dicc["Demand_occupation"])

    fig = pe.bar(df, x=barrio, y=desempleados, color=demanda_empleo, labels={'x':'Barrio', 'y': 'Tasa desempleo'})               
    st.write(fig)

def genero_desempleo():

    distrito = st.selectbox("Selecciona un distrito para ver el género de las personas desempleadas de cada barrio:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos barrios y el género de las personas desempleadas:", pag_lines)

    a = get_unemployed_neighborhood(distrito, n)
    df = pd.DataFrame(a)
    distritos = []
    barrio = []
    genero = []
    desempleados = []
    demanda_empleo = []
    for _, data in df.iterrows():
        for dicc in df["results"]:
            for c in dicc:
                if c == "District Name":
                    distritos.append(dicc["District Name"])
                elif "Number" == c:
                    desempleados.append(dicc["Number"])
                elif "Neighborhood Name" == c:
                    barrio.append(dicc["Neighborhood Name"])
                elif "Gender" == c:
                    genero.append(dicc["Gender"])     
                elif "Demand_occupation" == c:
                    demanda_empleo.append(dicc["Demand_occupation"])

    fig = pe.bar(df, x=barrio, y=desempleados, color=genero, labels={'x':'Barrio', 'y': 'Tasa desempleo'})               
    st.write(fig)



#--------------------------------------------GRÁFICOS RELACIÓN VARIABLES-------------------------------

def inmi_barrio():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos barrios y su tasa de inmigración:", pag_lines)

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
    fig = pe.line(x=barrios, y=inmigrantes, labels={'x':'', 'y':'Tasa inmigración'})

    st.write(fig)

def desempl_barrio():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos barrios y su tasa de desempleo:", pag_lines)

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
    fig = pe.line(x=barrios, y=desempleados, labels={'x':'', 'y':'Tasa desempleo'})

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
    fig = pe.line(x=barrios, y=poblacion, labels={'x':'', 'y':'Población total'})

    st.write(fig)


# gráfico relación inmigración-desempleo-total población
def sub_pl():
    #box to select the page
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para ver distintos barrios y la relación inmigración-desempleo de cada uno:", pag_lines)

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

    fig.add_trace(
        go.Scatter(x=barrios, y=poblacion, name="Población total"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text="Relación tasa inmigración y desempleo"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Barrios")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Inmigración</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Desempleo</b>", secondary_y=True)
    fig.update_yaxes(title_text="<b>Total</b>", secondary_y=True)

    st.write(fig)