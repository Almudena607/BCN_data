import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_test import diccionario_test

header = st.container()
dataset = st.container()
features = st.container()


with header:
    st.title("Prueba de streamlit hasta que me furulen los routers!")
    st.text("Quiero jugar con streamlit pero no lo puedo conectar a la api,\n así que lo voy haciendo con un .csv")

with dataset:
    st.header("A ver qué onda este dataset")

    neig_data = pd.read_csv("../data/immigrants_by_nationality.csv")
    st.write(neig_data.head())

    plt.figure(figsize =(6,4))
    plt.pie(diccionario_test.values(), labels= diccionario_test.keys())
    
with features:
    st.header("features(?)")
    st.text("este apartado no me va a ser muy útil creo pero weno")
