# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 04:02:10 2024

@author: altul
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/altul/Downloads/twaq/week7/strimlit/trained_model.sav', 'rb'))

# function 
def diabetes (input_data):
    #input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    return (prediction)

    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')
  
    
def main():
    
      
      # the name of the websit
    st.title('Diabetes Prediction Web App')
    
    Pregnancies = st.text_input('Enter the number of pregnancies: ')
    Glucose = st.text_input('Enter the glucose level: ')
    BloodPressure = st.text_input('Enter the blood pressure: ')
    SkinThickness = st.text_input('Enter the skin thickness: ')
    Insulin = st.text_input('Enter the insulin level: ')
    BMI = st.text_input('Enter the BMI: ')
    DiabetesPedigreeFunction = st.text_input('Enter the diabetes pedigree function: ')
    Age = st.text_input('Enter the age: ')
    
    
    # code for pediction 
    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(dignosis)
    
if __name__ == '__main__':
    main()