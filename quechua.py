import pandas as pd

verbos = pd.read_excel('quechua.xlsx')
################################################################
################################################################

#abrimos el excel, en el que se adjunta los tiempos verbales del quechua
datos = pd.read_excel('tarea4.xlsx')

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

def conju_quechua(base, numero, persona, tiempo):
  return base + D[tiempo][numero][persona]

pronombres = pd.read_excel('pronombres1.xlsx')

dfp = pd.read_excel('pronombres1.xlsx')
## Se seleccionan las columnas del dataframe
c = dfp.columns
## Se cambia el índice del dataframe para que sea la primera columna de este, es decir, la de la persona
dfp.set_index(c[0], inplace=True)
## Se convierte el dataframe en un diccionario
dp = dfp.to_dict()

def conju_final(base,numero,persona,tiempo):
  return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]

################################################################
################################################################
quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

import streamlit as st

base = st.selectbox(
    "Selecciona un verbo en quechua",quechua)

st.write("el verbo seleccionado en espanol:", dict_que_esp[base])

## persona

persona = st.selectbox(
    "Selecciona una persona", ["primera", "segunda", "tercera"])

## numero

numero = st.selectbox(
    "Seleciona un numero", ["singular", "plural"])

#tiempo

tiempo = st.selectbox(
    "Elige el tiempo verbal",["Presente","Presente progresivo","Presente habitual","Pasado experimentado","Pasado experimentado progresivo","Pasado experimentado habitual","Pasado no experimentado simple","Pasado no experimentado progres","Pasaso no experimentado habitua"])

st.write("El verbo conjugado es:", conju_final(base,numero,persona,tiempo))

