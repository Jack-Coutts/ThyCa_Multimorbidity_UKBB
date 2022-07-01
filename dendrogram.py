
from phase1_functions.cluster_dendrogram_functions import *

# Read in data and transpose
data = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt', 0, True)  # Index = userId

# Plot dendrogram using complete linkage
plot_dendro('UK Biobank Disease Clusters', data, 'complete', 'jaccard', 'complete_lnk_dendro.png')

# Plot dendrogram using single linkage
plot_dendro('UK Biobank Disease Clusters', data, 'complete', 'jaccard', 'single_lnk_dendro.png')
