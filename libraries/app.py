from pickle import load
import streamlit as st
import requests
import numpy as np

model = load(open("../models/salary_predictor_model.sav", "rb"))

st.set_page_config(page_title="Predicción de Salarios", page_icon="💰")

st.title("💰 Predicción de Salarios")
st.write("Ingresa los datos para estimar el salario:")

# Inputs
job_options = {
    "AI Engineer": 0,
    "Backend Developer": 1,
    "Business Analyst": 2,
    "Cloud Engineer": 3,
    "Cybersecurity Analyst": 4,
    "Data Analyst": 5,
    "Data Scientist": 6,
    "DevOps Engineer": 7,
    "Frontend Developer": 8,
    "Machine Learning Engineer": 9,
    "Product Manager": 10,
    "Software Engineer": 11
}
job_title = st.selectbox("Trabajo", list(job_options.keys()))
val1 = job_options[job_title]

val2 = st.number_input("Años de experiencia", min_value=0, max_value=20, step=1)

education_options = {
    "Bachelor": 0,
    "Diploma": 1,
    "High School": 2,
    "Master": 3,
    "PhD": 4
}
education_level = st.selectbox("Nivel de educación", list(education_options.keys()))
val3 = education_options[education_level]

# Botón
if st.button("Predecir salario"):
    
    data = np.array([[val1, val2, val3]])
    
    prediction = model.predict(data)[0]
    rounded_salary = round(prediction, -3)

    st.success(f"💵 Salario estimado: ${rounded_salary:,.0f}")