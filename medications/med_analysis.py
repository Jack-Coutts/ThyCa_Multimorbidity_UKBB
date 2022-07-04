from med_functions import *

# Read in disease data
data = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt', 0)

# Read in medication data
mdata = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/full_med_20003_phec_nona_over20.txt', 0)

# Create a list of all userIds for which there is medication data
med_ids = mdata.index.tolist()

# Retain disease data participants only if there is mediction data
data = data.loc[data['userId'].isin(med_ids)]

# Add thyroxine medication column to disease dataframe
add_col(data, 'thyroxine medication', mdata, 'm1140874852', 'm1140884516', 'm1140910814', 'm1141191044')

# Split the disease data into smaller dataframes
small_dfs = split_df(data, 'thyroxine medication', 40)

# Run association rule mining
results = multi_df_ARM(0.0001, 'confidence', 0.001, 'thyroxine medication',
                       '/data/home/bt211037/dissertation/medications/allmeds_arm_anal.tsv', small_dfs)