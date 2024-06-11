import pandas as pd
import streamlit as st

# Añadir un poco de CSS para personalizar la apariencia
st.markdown("""
    <style>
    .reportview-container {
        background-color: #FFFDD0;
    }
    .title {
        color: green;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
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

# Añadir una sección de explicación de tiempos verbales
st.markdown("""
<h2 class='subtitle'>Tiempos Verbales en Quechua</h2>
<p class='description'>
En quechua, al igual que en otras lenguas, los verbos se conjugan para reflejar el tiempo de la acción. A continuación se presentan los principales tiempos verbales en quechua:
</p>
<ul class='description'>
    <li><strong>Presente:</strong> Se utiliza para describir acciones que están ocurriendo en el momento actual.</li>
    <li><strong>Presente progresivo:</strong> Se usa para indicar que una acción está ocurriendo en este preciso momento de manera continua.</li>
    <li><strong>Presente habitual:</strong> Describe acciones que ocurren regularmente o de manera habitual.</li>
    <li><strong>Pasado experimentado:</strong> Se refiere a acciones que fueron experimentadas personalmente por el hablante en el pasado.</li>
    <li><strong>Pasado experimentado progresivo:</strong> Indica una acción en progreso que fue experimentada personalmente en el pasado.</li>
    <li><strong>Pasado experimentado habitual:</strong> Describe acciones que ocurrían regularmente en el pasado y fueron experimentadas personalmente.</li>
    <li><strong>Pasado no experimentado simple:</strong> Se usa para acciones pasadas que el hablante no experimentó personalmente.</li>
    <li><strong>Pasado no experimentado progresivo:</strong> Indica una acción en progreso en el pasado que no fue experimentada personalmente por el hablante.</li>
    <li><strong>Pasado no experimentado habitual:</strong> Describe acciones que ocurrían regularmente en el pasado pero no fueron experimentadas personalmente.</li>
</ul>
""", unsafe_allow_html=True)

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

# Mostrar el verbo conjugado
resultado = conju_final(base, numero, persona, tiempo)
if resultado:
    st.markdown(f"<h3 style='color: green; font-family: \"Comic Sans MS\", cursive, sans-serif;'>El verbo conjugado es: {resultado}</h3>", unsafe_allow_html=True)

# Añadir un botón de acción
if st.button('Más información sobre la lengua quechua'):
    st.write("El quechua es una familia de lenguas originarias de los Andes y la región de Cuzco. Es una de las lenguas más habladas en América del Sur.")
    
