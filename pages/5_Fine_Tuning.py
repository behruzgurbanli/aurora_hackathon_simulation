import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import time

st.title("Fine Tuning of the Parameters")

if 'model' in st.session_state:
    model_option = st.session_state['model_option']

    x_train = st.session_state['x_train']
    y_train = st.session_state['y_train']
    x_test = st.session_state['x_test']
    y_test = st.session_state['y_test']

    if model_option == 'LinearSVC':
        penalty_param = st.selectbox(
            'Penalty', 
            ('l1', 'l2'))
        C_param = st.number_input('Insert a number for the C parameter')
        max_iter_param = st.number_input('Insert a number for the max iterations parameter')
        model = LinearSVC(penalty=penalty_param, C=C_param, max_iter=int(max_iter_param))
    elif model_option == 'KNN':
        neighbors_param = st.number_input('Insert a number for the neigbors parameter')
        weights_param = st.selectbox(
            'Weight',
            ('uniform', 'distance'))
        leaf_size_param = st.number_input('Insert a number for the leaf size parameter')
        model = KNeighborsClassifier(n_neighbors=int(neighbors_param), weights=weights_param, leaf_size=int(leaf_size_param))
    elif model_option == 'SVC':
        C_param = st.number_input('Insert a number for the C parameter')
        kernel_param = st.selectbox(
            'Insert a parameter for the kernel',
            ('linear', 'poly', 'rbf', 'sigmoid'))
        max_iter_param = st.number_input('Insert a number for the max iterations parameter')
        model = SVC(C=C_param, kernel=kernel_param, max_iter=int(max_iter_param))
    elif model_option == 'Logistic Regression':
        C_param = st.number_input('Insert a number for the C parameter')
        solver_param = st.selectbox (
            'Solver',
            ("lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga"))
        max_iter_param = st.number_input('Insert a parameter for the max iteration')
        model = LogisticRegression(C=C_param, solver=solver_param, max_iter=int(max_iter_param))

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
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test,y_pred)
        st.success('The accuracy of our model is ' + str(accuracy))

    if st.button("Train the Model"):
        find_the_model()
else:
    st.error('You need to make a choice first!')