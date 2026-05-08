import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_agg_trans


def pay_cat():
    st.header("Payment Performance & Category Analysis")
    st.markdown("Evaluating the popularity and efficiency of different payment categories.")
    pyment_per=df_agg_trans.groupby(['transaction_type']).agg({'transaction_count': 'sum','transaction_amount':'sum'}).reset_index()
    pyment_per['avg_ticket_size']=(pyment_per['transaction_amount'])/pyment_per['transaction_count']
    df_perf=pyment_per.sort_values(by=['transaction_amount'],ascending=False).reset_index(drop=True)
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Payment Category Performance: Transaction amount")
        fig = px.bar(df_perf, x='transaction_type', y='transaction_amount',
                 labels={'transaction_type': 'Category', 'transaction_amount': 'Transaction amount', 'year': 'Year'},color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
        fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textangle=0)
        st.plotly_chart(fig, width='stretch')
    with col2:
        st.subheader("Category Distribution")
        df_pie = df_perf.groupby('transaction_type')['transaction_amount'].sum().reset_index()
        fig_pie = px.pie(df_pie, names='transaction_type', values='transaction_amount', hole=0.4,color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
        st.plotly_chart(fig_pie, width='stretch')
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Category Distribution Table (Transaction amount)")
        st.dataframe(df_perf[['transaction_type','transaction_amount']])
    with col2:
        st.subheader("Category Performance Table (Transaction count)")
        st.dataframe(df_perf[['transaction_type','transaction_count']])

