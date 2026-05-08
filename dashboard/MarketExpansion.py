import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_map_trans
def mar_exp():
    st.title("Transaction Analysis for Market Expansion")
    st.markdown("### Scenario: Identifying top districts for strategic decision making.")
    df_marketing = df_map_trans.groupby(['state']).agg({
    'transaction_amount': 'sum',
    'transaction_count': 'sum'
    }).reset_index()
    df_high_freq = df_marketing.sort_values('transaction_count', ascending=False).reset_index(drop=True)
    mar_exp=df_map_trans.groupby(['state','district']).agg({'transaction_count':'sum','transaction_amount':'sum'})
    filtered_df=mar_exp.sort_values(by='transaction_count',ascending=False).reset_index()
    st.subheader(" Districts by Transaction Value")
    selected_state = st.selectbox("Filter by State (Optional)", ['All'] + list(filtered_df['state'].unique()))
    
    if selected_state != 'All':
        filtered_df = filtered_df[filtered_df['state'] == selected_state]
    else:
        filtered_df = filtered_df
    fig = px.treemap(filtered_df, 
                         path=['state', 'district'], 
                         values='transaction_amount',
                         title='Transaction Value Distribution (State -> District)',
                         labels={'transaction_count': 'Transaction Count', 'state': 'State', 'district': 'District','transaction_amount': 'Transaction Value (₹)'},
                         color='transaction_count',hover_data=['transaction_count'],color_discrete_sequence=px.colors.qualitative.Light24)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
    st.plotly_chart(fig, width='stretch')
    st.write("**Top Performing Districts for respective state:**")
    st.dataframe(filtered_df)

    fig = px.bar(df_high_freq.head(10), 
             x='state', 
             y='transaction_count', 
             color='transaction_count',
             hover_data=['transaction_amount'],
             title="Top 10 States by Transaction Count",
             labels={'transaction_count': 'Transaction Count', 'state': 'State'},
             color_discrete_sequence=px.colors.qualitative.Light24)
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto', textangle=0,textfont_size=20)
    fig.update_layout(
    barmode='group', # This is now strictly enforced because every location has 2 bars
    xaxis=dict(tickmode='linear', dtick=1),
    width=1400, 
    height=600)
    st.plotly_chart(fig, width='stretch')
    col1,col2=st.columns(2)
    with col1:
        st.subheader('Top 5 Performing Districts')
        st.dataframe(filtered_df.head(5))

    with col2:
        st.subheader('Least 5 Performing Districts')
        st.dataframe(filtered_df.tail(5))

        
