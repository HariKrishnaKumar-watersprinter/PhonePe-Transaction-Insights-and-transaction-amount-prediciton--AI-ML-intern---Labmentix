import pandas as pd
from ETLPipeline.config import engine

#loading data from database
df_agg_trans = pd.read_sql("SELECT * FROM agg_transactions", engine)
df_agg_user = pd.read_sql("SELECT * FROM agg_users", engine)
df_agg_ins = pd.read_sql("SELECT * FROM agg_insurance", engine)

# Load Map Data
df_map_trans = pd.read_sql("SELECT * FROM map_transactions", engine)
df_map_user = pd.read_sql("SELECT * FROM map_users", engine)
df_map_ins = pd.read_sql("SELECT * FROM map_insurance", engine)

# Load Top Data
df_top_trans = pd.read_sql("SELECT * FROM top_transactions", engine)
df_top_user = pd.read_sql("SELECT * FROM top_users", engine)
df_top_ins = pd.read_sql("SELECT * FROM top_insurance", engine)

# loading merging data from database
#master_state_data=pd.read_sql_query("select * from master_state_data", engine)
#master_district_data=pd.read_sql_query("select * from master_district_data", engine)
print('data loaded successfully')