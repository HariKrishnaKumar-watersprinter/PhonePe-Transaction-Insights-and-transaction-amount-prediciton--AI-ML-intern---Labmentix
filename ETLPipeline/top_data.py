import os
import pandas as pd
from ETLPipeline.config import DATA_ROOT
import json
from datetime import datetime

# --- 3. TOP DATA ---
def extract_top_transaction():
    print("Processing Top Transactions...")
    path = os.path.join(DATA_ROOT, "top", "transaction", "country", "india", "state")
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
                    
                    # Process Districts
                    districts = content.get('data', {}).get('districts', [])
                    for d in districts:
                        metric = d.get('metric', [{}]) if d.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'entity_type': 'district',
                            'entity_name': d.get('entityName'),
                            'transaction_count': metric.get('count', 0),
                            'transaction_amount': int(metric.get('amount', 0))
                        })
                        
                    # Process Pincodes
                    pincodes = content.get('data', {}).get('pincodes', [])
                    for p in pincodes:
                        metric = p.get('metric', [{}]) if p.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'entity_type': 'pincode',
                            'entity_name': p.get('entityName'),
                            'transaction_count': metric.get('count', 0),
                            'transaction_amount': int(metric.get('amount', 0))
                        })
                except Exception as e:
                    print(f"Error {file_path}: {e}")
    return pd.DataFrame(data_rows)

def extract_top_user():
    print("Processing Top Users...")
    path = os.path.join(DATA_ROOT, "top", "user", "country", "india", "state")
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
                    
                    districts = content.get('data', {}).get('districts', [])
                    for d in districts:
                        metric = d.get('metric', [{}])[0] if d.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'entity_type': 'district',
                            'entity_name': d.get('name'),
                            'registered_users': metric.get('count', 0)
                        })
                        
                    pincodes = content.get('data', {}).get('pincodes', [])
                    for p in pincodes:
                        metric = p.get('metric', [{}])[0] if p.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'entity_type': 'pincode',
                            'entity_name': p.get('name'),
                            'registered_users': metric.get('count', 0)
                        })
                except Exception as e:
                    print(f"Error {file_path}: {e}")
    return pd.DataFrame(data_rows)

def extract_top_insurance():
    print("Processing Top Insurance...")
    # Path: data/top/insurance/country/india/state
    path = os.path.join(DATA_ROOT, "top", "insurance", "country", "india", "state")
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
                    
                    districts = content.get('data', {}).get('districts', [])
                    for d in districts:
                        metric = d.get('metric', [{}]) if d.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'entity_type': 'district',
                            'entity_name': d.get('entityName'),
                            'insurance_count': metric.get('count', 0),
                            'insurance_amount': int(metric.get('amount', 0))
                        })
                        
                    pincodes = content.get('data', {}).get('pincodes', [])
                    for p in pincodes:
                        metric = p.get('metric', [{}]) if p.get('metric') else {}
                        data_rows.append({
                            'state': state.replace('-', ' ').title(),
                            'year': int(year),
                            'quarter': int(quarter),
                            'entity_type': 'pincode',
                            'entity_name': p.get('entityName'),
                            'insurance_count': metric.get('count', 0),
                            'insurance_amount': int(metric.get('amount', 0))
                        })
                except Exception as e:
                    print(f"Error {file_path}: {e}")
    return pd.DataFrame(data_rows)