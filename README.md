# Sydney Housing Price Prediction

This project was developed for SIT307 and uses machine learning
to predict residential property sale prices in Sydney.

## Project Files

- `Sit307_8.1D.ipynb` - Jupyter Notebook containing data collection,
  preprocessing, feature engineering, model development and evaluation.

- `housing_data.csv` - Collected housing dataset used for the project.

- `app.py` - Source code for the deployed Streamlit web application.

- `housing_model.pkl` - Saved trained machine learning model used by
  the Streamlit application.

- `model_columns.pkl` - Stores the feature columns expected by the
  trained model.

- `requirements.txt` - Contains the Python packages required to run
  and deploy the Streamlit application.

## Web Application

The Streamlit application allows users to enter property information,
including suburb, property type, bedrooms, bathrooms, car spaces and
land size. The trained machine learning model then returns an estimated
sale price.

## Running the Application

Install the required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py