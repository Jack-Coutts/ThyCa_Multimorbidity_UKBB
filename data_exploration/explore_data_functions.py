import pandas as pd


# Write dataframe to tsv
def df_to_tsv(dataframe, filename, index=False):  # Write tsv from dataframe

    dataframe.to_csv(filename, sep='\t', index=index)

    return f'{filename} created.'  # Output text if tsv created.


# Read in dataframe as tsv
def tsv_to_df(tsv, index_col=False):

    data = pd.read_csv(tsv, sep='\t', header=0, index_col=index_col)  # Read in tsv
    return data


def find_col_frequency(tsv_file, colname, target_value):  # Frequency of column value

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=0)  # Read in tsv
    participant_num = len(list(data[colname]))  # Number of rows/participants
    col_of_interest = list(data[colname])  # Turn target column into list
    count = col_of_interest.count(target_value)  # Count number of target column value (e.g. 1) in list
    frequency = count/participant_num  # Find frequency of target value

    return count, frequency  # Return value count and frequency


def all_col_frequency(tsv_file, target_value, index_col=False):  # Return tsv with frequency of all columns

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=index_col)  # Read in tsv
    row_count = data.shape[0]  # Row count
    # List of column frequencies
    out_df_rows = [[i.count(target_value)/row_count] for i in [list(data[i]) for i in data.columns]]
    # Dataframe with column name as index and freq as column
    out_df = pd.DataFrame(out_df_rows, columns=['Frequency'])
    out_df.insert(0, 'diseases', list(data.columns))

    return out_df


def phecode_conversion_tsv(in_tsv, dictionary_tsv, index_col=False):  # Convert phecode to disease name or medication name

    data = pd.read_csv(in_tsv, sep='\t', header=0, index_col=index_col)  # Read in data tsv
    dict = pd.read_csv(dictionary_tsv, sep='\t', header=0, index_col=index_col)  # Read in phecode dictionary tsv

    new_colnames = [dict.loc[i][1] for i in list(data.columns)]  # list of new column names selecting from dictionary
    data.columns = new_colnames  # Replace column names in data

    return data  # Return dataframe with new column names


def phecode_row_conversion_tsv(in_tsv, dictionary_tsv, index_col=False):  # Convert phecode to disease name or medication name

    data = pd.read_csv(in_tsv, sep='\t', header=0, index_col=index_col)  # Read in data tsv
    dict = pd.read_csv(dictionary_tsv, sep='\t', header=0, index_col=index_col)  # Read in phecode dictionary tsv

    new_rownames = [dict.loc[i][1] for i in list(data['diseases'])]  # list of new column names selecting from dictionary
    data.index = new_rownames  # Replace column names in data

    return data  # Return dataframe with new column names


def phecode_conversion_df(data, dictionary_tsv, index_col=False):  # Convert phecode to disease name or medication name

    df = data
    dict = pd.read_csv(dictionary_tsv, sep='\t', header=0, index_col=index_col)  # Read in phecode dictionary tsv

    new_colnames = [dict.loc[i][1] for i in list(df.columns)]  # list of new column names selecting from dictionary
    df.columns = new_colnames  # Replace column names in data

    return df  # Return dataframe with new column names


def phecode_row_conversion_df(data, dictionary_tsv, index_col=False):  # Convert phecode to disease name or medication name

    df = data
    dict = pd.read_csv(dictionary_tsv, sep='\t', header=0, index_col=index_col)  # Read in phecode dictionary tsv

    new_rownames = [dict.loc[i][1] for i in list(df['diseases'])]  # list of new column names selecting from dictionary
    df.index = new_rownames  # Replace column names in data

    return df  # Return dataframe with new column names


# Select subset of dataframe based on column values
def subset_df(dataframe, col_of_interest, col_value):

    df = dataframe.loc[dataframe[col_of_interest] == col_value]  # Select rows based on column value
    return df  # Return dataframe subset


# Select subset of dataframe based on list
def subset_df_list(dataframe, col_of_interest, col_value_list):

    df = dataframe.loc[dataframe[col_of_interest] in col_value_list]  # Select rows based on column value
    return df  # Return dataframe subset


# Write information to output file
def write_out(message_list, filename):

    with open(filename, 'w') as file:

        file.writelines(message_list)

    return f'{filename} created.'

