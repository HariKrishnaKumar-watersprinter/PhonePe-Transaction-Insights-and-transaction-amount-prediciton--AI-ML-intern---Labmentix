import pandas as pd
import numpy as np
from ETLPipeline.config import engine


engine=engine
# Write your code to make your dataset analysis ready.
def wrangle_table(table_name):
    print(f"Wrangling dataset: {table_name}...")
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        original_shape = df.shape

# 1. Handling Missing Values
# Fill numeric NaN with 0 (assuming missing transactions means 0 activity)
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        df[numeric_cols] = df[numeric_cols].fillna(0)
 
# Fill object NaN with 'Unknown'
        obj_cols = df.select_dtypes(include=['object']).columns
        df[obj_cols] = df[obj_cols].fillna('Unknown')

# 2. Data Type Correction Ensure Year and Quarter are integers
        if 'year' in df.columns:
            df['year'] = df['year'].astype(int)
        if 'quarter' in df.columns:
            df['quarter'] = df['quarter'].astype(int)

# 3. String Standardization (Title Case for States/Districts)
        if 'state' in df.columns:
            df['state'] =df['state'].str.title().str.strip()
        if 'district' in df.columns:
            df['district'] = df['district'].str.title().str.strip()
# Fix specific known issues (e.g.,"District" suffix)

            df['district'] = df['district'].str.replace('District', '')

# 4. Deduplication
        df = df.drop_duplicates()

# Save back to SQL (Overwrite)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f" -> Cleaned {table_name}. Rows: {original_shape[0]} -> {df.shape[0]}")

    except Exception as e:
        print(f"Error wrangling {table_name}: {e}")