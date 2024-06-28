import pandas as pd
import streamlit as st

# Añadir un poco de CSS para personalizar la apariencia
st.markdown("""
    <style>
    .reportview-container {
        background-color: #FFFDD0;
    }
    .title {
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 3em;
        color: #D1A3A4;  /* Color palo rosa */
    }
    .subtitle {
        text-align: center;
        color: #4B0082;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .description {
        text-align: justify;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stSelectbox label {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #4B0082;
        font-size: 20px;
    }
    .stSelectbox div[role='listbox'] > div {
        font-size: 20px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Título de la página
st.markdown("<h1 class='title'>CONJUGADOR DE VERBOS EN QUECHUA Y AYMARA</h1>", unsafe_allow_html=True)

# Función y datos para el quechua
def cargar_datos_quechua():
    verbos_quechua = pd.read_excel('quechua_verbos.xlsx')
    quechua = pd.ExcelFile('tarea4.xlsx')
    D_quechua = {}
    for hoja in quechua.sheet_names:
        df = pd.read_excel('tarea4.xlsx', sheet_name=hoja)
        c = df.columns
        df.set_index(c[0], inplace=True)
        d = df.to_dict()
        D_quechua[hoja] = d
    pronombres_quechua = pd.read_excel('pronombres1.xlsx')
    dfp = pd.read_excel('pronombres1.xlsx')
    dfp.columns = dfp.columns.str.strip()
    c = dfp.columns
    dfp.set_index(c[0], inplace=True)
    dp_quechua = dfp.to_dict()
    return verbos_quechua, D_quechua, dp_quechua

# Función y datos para el aymara 
def cargar_datos_aymara():
    verbos_aymara = pd.read_excel('aimara_verbos.xlsx')
    aymara = pd.ExcelFile('aimara.xlsx')
    D_aymara = {}
    for hoja in aymara.sheet_names:
        df = pd.read_excel('aimara.xlsx', sheet_name=hoja)
        c = df.columns
        df.set_index(c[0], inplace=True)
        d = df.to_dict()
        D_aymara[hoja] = d
    pronombres_aymara = pd.read_excel('pronombres_aimara.xlsx')
    dfp = pd.read_excel('pronombres_aimara.xlsx')
    dfp.columns = dfp.columns.str.strip()
    c = dfp.columns
    dfp.set_index(c[0], inplace=True)
    dp_aymara = dfp.to_dict()
    return verbos_aymara, D_aymara, dp_aymara

# Diccionario de información de tiempos verbales (puedes ajustarlo según necesites)
tiempos_verbales_info = {
    "presente simple": "Se utiliza para describir acciones que están ocurriendo en el momento actual.",
    "presente habitual": "Describe acciones que ocurren regularmente o de manera habitual.",
    "pasado experimental": "Se refiere a acciones que fueron experimentadas personalmente por el hablante en el pasado.",
    "pasado habitual": "Describe acciones que ocurrían regularmente en el pasado y fueron experimentadas personalmente.",
    "pasado no experimentado": "Se usa para acciones pasadas que el hablante no experimentó personalmente.",
    "futuro":"Indica acciones que ocurrirán en un tiempo cercano al presente.",
    "futuro lejano": "Se utiliza para describir acciones que ocurrirán en un tiempo distante en el futuro."
    
}

# Función para conjugar verbos (puedes adaptarla según necesites)
def conju_final(base, numero, persona, tiempo, dp, D):
    try:
        resultado = dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]
        return resultado
    except KeyError as e:
        st.write(f"Error: La clave {e} no fue encontrada en los diccionarios")
        st.write(f"Valores actuales - Numero: {numero}, Persona: {persona}, Tiempo: {tiempo}")
        st.write(f"Claves en dp: {list(dp.keys())}")
        st.write(f"Claves en D[tiempo]: {list(D[tiempo].keys())}")
        return None
    
# Cargar datos
verbos_quechua, D_quechua, dp_quechua = cargar_datos_quechua()
verbos_aymara, D_aymara, dp_aymara = cargar_datos_aymara()

# Selección de lengua y configuración de datos correspondientes
lengua = st.selectbox(
    "Selecciona una lengua",
    ["Quechua", "Aymara"]
)

if lengua == "Quechua":
    verbos = verbos_quechua
    D = D_quechua
    dp = dp_quechua
    verbo_col = 'quechua'
elif lengua == "Aimara":
    verbos = verbos_aymara
    D = D_aymara
    dp = dp_aymara
    verbo_col = 'aimara'

# Verificar si la columna correspondiente existe en el DataFrame
if verbo_col in verbos.columns:
    verbos_lista = list(verbos[verbo_col])
    espanol_lista = list(verbos['espanol'])

    dict_que_esp = dict(zip(verbos_lista, espanol_lista))

    base = st.selectbox(
        f"Selecciona un verbo en {lengua.lower()}",
        verbos_lista
    )

    st.write("El verbo seleccionado en español:", dict_que_esp[base])

    # Selección de número
    numero = st.selectbox(
        "Selecciona un número", list(dp.keys())
    )

    # Selección de persona
    persona = st.selectbox(
        "Selecciona una persona", list(dp[numero].keys())
    )

    # Selección de tiempo
    tiempo = st.selectbox(
        "Elige el tiempo verbal", ["presente simple", "pasado experimental", "pasado no experimentado", "futuro", "futuro lejano", 
                                "pasado habitual", "presente habitual"]
    )

    # Mostrar la información del tiempo verbal seleccionado
    st.markdown(f"<p class='description'><strong>Información del tiempo verbal:</strong> {tiempos_verbales_info[tiempo]}</p>", unsafe_allow_html=True)

    # Mostrar el verbo conjugado
    resultado = conju_final(base, numero, persona, tiempo, dp, D)
    if resultado:
        st.markdown(f"<h3 style='color: #D1A3A4; font-family: \"Comic Sans MS\", cursive, sans-serif;'>El verbo conjugado es: {resultado}</h3>", unsafe_allow_html=True)
else: