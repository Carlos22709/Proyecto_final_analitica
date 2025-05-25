# app.py
import streamlit as st
import pandas as pd
import numpy as np
# import joblib  # Descomenta cuando tengas el modelo real
# modelo = joblib.load("modelo_ingresos.pkl")

st.set_page_config(page_title="Predicción de Ingreso", layout="centered")

st.title("💼 Predicción de Ingreso Mensual en Colombia")
st.markdown("Completa los siguientes campos para estimar tu ingreso laboral mensual:")

# ======== FORMULARIO DE ENTRADA ========
sexo = st.selectbox("Sexo", ["Masculino", "Femenino"])
edad = st.number_input("Edad", min_value=14, max_value=100, value=30)
etnia = st.selectbox("Grupo Étnico", ["Ninguno", "Afro", "Indígena", "Rom", "Otro"])
region = st.selectbox("Región", ["Bogotá", "Caribe", "Pacífico", "Centro", "Orinoquía", "Amazonía", "Otro"])
nivel_educativo = st.selectbox("Nivel Educativo", ["Primaria", "Secundaria", "Técnico", "Universitario", "Postgrado"])
ocupacion = st.selectbox("Ocupación", ["Empleado", "Independiente", "Desempleado", "Otro"])
tipo_contrato = st.selectbox("Tipo de Contrato", ["Formal", "Informal", "Ninguno"])
horas_trabajo = st.slider("Horas trabajadas por semana", 0, 80, 40)

# ======== BOTÓN DE PREDICCIÓN ========
if st.button("🔮 Predecir Ingreso"):
    # Simulación mientras no se tiene el modelo real
    ingreso_estimado = np.random.randint(800_000, 3_500_000)

    # --- Código real que se activará cuando tengas tu modelo ---
    # inputs_modelo = procesar_inputs(sexo, edad, etnia, region, nivel_educativo, ocupacion, tipo_contrato, horas_trabajo)
    # entrada_df = pd.DataFrame([inputs_modelo])
    # ingreso_estimado = modelo.predict(entrada_df)[0]

    st.success(f"✅ Tu ingreso mensual estimado es: **${int(ingreso_estimado):,} COP**")

# ======== CRÉDITOS ========
st.markdown("---")
st.subheader("ℹ️ Acerca de la app")
st.write("""
Aplicación desarrollada para el Examen Final del curso de Analítica de Datos.  
Los datos provienen de la Gran Encuesta Integrada de Hogares (GEIH 2021–2024).  
El modelo estima el ingreso mensual laboral a partir de variables demográficas, educativas y laborales.  
**Esta predicción es referencial y no sustituye asesoría profesional.**

Desarrollado por: *Tu Nombre Aquí*.
""")
