import pandas as pd
import streamlit as st
import datetime
import pickle


st.write(
    """
     # Insurance Cost Prediction
    """
)

#st.dataframe(cars_df.head())

age = st.number_input('Age',min_value=0,max_value=100,value=30)

col1, col2 = st.columns(2)


diabetes = col1.selectbox("Diabetes",
                           ["Yes", "No"])


blood_pressure = col1.selectbox("Blood Pressure",
                     ["Yes", "No"])

any_transplants = col2.selectbox("Any Transplants", 
                                   ["Yes", "No"])

any_chronic_disease = col2.selectbox("Any Chronic Disease", 
                                   ["Yes", "No"])

height = st.number_input('Height',min_value=145.0,max_value=190.0,value=150.0)		
weight = st.number_input('Weight',min_value=50.0,max_value=140.0,value=50.0)	

known_allergies = col1.selectbox("Known Allergies", 
                                   ["Yes", "No"])

history_of_cancer = col2.selectbox("History of Cancer", 
                                   ["Yes", "No"])

no_surgeries = st.selectbox("Number of Major Surgeries",
                       [0,1,2,3])								   


#input_features = [[2018.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
encode_dict = {
    "diabetes": {'Yes': 1, 'No': 0},
	"blood_pressure":{'Yes': 1, 'No': 0},
	"any_transplants":{'Yes': 1, 'No': 0},
	"any_chronic_disease":{'Yes': 1, 'No': 0},
	"known_allergies":{'Yes': 1, 'No': 0},
	"history_of_cancer":{'Yes': 1, 'No': 0}    
}

def model_pred(age,diabetes,blood_pressure,any_transplants,any_chronic_disease,known_allergies,history_of_cancer,height,weight,no_surgeries):

    ## loading the model
    with open("classifier.pkl", 'rb') as file:
        clas_model = pickle.load(file)
        input_features = [[age,diabetes,blood_pressure,any_transplants,any_chronic_disease,known_allergies,history_of_cancer,height,weight,no_surgeries]]
        return clas_model.predict(input_features)

if (st.button("Predict Premium")):
	
	diabetes = encode_dict['diabetes'][diabetes]
	blood_pressure = encode_dict['blood_pressure'][blood_pressure]
	any_transplants = encode_dict['any_transplants'][any_transplants]
	any_chronic_disease = encode_dict['any_chronic_disease'][any_chronic_disease]
	known_allergies = encode_dict['known_allergies'][known_allergies]
	history_of_cancer = encode_dict['history_of_cancer'][history_of_cancer]
	
	prem_price = model_pred(age,diabetes,blood_pressure,any_transplants,any_chronic_disease,known_allergies,history_of_cancer,height,weight,no_surgeries)
	st.text(f"Insurance Premium is {prem_price[0].round(2)} rupees.")
