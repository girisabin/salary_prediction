import streamlit as st
import joblib  # for loading the save model

# load the save model
model = joblib.load('age_profession_salary_prediction_model.pkl')

# title of the app
st.title("Age Profession Salary Predictor")

# input age from the user
age = st.number_input("Enter your age:",min_value=23, max_value=60, value=25)

st.write("For Profession Input")
st.write("1 for Enginner , 2 for Lawyer, 3 for Manager, 4 for Scientist and 0 for Doctor")
profession = st.number_input("Enter your profession:",min_value = 0, max_value = 4, value = 3)

# button to make the prediction
if st.button("Predict Salary Status"):
    prediction = model.predict([[age,profession]])  # make prediction using the loaded model

    st.success(f"Predicted Salary Status: ${prediction[0]}")