import streamlit as st 
import numpy as np
from sklearn.metrics import accuracy_score

st.title('Test Accuracy of Model')

if 'model' in st.session_state:
    model = st.session_state['model']
    x_test = st.session_state['x_test']
    y_test = st.session_state['y_test']

    option = st.selectbox(
        'How do you want to test?',
        ('--', 'Test Data', 'Custom Values'))

    if option == 'Test Data':

        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test,y_pred)

        st.info('The accuracy of our model is ' + str(accuracy))
    
    # CHANGED CUSTOM VALUES
    elif option == 'Custom Values':
        age = st.number_input('Age', -1)

        sex = st.selectbox(
            'Sex', 
            ("0", "1"))
        sex = int(sex)

        cp = st.selectbox(
        'Chest Pain Type',
        ('-1', '0', '1', '2', '3'))
        cp = int(cp)

        trestbps = st.number_input('Resting Blood Pressure', -1)

        chol = st.number_input('Serum Cholestoral in mg/dl', -1)
      
        fbs = st.number_input('Fasting blood sugar > 120 mg/dl', -1)
        
        restecg = st.selectbox(
            'Resting electrocardiographic results',
            ('-1', '0', '1', '2')
        )
        restecg = int(restecg)
        
        thalach = st.number_input('Maximum heart rate achieved', -1)        

        exang = st.number_input('Exercise induced angine', -1)

        oldpeak = float(st.number_input('ST depression induced by exercise relative to rest', -1))

        scope = st.number_input('The slope of the peak exercise ST segment', -1)

        ca = st.selectbox(
            'Number of major vessels colored by fluorosopy',
            ('0', '1', '2', '3')
        )
        ca = int(ca)

        test = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, scope, ca]).reshape(1, -1)

        if st.button('Predict'):
            if trestbps < 0 or chol < 0 or cp < 0 or age < 0 or thalach < 0:
                st.error("Please enter positive values.")

            score = model.predict(test)[0]
            result = ''

            if score == 0:
                result = 'No disease'
            elif score == 1:
                result = 'Disease'

            if -1 not in test:
                st.info('The predicted condition for the patient: ' + result)
else:
    st.error('The model is not trained yet!')