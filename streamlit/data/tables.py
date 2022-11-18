import streamlit as st
from data.st_data import get_total_immigrants, get_total_unemployed, get_total, all_neigh
import pandas as pd



def tablas_conclusiones():    
    barrio = st.selectbox("Select one neigborhood to search", all_neigh())
    data_total_inm = get_total_immigrants(barrio)
    data_total_unem = get_total_unemployed(barrio)
    data_total = get_total(barrio)
    st.table(data_total_inm)
    st.table(data_total_unem)
    st.table(data_total)

