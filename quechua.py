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
st.markdown("<h1 class='title'>CONJUGADOR DE VERBOS EN QUECHUA</h1>", unsafe_allow_html=True)

# Crear una barra lateral con opciones
opcion = st.sidebar.selectbox(
    "Navega por la información",
    ["Conjugador de verbos en quechua", "Historia sobre el quechua", "Por qué un conjugador de quechua", "Quiénes somos"]
)

# Mostrar contenido según la opción seleccionada
if opcion == "Historia sobre el quechua":
    st.markdown("<h2 class='subtitle'>Historia sobre el quechua</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p class='description'>
    El quechua es una familia de lenguas originarias de los Andes y la región de Cuzco. Es una de las lenguas más habladas en América del Sur, con millones de hablantes en países como Perú, Bolivia, Ecuador, Colombia y Argentina. La lengua quechua ha sido transmitida de generación en generación y tiene una rica historia que data de la época precolombina. A lo largo de los siglos, el quechua ha jugado un papel crucial en la cultura y la identidad de los pueblos andinos.
    </p>
    """, unsafe_allow_html=True)

elif opcion == "Por qué un conjugador de quechua":
    st.markdown("<h2 class='subtitle'>Por qué un conjugador de quechua</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p class='description'>
    La preservación y promoción de las lenguas indígenas es fundamental para mantener viva la riqueza cultural y la identidad de los pueblos originarios. El quechua, una de las lenguas más habladas en América del Sur, es un tesoro lingüístico que merece ser valorado y aprendido. Contar con traductores y conjugadores en quechua no solo facilita el aprendizaje de la lengua, sino que también contribuye a su revitalización y transmisión a las futuras generaciones. Estas herramientas permiten a los hablantes y estudiantes de quechua comunicarse con mayor precisión y confianza, promoviendo el uso cotidiano y académico de la lengua.
    </p>
    """, unsafe_allow_html=True)

