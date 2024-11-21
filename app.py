import streamlit as st
from src.data_processing import load_and_process_data
from src.model import train_model, predict_species
from src.features import encode_input_features

st.title('🤖 Machine Learning App')

df = load_and_process_data()
st.write(df)

input_features = st.sidebar.text_input('Enter penguin features')
encoded_input = encode_input_features(input_features)

clf = train_model(df)

prediction, prediction_proba = predict_species(clf, encoded_input)

st.subheader('Predicted Species')

st.write(f"Predicted species: {prediction[0]}")
st.write(f"Prediction probabilities: {prediction_proba}")
