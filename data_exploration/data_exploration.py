import pandas as pd
from explore_data_functions import *

# Frequency of all diseases in UK Biobank data
all_disease_freq = all_col_frequency('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt', 1, 0)
all_disease_freq = phecode_row_conversion_df(all_disease_freq, '/data/home/bt211037/dissertation/input/raw_data/ukbb_and_phec_clean.txt')
df_to_tsv(all_disease_freq, '/data/home/bt211037/dissertation/data_exploration/disease_frequencies.tsv')

# Frequency and count for ThyCa
ThyCa_count, ThyCa_freq = find_col_frequency('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt',
                                             'p193',
                                             1)

# Frequency of all medications in UK Biobank data
all_med_freq = all_col_frequency('/data/home/bt211037/dissertation/input/raw_data/full_med_20003_phec_nona_over20.txt', 1)
all_med_freq = phecode_row_conversion_df(all_med_freq, '/data/home/bt211037/dissertation/input/raw_data/ukbb_and_phec_clean.txt')
df_to_tsv(all_med_freq, '/data/home/bt211037/dissertation/data_exploration/medication_frequencies.tsv')

# Dataframe of thyroid cancer patients
ThyCa_pps = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt')
ThyCa_pps = subset_df(ThyCa_pps, 'p193', 1)

# Medication frequencies in ThyCa patients
meds = tsv_to_df('/data/home/bt211037/dissertation/input/raw_data/full_med_20003_phec_nona_over20.txt')
ThyCa_meds = subset_df_list(meds, 'userId', list(ThyCa_pps.index))
ThyCa_med_freq = all_col_frequency('/data/home/bt211037/dissertation/input/raw_data/full_med_20003_phec_nona_over20.txt', 1, 0)
ThyCa_med_freq = phecode_row_conversion_df(ThyCa_med_freq, '/data/home/bt211037/dissertation/input/raw_data/ukbb_and_phec_clean.txt')
df_to_tsv(ThyCa_med_freq, '/data/home/bt211037/dissertation/data_exploration/ThyCa_med_frequencies.tsv')

# Summary information
summary = ['\n',
           f'There is disease data for {ThyCa_count/ThyCa_freq} participants \n',
           '\n',
           f'ThyCa occurs at a frequency of {ThyCa_freq} meaning there are {ThyCa_count} with the disease \n',
           '\n',
           f'There is medication data for {len(meds.index)} individuals']

# Write summary file
write_out(summary, '/data/home/bt211037/dissertation/data_exploration/summary.txt')