import pandas as pd
import streamlit as st

# Leer el archivo de verbos en quechua y español
verbos = pd.read_excel('/mnt/data/quechua.xlsx')

# Leer y procesar el archivo de tiempos verbales del quechua
file_path = '/mnt/data/tarea4.xlsx'
quechua = pd.ExcelFile(file_path)
D = {}

for hoja in quechua.sheet_names:
    df = pd.read_excel(file_path, sheet_name=hoja)
    df.columns = df.columns.str.strip()  # Eliminar espacios en blanco en los nombres de las columnas
    df.rename(columns={df.columns[0]: 'Persona'}, inplace=True)  # Renombrar la primera columna a 'Persona'
    df.set_index('Persona', inplace=True)  # Establecer la columna 'Persona' como índice
    d = df.to_dict()
    D[hoja] = d
    # Mensaje de depuración
    st.write(f"Hoja: {hoja}")
    st.write("DataFrame:", df)
    st.write("Diccionario:", d)

# Leer y procesar el archivo de pronombres
pronombres = pd.read_excel('/mnt/data/pronombres1.xlsx')
dfp = pd.read_excel('/mnt/data/pronombres1.xlsx')
dfp.columns = dfp.columns.str.strip()  # Eliminar espacios en blanco en los nombres de las columnas
dfp.rename(columns={dfp.columns[0]: 'Persona'}, inplace=True)  # Renombrar la primera columna a 'Persona'
dfp.set_index('Persona', inplace=True)
dp = dfp.to_dict()

# Función para conjugar en quechua
def conju_final(base, numero, persona, tiempo):
    try:
        resultado = dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]
        return resultado
    except KeyError as e:
        st.write(f"Error: La clave {e} no fue encontrada en los diccionarios")
        st.write(f"Valores actuales - Numero: {numero}, Persona: {persona}, Tiempo: {tiempo}")
        st.write(f"Claves en dp: {list(dp.keys())}")
        st.write(f"Claves en D[{tiempo}]: {list(D[tiempo].keys())}")
        st.write(f"Diccionario D[{tiempo}]: {D[tiempo]}")
        return None

# Crear el diccionario de quechua a español
quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])
dict_que_esp = dict(zip(quechua, espanol))

# Streamlit UI
base = st.selectbox("Selecciona un verbo en quechua", quechua)
st.write("El verbo seleccionado en español:", dict_que_esp[base])

# Selección de persona, número y tiempo verbal
persona = st.selectbox("Selecciona una persona", ["primera", "segunda", "tercera"])
numero = st.selectbox("Selecciona un número", ["singular", "plural"])
tiempo = st.selectbox(
    "Elige el tiempo verbal",
    ["Presente", "Presente progresivo", "Presente habitual",
     "Pasado experimentado", "Pasado experimentado progresivo",
     "Pasado experimentado habitual", "Pasado no experimentado simple",
     "Pasado no experimentado progres", "Pasado no experimentado habitua"]
)

# Mostrar el verbo conjugado
resultado = conju_final(base, numero, persona, tiempo)
if resultado:
    st.write("El verbo conjugado es:", resultado)