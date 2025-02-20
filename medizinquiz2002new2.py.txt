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
    
    return sorted(points.items(), key=lambda x: x[1], reverse=True)

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
        "hands-on work": "Do you prefer working with your hands rather than paperwork?",
        "technology in medicine": "Are you interested in using advanced medical technology in your practice?",
        "research": "Would you like to be involved in medical research?",
        "leadership": "Do you see yourself in a leadership role in the future?",
        "palliative care": "Are you interested in end-of-life and palliative care?",
        "emergency response": "Do you like working in emergency response situations?",
        "mental health": "Are you passionate about mental health care?",
        "sports medicine": "Are you interested in treating athletes and sports-related injuries?",
        "nutrition": "Do you find human nutrition and dietary health fascinating?",
        "cosmetic procedures": "Would you enjoy performing aesthetic and cosmetic procedures?",
        "legal medicine": "Are you interested in forensic and legal medicine?",
        "rural healthcare": "Would you prefer working in rural or underserved areas?",
        "telemedicine": "Would you be comfortable consulting patients via telemedicine?",
        "pediatrics": "Would you like to specialize in treating children?",
        "oncology": "Are you interested in cancer treatment and research?",
        "anesthesiology": "Do you enjoy precision work and pain management?",
        "intensive care": "Would you like to work with critically ill patients?",
        "epidemiology": "Would you like to study disease patterns in populations?",
        "pathology": "Are you interested in diagnosing diseases based on lab analysis?",
        "radiology": "Do you prefer working with medical imaging and diagnostics?",
        "dermatology": "Are you interested in skin health and treatments?",
        "endocrinology": "Do you want to specialize in hormone-related diseases?",
        "nephrology": "Are you interested in kidney health and dialysis treatment?",
        "gastroenterology": "Would you like to work with digestive system diseases?",
        "rheumatology": "Do you want to specialize in autoimmune diseases?",
        "hematology": "Are you interested in blood disorders and transfusion medicine?",
        "family medicine": "Do you enjoy providing comprehensive care for all age groups?",
        "infectious disease": "Would you like to work with pandemics and emerging diseases?",
    	"medical education": "Would you enjoy teaching and training future doctors?",
    	"hospital setting": "Do you prefer working in a hospital environment?",
    	"private practice": "Would you like to run your own medical practice?",
    	"surgical precision": "Do you have excellent hand-eye coordination and precision?",
    	"patient counseling": "Do you enjoy counseling and educating patients about their health?",
    	"global health": "Are you interested in improving healthcare in developing countries?",
    	"disaster medicine": "Would you like to work in disaster relief and emergency response teams?",
    	"infectious disease research": "Do you want to research and develop treatments for infectious diseases?",
    	"genetic counseling": "Would you enjoy advising patients on hereditary conditions?",
    	"sleep medicine": "Are you interested in studying and treating sleep disorders?",
    	"pain management": "Do you want to help patients manage chronic pain conditions?",
   	 "lifestyle medicine": "Do you want to focus on disease prevention through lifestyle changes?",
    	"geriatrics specialization": "Would you like to improve the quality of life for elderly patients?",
    	"pediatric surgery": "Are you interested in performing surgeries on children?",
    	"neurosurgery": "Do you want to specialize in brain and spinal cord surgery?",
    	"cardiac surgery": "Are you interested in operating on heart conditions?",
    	"transplant medicine": "Would you like to work in organ transplantation?",
    	"addiction medicine": "Would you like to help patients with substance use disorders?",
    	"rehabilitative therapy": "Are you interested in working with patients recovering from injuries?",
    	"radiation oncology": "Would you like to treat cancer patients with radiation therapy?",
    	"nuclear medicine": "Are you interested in using radioactive substances for diagnosis and treatment?",
    	"clinical pharmacology": "Would you enjoy studying the effects of drugs on the human body?",
    	"sports rehabilitation": "Do you want to help athletes recover from injuries?",
    	"occupational therapy": "Are you interested in helping people regain function after injury or illness?",
    	"prosthetics & orthotics": "Would you like to design and fit artificial limbs and braces?",
    	"emergency surgery": "Do you enjoy working under extreme pressure in the ER?",
    	"endocrinology & metabolism": "Would you like to specialize in metabolic disorders such as diabetes?",
    	"ophthalmology": "Are you interested in treating eye diseases and performing eye surgery?",
    	"otorhinolaryngology": "Would you like to treat conditions of the ear, nose, and throat?",
    	"urology": "Are you interested in diseases of the urinary tract and male reproductive organs?",
    	"gynecology": "Would you like to specialize in women's reproductive health?",
    	"maternal-fetal medicine": "Would you like to care for high-risk pregnancies?",
    	"neonatology": "Would you enjoy working with newborns, especially premature infants?",
    	"speech therapy": "Are you interested in helping patients with speech and swallowing disorders?",
    	"clinical psychology": "Would you like to focus on psychotherapy and mental health assessments?",
    	"psychiatric research": "Are you interested in studying mental health disorders?",
    	"neuropsychiatry": "Would you like to specialize in brain disorders that affect behavior?",
    	"autism & developmental disorders": "Are you interested in working with patients with autism and related conditions?",
    	"clinical ethics": "Do you enjoy debating medical ethics and policy?",
    	"medical journalism": "Would you like to write about medicine for the public or professionals?",
    	"health informatics": "Are you interested in improving healthcare through technology and data analysis?",
    	"robotic-assisted surgery": "Would you like to work with robotic surgical systems?",
    	"forensic toxicology": "Are you interested in analyzing drugs and poisons in forensic cases?",
    	"military trauma medicine": "Would you like to treat soldiers in combat situations?",
    	"space medicine": "Are you interested in the effects of space travel on human health?",
    	"wilderness medicine": "Would you like to provide medical care in remote or extreme environments?",
    	"biomedical engineering": "Do you want to design medical devices and prosthetics?",
    	"epigenetics": "Are you interested in how genes are influenced by environment and lifestyle?",
    	"clinical trials": "Would you like to lead studies on new treatments and medications?",
    	"medical policymaking": "Are you interested in shaping healthcare laws and policies?"
    }
    
    answers = {}
    for key, question in questions.items():
        answers[key] = st.radio(question, [True, False])
    
    if st.button("Show Result"):
        sorted_specialties = calculate_specialty(answers)
        
        st.subheader("Your Key Work Preferences:")
        if answers["patient interaction"]:
            st.write("- You prefer frequent patient interaction.")
        if answers["operative procedures"]:
            st.write("- You enjoy performing surgeries.")
        if answers["no night shifts"]:
            st.write("- You prefer predictable working hours.")
        if answers["research"]:
            st.write("- You have an interest in medical research and innovation.")
        if answers["palliative care"]:
            st.write("- You have a strong interest in compassionate, end-of-life care.")
        
        st.subheader("Top Matching Specialties:")
        for spec, score in sorted_specialties[:5]:
            st.write(f"**{spec}** - {score} points")
        
if __name__ == "__main__":
    main()










