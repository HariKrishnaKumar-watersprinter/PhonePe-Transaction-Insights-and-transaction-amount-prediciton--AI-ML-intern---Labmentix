import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from ETLPipeline.data_loading import df_map_trans


def competitiveBenchmarking():
    st.header("Competitive Benchmarking (Internal)")
    st.markdown("Comparing State performance against National Average to identify leaders and laggards.") 
    state_volumes = df_map_trans.groupby(['state', 'year'])['transaction_amount'].sum().reset_index()
    state_volumes = state_volumes.rename(columns={'transaction_amount': 'total_state_volume'})

    # Calculate national volumes by year
    national_volumes = df_map_trans.groupby('year')['transaction_amount'].sum().reset_index()
    national_volumes = national_volumes.rename(columns={'transaction_amount': 'total_national_volume'})

    # Merge state and national volumes
    view_state_benchmark = pd.merge(state_volumes, national_volumes, on='year')

    # Calculate market share percentage
    view_state_benchmark['market_share_percent'] = (view_state_benchmark['total_state_volume'] / 
                                               view_state_benchmark['total_national_volume'].replace(0, np.nan)) * 100

    # Calculate the threshold for "Above Average" (1 divided by the number of states)
    state_count = df_map_trans['state'].nunique()
    threshold = 1.0 / state_count

    # Determine performance tier
    view_state_benchmark['performance_tier'] = np.where(
    (view_state_benchmark['total_state_volume'] / view_state_benchmark['total_national_volume'].replace(0, np.nan)) > threshold,
    'Above Average',
    'Below Average')
    df_year=view_state_benchmark.sort_values(by='market_share_percent', ascending=False).reset_index(drop=True)
    fig = px.scatter(df_year, x='market_share_percent', y='total_state_volume', color='performance_tier',
                     hover_name='state', size='total_state_volume',
                     title=f"State Performance Quadrant",
                     labels={'market_share_percent': 'Market Share (%)', 'total_state_volume': 'State Volume'},
                     log_y=True)
    fig.add_vline(x=df_year['market_share_percent'].mean(), line_dash="dash", line_color="gray", annotation_text="Avg Share")
    fig.update_layout(
        xaxis=dict(tickmode='linear', dtick=1),
        width=1400,
        height=500,
        barmode='group',
        xaxis_title="Market Share (%)",
        yaxis_title="Transaction Amount")
    st.plotly_chart(fig, width='stretch')
    st.markdown("""
    **Quadrant Interpretation:**
    - **Top Right (Leaders):** High Market Share, High Volume. (Maintain dominance).
    - **Bottom Left (Niche):** Low Share, Low Volume. (Requires growth strategy).
    """)
    st.subheader("State Benchmark View:")
    selected_state = st.selectbox('Performance Tier', df_year['performance_tier'].unique())
    st.dataframe(df_year[df_year['performance_tier']==selected_state])