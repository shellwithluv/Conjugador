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

# Función para cargar datos de una hoja específica
def cargar_datos(lengua):
    verbos = pd.read_excel('aimara_verbos.xlsx', sheet_name=lengua)
    return verbos

# Diccionario de información de tiempos verbales
tiempos_verbales_info = {
    "presente simple": "Se utiliza para describir acciones que están ocurriendo en el momento actual.",
    "presente habitual": "Describe acciones que ocurren regularmente o de manera habitual.",
    "pasado experimental": "Se refiere a acciones que fueron experimentadas personalmente por el hablante en el pasado.",
    "pasado habitual": "Describe acciones que ocurrían regularmente en el pasado y fueron experimentadas personalmente.",
    "pasado no experimentado": "Se usa para acciones pasadas que el hablante no experimentó personalmente.",
    "futuro": "Indica acciones que ocurrirán en un tiempo cercano al presente.",
    "futuro lejano": "Se utiliza para describir acciones que ocurrirán en un tiempo distante en el futuro."
}

# Función para conjugar verbos
def conju_final(base, numero, persona, tiempo, dp, D):
    try:
        resultado = dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]
        return resultado
    except KeyError as e:
        st.write(f"Error: La clave {e} no fue encontrada en los diccionarios")
        st.write(f"Valores actuales - Numero: {numero}, Persona: {persona}, Tiempo: {tiempo}")
        st.write(f"Claves en dp: {list(dp.keys())}")
        st.write(f"Claves en dp[numero]: {list(dp[numero].keys())}")
        st.write(f"Claves en D[tiempo]: {list(D[tiempo].keys())}")
        return None

# Selección de lengua
lengua = st.selectbox(
    "Selecciona una lengua",
    ["Quechua", "Aymara"]
)

# Cargar datos de la lengua seleccionada
verbos = cargar_datos(lengua)

# Verificar las columnas disponibles en el DataFrame
st.write(f"Columnas disponibles en el DataFrame de {lengua.lower()}: {verbos.columns.tolist()}")

# Definir la columna de los verbos y cargar los datos de conjugación y pronombres
verbo_col = lengua.lower()
if verbo_col in verbos.columns:
    verbos_lista = list(verbos[verbo_col])
    espanol_lista = list(verbos['espanol'])

    dict_que_esp = dict(zip(verbos_lista, espanol_lista))

    base = st.selectbox(
        f"Selecciona un verbo en {lengua.lower()}",
        verbos_lista
    )

    st.write("El verbo seleccionado en español:", dict_que_esp[base])

    # Cargar datos de conjugación y pronombres
    D = {}
    dp = {}
    
    # Cargar datos de conjugación y pronombres específicos según la lengua
    if lengua == "Quechua":
        quechua = pd.ExcelFile('tarea4.xlsx')
        for hoja in quechua.sheet_names:
            df = pd.read_excel('tarea4.xlsx', sheet_name=hoja)
            c = df.columns
            df.set_index(c[0], inplace=True)
            d = df.to_dict()
            D[hoja] = d
        pronombres_quechua = pd.read_excel('pronombres1.xlsx')
        dfp = pd.read_excel('pronombres1.xlsx')
        dfp.columns = dfp.columns.str.strip()
        c = dfp.columns
        dfp.set_index(c[0], inplace=True)
        dp = dfp.to_dict()
    elif lengua == "Aymara":
        aymara = pd.ExcelFile('aimara.xlsx')
        for hoja in aymara.sheet_names:
            df = pd.read_excel('aimara.xlsx', sheet_name=hoja)
            c = df.columns
            df.set_index(c[0], inplace=True)
            d = df.to_dict()
            D[hoja] = d
        pronombres_aymara = pd.read_excel('pronombres_aimara.xlsx')
        dfp = pd.read_excel('pronombres_aimara.xlsx')
        dfp.columns = dfp.columns.str.strip()
        c = dfp.columns
        dfp.set_index(c[0], inplace=True)
        dp = dfp.to_dict()

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
    st.write(f"Error: La columna '{verbo_col}' no existe en el archivo de verbos para {lengua.lower()}.")