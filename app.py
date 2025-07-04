
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from utils.preprocessor import preprocess_input

# Load model and scaler
model = joblib.load('models/LR_model.pkl')

scaler = joblib.load('models/scaler.pkl')

st.title("Supply Chain Emissions Prediction")

st.markdown("""
This app predicts **Supply Chain Emission Factors with Margins** based on DQ metrics and other parameters.
""")

# Input form
with st.form("prediction_form"):
    substance = st.selectbox("Substance", ['carbon dioxide', 'methane', 'nitrous oxide', 'other GHGs'])
    unit = st.selectbox("Unit", ['kg/2018 USD, purchaser price', 'kg CO2e/2018 USD, purchaser price'])
    source = st.selectbox("Source", ['Commodity', 'Industry'])
    supply_wo_margin = st.number_input("EmissionFactor_woMargin", min_value=0.0)
    margin = st.number_input("EmissionMargin", min_value=0.0)
    dq_reliability = st.slider("DQ Reliability", 0.0, 1.0)
    dq_temporal = st.slider("DQ Temporal Correlation", 0.0, 1.0)
    dq_geo = st.slider("DQ Geographical Correlation", 0.0, 1.0)
    dq_tech = st.slider("DQ Technological Correlation", 0.0, 1.0)
    dq_data = st.slider("DQ Data Collection", 0.0, 1.0)
    # year = st.selectbox("Year", list(range(2010, 2017)))

    submit = st.form_submit_button("Predict")

if submit:
    input_data = {
        'Substance': substance,
        'Unit': unit,
        'EmissionFactor_woMargin': supply_wo_margin,
        'EmissionMargin': margin,
        'Reliability': dq_reliability,
        'TemporalCorrelation': dq_temporal,
        'GeoCorrelation': dq_geo,
        'TechCorrelation': dq_tech,
        'DataCollection': dq_data,
        'Source': source,
        # 'Year': year
    }

    input_df = preprocess_input(pd.DataFrame([input_data]))
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Supply Chain Emission Factor with Margin: **{prediction[0]:.4f}**")