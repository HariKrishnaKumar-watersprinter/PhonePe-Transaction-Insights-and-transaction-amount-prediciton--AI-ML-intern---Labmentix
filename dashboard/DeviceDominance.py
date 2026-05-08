import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_agg_user,df_agg_trans

def device_dominance():
    st.title("Device Dominance & User Engagement")
    st.markdown("### Scenario: Enhancing app performance based on device brands.")
    st.subheader("Market Share by Brand")
    user_dy=df_agg_user.groupby(['brand']).agg({'user_count': 'sum'}).reset_index()
    user_dy['market_share_percentage']=((user_dy['user_count'])/sum(user_dy['user_count'])*100).round(2)
    df=user_dy.sort_values(by='market_share_percentage',ascending=False).reset_index()
    col1,col2=st.columns(2)
    with col2:
        fig = px.pie(df, values='user_count', names='brand', 
                         title='User Distribution by Device Brand',
                         hole=0.4)

        fig.update_traces(textposition='inside', textinfo='percent+label',textfont_size=20)
        fig.update_layout(
        barmode='group', # This is now strictly enforced because every location has 2 bars
        xaxis=dict(tickmode='linear', dtick=1),
        width=1400, 
        height=500)
        st.plotly_chart(fig, width='stretch')

    with col1:
        fig_bar = px.bar(df.head(10), x='brand', y='user_count',
                             title="Top 10 Device Brands by User Count",
                             labels={'user_count': 'User Count', 'brand': 'Brand'},color_discrete_sequence=px.colors.qualitative.Alphabet)
        fig_bar.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textangle=270,textfont_size=20)
        fig_bar.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1500,height=500)
        st.plotly_chart(fig_bar, width='stretch')   
    col1, col2 = st.columns(2)
    with col1:
            st.subheader('Top 3 device brands by market share')
            st.dataframe(df[['brand','market_share_percentage']].head(3))

    with col2:
        st.subheader('Least 3 device brands by market share')
        st.dataframe(df[['brand','market_share_percentage']].tail(3))
    
    