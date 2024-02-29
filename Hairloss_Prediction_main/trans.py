# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import random
# Load the Demenia dataset into DataFrame.
df = pd.read_csv('hair_loss_intggggg.csv')

# Perform feature and target split
X = df[["Genetics", "Hormonal Changes", "Medical Conditions", "Medications & Treatments",
        "Nutritional Deficiencies", "Stress","Age", "Poor Hair Care Habits", "Environmental Factors",
        "Smoking", "Weight Loss"]]
y = df["Hair Loss"]

# Create the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the data on model
model.fit(X, y)

# Get the model score
score = model.score(X, y)

# Predict the value
features1 = [0,0,6,0,1,2,30,0,1,1,0]  # Replace with your actual feature values

prediction = model.predict(np.array(features1).reshape(1, -1))

# Print results
print("Model Score:", score)
print("Prediction:", prediction)

#accuracy
print("Accuracy of Model is ", score*100,"%")


