import streamlit as st
import pandas as pd


from transformers import pipeline

@st.cache_resource  # 👈 Add the caching decorator
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

query = st.text_input("Your query", value="I love Movies & Tech")
if query:
    result = model(query)[0]  # 👈 Classify the query text
    st.write(result)
















# data1 = st.file_uploader("Upload your file to perform 'EDA' on it")

# @st.cache_data  # 👈 Add the caching decorator
# def load_data(data1):
#     df = pd.read_csv(data1)
#     return df

# df = load_data(data1)
# st.dataframe(df)

# # st.write(df.head(10))
# st.button("Rerun")