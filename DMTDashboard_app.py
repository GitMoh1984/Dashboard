import streamlit as st
import pandas as pd

st.title("welcome to DMT Dashboard")
st.sidebar.markdown("# Main page 🎈")
upload_file = st.file_uploader("Choose a CSV or file", type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.subheader("Data Preview")
    st.write(df.head())
    st.subheader("Data Summary")
    st.write(df.describe())
    st.subheader("Filter data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select Columns to Filter ", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Values to be Filtered", unique_values)
    filtered_df = df[df[selected_column] == selected_value]
    st.subheader("Display Filtered Data")
    st.write(filtered_df)
st.sidebar.markdown("# Sub page ")
