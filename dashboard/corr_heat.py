import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src.mldata import ml_data
from ETLPipeline.config import engine
def corr_heat():
    st.title('Correlation Heatmap')
    st.write('This heatmap shows the correlation between numeric features in the dataset.')
    ml_feature_matrix=ml_data()
    numeric_cols = ml_feature_matrix.select_dtypes(include=['number']).columns
    corr_matrix = ml_feature_matrix[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(9, 7))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # hide upper triangle
    sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True, fmt='.2f',
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    ax=ax)
    ax.set_title('Correlation Heatmap — Numeric Features', fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)