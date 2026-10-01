import streamlit as st
import pandas as pd
import joblib

# Load trained model and feature columns
model = joblib.load('housing_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("Sydney Housing Price Prediction")

st.write(
    "Enter the property details below to estimate its sale price."
)

# User inputs
suburb = st.selectbox(
    "Suburb",
    ["Parramatta", "Blacktown", "Campbelltown"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "House", "Semi-detached"]
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

car_space = st.number_input(
    "Car Spaces",
    min_value=0,
    max_value=10,
    value=1
)

land_size = st.number_input(
    "Land Size (m²)",
    min_value=0.0,
    value=300.0
)

total_rooms = bedrooms + bathrooms

# Create input dataframe
input_data = pd.DataFrame({
    'Bedrooms': [bedrooms],
    'Bathrooms': [bathrooms],
    'CarSpace': [car_space],
    'LandSize': [land_size],
    'TotalRooms': [total_rooms],
    'Suburb': [suburb],
    'PropertyType': [property_type]
})

# Convert categorical variables into dummy variables
input_data = pd.get_dummies(
    input_data,
    columns=['Suburb', 'PropertyType']
)

# Make columns match the model training data
input_data = input_data.reindex(
    columns=model_columns,
    fill_value=0
)

if st.button("Predict Sale Price"):

    prediction = model.predict(input_data)[0]

    st.subheader("Estimated Sale Price")

    st.success(f"${prediction:,.0f}")