elif opcion == "Quiénes somos":
    st.markdown("<h2 class='subtitle'>Quiénes somos</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p class='description'>
    Este es un proyecto del curso "Linguistica computacional". El objetivo es proporcionar herramientas y recursos que faciliten el aprendizaje y uso del quechua en la vida cotidiana y académica. Creemos en la importancia de mantener vivas las lenguas originarias y de transmitirlas a las futuras generaciones. A través de este conjugador de verbos en quechua, esperamos contribuir a la revitalización de esta hermosa lengua y apoyar a los estudiantes y hablantes de quechua en su camino de aprendizaje.
    </p>
    """, unsafe_allow_html=True)

# Añadir un subtítulo
st.markdown("<h2 class='subtitle'>Aprende y diviértete conjugando verbos en quechua</h2>", unsafe_allow_html=True)

# Añadir una descripción
st.markdown("""
<p class='description'>
La preservación y promoción de las lenguas indígenas es fundamental para mantener viva la riqueza cultural y la identidad de los pueblos originarios. 
El quechua, una de las lenguas más habladas en América del Sur, es un tesoro lingüístico que merece ser valorado y aprendido. 
Contar con traductores y conjugadores en quechua no solo facilita el aprendizaje de la lengua, sino que también contribuye a su revitalización y transmisión a las futuras generaciones. 
Estas herramientas permiten a los hablantes y estudiantes de quechua comunicarse con mayor precisión y confianza, promoviendo el uso cotidiano y académico de la lengua.
</p>
""", unsafe_allow_html=True)

# Añadir un botón de acción
if st.button('Más información sobre la lengua quechua'):
    st.write("El quechua es una familia de lenguas originarias de los Andes y la región de Cuzco. Es una de las lenguas más habladas en América del Sur.")

# Diccionario de información de tiempos verbales
tiempos_verbales_info = {
    "Presente simple": "Se utiliza para describir acciones que están ocurriendo en el momento actual.",
    "Presente progresivo": "Se usa para indicar que una acción está ocurriendo en este preciso momento de manera continua.",
    "Presente habitual": "Describe acciones que ocurren regularmente o de manera habitual.",
    "Pasado experimentado": "Se refiere a acciones que fueron experimentadas personalmente por el hablante en el pasado.",
    "Pasado experimentado progresivo": "Indica una acción en progreso que fue experimentada personalmente en el pasado.",
    "Pasado experimentado habitual": "Describe acciones que ocurrían regularmente en el pasado y fueron experimentadas personalmente.",
    "Pasado no experimentado simple": "Se usa para acciones pasadas que el hablante no experimentó personalmente.",
    "Pasado no experimentado progresivo": "Indica una acción en progreso en el pasado que no fue experimentada personalmente por el hablante.",
    "Pasado no experimentado habitual": "Describe acciones que ocurrían regularmente en el pasado pero no fueron experimentadas personalmente."
}

verbos = pd.read_excel('quechua.xlsx')
################################################################
################################################################

#abrimos el excel, en el que se adjunta los tiempos verbales del quechua

quechua = pd.ExcelFile('tarea4.xlsx')
# Se define un diccionario vacío que se usará para almacenar otros diccionarios que representan
# cada hoja de cálculo del archivo Excel.
D = {}
# Este bucle for recorre cada hoja en el archivo de Excel, el cual devuelve una lista de los nombres de todas las hojas en el archivo.
for hoja in quechua.sheet_names:
  #Acá, se leerá cada hoja del Excel como un dataframe
  df = pd.read_excel('tarea4.xlsx', sheet_name=hoja)
  #Se obtiene los nombres de las columnas del DataFrame df y los almacena en la variable c.
  c = df.columns
  # Establece la primera columna del DataFrame (c[0]) como índice del DataFrame
  df.set_index(c[0], inplace = True)
  # Convierte el DataFrame (que ahora tiene la primera columna como índice) en un diccionario,
  # donde la clave es el índice y el valor son los otros valores de las filas asociadas a ese índice.
  d = df.to_dict()
  # Acá, se insertan un diccionario dentro de otro diccionario 'D',
  # donde cada diccionario interno representa una tiempo verbal en el archivo de excel.
  D[hoja] = d

pronombres = pd.read_excel('pronombres1.xlsx')

dfp = pd.read_excel('pronombres1.xlsx')
dfp.columns = dfp.columns.str.strip()  # Eliminar espacios en blanco en los nombres de las columnas
## Se seleccionan las columnas del dataframe
c = dfp.columns
## Se cambia el índice del dataframe para que sea la primera columna de este, es decir, la de la persona
dfp.set_index(c[0], inplace=True)
## Se convierte el dataframe en un diccionario
dp = dfp.to_dict()

def conju_final(base, numero, persona, tiempo):
    try:
        resultado = dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]
        return resultado
    except KeyError as e:
        st.write(f"Error: La clave {e} no fue encontrada en los diccionarios")
        st.write(f"Valores actuales - Numero: {numero}, Persona: {persona}, Tiempo: {tiempo}")
        st.write(f"Claves en dp: {list(dp.keys())}")
        st.write(f"Claves en D[tiempo]: {list(D[tiempo].keys())}")
        return None

################################################################
################################################################
quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua, espanol))

base = st.selectbox(
    "Selecciona un verbo en quechua", quechua)

st.write("el verbo seleccionado en español:", dict_que_esp[base])

## persona

persona = st.selectbox(
    "Selecciona una persona", ["primera", "segunda", "tercera"])

## numero

numero = st.selectbox(
    "Selecciona un número", ["singular", "plural"])

#tiempo

tiempo = st.selectbox(
    "Elige el tiempo verbal", ["Presente simple", "Presente progresivo", "Presente habitual",
                               "Pasado experimentado", "Pasado experimentado progresivo", "Pasado experimentado habitual",
                               "Pasado no experimentado simple", "Pasado no experimentado progres", "Pasado no experimentado habitual"])
# Mostrar la información del tiempo verbal seleccionado
st.markdown(f"<p class='description'><strong>Información del tiempo verbal:</strong> {tiempos_verbales_info[tiempo]}</p>", unsafe_allow_html=True)

# Mostrar el verbo conjugado
resultado = conju_final(base, numero, persona, tiempo)
if resultado:
    st.markdown(f"<h3 style='color: #D1A3A4; font-family: \"Comic Sans MS\", cursive, sans-serif;'>El verbo conjugado es: {resultado}</h3>", unsafe_allow_html=True)

