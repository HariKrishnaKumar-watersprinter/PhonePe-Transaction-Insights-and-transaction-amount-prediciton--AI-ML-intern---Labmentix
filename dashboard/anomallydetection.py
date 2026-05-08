from src.frauddetection import detect_fraud_anomalies
import pandas as pd 
import streamlit as st
import plotly.express as px
def fraud_det():
    st.header("Anomaly Detection in Transactions")
    st.markdown("**Goal:** Identify statistical outliers potentially indicating fraud or errors.")

    df_anom = detect_fraud_anomalies()
    anomalies = df_anom[df_anom['is_anomaly'] == 'Suspicious']
    
    col1,col2=st.columns(2)   
    col1.metric("Total Records Analyzed", len(df_anom))
    col2.metric("Anomalies Detected", len(anomalies), delta_color="inverse")

    
    fig = px.scatter(df_anom, x='total_users', y='total_tx_amount', color='is_anomaly',
                             title="Transaction Amount vs User Count (Outlier Detection)",
                             hover_data=['state', 'year', 'quarter'])
    fig.update_layout(xaxis=dict(title_text='Total Users'), yaxis=dict(title_text='Total Transaction Amount'),width=1400,
                               height=500)
    st.plotly_chart(fig, width='stretch')
    st.write("### Suspicious Records Details")
    st.dataframe(anomalies.sort_values('total_tx_amount', ascending=False).head(10).reset_index(drop=True))
        
    st.error("Note: 'Suspicious' records indicate statistical deviation from the norm (e.g., high transaction volume with unexpectedly low user base). These require audit.")

    
