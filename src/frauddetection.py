import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from src.mldata import ml_data
from ETLPipeline.config import engine    

def detect_fraud_anomalies():
    """
    Business Case: Fraud Detection
    Detects outliers in transaction amounts vs user counts (Potential synthetic transactions)
    """
    
    df=ml_data()
    # Features: We look for high amount but low user count (Suspicious)
    features = df[['total_tx_amount', 'total_users', 'avg_tx_value']]
    
    # Isolation Forest
    iso_forest = IsolationForest(contamination=0.05, random_state=42) # 5% anomaly rate
    df['anomaly_score'] = iso_forest.fit_predict(features)
    
    # -1 is anomaly, 1 is normal
    df['is_anomaly'] = df['anomaly_score'].apply(lambda x: 'Suspicious' if x == -1 else 'Normal')
    
    # Save results
    df.to_sql(
        'analysis_fraud_detection', con=engine, if_exists='replace', index=False
    )
    return df