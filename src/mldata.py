import streamlit as st
import pandas as pd 
import numpy as np 
import sqlalchemy as sa
from ETLPipeline.config import engine
from ETLPipeline.data_loading import df_map_user,df_map_trans,df_map_ins,df_agg_ins
from src.Data_wrangling import wrangle_table

def ml_data():
    # Group transaction data by state, year, and quarter
    trans_grouped = df_map_trans.groupby(['state', 'year', 'quarter']).agg({
        'transaction_count': 'sum',
        'transaction_amount': 'sum'
    }).reset_index()

    # Group user data by state, year, and quarter
    user_grouped = df_map_user.groupby(['state', 'year', 'quarter']).agg({
        'registered_users': 'sum','app_opens': 'sum'
    }).reset_index()

    # Group insurance data by state, year, and quarter
    ins_grouped = df_map_ins.groupby(['state', 'year', 'quarter']).agg({
        'insurance_count': 'sum','insurance_amount': 'sum'
    }).reset_index()

    # Merge the grouped dataframes
    ml_feature_matrix = pd.merge(trans_grouped, user_grouped, on=['state', 'year', 'quarter'])
    ml_feature_matrix = pd.merge(ml_feature_matrix, ins_grouped, on=['state', 'year', 'quarter'])

    # Rename columns to match the SQL query
    ml_feature_matrix = ml_feature_matrix.rename(columns={
        'transaction_count': 'total_tx_count',
        'transaction_amount': 'total_tx_amount',
        'registered_users': 'total_users',
        'app_opens': 'total_app_opens',
        'insurance_count': 'insurance_count',
        'insurance_amount': 'insurance_amount'
    })

    # Calculate derived features
    ml_feature_matrix['avg_tx_value'] = ml_feature_matrix['total_tx_amount'] / ml_feature_matrix['total_tx_count'].replace(0, np.nan)
    ml_feature_matrix['avg_app_opens_per_user'] = ml_feature_matrix['total_app_opens'] / ml_feature_matrix['total_users'].replace(0, np.nan)
    ml_feature_matrix['insurance_penetration_rate'] = ml_feature_matrix['insurance_count'] / ml_feature_matrix['total_users'].replace(0, np.nan)

    # Sort by state, year, and quarter to prepare for the lead calculation
    ml_feature_matrix = ml_feature_matrix.sort_values(['state', 'year', 'quarter'])

    # Calculate future transaction amount (equivalent to LEAD window function)
    ml_feature_matrix['future_tx_amount'] = ml_feature_matrix.groupby('state')['total_tx_amount'].shift(-1)

    # Manually drop both View and Table to prevent 1471 (Not Insertable) and 1051 (Unknown Table) errors
    #with engine.connect() as conn:
        #conn.execute(sa.text("DROP VIEW IF EXISTS ml_feature_matrix"))
        #conn.execute(sa.text("DROP TABLE IF EXISTS ml_feature_matrix"))
        #conn.commit()

    # Save to sql database
    ml_feature_matrix.to_sql(name='ml_feature_matrix', con=engine, if_exists='replace', index=False)
    
    # Clean the table using the utility function (passing the table name string)
    wrangle_table('ml_feature_matrix')
    
    return ml_feature_matrix
