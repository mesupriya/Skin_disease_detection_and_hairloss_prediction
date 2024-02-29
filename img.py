import streamlit as st
from Hairloss_Prediction_main.main import Hmain
from Skin_Disease_detection_main.app import Smain
from streamlit_extras.switch_page_button import switch_page
def Imain():
    # Provide file paths for your images
    image1_path = "skin2.jpg"
    image2_path = "hair2.jpg"

    #st.title("Home page")
    st.markdown("<h1 style='text-align:center'>Home Page</h1>",unsafe_allow_html=True)
    st.title("")
    # Display images in a two-column layout with space in between
    col1, col2, col3 = st.columns([12,9,12])

    # Display Image 1 in the first column
    with col1:
        col1.image(image1_path, width=400)
        st.write("Skin diseases include all conditions that clog,irritate or inflame your skin. Often, skin diseases cause rashes or other changes in your skin’s appearance.")
        st.write('<a href="https://my.clevelandclinic.org/health/diseases/21573-skin-diseases" >click here to know about skin disease</a>',unsafe_allow_html=True)

 
    
    # Insert some space between the columns
    #st.markdown("<br>", unsafe_allow_html=True)

    # Display Image 2 in the second column
    with col3:
        col3.image(image2_path, width=400)
        st.write("Hair loss can happen due to many variables, such as genetic factors, vitamin deficiencies, skin problems,hormonal problems, stress and depression.etc")
        st.write('<a href="https://my.clevelandclinic.org/health/diseases/21753-hair-loss" >click here to know about Hair loss</a>',unsafe_allow_html=True)


  


if __name__ == "__main__":
    main()
