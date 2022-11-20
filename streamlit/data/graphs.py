import pandas as pd
import streamlit as st
from data.st_data import get_neighborhoods, get_immigrants_nationality, all_nationality, get_immigrants_neighborhood, all_district, get_unemployed_neighborhood
import plotly.graph_objs as go
import plotly.express as pe
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#--------------------------------------------GRÁFICOS INMIGRACIÓN------------------------------- 
########!!!!!!!! 
def barrio_inmigrantes():

    #boxes to select the district and the page
    distrito = st.selectbox("Selecciona el distrito:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Seleccsjfgjshkgb los datos de la inmigración de empleo en función del barrio:", pag_lines)


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
    
    fig = pe.bar(df, x=barrio, y=inmigrantes, color=nacionalidad)   
    st.write(fig)



def distrito_inmigrantes():

    #boxes to select the nationality and the page
    nationality = st.selectbox("Selecciona el país para ver los datos de esa nacionalidad:", all_nationality())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la página para bhsjfks los datos de inmigrantes según el distrito:", pag_lines)

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

    distrito = st.selectbox("Selecciona mdfbn mc distrito:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Selecciona la fhjdscbhsak para ver los datos de la demanda de empleo en función del barrio:", pag_lines)

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

    distrito = st.selectbox("Selecdfjgnlkciona mdfbn mc distrito:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Seleccionadsijklhjdscbhsak para ver los datos de la demanda de empleo en función del barrio:", pag_lines)

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
    n = st.selectbox("Selecciona la pág para ver los datos de inmigrantes según el barrio:", pag_lines)

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
    n = st.selectbox("Selecciona la pagina para ver los datos de población total según el barrio:", pag_lines)

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


































#--------------------------------------------GRÁFICOS POBLACIÓN-------------------------------
#x barrio y number c edad
#def edades_poblacion():

#    distrito = st.selectbox("Selecdfjgnlkciondsfnma mdfbn mc distrito:", all_district())
#    pag_lines = [0,1,2,3,4,5,6,7] 
#    n = st.selectbox("Seleccionadsijklhjdscbhdnfjksak para ver los datos de la demanda de empleo en función del barrio:", pag_lines)

#    a = get_population_neighborhood(distrito, n)
#    df = pd.DataFrame(a)
#    distritos = []
#    barrio = []
#    genero = []
#    total = []
#    edad = []
#    for _, data in df.iterrows():
#        for dicc in df["results"]:
#            for c in dicc:
#                if c == "District.Name":
#                    distritos.append(dicc["District.Name"])
#                elif "Number" == c:
#                    total.append(dicc["Number"])
#                elif "Neighborhood.Name" == c:
#                    barrio.append(dicc["Neighborhood.Name"])
#                elif "Gender" == c:
#                    genero.append(dicc["Gender"])     
#                elif "Age" == c:
#                    edad.append(dicc["Age"])    

#    fig = pe.bar(df, x=barrio, y=total, color=edad, labels={'x':'Barrio', 'y': 'Población total'})               
#    st.write(fig) 



"""def genero_poblacion():

    distrito = st.selectbox(" mdfbn mdfgc distrito:", all_district())
    pag_lines = [0,1,2,3,4,5,6,7] 
    n = st.selectbox("Seleccionadsijklhjdscbhsak vnc ver los datos de la demanda de empleo en función del barrio:", pag_lines)

    a = get_population_neighborhood(distrito, n)
    df = pd.DataFrame(a)
    distritos = []
    barrio = []
    genero = []
    total = []
    edad = []
    for _, data in df.iterrows():
        for dicc in df["results"]:
            for c in dicc:
                if c == "District.Name":
                    distritos.append(dicc["District.Name"])
                elif "Number" == c:
                    total.append(dicc["Number"])
                elif "Neighborhood.Name" == c:
                    barrio.append(dicc["Neighborhood.Name"])
                elif "Gender" == c:
                    genero.append(dicc["Gender"])     
                elif "Age" == c:
                    edad.append(dicc["Age"])    

    fig = pe.bar(df, x=barrio, y=total, color=genero, labels={'x':'Barrio', 'y': 'Población total'})               
    st.write(fig)
"""