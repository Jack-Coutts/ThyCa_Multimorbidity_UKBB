from arm_functions import *

# Read in cluster tsv - userId as index
data = tsv_to_df('/data/home/bt211037/dissertation/cluster_analysis/ThyCa_cluster.tsv', 0)

# Create a list of smaller dataframes from the larger one
small_dfs = split_df(data, 'p193', 20)

# Run analysis of each dataframe and save association riles involving ThyCa
results = multi_df_ARM(0.0001, 'lift', 1.5, 'p193',
                       '/data/home/bt211037/dissertation/association_rule_mining/ThyCa_arm_results.tsv',
                       small_dfs)

