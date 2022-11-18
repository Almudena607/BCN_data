import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from data.st_data import all_neigh, get_neighborhoods



def total_immigrants(stats):
    dependiente = stats["_id"]
    independiente = stats["Total Immigrants"]
    plt.bar(dependiente, independiente)

def graphs_concl():
    df = pd.DataFrame(get_neighborhoods())
    x = all_neigh()
    y = df["Total Population"]
    st.line_chart(df, x, y , width=0, height=0, use_container_width=True)