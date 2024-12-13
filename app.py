import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
from PIL import Image
from PIL import Image

load_hdmodel=pickle.load(open('Models/hdmodel.sav','rb'))
load_dbmodel=pickle.load(open('Models/diabetes_model.sav','rb'))
load_pkmodel=pickle.load(open('Models/parkinsons_model.sav','rb'))
st.write(f"# Disease Prediction Application")
st.write(f"## Please provide your details")

with st.sidebar:
    selected = option_menu("Choose the Disease", ["Heart Disease Prediction", "Diabetes Prediction", "Parkinson Prediction"])

if selected=="Heart Disease Prediction":
    st.write(f"## Heart Disease Prediction")
    col1,col2,col3=st.columns(3)
    with col1:
        st.write(f"## Enter your details")
        age = st.text_input("Type your age")
        sex = st.text_input("Type your sex")
        cp = st.text_input("Type your cp")
        testbps = st.text_input("Type your testbps")
        chol = st.text_input("Type your chol")
        fbs = st.text_input("Type your fbs")
    with col2:
        st.write(f"## Enter your details")
        #restecg = st.text_input("Type your restecg")
        restecg = st.text_input("Type your restecg")
        thalach = st.text_input("Type your thalach")
        exang = st.text_input("Type your exang")
        oldpeak = st.text_input("Type your oldpeak")
        slope = st.text_input("Type your slope")
        ca = st.text_input("Type your ca")
        thal = st.text_input("Type your thal")
    with col3:
        image=Image.open("images/heart.png")
        st.image(image, caption='Heart Disease')

    if st.button("Predict"):
        data = [age, sex, cp, testbps, chol, fbs, restecg,thalach, exang, oldpeak, slope, ca, thal]
        data1 = np.array(data, dtype=float).reshape(1, -1)
        prediction = load_hdmodel.predict(data1).reshape(-1, 1)
        if prediction == 0:
            prediction_1 = "No Disease"
        else:
            prediction_1 = "Disease"
        st.write(f"## Prediction: {prediction_1}")
if selected=="Diabetes Prediction":
    st.write(f"## Diabetes Prediction") 
    # Take User inputs
    col1, col2, col3= st.columns(3)
   
    with col1:
        Pregnancies = st.text_input('No of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI')
    if st.button("Predict"):
        data2 = [Pregnancies, SkinThickness, DiabetesPedigreeFunction, Glucose, Insulin, Age,BloodPressure, BMI]
        data3 = np.array(data2, dtype=float).reshape(1, -1)
        prediction = load_dbmodel.predict(data3).reshape(-1, 1)
        if prediction == 0:
            prediction_1 = "No Disease"
        else:
            prediction_1 = "Disease"
        st.write(f"## Prediction: {prediction_1}")

if selected=='Parkinson Prediction':
    st.write(f"## Parkinsons Preciction")
    # Take User inputs
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('Fo(Hz)')
        RAP = st.text_input('RAP')
        APQ3 = st.text_input('APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('Fhi(Hz)')
        PPQ = st.text_input('PPQ')
        APQ5 = st.text_input('APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')
       
    with col3:
        flo = st.text_input('Flo(Hz)')
        DDP = st.text_input('DDP')
        APQ = st.text_input('APQ')
        DFA = st.text_input('DFA')
 
       
    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
        Shimmer = st.text_input('Shimmer')
        DDA = st.text_input('DDA')
        spread1 = st.text_input('spread1')
       
    with col5:
        Jitter_Abs = st.text_input('Jitter(Abs)')
        Shimmer_dB = st.text_input('Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')
    
    if st.button("Predict"):
        data = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        data_array = np.array(data, dtype=float).reshape(1,-1)
        prediction = parkinsons_model.predict(data_array)
        if prediction == 0:
            prediction_1 = "No Disease"
        else:
            prediction_1 = "Disease"
        st.write(f"## Prediction: {prediction_1}")