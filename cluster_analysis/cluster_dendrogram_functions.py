import pandas as pd
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as shc


# Function to read in dataframe from tsv
def tsv_to_df(tsv, index_col=False, transpose=False):
    data = pd.read_csv(tsv, sep='\t', header=0, index_col=index_col)  # Read in tsv
    if transpose:
        data = data.T  # Data needs to be transposed for clustering

    return data


# Create a dendrogram png file
def plot_dendro(title, data, meth, metric, filename):
    # Plot figure
    plt.figure(figsize=(8, 6))
    dend = shc.dendrogram(shc.linkage(data, method=meth, metric=metric))
    plt.title(title)
    plt.xlabel('Diseases')
    plt.ylabel(metric + ' distance')

    # Save figure
    plt.savefig(filename, dpi=300)

