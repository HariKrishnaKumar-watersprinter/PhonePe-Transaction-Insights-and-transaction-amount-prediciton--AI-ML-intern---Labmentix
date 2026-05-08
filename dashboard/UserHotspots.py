import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_map_user
from ETLPipeline.mergedata_load import master_state_data

def user_reg():
    st.title("User Registration Analysis")
    st.markdown("### Scenario: Identifying pincodes with most user registrations.")
    user_anay = master_state_data.groupby(['state','year']).agg({
    'agg_user_count': 'sum'})
    df=user_anay.sort_values(by='agg_user_count',ascending=False).reset_index()
    st.subheader("Year wise User Density")
    fig = px.bar(df, x='year', y='agg_user_count', 
                     color='state',labels={'agg_user_count': 'Registered Users', 'state': 'State', 'year': 'Year'},
                     color_discrete_sequence=px.colors.qualitative.Alphabet)
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='outside',textangle=0)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
    st.plotly_chart(fig, width='stretch')
    st.subheader('Highest User Base')
    st.dataframe(df[['state','agg_user_count']].head(1))
    col1,col2=st.columns(2)
    with col1:
        st.subheader('Top 5 Performing user States ')
        st.dataframe(df.head(5).reset_index(drop=True))
    with col2:
        st.subheader('Top 5 lower user States')
        st.dataframe(df.tail(5).reset_index(drop=True))
    st.info("**Insight:** These pincodes are high-density user zones. They are ideal locations for testing new product rollouts or physical merchant partnership programs.")
    
    user_eng=df_map_user.groupby(['state','district']).agg({'registered_users':'sum','app_opens':'sum'}).reset_index()
    user_eng=user_eng.sort_values(by='registered_users',ascending=False).reset_index()
    user_eng['location'] = user_eng['district'] + ', ' + user_eng['state']
    fig = px.bar(user_eng.head(10), x='location', y=['app_opens'], 
             title="Top 10 State and District wise app opens",color_discrete_sequence=px.colors.qualitative.Safe,labels={'app_opens': 'App Opens', 'registered_users': 'Registered Users', 'location': 'Location'})
    fig.update_layout(barmode='group', 
                  xaxis=dict(tickmode='linear', dtick=1), 
                  width=1400, 
                  height=600)
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textangle=0)
    st.plotly_chart(fig, width='stretch')
    col1,col2=st.columns(2)
    with col1:
        st.subheader('Top 5 District by user Engagement')
        st.dataframe(user_eng[['location','app_opens']].head(5).reset_index(drop=True))
    with col2:
        st.subheader('Top 5 lower District by user Engagement')
        st.dataframe(user_eng[['location','app_opens']].tail(5).reset_index(drop=True))
    st.success("**Insight:** These districts show high app engagement. They are ideal for launching new product features or targeted marketing campaigns.")