import streamlit as st
import numpy as np
import pandas as pd
import joblib

from eda import eda_page
from prediction import model_page

#Load data
data = pd.read_csv("shipping.csv")

st.header('Milestone 2')
st.write("""
Created by Albert Novanto P J - HCK015 """)

st.write(" `Shipping_Classification` database")
st.write("Dataset `shipping`")
data

def main():
    # Define menu options
    menu_options = ["Data Analysis", "Model Prediction"]

    # Create sidebar menu
    selected_option = st.sidebar.radio("Menu", menu_options)

    # Display selected page
    if selected_option == "Data Analysis":
        eda_page()
    elif selected_option == "Model Prediction":
        model_page()


if __name__ == "__main__":
    main()