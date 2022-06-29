import pandas as pd


def find_col_frequency(tsv_file, colname, target_value):  # Frequency of column value

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=0)  # Read in tsv
    participant_num = len(data.index)  # Number of rows/participants
    col_of_interest = list(data[colname])  # Turn target column into list
    count = col_of_interest.count(target_value)  # Count number of target column value (e.g. 1) in list
    frequency = count/participant_num  # Find frequency of target value

    return count, frequency  # Return value count and frequency


def all_col_frequency(tsv_file):

    pass



def phecode_conversion():  # Convert phecode to disease name or medication name

    pass

