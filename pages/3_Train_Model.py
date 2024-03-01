import streamlit as st 
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import time

st.title('Train Model on Iris Data')

if 'data' in st.session_state:
    df = st.session_state['data']

    x = df.drop(["target", "thal"],axis=1)
    y = df["target"]

    x_train , x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    st.session_state['x_train'] = x_train
    st.session_state['y_train'] = y_train
    st.session_state['x_test'] = x_test
    st.session_state['y_test'] = y_test

    # MODELS ARE CHANGED
    model_option = st.selectbox(
        'Select your favorite model:',
        ('--', 'LinearSVC', 'KNN', 'SVC', 'Logistic Regression'))
    st.session_state['model_option'] = model_option

    if model_option == 'LinearSVC':
        model = LinearSVC()
    elif model_option == 'KNN':
        model = KNeighborsClassifier()
    elif model_option == 'SVC':
        model = SVC()
    elif model_option == 'Logistic Regression':
        model = LogisticRegression()

    def find_the_model():
        progress_text = "Model training in progress..."
        my_bar = st.sidebar.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        my_bar.empty()
        model.fit(x_train,y_train)
        st.session_state['model'] = model
        st.info('Model is trained successfully', icon="ℹ️")

    if model_option != "--" and st.button("Train the Model"):
        find_the_model()
else:
    st.error('You need to upload the data before trtaining the model!')