import streamlit as st
import pandas as pd
import numpy as np
import joblib
from ETLPipeline.mergedata_load import master_state_data
from sklearn.preprocessing import RobustScaler
import datetime
from src.data_spliting import data_split
from ETLPipeline.config import engine
def ml_pred():
    pipeline=data_split()
    st.subheader("Growth Predictor (ML Model)")
    st.write("Input current metrics to predict next quarter's transaction value:")
    pd.set_option('future.no_silent_downcasting', True)
    # Simple UI for Prediction
    state=st.selectbox("Select State",master_state_data["state"].unique())
    year=st.selectbox("Select Year",range(datetime.datetime.now().year, 2016, -1))
    quarter=st.selectbox("Select Quarter",["1","2","3","4"])
    total_tx_count = st.number_input("Current Transaction Count", value=1000000)
    total_tx_amt = st.number_input("Current Transaction Amount", value=500000)
    total_user_count = st.number_input("Current User Count", value=10000)
    total_app_opens=st.number_input("Total App Opens", value=100000)
    insurance_count=st.number_input("Insurance Count", value=10000)
    insurance_amount=st.number_input("Insurance Amount", value=10000)
    input_df=pd.DataFrame([{
        "state":state,
        "year":year,
        "quarter":quarter,
        "total_tx_count":total_tx_count,
        "total_tx_amount":total_tx_amt,
        "total_users":total_user_count,
        "total_app_opens":total_app_opens,
        "insurance_count":insurance_count,
        "insurance_amount":insurance_amount
    }])
    df=input_df.copy()   
    input_df['state']=input_df['state'].replace({'Andaman & Nicobar Islands':0, 'Andhra Pradesh':1, 'Arunachal Pradesh':2, 'Assam':3, 'Bihar':4, 'Chandigarh':5, 'Chhattisgarh':6, 'Dadra & Nagar Haveli & Daman & Diu':7, 'Delhi':8, 'Goa':9, 'Gujarat':10, 'Haryana':11, 'Himachal Pradesh':12, 'Jammu & Kashmir':13, 'Jharkhand':14, 'Karnataka':15, 'Kerala':16, 'Ladakh':17, 'Lakshadweep':18, 'Madhya Pradesh':19, 'Maharashtra':20, 'Manipur':21, 'Meghalaya':22, 'Mizoram':23, 'Nagaland':24, 'Odisha':25, 'Puducherry':26, 'Punjab':27, 'Rajasthan':28, 'Sikkim':29, 'Tamil Nadu':30, 'Telangana':31, 'Tripura':32, 'Uttar Pradesh':33, 'Uttarakhand':34, 'West Bengal':35})
    
    
    
    scaler_df=pipeline.transform(input_df)
    scaler_df=pd.DataFrame(scaler_df,columns=input_df.columns)
    if st.button("Predict Future Value"):
        try:
            model = joblib.load("models/xgboost.pkl")
            # Dummy year/quarter for prediction array
            prediction = model.predict(scaler_df)[0]
            st.success(f"Predicted Transaction Amount for Next Quarter: ₹{prediction/1e7:.2f} Crores")
            df["predicted_tx_amt"] = prediction
            st.dataframe(df)
            df.to_sql(name='future_predicted_value_table', con=engine, if_exists='append', index=False)
            st.success('Data saved to database')
        except:
            st.error("Model not found. Please run ml_pipeline.py first.")