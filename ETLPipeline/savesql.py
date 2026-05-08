from agg_data import extract_aggregated_transaction, extract_aggregated_user, extract_aggregated_insurance
from map_data import extract_map_transaction, extract_map_user, extract_map_insurance
from top_data import extract_top_transaction, extract_top_user, extract_top_insurance

from ETLPipeline.config import engine
import pandas as pd

# LOADING FUNCTION TO DATABASE
def load_to_database(df, table_name):
    if df.empty:
        print(f"Skipping {table_name}: No data extracted.")
        return

    print(f"Loading {len(df)} rows into table '{table_name}'...")
    df = df.where(pd.notnull(df), None)
    
    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',
            index=False,
          
        )
        print(f"Successfully loaded {table_name}.")
    except Exception as e:
        print(f"Error loading {table_name}: {e}")
load_to_database(extract_aggregated_transaction(), "agg_transactions")
load_to_database(extract_aggregated_user(), "agg_users")
load_to_database(extract_aggregated_insurance(), "agg_insurance")
    
    # 2. Map
load_to_database(extract_map_transaction(), "map_transactions")
load_to_database(extract_map_user(), "map_users")
load_to_database(extract_map_insurance(), "map_insurance")
    
    # 3. Top
load_to_database(extract_top_transaction(), "top_transactions")
load_to_database(extract_top_user(), "top_users")
load_to_database(extract_top_insurance(), "top_insurance")
# MAIN EXECUTION
from merging_data import df_state_final,df_district_final
def merge_sql():
    # Save State Master Table
    df_state_final.to_sql(
    name="master_state_data", 
    con=engine, 
    if_exists='replace', 
    index=False)
    print(" -> 'master_state_data' table created successfully.")

# Save District Master Table
    df_district_final.to_sql(
    name="master_district_data", 
    con=engine, 
    if_exists='replace', 
    index=False)
    print(" -> 'master_district_data' table created successfully.")

    print("All tables merged and saved.")
   
   
merge_sql()
print("ETL Process Completed Successfully.")
# 4. SAVING MASTER TABLES TO SQL
print("Saving Master Tables to SQL...")

   
