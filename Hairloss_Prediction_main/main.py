"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import pages

from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent))
os.environ["PYTHONPATH"] = str(Path(__file__).parent.parent)

from Hairloss_Prediction_main.H_web_functions import load_data
from Hairloss_Prediction_main.Tabs import home, data, predict

def Hmain():
    # Configure the app
    


    # Dictionary for pages
    Tabs = {
        "Home": home,
        "Data Info": data,
        "Prediction": predict,
        
        #"About me": about
    }

    # Create a sidebar
    # Add title to sidear
    st.sidebar.title("Navigation")

    # Create radio option to select the page
    page = st.sidebar.radio("Pages", list(Tabs.keys()))



    # Loading the dataset.
    df, X, y = load_data()

    # Call the app funciton of selected page to run
    if page in ["Prediction"]:
        Tabs[page].app(df, X, y)
    elif (page == "Data Info"):
        Tabs[page].app(df)
    else:
        Tabs[page].app()
