import pandas as pd


def find_col_frequency(tsv_file, col_name):

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=0)
    participant_num = len(data.index)

    pass


def all_col_frequency():

    pass


def count_col_yes():  # Number of participants with 1 in column e.g. num of participants with ThyCa

    pass