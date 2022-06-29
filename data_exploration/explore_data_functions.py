import pandas as pd


def df_to_tsv(dataframe, filename):  # Write tsv from dataframe

    dataframe.to_csv(filename, sep='\t', index=False)

    return f'{filename} created.'  # Output text if tsv created.


def find_col_frequency(tsv_file, colname, target_value):  # Frequency of column value

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=0)  # Read in tsv
    participant_num = len(data.index)  # Number of rows/participants
    col_of_interest = list(data[colname])  # Turn target column into list
    count = col_of_interest.count(target_value)  # Count number of target column value (e.g. 1) in list
    frequency = count/participant_num  # Find frequency of target value

    return count, frequency  # Return value count and frequency


def all_col_frequency(tsv_file, target_value):  # Return tsv with frequency of all columns

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=0)  # Read in tsv
    row_count = len(data.index)  # Row count
    # List of column frequencies
    out_df_rows = [[i.count(target_value)/row_count] for i in [list(data[i]) for i in data.columns]]
    # Dataframe with column name as index and freq as column
    out_df = pd.DataFrame(out_df_rows, columns=['Frequency'], index=data.columns)

    return out_df


def phecode_conversion(in_tsv, dictionary_tsv):  # Convert phecode to disease name or medication name

    data = pd.read_csv(in_tsv, sep='\t', header=0, index_col=0)  # Read in data tsv
    dict = pd.read_csv(dictionary_tsv, sep='\t', header=0, index_col=0)  # Read in phecode dictionary tsv

    new_colnames = [dict.loc[i][0] for i in list(data.columns)]  # list of new column names selecting from dictionary
    data.columns = new_colnames  # Replace column names in data

    return data  # Return dataframe with new column names

