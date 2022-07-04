import pandas as pd


# Write dataframe to tsv
def df_to_tsv(dataframe, filename, index=False):  # Write tsv from dataframe

    dataframe.to_csv(filename, sep='\t', index=index)

    return f'{filename} created.'  # Output text if tsv created.


# Function to read in dataframe from tsv
def tsv_to_df(tsv, index_col=False):
    data = pd.read_csv(tsv, sep='\t', header=0, index_col=index_col)  # Read in tsv
    return data


# Read in disease data
disease_data = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt', 0)

# Read in operation data
op_data = tsv_to_df('/data/home/bt211037/dissertation/data_exploration/hes_oper_dates_clean.txt', 0)

# Select only patients with thyroid cancer
disease_data = disease_data.loc[disease_data['p193'] == 1]

# Create a list of thyca patients
thyca_patients = list(disease_data.index)

# Only look at operations in thyca patients
op_data = op_data.loc[op_data.index.isin(thyca_patients)]

# Look at those with throidectomy
thyroidecto = op_data.loc[op_data['oper4'].str.contains('b08', case=False, na=False)]

print(len(thyroidecto.index))




