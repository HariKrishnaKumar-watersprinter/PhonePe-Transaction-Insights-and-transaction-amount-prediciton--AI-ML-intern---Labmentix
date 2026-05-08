import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_map_trans
from ETLPipeline.config import engine
from ETLPipeline.mergedata_load import master_state_data
def trans_dy():
    st.title("Decoding Transaction Dynamics")
    st.markdown("### Scenario: Identifying growth and stagnation across states.")
    trans_dy=master_state_data.groupby(['state','year']).agg({'agg_trans_amount':'sum','agg_trans_count':'sum'}).reset_index()
    trans_dy['prev_year_amount']=trans_dy['agg_trans_amount'].shift(1)
    trans_dy['growth_rate'] = ((trans_dy['agg_trans_amount'] - trans_dy['prev_year_amount']) / trans_dy['prev_year_amount']) * 100
    trans_dy=trans_dy.sort_values(by=['agg_trans_amount'],ascending=False).reset_index(drop=True)
    trans_dy.fillna(0)
    if not trans_dy.empty:
        #col1,col2=st.columns(2)
        #with col1:
            st.subheader("State-wise Transaction Amount Trend")
            fig = px.bar(trans_dy, x='year', y='agg_trans_amount', color='state',
                         title="Transaction Amount by Year (Top States)",
                         labels={'year': 'Year','agg_trans_amount': 'Transaction Amount (₹)', 'state': 'State'},
                         barmode="relative",color_discrete_sequence=px.colors.qualitative.Alphabet)
            fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
            fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textfont_size=40)
            st.plotly_chart(fig, width='stretch')

        #with col2:
            st.subheader("Growth Insights")
            # Identify Top Growing States
            df=trans_dy
            top_growth = df[df['year'] == df['year'].max()].nlargest(5, 'growth_rate')
            st.write("Top 5 Fastest Growing States (Latest Year):")
            st.dataframe(top_growth[['state', 'growth_rate']].reset_index(drop=True).style.format({'growth_rate': '{:.2f}%'}))
                    
            st.write("States with Declining Growth:")
            decline = df[(df['growth_rate'] < 0) & (df['year'] == df['year'].max())]
            if not decline.empty:
                st.warning(f"Found {len(decline)} states with negative growth.")
            else:
                st.success("All states showed positive growth in the latest year.")
                
        # Recommendation
            st.info("**Insight:** States with high growth rates are prime markets for new feature launches, while stagnant states require targeted re-engagement campaigns.")
        
    st.header("Transaction Analysis Across States and Districts")
    st.markdown("**Goal:** Identify top performing regions for expansion.")
    trans_s_d=df_map_trans.groupby(['state','district']).agg({'transaction_count':'sum','transaction_amount':'sum'})
    df_state=trans_s_d.sort_values(by='transaction_amount',ascending=False).reset_index()
    df_state['location']=df_state['state']+' '+df_state['district']
    fig = px.bar(df_state.head(15), x='location', y=['transaction_amount'], title="Top 15 States by Transaction Value",
                 labels={'transaction_amount': 'Transaction Value (₹)', 'transaction_count': 'Transaction Count', 'state': 'State'},color_discrete_sequence=px.colors.qualitative.Pastel1)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textfont_size=40)
    st.plotly_chart(fig, width='stretch')

    # Top Districts Drill Down
    state_select = st.selectbox("Select State for District Analysis", df_state['state'].unique())
    query = f"""
        SELECT district, SUM(transaction_amount) as amt 
        FROM map_transactions 
        WHERE state = '{state_select}' 
        GROUP BY district 
        ORDER BY amt DESC LIMIT 10
    """
    df_dist = pd.read_sql(query, engine)
    
    fig2 = px.pie(df_dist, names='district', values='amt', title=f"Top Districts in {state_select}",color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
    st.plotly_chart(fig2, width='stretch')