import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_agg_ins,df_agg_user,df_agg_trans,df_map_ins,df_map_user,df_map_trans,df_top_ins,df_top_user,df_top_trans
from ETLPipeline.mergedata_load import master_state_data,master_district_data
from dashboard.TRANSACTIONDYNAMICS import trans_dy
from dashboard.DeviceDominance import device_dominance
from dashboard.InsurancePenetration import insurance_pen
from dashboard.MarketExpansion import mar_exp
from dashboard.UserHotspots import user_reg
from dashboard.PaymentPerformance import pay_cat
from dashboard.TrendAnalysis import trend_anay
from dashboard.competitiveBenchmarking import competitiveBenchmarking
from dashboard.ProductDevelopment import product_dep
from dashboard.corr_heat import corr_heat
from dashboard.anomallydetection import fraud_det
from src.growthprediciton import ml_pred

# ==============================================================================
# 3. SIDEBAR NAVIGATION
# ==============================================================================

st.set_page_config(layout="wide", page_title="PhonePe Strategic Insights", page_icon="💸📈")
st.sidebar.title("PhonePe Pulse Analysis")
st.sidebar.info("""
**Project Objective:**  
Analyze transaction dynamics, user engagement, and insurance potential to drive business strategy.
""")

options = ["🏠 Home & Executive Summary", #'📊 Transaction Dynamics', #'📱 Device Dominance', 
           #'💰 Insurance Penetration', '📈 Market Expansion', '💼 User Hotspots','🗺️ Payment Performance'
           #,"📈 Trend Analysis","🚨 Competitive Benchmarking","📈 Product Development",'📊 Correlation Heatmap',"🚨Fraud Detection (ML)",
           "📈 Growth Prediction"]
selection = st.sidebar.radio("Select Business Case:", options)


if selection == "🏠 Home & Executive Summary":
    st.title("📊 PhonePe Transaction Integrated Business & ML Analytics")
    st.write("""
    This dashboard presents findings from the PhonePe Pulse GitHub data analysis. 
    It focuses on 5 key business cases: Transaction Growth, Device Market Share, 
    Insurance Opportunities, Geographical Expansion, and User Registration patterns.
    """)
    st.markdown("### End-to-End Analysis: ETL -> SQL -> ML -> Strategy")
    # Key Metrics Row
    col1, col2, col3,col4,col5 = st.columns(5)
    
    # Fetching quick stats
    df_trans = df_agg_trans.agg({
        'transaction_amount':'sum',
        'transaction_count':'sum'
    })
    df_users = df_agg_user.agg({
        'user_count':'sum'
    })
    total_ins = master_state_data['agg_ins_amount'].sum()
    if not df_trans.empty and not df_users.empty:
        col1.metric("Total Transaction Value", f"₹{df_trans['transaction_amount']/1e12:.2f} Trillion")
        col2.metric("Total Transactions", f"{df_trans['transaction_count']/1e9:.2f} Billion")
        col3.metric("Total Registered Users", f"{df_users['user_count']/1e9:.2f} Billion")
        col4.metric("Total Insurance Amount", f"₹{total_ins/1e12:.2f} Trillion")
        col5.metric("States Analyzed", master_state_data['state'].nunique())
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8,tab9,tab10,tab11 = st.tabs([
           "📊 Transaction Dynamics",
           "📱 Device Dominance",
           "💰 Insurance Penetration",
           "📈 Market Expansion",
           "💼  User Hotspots",
           "📊 Payment Performance",
           "📈 Trend Analysis",
           "🚨 Competitive Benchmarking",
           '📊 Correlation Heatmap',
           "🚨Fraud Detection (ML)",
           "📈 Product Development"
           ])
    with tab1:
        trans_dy()
    with tab2:
        device_dominance()
    with tab3:
        insurance_pen()
    with tab4:
        mar_exp()
    with tab5:
        user_reg()
    with tab6:
        pay_cat()
    with tab7:
        trend_anay()
    with tab8:
        competitiveBenchmarking()
    with tab9:
        corr_heat()
    with tab10:
        fraud_det()
    with tab11:
        product_dep()
#elif selection == "📊 Transaction Dynamics":
    #trans_dy()
#elif selection == "📱 Device Dominance":
    #device_dominance()
#elif selection == "💰 Insurance Penetration":
    #insurance_pen()
#elif selection == "📈 Market Expansion":
    #mar_exp()
#elif selection == "💼 User Hotspots":
    #user_reg()
#elif selection == "🗺️ Payment Performance":
    #pay_cat()
#elif selection == "📈 Trend Analysis":
    #trend_anay()
#elif selection == "🚨 Competitive Benchmarking":
    #competitiveBenchmarking()
#elif selection == "📈 Product Development":
    #product_dep()
#elif selection == '📊 Correlation Heatmap':
    #corr_heat()
#elif selection == "🚨Fraud Detection (ML)":
    #fraud_det()
elif selection == "📈 Growth Prediction":
    ml_pred()