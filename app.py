import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Initialize an empty DataFrame
df = pd.DataFrame()

# File upload
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.write("File uploaded successfully!")
    st.sidebar.write(f"DataFrame shape: {df.shape}")

# Sidebar options
st.sidebar.header('Exploration Options')
option = st.sidebar.radio('Choose an action:', 
                         ('Show DataFrame', 'Data Types', 'Statistical Summary', 'Missing Values', 'Correlation Matrix', 
                          'Column Exploration', 'Show Histogram', 'Show Boxplot'))

# Show DataFrame's first rows
if option == 'Show DataFrame':
    st.header('DataFrame Preview')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        show_first_last = st.sidebar.radio('Choose view:', ('First Rows', 'Last Rows'))
        if show_first_last == 'First Rows':
            st.write(df.head(),use_container_width=True)
        elif show_first_last == 'Last Rows':
            st.write(df.tail(),use_container_width=True)

# Show data types
elif option == 'Data Types':
    st.header('Data Types')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.dtypes,use_container_width=True)

# Show statistical summary
elif option == 'Statistical Summary':
    st.header('Statistical Summary')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        summary = df.describe(include='all')
        st.dataframe(summary, use_container_width=True)

# Show missing values
elif option == 'Missing Values':
    st.header('Missing Values')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.isnull().sum())

# Correlation Matrix
elif option == 'Correlation Matrix':
    st.header('Correlation Matrix')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.empty:
            st.write("No numeric columns available for correlation.")
        else:
            corr = numeric_df.corr()
            st.write(corr)
            
            # Create figure
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
            st.pyplot(fig)

# Column selection and exploration
elif option == 'Column Exploration':
    st.header('Column Exploration')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        column = st.sidebar.selectbox('Select Column for Exploration', df.columns.tolist())
        
        # Value counts
        if st.sidebar.button('Show Value Counts'):
            st.write(df[column].value_counts())

        # Unique values
        if st.sidebar.button('Show Unique Values'):
            st.write(df[column].unique())

# Histogram
elif option == 'Show Histogram':
    st.header('Histogram')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        column = st.sidebar.selectbox('Select Column for Histogram', df.columns.tolist())
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(df[column].dropna(), kde=True, ax=ax)
        st.pyplot(fig)

# Boxplot
elif option == 'Show Boxplot':
    st.header('Boxplot')
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        column = st.sidebar.selectbox('Select Column for Boxplot', df.columns.tolist())
        if df[column].dtype not in [np.float64, np.int64]:
            st.write(f"The selected column '{column}' is not numeric. Please select a numeric column.")
        else:
            plt.figure(figsize=(8, 6))
            sns.boxplot(y=df[column].dropna())
            st.pyplot()
