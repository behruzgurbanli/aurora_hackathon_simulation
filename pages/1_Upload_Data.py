import streamlit as st 
import pandas as pd

st.title('Upload Diabetes Data')

if 'data' in st.session_state:
    st.info('Data is already uploaded!', icon="ℹ️")
    st.write(st.session_state['data'].head())

else:
    uploaded_file = st.file_uploader("", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        expected = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
        actual = list(df.columns)
        if actual == expected:
            st.write(df.head())
            st.session_state['data'] = df
            st.info('Data uploaded successfully!', icon="ℹ️")
        else:
            st.error("Please upload the correct file!")