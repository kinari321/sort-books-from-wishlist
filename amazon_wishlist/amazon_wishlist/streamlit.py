import pandas as pd
import streamlit as st

# Read the JSON file into a DataFrame
df = pd.read_json("./amazon.json")

# Display the DataFrame as a table
st.write(df)