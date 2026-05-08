import pandas as pd
from data_loading import df_agg_trans,df_agg_user,df_agg_ins,df_map_trans,df_map_user,df_map_ins,df_top_trans,df_top_user,df_top_ins  

# 2. PRE-PROCESSING & AGGREGATION
# --- PREPARE STATE-LEVEL DATA ---
# 1. Aggregated Transactions (Sum of all types per State/Year/Quarter)
state_trans = df_agg_trans.groupby(['state', 'year', 'quarter']).agg({
    'transaction_count': 'sum',
    'transaction_amount': 'sum'
}).reset_index().rename(columns={
    'transaction_count': 'agg_trans_count',
    'transaction_amount': 'agg_trans_amount'
})

# 2. Aggregated Users (Sum of all brands per State/Year/Quarter)
state_users = df_agg_user.groupby(['state', 'year', 'quarter']).agg({
    'user_count': 'sum',
    'user_percentage': 'sum' # Note: Sum of percentages might exceed 100 depending on data, usually we take mean or sum of counts
}).reset_index().rename(columns={
    'user_count': 'agg_user_count'
})

# 3. Aggregated Insurance (Sum per State/Year/Quarter)
state_ins = df_agg_ins.groupby(['state', 'year', 'quarter']).agg({
    'insurance_count': 'sum',
    'insurance_amount': 'sum'
}).reset_index().rename(columns={
    'insurance_count': 'agg_ins_count',
    'insurance_amount': 'agg_ins_amount'
})

# 4. Top Transactions (We take ONLY the top entity per state/period or aggregate. 
#    Here we aggregate the 'top' table to get state-level summary of top performers)
top_trans_state = df_top_trans.groupby(['state', 'year', 'quarter']).agg({
    'transaction_count': 'sum',
    'transaction_amount': 'sum'
}).reset_index().rename(columns={
    'transaction_count': 'top_trans_count',
    'transaction_amount': 'top_trans_amount'
})

# 5. Top Users (Aggregate top users)
top_user_state = df_top_user.groupby(['state', 'year', 'quarter']).agg({
    'registered_users': 'sum'
}).reset_index().rename(columns={
    'registered_users': 'top_user_count'
})

# 6. Top Insurance (Aggregate)
top_ins_state = df_top_ins.groupby(['state', 'year', 'quarter']).agg({
    'insurance_count': 'sum',
    'insurance_amount': 'sum'
}).reset_index().rename(columns={
    'insurance_count': 'top_ins_count',
    'insurance_amount': 'top_ins_amount'
})


# --- PREPARE DISTRICT-LEVEL DATA ---

# 1. Map Transactions (Already at district level)
dist_trans = df_map_trans.groupby(['state', 'year', 'quarter', 'district']).agg({
    'transaction_count': 'sum',
    'transaction_amount': 'sum'
}).reset_index().rename(columns={
    'transaction_count': 'map_trans_count',
    'transaction_amount': 'map_trans_amount'
})

# 2. Map Users
dist_users = df_map_user.groupby(['state', 'year', 'quarter', 'district']).agg({
    'registered_users': 'sum',
    'app_opens': 'sum'
}).reset_index().rename(columns={
    'registered_users': 'map_reg_users',
    'app_opens': 'map_app_opens'
})

# 3. Map Insurance
dist_ins = df_map_ins.groupby(['state', 'year', 'quarter', 'district']).agg({
    'insurance_count': 'sum',
    'insurance_amount': 'sum'
}).reset_index().rename(columns={
    'insurance_count': 'map_ins_count',
    'insurance_amount': 'map_ins_amount'
})
# ==============================================================================
# 3. MERGING DATA
# ==============================================================================
print("Merging tables...")
# --- MERGE STATE-LEVEL DATA ---
dfs_state = [state_trans, state_users, state_ins, top_trans_state, top_user_state, top_ins_state]

# Merge all dataframes sequentially on ['state', 'year', 'quarter']
from functools import reduce
df_state_final = reduce(lambda left, right: pd.merge(left, right, on=['state', 'year', 'quarter'], how='outer'), dfs_state)

# Fill NaN values with 0 (if any data was missing for a specific quarter)
df_state_final = df_state_final.fillna(0)


# --- MERGE DISTRICT-LEVEL DATA ---
dfs_district = [dist_trans, dist_users, dist_ins]

# Merge all dataframes sequentially on ['state', 'year', 'quarter', 'district']
df_district_final = reduce(lambda left, right: pd.merge(left, right, on=['state', 'year', 'quarter', 'district'], how='outer'), dfs_district)

# Fill NaN values with 0
df_district_final = df_district_final.fillna(0)
print('Table merged')