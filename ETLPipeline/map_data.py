import os
import pandas as pd
from ETLPipeline.config import DATA_ROOT
import json
from datetime import datetime
# --- 2. MAP DATA ---
def extract_map_transaction():
    print("Processing Map Transactions...")
    path = os.path.join(DATA_ROOT, "map", "transaction", "hover", "country", "india", "state")
    data_rows = []
    if not os.path.exists(path): return pd.DataFrame()

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if not os.path.isdir(state_path): continue
        
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            if not os.path.isdir(year_path): continue
            
            for quarter_file in os.listdir(year_path):
                if not quarter_file.endswith('.json'): continue
                quarter = quarter_file.split('.')[0]
                file_path = os.path.join(year_path, quarter_file)
                
                try:
                    with open(file_path, 'r') as f:
                        content = json.load(f)
                    hover_data = content.get('data', {}).get('hoverDataList', [])
                    
                    for item in hover_data:
                        district = item.get('name')
                        metric = item.get('metric', [{}])[0] if item.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'district': district,
                            'transaction_count': metric.get('count', 0),
                            'transaction_amount': int(metric.get('amount', 0))
                        })
                except Exception as e:
                    print(f"Error {file_path}: {e}")
    return pd.DataFrame(data_rows)

def extract_map_user():
    print("Processing Map Users...")
    path = os.path.join(DATA_ROOT, "map", "user", "hover", "country", "india", "state")
    data_rows = []
    if not os.path.exists(path): return pd.DataFrame()

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if not os.path.isdir(state_path): continue
        
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            if not os.path.isdir(year_path): continue
            
            for quarter_file in os.listdir(year_path):
                if not quarter_file.endswith('.json'): continue
                quarter = quarter_file.split('.')[0]
                file_path = os.path.join(year_path, quarter_file)
                
                try:
                    with open(file_path, 'r') as f:
                        content = json.load(f)
                    hover_data = content.get('data', {}).get('hoverData', {})
                    
                    # hover_data is a dictionary where keys are district names and values are the metrics
                    for district, metric in hover_data.items():
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'district': district,
                            'registered_users': metric.get('registeredUsers', 0),
                            'app_opens': metric.get('appOpens', 0)
                        })
                except Exception as e:
                    print(f"Error {file_path}: {e}")
    return pd.DataFrame(data_rows)

def extract_map_insurance():
    print("Processing Map Insurance...")
    # Path: data/map/insurance/hover/country/india/state
    path = os.path.join(DATA_ROOT, "map", "insurance", "hover", "country", "india", "state")
    data_rows = []
    if not os.path.exists(path): return pd.DataFrame()

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if not os.path.isdir(state_path): continue
        
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            if not os.path.isdir(year_path): continue
            
            for quarter_file in os.listdir(year_path):
                if not quarter_file.endswith('.json'): continue
                quarter = quarter_file.split('.')[0]
                file_path = os.path.join(year_path, quarter_file)
                
                try:
                    with open(file_path, 'r') as f:
                        content = json.load(f)
                    hover_data = content.get('data', {}).get('hoverDataList', [])
                    
                    for item in hover_data:
                        district = item.get('name')
                        metric = item.get('metric', [{}])[0] if item.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'district': district,
                            'insurance_count': metric.get('count', 0),
                            'insurance_amount': int(metric.get('amount', 0))
                        })
                except Exception as e:
                    print(f"Error {file_path}: {e}")
    return pd.DataFrame(data_rows)