import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_map_ins


def insurance_pen():

    st.title("Insurance Penetration & Growth Potential")
    st.markdown("### Scenario: Identifying untapped opportunities for insurance adoption.")
    ins_pen=df_map_ins.groupby(['state','district']).agg({'insurance_count':'sum','insurance_amount':'sum'})
    df=ins_pen.sort_values(by='insurance_amount',ascending=False).reset_index()
    st.subheader("Insurance Value by State")
    fig = px.bar(df.head(10), x='state', y='insurance_amount',color='district',
                             title="Top 10 States by Insurance Amount",
                             labels={'insurance_amount': 'Insurance Amount (₹)', 'state': 'State'},color_discrete_sequence=px.colors.qualitative.G10)
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='outside',textangle=0)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1),width=1400,height=500)
    st.plotly_chart(fig,width='stretch')

    st.metric("Highest Insurance Value", f"{df['state'].iloc[0]}")
    st.metric("Total Policies:", f"{df['insurance_count'].iloc[0]:,}")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Potential Markets (Top 5 by Value):")
        st.dataframe(df.head(5)[['state', 'insurance_count']])
    with col2:
            # Identify potential markets (High transaction but lower insurance? - requires complex join, simplified here)
            st.write("Potential Markets (Bottom 5 by Value):")
            st.dataframe(df.tail(5)[['state', 'insurance_count']].reset_index(drop=True))
    st.success("**Recommendation:** Focus marketing efforts on the top 5 states for revenue, and the bottom 5 states for awareness campaigns to drive adoption.")
