import streamlit as st
from data.st_data import all_neigh, get_total, get_total_immigrants, get_total_unemployed
import pandas as pd

pf = pd.DataFrame()


def conclus_page():
    barrio = st.selectbox("Select one neigborhood to search", all_neigh())
    data = get_total_immigrants(barrio)
    st.write(data)






    

