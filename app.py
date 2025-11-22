import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

# Inputs
MedInc = st.number_input("Median Income", 0.0)
HouseAge = st.number_input("House Age", 0.0)
AveRooms = st.number_input("Average Rooms", 0.0)
AveBedrms = st.number_input("Average Bedrooms", 0.0)
Population = st.number_input("Population", 0.0)
AveOccup = st.number_input("Average Occupancy", 0.0)
Latitude = st.number_input("Latitude", 0.0)
Longitude = st.number_input("Longitude", 0.0)

if st.button("Predict"):
    data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    result = model.predict(data)[0]
    st.write(f"🏡 Predicted House Price: ${result:.2f} (in 100k)")
