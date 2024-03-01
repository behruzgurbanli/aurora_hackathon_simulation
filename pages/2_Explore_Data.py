import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Exploratory Data Analysis")

if 'data' in st.session_state:
    df = st.session_state['data']
    option = st.selectbox(
        'Select your favorite model:',
        ('--', 'Scatter Plot', 'Histogram', 'Heatmap'))
    if option == 'Scatter Plot':
        fig, ax = plt.subplots()
        sns.scatterplot(x=df['age'], y=df['thalach'], hue=df["target"])
        plt.xlabel('Age')
        plt.ylabel('Maximum Heart Rate Achieved')
        st.pyplot(fig)
    elif option == 'Histogram':
        fig, ax = plt.subplots()
        needed_data = df.drop(['sex', 'cp', 'fbs', 'restecg', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'], axis=1)
        sns.histplot(data=needed_data, kde=True)
        st.pyplot(fig, use_container_width=True)
    elif option == 'Heatmap':
        fig, ax = plt.subplots()
        sns.heatmap(df.corr())
        st.pyplot(fig, use_container_width=True)