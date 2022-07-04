from create_cluster_functions import *

# Read in data and transpose
data = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt', 0, True)  # Index = userId

# Run clustering to find cluster allocations
predictions = h_clust_single(data, 'jaccard', 0.955)

# Find the thyroid cancer cluster
ThyCa_clust = find_ThyCa_clust(data, 'p193', predictions)

# Create a list of diseases in ThyCa cluster
target_diseases = list_clust_diseases(ThyCa_clust, predictions, data)

# Create tsv containing only data for diseases in ThyCa cluster
refined_dataframe(data, target_diseases, '/data/home/bt211037/dissertation/cluster_analysis/ThyCa_cluster.tsv', 0)

