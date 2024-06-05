import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load data from a CSV file
data = pd.read_csv('shipping.csv')

def eda_page():

    st.title("Exploratory Data Analysis")
    st.write('Data exploration is made to better understand the dataset')
    st.subheader("Distribution of reached on time and Not reached on time Patient")

    # Make plot pie on reached on time
    infected_pie_chart_fig, ax = plt.subplots(figsize=(10, 8))

    # Set the background color of the plot to dark
    ax.patch.set_facecolor('#333333')

    # Create the pie chart
    ax.pie(data['Reached.on.Time_Y.N'].value_counts(), labels=['NOT reached on time', 'reached on time'], 
            explode=[0,0.1], autopct='%.0f%%', colors=['#007bff', '#ffa07a'])

    # Display the plot using Streamlit
    st.pyplot(infected_pie_chart_fig)
    st.write("**Description**:")
    st.write('Based on the figure above, there is an imbalance between an reached on time and NOT reached on time. The figure shows that there are 60% of Non reached on time and there are only 40% of reached on time')
    st.write()
    
    st.subheader("Check Infected Patient Distribution from Categorical Data")

    cat_columns = data.select_dtypes(include=['object']).columns

    # Create a figure with a specified size
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(20, 4))

    # Loop through the categorical columns and create a countplot for each
    for i, col in enumerate(cat_columns[:4]):
        sns.countplot(data=data, x=col, hue=data['Reached.on.Time_Y.N'], palette='pastel', ax=axs[i])


    # Display boxplot using Streamlit
    st.pyplot(fig)
    st.write("""**penjelasan**  \n* warehouse_block : pada F banyak not reached on time\n* mode_of_shipment : pada ship di dapat banyak not reached on time\n* product_importance : pada low di dapat banyak not reached on time\n* gender : pada gender keduanya banyak not reached on time""")
   

    cols = data.select_dtypes(include=['int64']).columns

    num_rows = 3
    num_cols = 2

    fig = plt.figure(figsize=(20, 20))

    for index in range(1, num_rows*num_cols):
        fig.add_subplot(num_rows, num_cols, index)
        sns.boxplot(data=data, y=cols[index-1])

    st.pyplot(fig)
    st.write("**penjelasan**:")
    st.write("""dari kolom numerical di dapatkan :
- banyak data **outliers** dan harus di handle""")

    # Check the histogram of the categorical data
    fig = plt.figure(figsize=(20, 20))
    cols = data.select_dtypes(include=['object']).columns
    sns.countplot(data=data,x="Mode_of_Shipment")
    plt.title("Type of shipments (Most Used)")
    st.pyplot(fig)
    st.write("**penjelasan**:")
    st.write("""* mode_of_shipment: di dapat banyak yang menggunakan *ship*""")

    # Grouping the data
    grouped = data.groupby(["Mode_of_Shipment","Product_importance"])["Cost_of_the_Product"].sum().unstack()

    # Creating a bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title("Model of shipment vs product_cost")

    # Displaying the plot in Streamlit
    st.pyplot(fig)

    # Grouping the data
    grouped = data.groupby(["Mode_of_Shipment","Product_importance"])["Weight_in_gms"].sum().unstack()

    # Creating a bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title("Model of shipment vs Weight_in_gms")

    # Displaying the plot in Streamlit
    st.pyplot(fig)

    # Grouping the data
    grouped = data.groupby(["Mode_of_Shipment","Product_importance"])["Discount_offered"].sum().unstack()

    # Creating a bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title("Model of shipment vs Discount_offered")

    # Displaying the plot in Streamlit
    st.pyplot(fig)
    st.write("**penjelasan**:")
    st.write('Untuk diskon kapal ditawarkan lebih banyak dan juga karena harga dan berat produk semakin banyak orang yang memilih kapal')
    