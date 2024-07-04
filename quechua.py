import pandas as pd
import streamlit as st

#Se añade un poco de CSS para personalizar la apariencia de la página
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

#Se inserta el título de la página
st.markdown("<h1 class='title'>CONJUGADOR DE VERBOS EN QUECHUA Y AYMARA</h1>", unsafe_allow_html=True)

#Se crea una barra lateral con diversas opciones
st.sidebar.title("Menú")
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    ("Quienes somos", "Por qué es importante estudiar estas lenguas", "Bibliografía")
)

if opcion == "Quienes somos":
    st.sidebar.markdown("""
        Este es un trabajo final del curso de Linguística Computacional de la PUCP. La misión es proporcionar herramientas digitales que faciliten el aprendizaje y la difusión del quechua y el aymara.
    """)
elif opcion == "Por qué es importante estudiar estas lenguas":
    st.sidebar.markdown("""
        Estudiar lenguas originarias como el quechua y el aymara es crucial para preservar la riqueza cultural y lingüística de nuestras comunidades. Estas lenguas contienen conocimientos ancestrales y una visión única del mundo que debemos valorar y mantener vivos.
    """)
elif opcion == "Bibliografía":
    st.sidebar.markdown("""
        La bibliografía utilizada para desarrollar este conjugador de verbos incluye el libro de Rodolfo Cerrón-Palomino "Quechumara: Estructuras paralelas del quechua y aimara (2008)".
    """)
# Función para cargar datos de Quechua desde archivos Excel
def cargar_datos_quechua():
    # Cargar el archivo de verbos en Quechua
    verbos_quechua = pd.read_excel('quechua_verbos.xlsx')
    # Cargar el archivo que contiene varias hojas de datos de Quechua
    quechua = pd.ExcelFile('tarea4.xlsx')
    # Diccionario para almacenar los datos de las diferentes hojas
    D_quechua = {}
    # Iterar sobre cada hoja del archivo Excel
    for hoja in quechua.sheet_names:
        df = pd.read_excel('tarea4.xlsx', sheet_name=hoja)
        c = df.columns
        df.set_index(c[0], inplace=True)
        d = df.to_dict()
        D_quechua[hoja] = d
    # Cargar el archivo de pronombres en Quechua
    pronombres_quechua = pd.read_excel('pronombres1.xlsx')
    dfp = pd.read_excel('pronombres1.xlsx')
    dfp.columns = dfp.columns.str.strip()
    c = dfp.columns
    dfp.set_index(c[0], inplace=True)
    dp_quechua = dfp.to_dict()
    # Retornar los datos cargados
    return verbos_quechua, D_quechua, dp_quechua

# Función para cargar datos de Aymara desde archivos Excel
def cargar_datos_aymara():
    # Cargar el archivo de verbos en Aymara
    verbos_aymara = pd.read_excel('aimara_verbos.xlsx')
    # Cargar el archivo que contiene varias hojas de datos de Aymara
    aymara = pd.ExcelFile('aimara.xlsx')
    # Cargar el archivo que contiene varias hojas de datos de Aymara
    D_aymara = {}
    # Cargar el archivo que contiene varias hojas de datos de Aymara
    for hoja in aymara.sheet_names:
        df = pd.read_excel('aimara.xlsx', sheet_name=hoja)
        c = df.columns
        df.set_index(c[0], inplace=True)
        d = df.to_dict()
        D_aymara[hoja] = d
    # Cargar el archivo que contiene varias hojas de datos de Aymara
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

# Función para conjugar verbos
def conju_final(base, numero, persona, tiempo, dp, D):
    # Limpiamos los espacios en blanco de los parámetros
    base = base.strip()
    numero = numero.strip()
    persona = persona.strip()
    tiempo = tiempo.strip()

    try:
        # Comprobar que los valores en los diccionarios sean cadenas de texto
        if type(dp[numero][persona])!=str or type(D[tiempo][numero][persona])!=str:
            return False
        else:
            # Construir la conjugación combinando el pronombre, la base del verbo y el sufijo del tiempo verbal
            resultado = dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]
            return resultado
    except KeyError as e:
        # Manejar errores de clave no encontrada
        st.write(f"Error: La clave {e} no fue encontrada en los diccionarios")
        st.write(f"Valores actuales - Numero: {numero}, Persona: {persona}, Tiempo: {tiempo}")
        st.write(f"Claves en dp: {list(dp.keys())}")
        st.write(f"Claves en D[tiempo]: {list(D[tiempo].keys())}")
        return None
    
# Cargar datos de Quechua y Aymara
verbos_quechua, D_quechua, dp_quechua = cargar_datos_quechua()
verbos_aymara, D_aymara, dp_aymara = cargar_datos_aymara()

# Selección de lengua y configuración de datos correspondientes
lengua = st.selectbox(
    "Selecciona una lengua",
    ["Quechua","Aymara"]
)

# Configuración de datos según la lengua seleccionada
if lengua == "Quechua":
    verbos = verbos_quechua
    D = D_quechua
    dp = dp_quechua
    quechua = list(verbos['quechua'])
    espanol = list(verbos['espanol'])
    dict_que_esp = dict(zip(quechua, espanol))
    base = st.selectbox(
        "Selecciona un verbo en " + lengua.lower(), quechua)

elif lengua == "Aymara":
    verbos = verbos_aymara
    D = D_aymara
    dp = dp_aymara
    verbo_col = 'aimara'
    aimara = list(verbos['aimara'])
    espanol = list(verbos['espanol'])
    dict_que_esp = dict(zip(aimara, espanol))
    base = st.selectbox(
        "Selecciona un verbo en " + lengua.lower(), aimara)

# Mostramos el verbo seleccionado en español
st.write("El verbo seleccionado en español:", dict_que_esp[base])

# Selección de número
numero = st.selectbox(
    "Selecciona un número", list(dp.keys())
)

# Selección de persona
persona = st.selectbox(
    "Selecciona una persona", list(dp[numero].keys())
)

#Selección de tiempo verbal
tiempo = st.selectbox(
    "Elige el tiempo verbal", ["presente simple", "pasado experimental", "pasado no experimentado","futuro","futuro lejano",
                               "pasado habitual","presente habitual"])
# Mostrar la información del tiempo verbal seleccionado
st.markdown(f"<p class='description'><strong>Información del tiempo verbal:</strong> {tiempos_verbales_info[tiempo]}</p>", unsafe_allow_html=True)

# Mostrar el verbo conjugado
resultado = conju_final(base, numero, persona, tiempo, dp, D)
if resultado:
    st.markdown(f"<h3 style='color: #D1A3A4; font-family: \"Comic Sans MS\", cursive, sans-serif;'>El verbo conjugado es: {resultado}</h3>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='color: #D1A3A4; font-family: \"Comic Sans MS\", cursive, sans-serif;'>No existe la conjugación. Por favor, selecciona otra combinación de valores.</hjson>", unsafe_allow_html=True)