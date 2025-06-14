import streamlit as st
import pandas as pd

# Load the correct mapping file
product_mapping = pd.read_csv("Updated_Master_Product_Mapping_1.csv")

# Streamlit input
user_input = st.text_input("Enter a Manufacturer Product Number:")

# Check if input is valid before processing
if user_input and isinstance(user_input, str):
    cleaned_input = user_input.strip().upper()
    result = product_mapping[product_mapping['Competitor Product Number'].str.strip().str.upper() == cleaned_input]

    if not result.empty:
        st.success("✅ Match Found:")
        st.write(result[['Brand', 'Kerr Equivalent']])
    else:
        st.warning("No matching Kerr Product Number found.")
else:
    st.info("Please enter a valid Manufacturer Product Number.")
