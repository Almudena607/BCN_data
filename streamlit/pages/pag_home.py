import streamlit as st

def home():
    def title(text,size,color):
        st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)
        
    def header(text):
        st.markdown(f"<p style='color:white;'>{text}</p>",unsafe_allow_html=True)

    title("Inmigración y desempleo en los barrios de Barcelona en 2017", 50, "white")
    
    st.text("Este proyecto pretende mostrar la tasa de desempleo e inmigración en relación con\nla población total de Barcelona en el año 2017.")
    st.text("Para ello se toman como variables independientes los barrios o distritos de\nBarcelona, y como variables independientes, la cantidad de población pertenecientes\nal grupo de inmigrantes, desempleados o el total.\nTambién se tendrá en cuenta el año de recogida de datos.")
