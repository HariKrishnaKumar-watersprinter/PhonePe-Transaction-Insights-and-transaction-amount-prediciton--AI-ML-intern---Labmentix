import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_map_trans

def trend_anay():
    st.header("Trend Analysis: Growth Over Time")
    st.markdown("Examining transaction trends to anticipate demand fluctuations.")
    df_trend=df_map_trans.groupby(['year','quarter']).agg({'transaction_amount': 'sum'}).reset_index()
    df_trend['prev_quarter_volume']=df_trend['transaction_amount'].shift(1)
    df_trend['growth_rate'] = (df_trend['transaction_amount'] - df_trend['prev_quarter_volume']) / df_trend['prev_quarter_volume'] * 100
    df_trend.fillna(0)
    fig=px.line(x=df_trend['year'].astype(str) + "-Q" + df_trend['quarter'].astype(str), 
                             y=df_trend['transaction_amount'],markers=True,
                             title='National Transaction Volume Trend',
                             labels={'x': 'Years and Quarter', 'y': 'Transaction Amount'},color_discrete_sequence=px.colors.qualitative.Safe)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
    st.plotly_chart(fig, width='stretch')
    df_trend['year_quarter'] = df_trend['year'].astype(str) + '-Q' + df_trend['quarter'].astype(str)
    df_trend=df_trend.sort_values(['growth_rate'], ascending=False).reset_index(drop=True)
    # Create the bar chart
    fig2 = px.bar(
    df_trend, 
    x='year_quarter', 
    y='growth_rate', 
    color='quarter',
    title="Quarterly Growth Rate (%)",
    color_discrete_sequence=px.colors.qualitative.Light24,
    category_orders={'year_quarter': sorted(df_trend['year_quarter'].unique())})

    # Update layout
    fig2.update_layout(
    xaxis=dict(tickmode='linear', dtick=1),
    width=1400,
    height=500,
    barmode='group',
    xaxis_title="Year-Quarter",
    yaxis_title="Growth Rate (%)")

    # Add text labels
    fig2.update_traces(
    texttemplate='%{y:.2f}%', 
    textposition='auto',
    textangle=270,textfont_size=30)
    st.plotly_chart(fig2, width='stretch')
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Top 5 growth rate (highest growth)')
        st.dataframe(df_trend[['year_quarter','growth_rate']].head(5))
    with col2:
        st.subheader('Least 5 growth rate(Lowest growth)')
        st.dataframe(df_trend[['year_quarter','growth_rate']].tail(5))

    