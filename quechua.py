import pandas as pd

verbos = pd.read_excel('quechua.xlsx')

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

import streamlit as st

option = st.selectbox(
    "Selecciona un verbo en quechua",quechua)

st.write("el verbo seleccionado en espanol:", dict_que_esp[option])

## persona

persona = st.selectbox(
    "Selecciona una persona", ["primera", "segunda", "tercera"])

## numero

numero = st.selectbox(
    "Seleciona un numero", ["singular", "plural"])

#tiempo

tiempo = st.radio(
    "Elige el tiempo verbal",
    [":rainbow[Presente]", ":yellow[Pasado]", ":blue[Futuro]"],
    index=None,
)

st.write("Tu elegiste:", tiempo)

