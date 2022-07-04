import pandas as pd
from scipy.cluster.hierarchy import single, fcluster
from scipy.spatial.distance import pdist


# Function to read in dataframe from tsv
def tsv_to_df(tsv, index_col=False, transpose=False):
    data = pd.read_csv(tsv, sep='\t', header=0, index_col=index_col)  # Read in tsv
    if transpose:
        data = data.T  # Data needs to be transposed for clustering

    return data


# Write dataframe to tsv
def df_to_tsv(dataframe, filename, index=False):  # Write tsv from dataframe

    dataframe.to_csv(filename, sep='\t', index=index)

    return f'{filename} created.'  # Output text if tsv created.


# Create a list of cluster predictions
def h_clust_single(data, metric, distance_cutoff):
    # calculate pairwise distances between observations in n-dimensional space.
    y = pdist(data, metric=metric)

    # perform complete linkage on a condensed distance matrix.
    Z = single(y)

    # form cluster label from the hierarchical clustering defined by the given linkage matrix
    labels = fcluster(Z, distance_cutoff, criterion='distance')  # Number refers to jaccard distance cutoff

    return list(labels)


# Find number of diseases in each cluster
def clust_size(predictions):
    clusters = list(set(predictions))

    lst = []

    for item in clusters:
        item = int(item)
        num = predictions.count(item)
        lst.append(str(item) + ' = ' + str(num))

    return lst


# Find position of ThyCa
def find_ThyCa_clust(dataframe, target_col, predictions):
    # ThyCa
    diseases = list(dataframe.index)
    ThyCa_pos = diseases.index(target_col)
    ThyCa_clust = predictions[ThyCa_pos]

    return ThyCa_clust


# Create list of diseases in target cluster
def list_clust_diseases(ThyCa_clust, predictions, dataframe):
    target_diseases = []
    count = 0

    diseases = list(dataframe.index)

    for item in diseases:

        clust = predictions[count]

        if clust == ThyCa_clust:

            target_diseases.append(item)

        else:
            pass

        count += 1

    return target_diseases


# Create new dataframe and save as tsv
def refined_dataframe(initial_dataframe, target_diseases, filename, index):
    target_df = initial_dataframe.loc[target_diseases]

    target_df = target_df.T

    # save as tsv file
    df_to_tsv(target_df, filename, index)

    return target_df

