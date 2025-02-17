import streamlit as st
import pandas as pd

def calculate_specialty(answers):
    points = {
        "Emergency Medicine": 0,
        "Surgery": 0,
        "Neurology": 0,
        "Psychiatry": 0,
        "Cardiology": 0,
        "Radiology": 0,
        "General Medicine": 0,
        "Dermatology": 0,
        "Pathology": 0,
        "Tropical Medicine": 0,
        "Human Genetics": 0,
        "Military Medicine": 0,
        "Robotic Surgery": 0,
        "Naturopathy": 0,
        "Forensic Medicine": 0,
        "Rehabilitation Medicine": 0,
        "Geriatrics": 0,
        "Occupational Medicine": 0,
        "Pharmacology": 0,
        "Public Health": 0,
        "Aerospace Medicine": 0,
    }
    
    if answers["quick decisions"]:
        points["Emergency Medicine"] += 2
        points["Surgery"] += 1
    if answers["analytical thinking"]:
        points["Neurology"] += 2
        points["Radiology"] += 2
    if answers["patient interaction"]:
        points["General Medicine"] += 2
        points["Psychiatry"] += 2
    if answers["operative procedures"]:
        points["Surgery"] += 2
        points["Robotic Surgery"] += 1
    if answers["no night shifts"]:
        points["Dermatology"] += 2
        points["Radiology"] += 1
    if answers["infectious diseases"]:
        points["Tropical Medicine"] += 2
    if answers["genetics"]:
        points["Human Genetics"] += 2
    if answers["military medicine"]:
        points["Military Medicine"] += 2
    if answers["rehabilitation"]:
        points["Rehabilitation Medicine"] += 2
    if answers["geriatrics"]:
        points["Geriatrics"] += 2
    if answers["occupational medicine"]:
        points["Occupational Medicine"] += 2
    if answers["public health"]:
        points["Public Health"] += 2
    if answers["pharmacology"]:
        points["Pharmacology"] += 2
    if answers["aerospace medicine"]:
        points["Aerospace Medicine"] += 2
    
    best_fit = max(points, key=points.get)
    return best_fit

def main():
    st.title("Medical Specialty Quiz")
    
    st.write("Answer the following questions to find out which medical specialty suits you best!")
    
    answers = {
        "quick decisions": st.radio("Do you enjoy making quick decisions?", [True, False]),
        "analytical thinking": st.radio("Do you enjoy detailed analysis?", [True, False]),
        "patient interaction": st.radio("Is direct patient interaction important to you?", [True, False]),
        "operative procedures": st.radio("Are you interested in performing surgical procedures?", [True, False]),
        "no night shifts": st.radio("Do you prefer regular working hours without night shifts?", [True, False]),
        "infectious diseases": st.radio("Are you interested in tropical medicine and infectious diseases?", [True, False]),
        "genetics": st.radio("Are you interested in genetic disorders?", [True, False]),
        "military medicine": st.radio("Could you envision a career in military medicine?", [True, False]),
        "rehabilitation": st.radio("Would you like to work with rehabilitation patients?", [True, False]),
        "geriatrics": st.radio("Are you interested in geriatric medicine?", [True, False]),
        "occupational medicine": st.radio("Are you interested in occupational medicine and work-related diseases?", [True, False]),
        "pharmacology": st.radio("Are you interested in pharmacology and drug development?", [True, False]),
        "public health": st.radio("Would you like to work in public health?", [True, False]),
        "aerospace medicine": st.radio("Could you imagine a career in aerospace medicine?", [True, False]),
    }
    
    if st.button("Show Result"):
        specialty = calculate_specialty(answers)
        st.success(f"Based on your answers, the best-fitting medical specialty for you is: {specialty}!")
        
if __name__ == "__main__":
    main()
