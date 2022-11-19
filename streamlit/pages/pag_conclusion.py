import streamlit as st
from data.graphs import  total_barrio, data_fr, sub_pl, graph_facil, desempl_barrio, inmi_barrio



def conclus_page():
    def title(text,size,color):
        st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)

        title("Conclusiones", 35, "white")
        
    st.text("blah blah blah")


    #presentación datos en gráficos
    data_fr()
    graph_facil()

    desempl_barrio()
    inmi_barrio()
    total_barrio()

    sub_pl()








    

