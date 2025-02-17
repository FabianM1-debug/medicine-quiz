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
    
    for key, value in answers.items():
        if value:
            if key in ["quick decisions", "high-pressure work"]:
                points["Emergency Medicine"] += 2
            if key in ["analytical thinking", "problem-solving"]:
                points["Neurology"] += 2
                points["Radiology"] += 2
            if key in ["patient interaction", "long-term care"]:
                points["General Medicine"] += 2
                points["Psychiatry"] += 2
            if key in ["operative procedures", "hands-on work"]:
                points["Surgery"] += 2
                points["Robotic Surgery"] += 1
            if key in ["no night shifts", "structured work hours"]:
                points["Dermatology"] += 2
                points["Radiology"] += 1
            if key in ["infectious diseases"]:
                points["Tropical Medicine"] += 2
            if key in ["genetics"]:
                points["Human Genetics"] += 2
            if key in ["military medicine"]:
                points["Military Medicine"] += 2
            if key in ["rehabilitation"]:
                points["Rehabilitation Medicine"] += 2
            if key in ["geriatrics"]:
                points["Geriatrics"] += 2
            if key in ["occupational medicine"]:
                points["Occupational Medicine"] += 2
            if key in ["public health"]:
                points["Public Health"] += 2
            if key in ["pharmacology"]:
                points["Pharmacology"] += 2
            if key in ["aerospace medicine"]:
                points["Aerospace Medicine"] += 2
    
    best_fit = max(points, key=points.get)
    return best_fit

def main():
    st.title("Medical Specialty Quiz")
    
    st.write("Answer the following questions to find out which medical specialty suits you best!")
    
    questions = {
        "quick decisions": "Do you enjoy making quick decisions?",
        "analytical thinking": "Do you enjoy detailed analysis?",
        "patient interaction": "Is direct patient interaction important to you?",
        "operative procedures": "Are you interested in performing surgical procedures?",
        "no night shifts": "Do you prefer regular working hours without night shifts?",
        "infectious diseases": "Are you interested in tropical medicine and infectious diseases?",
        "genetics": "Are you interested in genetic disorders?",
        "military medicine": "Could you envision a career in military medicine?",
        "rehabilitation": "Would you like to work with rehabilitation patients?",
        "geriatrics": "Are you interested in geriatric medicine?",
        "occupational medicine": "Are you interested in occupational medicine and work-related diseases?",
        "pharmacology": "Are you interested in pharmacology and drug development?",
        "public health": "Would you like to work in public health?",
        "aerospace medicine": "Could you imagine a career in aerospace medicine?",
        "problem-solving": "Do you enjoy solving complex problems?",
        "high-pressure work": "Do you thrive in high-pressure situations?",
        "long-term care": "Would you enjoy treating patients over a long period?",
        "structured work hours": "Do you prefer highly structured and predictable work hours?",
        "hands-on work": "Do you prefer working with your hands rather than paperwork?"
    }
    
    answers = {}
    for key, question in questions.items():
        answers[key] = st.radio(question, [True, False])
    
    if st.button("Show Result"):
        specialty = calculate_specialty(answers)
        st.success(f"Based on your answers, the best-fitting medical specialty for you is: {specialty}!")
        
if __name__ == "__main__":
    main()
