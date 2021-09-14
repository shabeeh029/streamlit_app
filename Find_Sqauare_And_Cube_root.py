#Square Root- 
import streamlit as st

st.title("Find Square Root-")
x= st.slider('Select Your Number in Slider-', min_value=0 , max_value=1000)
st.write("Your Value Is-", x, 'And Square Root Is-', x**0.5)


#Cube Root-


st.title("Find Cube Root-")
x= st.slider('Select Your Number in slider-', min_value=0 , max_value=1000)
st.write("Your Value Is-", x, 'And Cube Root Is-', x**(1/3))
 