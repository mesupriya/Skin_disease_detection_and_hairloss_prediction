import streamlit as st
from Hairloss_Prediction_main.main import Hmain
from Skin_Disease_detection_main.app import Smain
from img import Imain

# Page 1
def page1():
    st.title("Skin Disease Detection")
    #st.write("This is page 1.")

# Page 2
def page2():
    st.title("Hair loss predection")
    #st.write("This is page 2.")

# Sidebar to switch between pages
page = st.sidebar.selectbox(
    "Select a page",
    ("Home Page","Skin Disease Detection", "Hair loss predection")
)

# Display the selected page
if page == "Skin Disease Detection":
    Smain()
elif page == "Hair loss predection":
    Hmain()
else :
    Imain()