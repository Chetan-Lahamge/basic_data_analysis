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
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File uploaded successfully!")
    st.write(f"DataFrame shape: {df.shape}")

# Show DataFrame's first rows
if st.button('First Rows'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.head())

# Show DataFrame's last rows
if st.button('Last Rows'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.tail())

# Show data types
if st.button('Data Types'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.dtypes)

# Show statistical summary
if st.button('Statistical Summary'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.describe(include='all'))

# Show missing values
if st.button('Missing Values'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df.isnull().sum())

# Correlation Matrix
if st.button('Correlation Matrix'):
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
column = st.selectbox('Select Column for Exploration', df.columns.tolist())

# Value counts
if st.button('Show Value Counts'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df[column].value_counts())

# Unique values
if st.button('Show Unique Values'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        st.write(df[column].unique())

# Histogram
if st.button('Show Histogram'):
    if df.empty:
        st.write("Please upload a CSV file.")
    else:
        plt.figure(figsize=(8,6))
        sns.histplot(df[column].dropna(), kde=True)
        st.pyplot()

# Boxplot
if st.button('Show Boxplot'):
    if df.empty:
        st.write("Please upload a CSV file.")
    elif df[column].dtype not in [np.float64, np.int64]:
        st.write(f"The selected column '{column}' is not numeric. Please select a numeric column.")
    else:
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=df[column].dropna())
        st.pyplot()