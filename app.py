import copy
import json
import pandas as pd

import streamlit as st

from utils import (
    read_csv_file
)

from data_paths import (
    PHARMA_DATA_PATH,
    MEDICAL_EQUIPMENT_DATA_PATH,
    CUSTOMS_DATA_PATH
)


st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 3em;
            color: #3498db; /* Un azul profesional y sobrio */
            font-family: 'Roboto', sans-serif;
            margin-bottom: 0.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.2em;
        }
        .sub-title {
            text-align: center;
            font-size: 1.2em;
            color: #34495E;
            font-family: 'Arial', sans-serif;
            margin-bottom: 2em;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            color: #95A5A6;
            font-family: 'Arial', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# carousel(items=test_items, width=0.5, )

# Título de la aplicación centrado y con estilo
st.markdown("<h1 class='main-title'>DatosNow</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Ayudamos a los equipos profesionales en datos a integrar datos segmentados en tiempo real sin retrasos por recolección</p>", unsafe_allow_html=True)

# Descripción de la aplicación
# st.write("""
# Ayudamos a los equipos de datos integrar datos especializados en tiempo real, asegurando que la información esté limpia y lista para su uso.
# """)

data_paths = {
    "Farmacia": PHARMA_DATA_PATH,
    "Dispositivos Médicos": MEDICAL_EQUIPMENT_DATA_PATH,
    "Aduanas": CUSTOMS_DATA_PATH
}


category = st.selectbox("Selecciona una categoría para ver una muestra de datos:",
                         (
                             "Farmacia",
                             "Dispositivos Médicos",
                             "Aduanas"
                         ))
try:
    # data_df = read_csv_file(data_paths[st.session_state["custom_title"]])
    data_df = read_csv_file(data_paths[category])
    # columns_df = pd.DataFrame(column_names, columns=["Atributos"])
    # st.dataframe(columns_df, hide_index=True)
    st.write("Estás viendo los datos de: ", category)
    column_names = data_df.columns.tolist()
    st.write("Total de columnas: ", len(column_names))
    api_button = st.link_button("Usar API", url="https://wa.link/l5qwwo", type="primary")
    form = st.form("my_form")
    d = st.dataframe(data_df, hide_index=True,)    
except:
    st.write("Estamos trabajando en la selección de fuentes de datos de ", category)
    api_button = st.link_button("Quiero saber más", url="https://wa.link/l5qwwo", type="primary")

