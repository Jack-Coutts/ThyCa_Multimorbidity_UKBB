import pandas as pd


# Write dataframe to tsv
def df_to_tsv(dataframe, filename, index=False):  # Write tsv from dataframe

    dataframe.to_csv(filename, sep='\t', index=index)

    return f'{filename} created.'  # Output text if tsv created.


# Function to read in dataframe from tsv
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


# Function for frequency of each column in dataframe (assuming binary data)
def all_col_frequency(tsv_file, target_value, index_col=False):  # Return tsv with frequency of all columns

    data = pd.read_csv(tsv_file, sep='\t', header=0, index_col=index_col)  # Read in tsv
    row_count = data.shape[0]  # Row count
    # List of column frequencies
    out_df_rows = [[p.count(target_value)/row_count] for p in [list(data[i]) for i in data.columns]]
    # Dataframe with two columns disease name and frequency
    out_df = pd.DataFrame(out_df_rows, columns=['frequency'])
    out_df.insert(0, 'diseases', list(data.columns))

    return out_df


# Function for converting phecodes to disease names. Works when disease names contained in a column.
def phecode_col_conversion(data, dictionary_df, replace_col, key_col, new_col, index_col=False):

    dataframe = data # re-assign dataframe
    dataframe = dataframe.drop(0, axis=0)  # Drop userId
    r = list(dataframe[replace_col])  # Create a list of phecodes in existing df
    new = []  # New column entries (disease names)

    for item in r:  # Iterate over phecodes
        # Iterate over dictionary df keys (phecodes) and values (disease names)
        for key, value in zip(list(dictionary_df[key_col]), list(dictionary_df[new_col])):
            if item == key:  # If phecode in current df
                new.append(value)  # Add corresponding disease name to new list
            else:  # If not pass
                pass

    dataframe[replace_col] = new  # Replace phecodes in disease column with disease names

    return dataframe  # Return new dataframe


# Function for converting phecodes to disease names. Works when disease names are the headers.
def phecode_header_conversion(data, dictionary_df, key_col, new_col, index_col=False):

    dataframe = data # re-assign dataframe
    dataframe = dataframe.drop(0, axis=1)  # Drop userId
    r = list(dataframe.columns)  # Create a list of phecodes in existing df
    new = []  # New column entries (disease names)

    for item in r:  # Iterate over phecodes
        # Iterate over dictionary df keys (phecodes) and values (disease names)
        for key, value in zip(list(dictionary_df[key_col]), list(dictionary_df[new_col])):
            if item == key:  # If phecode in current df
                new.append(value)  # Add corresponding disease name to new list
            else:  # If not pass
                pass

    dataframe.set_axi(new, 1, inplace=True)   # Replace phecodes in disease column with disease names

    return dataframe  # Return new dataframe


# Select subset of dataframe based on column values
def subset_df(dataframe, col_of_interest, col_value):
    df = dataframe.loc[dataframe[col_of_interest] == col_value]  # Select rows based on column value
    return df  # Return dataframe subset


# Select subset of dataframe based on list
def subset_df_list(dataframe, col_of_interest, col_value_list):
    df = dataframe.loc[dataframe[col_of_interest].isin(col_value_list)]  # Select rows based on column value
    return df  # Return dataframe subset


# Write information to output file
def write_out(message_list, filename):

    with open(filename, 'w') as file:

        file.writelines(message_list)

    return f'{filename} created.'

