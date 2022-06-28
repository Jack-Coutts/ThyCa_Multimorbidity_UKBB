import pandas as pd


def find_col_frequency(tsv_file, col_name):

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=0)

    pass

