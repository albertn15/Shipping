import streamlit as st
import numpy as np
import pandas as pd
import joblib

def model_page():
    st.title("UNTUK MEMPREDIKSI SHIPPING YANG REACH ON TIME OR NOT REACH ON TIME")
    st.write("")
    st.sidebar.header('User Input Features')

    input_data = user_input()

    st.subheader('User Input')
    st.write(input_data)

    load_model = joblib.load("knn_best_model_pipeline.joblib")

    prediction = load_model.predict(input_data)

    if prediction == 1:
        prediction = 'reached on time'
    else:
        prediction = 'NOT reached on time'

    st.write('Based on user input, the model predicted: ')
    st.write(prediction)

def user_input(num_rows=1):
    Customer_care_calls = st.sidebar.number_input('Customer_care_calls', 2, 7,)
    Cost_of_the_Product = st.sidebar.number_input('Cost_of_the_Product', 96, 310)
    Prior_purchases = st.sidebar.number_input('Prior_purchases', 2.0, 5.5)
    Discount_offered = st.sidebar.number_input('Discount_offered', 1, 19)
    Weight_in_gms = st.sidebar.number_input('Weight_in_gms', 1492, 5017)
    Product_importance = st.sidebar.selectbox('Product_importance', ['low', 'high', 'medium'])
        
    data = {
        'Customer_care_calls': Customer_care_calls,
        'Cost_of_the_Product': Cost_of_the_Product,
        'Prior_purchases': Prior_purchases,
        'Discount_offered': Discount_offered,
        'Weight_in_gms': Weight_in_gms,
        'Product_importance': Product_importance,
        }
    features = pd.DataFrame(data, index=[0])
    return features