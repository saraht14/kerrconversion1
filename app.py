
import streamlit as st
import pandas as pd

# Load the product mapping CSV
product_mapping = pd.read_csv('product_mapping.csv')

# Streamlit app layout
st.title("Kerr Product Number Finder")

# Text input for Manufacturer Product Number
user_input = st.text_input("Enter Manufacturer Product Number:")

# Search and display result
if user_input:
    result = product_mapping[product_mapping['Manufacturer_Product_Number'].str.strip().str.upper() == user_input.strip().upper()]
    if not result.empty:
        st.write("### ✅ Match Found:")
        st.write(result)
    else:
        st.warning("No matching Kerr Product Number found.")
else:
    st.warning("Please enter a Manufacturer Product Number.")
