"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Demenia dataset into DataFrame.
    df = pd.read_csv('Hairloss_Prediction_main/hair_loss_intggggg.csv')

    # Perform feature and target split
   # X = df[["total_protein","total_keratine","hair_texture","vitamin","manganese","iron","calcium","body_water_content","stress_level","liver_data"]]
    #y = df['hair_fall']
    #X = df.drop("Hair Loss", axis=1)
    X = df[["Genetics", "Hormonal Changes", "Medical Conditions", "Medications & Treatments",
                        "Nutritional Deficiencies", "Stress","Age", "Poor Hair Care Habits", "Environmental Factors",
                        "Smoking", "Weight Loss"]]
    y = df["Hair Loss"]
    return df, X, y

@st.cache_data()
def train_model(X, y):
    
    """This function trains the model and return the model and model score"""
    #split the data into training and test dataset
    # Normalize the features using Min-Max scaling
    scaler = MinMaxScaler()
    X_normalized = scaler.fit_transform(X)
    x_train,x_test,y_train,y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=30)

    model = RandomForestClassifier(n_estimators= 109, random_state= 308)

    
    # Fit the data on model
    model.fit(x_train, y_train)
    # Get the model score
    score = model.score(x_test, y_test)

    # Return the values
    return model, score

def predict(X, y, features1):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features1).reshape(1, -1))

    return prediction, score
