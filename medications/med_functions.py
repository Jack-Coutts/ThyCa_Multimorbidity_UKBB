import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules


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


# Function to add Thyroxine medication column to disease data
def add_col(target_df, value, colname, ref_df, *args):
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


# Split large dataframe into many smaller ones
def split_df(dataframe, col_of_interest, split_num):
    # Store column of interest
    col = dataframe[col_of_interest]

    # Create a dataframe where they col of interest row is removed
    data_noThyCa = dataframe.drop(col_of_interest, axis=1)

    # Split the dataframe (creates an array)
    split_array = np.array_split(data_noThyCa, split_num, axis=1)

    # Empty list
    split_dataframes = []

    # Turn each item in array to df
    for index, item in enumerate(split_array):
        # Turn into df
        df = pd.DataFrame(item)

        # Add column of interest
        df[col_of_interest] = col

        # Create list of the split dataframes
        split_dataframes.append(df)

    return split_dataframes


# Function that runs the full analysis on a dataframe
def arm_analysis(dataframe, min_support, metric, min_threshold, target_col):
    # convert target col to lowercase
    target_col = target_col.lower()

    # Create Apriori model
    model = apriori(dataframe, min_support=min_support, use_colnames=True)

    # Get interpretation values
    rules = association_rules(model, metric=metric, min_threshold=min_threshold)

    # Select rows containing ThyCa
    ThyCa_rules = rules.loc[
        (rules['antecedents'].astype(str).str.lower().str.contains(target_col))
        |
        (rules['consequents'].astype(str).str.lower().str.contains(target_col))
        ]

    return ThyCa_rules


# Function that runs ARM analysis on multiple dataframes and combines the results
def multi_df_ARM(min_support, metric, min_threshold, target_col, out_filename, df_lst):
    result_lst = []  # Create empty list

    # Run analysis on each dataframe entered and add reults to a list
    for item in df_lst:
        # Run analysis
        results = arm_analysis(item, min_support, metric, min_threshold, target_col)

        # Convert from frozenset to list
        results['antecedents'] = results['antecedents'].apply(list)
        results['consequents'] = results['consequents'].apply(list)

        # Create list of rule dataframe
        result_lst.append(results)

    # Combine all the results dataframes
    all_results = pd.concat(result_lst)

    # Write to tsv
    all_results.to_csv(out_filename, sep='\t')

    return all_results

