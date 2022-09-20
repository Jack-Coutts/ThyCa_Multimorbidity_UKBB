# Assessing Thyroid Cancer multimorbidity using the UK Biobank database

<p align="center">
<img src="https://github.com/Jack-Coutts/ThyCa_Multimorbidity_UKBB/blob/main/ThyCa_multimorbidity.png" width=75% height=75% class="center">
</p>

***Abstract:*** *Thyroid cancer is the most common endocrine malignancy worldwide and has reached epidemic levels in recent years. Diagnostic techniques for thyroid cancer have significant limitations and the disease is often diagnosed alongside other conditions. Multimorbidity refers to the coexistence of at least two chronic conditions in a single individual and the term comorbidity, for the purpose of this work, refers to a disease that co-occurs with the reference disease. Multimorbidity is becoming an increasingly important priority for clinicians, researchers, and health authorities due to the substantial impact it has on individuals and health authorities globally. Multimorbidity has a disproportionally large effect on patient mortality for cancers with less severe diagnoses and this is highly relevant for thyroid cancer where the 10-year survival for 95% of individuals is 90%. Some research has suggested that approximately 20% of deaths in thyroid cancer patients are due to multimorbidity rather than the primary disease. Despite this, little is known about thyroid cancer multimorbidity.*

*The growing focus on data collection and existence of large biomedical databases have allowed researched to start using machine learning techniques to address problems like multimorbidity. This work looked to use unsupervised machine learning techniques to identify comorbidities of thyroid cancer using data from the UK Biobank database. Agglomerative hierarchical clustering and association rule mining were used to identify association rules between other disease and thyroid cancer as well quantify the strength of the relationships. Several known disease relationships and some previously undescribed comorbidities were identified here, with a key finding being the identification of eye cancer as a comorbidity of thyroid cancer.*


## Data Source 

This research was conducted using data from UK Biobank, a major biomedical database: [www.ukbiobank.ac.uk](https://www.ukbiobank.ac.uk/).

Specifically, this work used binary disease and medication data for 394,884 and 294,699 individuals respectively. The relationship between 786 diseases and thyroid cancer was examined as well as the relationship between three drugs prescribed for thyroid cancer and the 786 diseases.

*Reference:*

Sudlow, C. et al. (2015) ‘UK Biobank: An Open Access Resource for Identifying the Causes of a Wide Range of Complex Diseases of Middle and Old Age’, PLoS Medicine, 12(3), p. e1001779. Available at: https://doi.org/10.1371/journal.pmed.1001779.


## Methodology

The methodology used for this work was adapted from Zemedikun et al. in which agglomerative hierarchical clustering was used to identify a cluster of disease related to thyroid cancer that was small enough for association rule mining to run. The clustering technique used the Jaccard distance metric and the single linkage method. Following this, association rule mining was applied to identify association rules between diseases. The association rules were measured by a value known as the lift which is a number representing how often two diseases are seen to co-occur compared to how often they would be expected to co-occur by chance. The higher the lift, the stronger the association between two diseases.

The protocol was also applied for three medications prescribed to individuals following a thyroidectomy, a common thyroid cancer treatment, to determine whether the disease results were due to thyroid cancer or drugs prescribed for it.

This research utilised Queen Mary's Apocrita HPC facility, supported by QMUL Research-IT. http://doi.org/10.5281/zenodo.438045

*Reference:*

Zemedikun, D.T. et al. (2018) ‘Patterns of Multimorbidity in Middle-Aged and Older Adults: An Analysis of the UK Biobank Data’, Mayo Clinic Proceedings, 93(7), pp. 857–866. Available at: https://doi.org/10.1016/j.mayocp.2018.02.012.


## Results

The results for thyroid cancer multimorbidity can bee seen in the figure below:

<p align="center">
<img src="https://github.com/Jack-Coutts/ThyCa_Multimorbidity_UKBB/blob/main/ThyCa_multimorbidity.png" width=75% height=75% class="center">
</p>

The results for each of the three medications and the three medications combined can be seen below:

<p align="center">
<img src="https://github.com/Jack-Coutts/ThyCa_Multimorbidity_UKBB/blob/main/ThyCa_drugs.png" width=75% height=75% class="center">
</p>

## Acknowledgements

I would like to thank Dr Eirini Marouli for her help and suppor throughout the duration of this project.
