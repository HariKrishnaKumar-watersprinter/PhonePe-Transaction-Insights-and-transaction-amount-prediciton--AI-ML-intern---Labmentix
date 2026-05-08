import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler,LabelEncoder
from src.mldata import ml_data
from sklearn.pipeline import Pipeline

def data_split():
    df=ml_data()
    le=LabelEncoder()
    df['state']=le.fit_transform(df['state'])
    df=df.drop(columns=['avg_tx_value','avg_app_opens_per_user','insurance_penetration_rate'])
    df1=df.copy()
    pipeline = Pipeline([
        ('scaler', RobustScaler())
    ])
    scaled_df=pipeline.fit_transform(df1.drop(columns=['future_tx_amount'],inplace=False))
    column_names=df.columns.drop('future_tx_amount')
    df=pd.DataFrame(scaled_df,columns=column_names)
    x=df
    y=df1['future_tx_amount']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return pipeline
    
