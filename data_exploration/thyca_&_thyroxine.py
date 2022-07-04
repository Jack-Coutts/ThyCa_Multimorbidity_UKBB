import pandas as pd

# List of ThyCa participants
data = pd.read_csv('/data/home/bt211037/dissertation/input/raw_data/phecodes_clean_2021.txt', sep='\t', header=0)

lst = list(data['userId'].loc[data['p193'] == 1])

ThyCa = len(lst)

# load med data
mdata = pd.read_csv('/data/home/bt211037/dissertation/input/raw_data/full_med_20003_phec_nona_over20.txt', sep='\t', header=0)

mdataThyCa = mdata.loc[mdata['userId'].isin(lst)]

lst2 = list(mdataThyCa['userId'].loc[(mdataThyCa['m1140874852'] == 1) |
                                     (mdataThyCa['m1140884516'] == 1) |
                                     (mdataThyCa['m1140910814'] == 1) |
                                     (mdataThyCa['m1141191044'] == 1)])

ThyCa_thyrox = len(lst2)

percent_ThyCa = (ThyCa_thyrox / ThyCa) * 100


# Find the prevalence of each medication among ThyCa patients

def find_prevalence(dataframe):
    participant_num = len(dataframe.index)
    diseases = list(dataframe.columns)

    count_dic = {}
    prev_dic = {}

    for item in diseases:

        col = dataframe[item]
        count = 0

        for entry in col:

            if entry == 1:

                count += 1

            elif entry == '1':

                count += 1
            else:

                pass

        count_dic[item] = count
        prev_dic[item] = str((count_dic[item] / participant_num) * 100)

    return prev_dic


prevalence = find_prevalence(mdataThyCa)

# Convert dictionary to dataframe
prevalence_df = pd.DataFrame.from_dict(prevalence, orient='index', columns=['Prevalence (%)'])

# Give index a title
prevalence_df.index.name = 'Medicine Phecodes'

# save as tsv file
prevalence_df.to_csv('/data/home/bt211037/dissertation/data_exploration/thyca_med_prev.tsv', sep='\t')