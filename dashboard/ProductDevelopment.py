import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_agg_user,df_agg_trans
    
def product_dep():   
    st.header("Product Development Insights")
    st.markdown("Data-driven recommendations for new features and services.")
    df_cat = df_agg_trans.groupby(['transaction_type']).agg({'transaction_count': 'sum'}).reset_index()
    df_cat = df_cat.sort_values(by='transaction_count', ascending=False)

    df_device=df_agg_user.groupby(['brand']).agg({'user_count': 'sum'}).reset_index()
    df_device=df_device.sort_values(by='user_count', ascending=False)
    top_cat = df_cat.loc[df_cat['transaction_count'].idxmax(), 'transaction_type']
    col1, col2 = st.columns(2)

    
    st.subheader("Feature Demand Analysis")
    st.write("Based on Transaction Categories:")
        
        # Simple Logic for Product recommendation
    top_cat = df_cat.loc[df_cat['transaction_count'].idxmax(), 'transaction_type']
    st.metric("Most Popular Category", top_cat)
        
    st.markdown("""
        **Proposed Features:**
        1. **Smart Recharge:** Since Recharge is high frequency, add "One-Click Recharge" widget.
        2. **Merchant Tools:** If Merchant Payments are high, develop "Digital Ledger" for shopkeepers.
        3. **Insurance EMI:** If Insurance is growing, offer "Pay Premium via UPI" installments.
        """)
        
    
    st.subheader("Device Optimization Strategy")
    st.write("Top 5 Device Brands:")
    st.dataframe(df_device.head(5).reset_index(drop=True))
        
    st.warning(f"Priority QA Testing: Focus app optimization on **{df_device.iloc[0]['brand']}** devices to ensure crash-free experience for the majority user base.")