import pandas as pd
from ETLPipeline.config import engine

master_state_data=pd.read_sql_query("select * from master_state_data", engine)
master_district_data=pd.read_sql_query("select * from master_district_data", engine)