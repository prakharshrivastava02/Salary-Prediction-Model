import streamlit as st
from joblib import dump, load
import numpy as np

def load_model():
    model = load('salary.joblib')
    return model
model = load_model()
def show_predict_page():
    st.title(" Salary Prediction Model")

    st.write("""### We need some information to predict the salary""")

    st.write("1 college - student's college (binary: 1 - goverment 0 - private) 2 sex - student's sex (binary: 1 - female or 0 - male) 3 age - student's age (numeric: from 15 to 22) 4 failures - backlogs 5 number of projects 6 number of certificates 7 absences - number of college absences (numeric: from 0 to 93) 8 cgpa")
    
    college = (
        "goverment",
        "private",
    )

    sex = (
        "male",
        "female",
    )

    college = st.number_input("College")
    sex = st.number_input("Gender")
    age = st.slider("age",18,50,1)
    failure = st.number_input("backlogs")
    project = st.number_input("project")
    certification = st.number_input("certification")
    attendance = st.number_input("attendance")
    cgpa = st.slider("CGPA", 0.0, 10.0, 0.1)

    ok = st.button("Calculate Salary")
    if ok:
        features = np.array([[college,sex,age,failure,project,certification,attendance,cgpa]])
        salary = model.predict(features)
        st.subheader(f"The estimated salary is Rs{salary[0]:.2f} LPA ")