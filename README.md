# Examen Final – Analítica de Datos

Este proyecto corresponde al examen final del curso **Analítica de Datos**, Universidad de La Sabana (2025-I).  
Consiste en el desarrollo de un modelo de predicción de ingreso laboral mensual a partir de variables socioeconómicas usando técnicas de aprendizaje automático, y su despliegue como aplicación interactiva.

---

## Acceso directo a la aplicación

La aplicación se encuentra desplegada en Streamlit Cloud:

 [Haz clic aquí para abrir la app](https://carlos22709-proyecto-final-analitica-app-7oyjpb.streamlit.app)

---

## Descripción técnica

- Modelo: `XGBoostRegressor` optimizado con `Pipeline` de preprocesamiento.
- Variables utilizadas: edad, sexo, etnia, nivel educativo, departamento, ocupación, horas trabajadas, tipo de contrato.
- Clasificación binaria complementaria: ingreso alto vs. bajo según umbral optimizado (maximiza F1-score).
- Umbral obtenido: ~\$1.300.000 COP (calculado con `precision_recall_curve`).
- Fuente de datos: GEIH (Gran Encuesta Integrada de Hogares), DANE 2021–2024.

---

## Reproducibilidad

Los siguientes archivos se incluyen en el repositorio del proyecto:

- `app.py`: aplicación final en Streamlit.
- `modelo_hibrido.pkl`: pipeline entrenado y serializado.
- `requirements.txt`: dependencias necesarias para reproducir el entorno.


