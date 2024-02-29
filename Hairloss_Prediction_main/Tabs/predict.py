"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions

from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent))
os.environ["PYTHONPATH"] = str(Path(__file__).parent.parent)

from Hairloss_Prediction_main.H_web_functions import predict 


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Early Prediction of Demenia.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    #Age = st.slider("Age", float(df["Age"].min()), float(df["Age"].max()))
    Age = int(st.number_input("Enter Age : "))

    col1, col2, col3 = st.columns(3)

    with col1:
        Genetics = st.radio("Genetics",["No","Yes"])
        Genetics1 = Genetics.index(Genetics) 
        
        Hormonal_Changes = st.radio("Hormonal Changes", ["No","Yes"])
        Hormonal_Changes1=Hormonal_Changes.index(Hormonal_Changes)

        Weight_Loss = st.radio("Weight Loss",["No","Yes"])
        Weight_Loss1=Weight_Loss.index(Weight_Loss)
            

    with col2:
        Stress = st.radio("Stress",["High","Low","Moderate"])
        Stress1=Stress.index(Stress)

        Poor_Hair_Care_Habits = st.radio("Poor Hair Care Habits",["No","Yes"])
        Poor_Hair_Care_Habits1=Poor_Hair_Care_Habits.index(Poor_Hair_Care_Habits)

    with col3:
        Environmental_Factors = st.radio("Environmental Factors",["No","Yes"])
        Environmental_Factors1=Environmental_Factors.index(Environmental_Factors)

        Smoking = st.radio("Smoking",["No","Yes"])
        Smoking1=Smoking.index(Smoking)



    #Medical_Conditions = st.slider("Medical Conditions", int(df["Medical Conditions"].min()), int(df["Medical Conditions"].max()))

    #Medications_and_Treatments = st.slider("Medications & Treatments", int(df["Medications & Treatments"].min()), int(df["Medications & Treatments"].max()))

    
    Medical_Conditions= st.selectbox("Medical Conditions", ['Alopecia Areata', 'Androgenetic Alopecia', 'Dermatitis', 'Dermatosis', 'Eczema',
                                          'None', 'Psoriasis', 'Ringworm', 'Scalp Infection',
                                          'Seborrheic Dermatitis',"Thyroid Problems"])
    Medical_Conditions1=Medical_Conditions.index(Medical_Conditions)
    
    Nutritional_Deficiencies = st.selectbox("Nutritional Deficiencies",['Biotin Deficiency','Iron deficiency','Magnesium deficiency',
                                            'None','Omega-3 fatty acids','Protein deficiency','Selenium deficiency',
                                            'Vitamin A Deficiency','Vitamin D Deficiency','Vitamin E deficiency',"Zinc Deficiency"])
    Nutritional_Deficiencies1=Nutritional_Deficiencies.index(Nutritional_Deficiencies)
    
    Medications_and_Treatments=st.selectbox("Medications and Treatments",['Accutane','Antibiotics','Antidepressants','Antifungal Cream',
                                                                          'Blood Pressure Medication','Chemotherapy','Heart Medication','Immunomodulators',
                                                                          'None','Rogaine',"Steroids"])
    Medications_and_Treatments1=Medications_and_Treatments.index(Medications_and_Treatments)

    #Hair_Loss = st.slider("Hair Loss", float(df["Hair Loss"].min()), float(df["Hair Loss"].max()))

    # Create a list to store all the features
    features = [Genetics,Hormonal_Changes,Medical_Conditions,Medications_and_Treatments,Nutritional_Deficiencies,Stress,Age,Poor_Hair_Care_Habits,Environmental_Factors,Smoking,Weight_Loss]
    features1 = [Genetics1,Hormonal_Changes1,Medical_Conditions1,Medications_and_Treatments1,Nutritional_Deficiencies1,Stress1,Age,Poor_Hair_Care_Habits1,Environmental_Factors1,Smoking1,Weight_Loss1]

    
    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["Genetics", "Hormonal Changes", "Medical Conditions", "Medications & Treatments",
                        "Nutritional Deficiencies", "Stress","Age", "Poor Hair Care Habits", "Environmental Factors",
                        "Smoking", "Weight Loss"]
    st.dataframe(df3)

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features1)
        print(score)
        #score = score#correction factor
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The person has no risk of Hair Loss")
        elif (prediction == 0):
            st.error("The person has risk of few hair loss if not maintained")
       # elif (prediction == 3):
        #    st.error("The person has risk of medium hair loss if not maintained")
        #elif (prediction == 4):
         #   st.error("The person has risk of acute hair loss if not maintained")
        #elif (prediction == 5):
         #   st.error("The person has risk of acute baldness and may have genetic causes.")'''
        
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100)), "%")
        