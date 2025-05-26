import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar modelo
modelo = joblib.load("modelo_hibrido.pkl")

# Variables en orden
FEATURES = [
    'EDAD', 'SEXO_NACIMIENTO', 'ETNIA', 'DPTO',
    'MAXIMO_NIVEL_EDUCATIVO', 'OCUPACION',
    'EXISTENCIA_CONTRATO', 'HORAS_TRABAJO'
]

# Umbrales socioeconómicos realistas en COP
UMBRAL_BAJO = 1_200_000
UMBRAL_ALTO = 5_000_000

# Clasificación en tres clases
def clasificar_ingreso(valor):
    if valor < UMBRAL_BAJO:
        return "bajo ingreso"
    elif valor < UMBRAL_ALTO:
        return "medio ingreso"
    else:
        return "alto ingreso"

# Función de predicción
def predict_ingreso_y_clase(input_dict, best_reg):
    df_in = pd.DataFrame([input_dict], columns=FEATURES)
    cat_feats = [c for c in FEATURES if c not in ['EDAD','HORAS_TRABAJO']]
    for c in cat_feats:
        df_in[c] = df_in[c].astype(str)
    ingreso_pred = best_reg.predict(df_in)[0]
    clase_pred = clasificar_ingreso(ingreso_pred)
    return {
        'ingreso_predicho': float(ingreso_pred),
        'clase_predicha': clase_pred
    }

# Interfaz de Streamlit
st.set_page_config(page_title="Predicción de Ingreso", layout="centered")
st.title("🔍 Predicción de Ingreso Mensual en Colombia")

# Diccionarios de mapeo
genero_map = {'Hombre': '1', 'Mujer': '2', 'Hombre trans': '3', 'Mujer trans': '4'}
etnia_map = {'Indígena': '1', 'Gitano (Rom)': '2', 'Raizal': '3', 'Palenquero': '4', 'Afrodescendiente': '5', 'Ninguno': '6'}
dpto_map = {'Antioquia': '5', 'Atlántico': '8', 'Bogotá D.C.': '11', 'Bolívar': '13', 'Boyacá': '15', 'Caldas': '17', 'Caquetá': '18', 'Cauca': '19', 'Cesar': '20', 'Córdoba': '23', 'Cundinamarca': '25', 'Chocó': '27', 'Huila': '41', 'La Guajira': '44', 'Magdalena': '47', 'Meta': '50', 'Nariño': '52', 'Norte de Santander': '54', 'Quindío': '63', 'Risaralda': '66', 'Santander': '68', 'Sucre': '70', 'Tolima': '73', 'Valle del Cauca': '76'}
ed_map = {'Ninguno': '1', 'Preescolar': '2', 'Básica primaria (1°-5°)': '3', 'Básica secundaria (6°-9°)': '4', 'Media académica (Bachillerato clásico)': '5', 'Media técnica (Bachillerato técnico)': '6', 'Normalista': '7', 'Técnica profesional': '8', 'Tecnológica': '9', 'Universitaria': '10', 'Especialización': '11', 'Maestría': '12', 'Doctorado': '13', 'No sabe / No informa': '99'}
ocup_map = {'Fuerzas militares': '0', 'Directores y gerentes': '1', 'Profesionales, científicos e intelectuales': '2', 'Técnicos y profesionales de nivel medio': '3', 'Personal de apoyo administrativo': '4', 'Trabajadores de los servicios y vendedores': '5', 'Agricultores y trabajadores agropecuarios': '6', 'Oficiales, operarios, artesanos': '7', 'Operadores de máquinas': '8', 'Ocupaciones elementales': '9'}
contrato_map = {"Sí": "1", "No": "0"}

# Inputs
sexo = st.selectbox("Sexo", list(genero_map.keys()))
edad = st.number_input("Edad", min_value=14, max_value=100, value=30)
etnia = st.selectbox("Grupo Étnico", list(etnia_map.keys()))
region = st.selectbox("Departamento", list(dpto_map.keys()))
nivel_educativo = st.selectbox("Nivel Educativo", list(ed_map.keys()))
ocupacion = st.selectbox("Tipo de Ocupación", list(ocup_map.keys()))
tipo_contrato = st.selectbox("¿Tiene contrato?", list(contrato_map.keys()))
horas_trabajo = st.slider("Horas trabajadas por semana", 0, 80, 40)

# Botón de predicción
if st.button("🔮 Predecir Ingreso"):
    entrada = {
        'EDAD': edad,
        'SEXO_NACIMIENTO': genero_map[sexo],
        'ETNIA': etnia_map[etnia],
        'DPTO': dpto_map[region],
        'MAXIMO_NIVEL_EDUCATIVO': ed_map[nivel_educativo],
        'OCUPACION': ocup_map[ocupacion],
        'EXISTENCIA_CONTRATO': contrato_map[tipo_contrato],
        'HORAS_TRABAJO': horas_trabajo
    }

    resultado = predict_ingreso_y_clase(entrada, modelo)

    st.success(f"✅ Ingreso mensual estimado: **${int(resultado['ingreso_predicho']):,} COP**")
    st.info(f"📊 Clasificación socioeconómica: **{resultado['clase_predicha'].capitalize()}**")

# Información
st.markdown("---")
st.subheader("ℹ️ Acerca de la app")
st.write("""
Aplicación desarrollada para el Examen Final del curso de Analítica de Datos.  
Los datos provienen de la Gran Encuesta Integrada de Hogares (GEIH 2021–2024).  
El modelo estima el ingreso mensual laboral y lo clasifica como bajo, medio o alto según umbrales socioeconómicos oficiales.  
**Esta predicción es referencial y no sustituye asesoría profesional.**

Desarrollado por: Carlos Augusto Sánchez Lombana, Jorge Esteban Díaz Bernal, Laura Camila Rodríguez León.
""")
