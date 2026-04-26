import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model_pipeline.pkl", "rb"))

st.title("HR Attrition Prediction")

age = st.slider("Age", 18, 60, 30)
distance = st.slider("Distance From Home", 1, 50, 10)
education = st.slider("Education Level", 1, 5, 3)
years = st.slider("Years At Company", 0, 40, 5)

income = st.number_input("Monthly Income", 1000, 20000, 5000)
satisfaction = st.slider("Job Satisfaction", 1, 4, 3)

travel = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
dept = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
role = st.selectbox("Job Role", [
    "Sales Executive","Research Scientist","Laboratory Technician",
    "Manufacturing Director","Healthcare Representative",
    "Manager","Sales Representative","Research Director","Human Resources"
])

# Create input
data = pd.DataFrame({
    "Age":[age],
    "BusinessTravel":[travel],
    "Department":[dept],
    "DistanceFromHome":[distance],
    "Education":[education],
    "JobRole":[role],
    "MonthlyIncome":[income],
    "JobSatisfaction":[satisfaction],
    "YearsAtCompany":[years]
})

if st.button("Predict"):
    result = model.predict(data)[0]

    if result == 1:
        st.error("Employee likely to leave")
    else:
        st.success("Employee likely to stay")
