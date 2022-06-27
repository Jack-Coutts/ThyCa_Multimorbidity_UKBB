import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.cluster.hierarchy import ward, median, centroid, weighted, average, complete, single, fcluster
from scipy.spatial.distance import pdist


# Create dictionary containing userId and yes/no Thyroxine-based medication
# Add a column to a dataframe depending on the column value of multiple other columns
# 1 if value present in selected columns and 0 if not

def new_col_dic(target_df, value, colname, out_file, ref_df, *args):
    dictionary = {}

    for index, row in ref_df.iterrows():

        count = 0

        for item in args:

            if row[item] == value:

                count += 1

                if count < 2:

                    dictionary[index] = 1

                else:
                    pass
            else:
                pass

        if count == 0:
            dictionary[index] = 0

    new_col = []

    for index, row in target_df.iterrows():
        new_col.append(dictionary[index])

    target_df[colname] = new_col

    # save as tsv file
    # target_df.to_csv(out_file, sep='\t')


# Create a dendrogram png file
def plot_dendro(title, data, meth, metric, filename):
    # Plot figure
    plt.figure(figsize=(16, 8))
    dend = shc.dendrogram(shc.linkage(data, method=meth, metric=metric))
    plt.title(title)
    plt.xlabel('Diseases')
    plt.ylabel(metric + ' distance')

    # Save figure
    plt.savefig(filename, dpi=300)


# Create a list of cluster predictions
def h_clust_complete(data, metric, distance_cutoff):
    # calculate pairwise distances between observations in n-dimensional space.
    y = pdist(data, metric=metric)

    # perform complete linkage on a condensed distance matrix.
    Z = complete(y)

    # form cluster label from the hierarchical clustering defined by the given linkage matrix
    labels = fcluster(Z, distance_cutoff, criterion='distance')  # Number refers to jaccard distance cutoff

    return list(labels)


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
def refined_dataframe(initial_dataframe, target_diseases, filename):
    target_df = initial_dataframe.loc[target_diseases]

    target_df = target_df.T

    # save as tsv file
    target_df.to_csv(filename, sep='\t')

    return target_df
