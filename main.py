# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from helper_functions import llm
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Dear citizen, welcome to your Medishield and Medisave information assistant. \n
How can I help you navigate your healthcare planning today? Your well-being is important to us!")

# Check if the password is correct.  
if not check_password():  
    st.stop()

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()

    print(course_details)
    df = pd.DataFrame(course_details)
    df 

with st.expander("Disclaimer"): 
    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. \n
    The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, \n
    especially those related to financial, legal, or healthcare matters.Furthermore, please be aware that the LLM may generate \n
    inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with \n
    qualified professionals for accurate and personalized advice.")
