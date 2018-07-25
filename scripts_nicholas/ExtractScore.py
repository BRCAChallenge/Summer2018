# The goal is to create a formatted csv file that contains each variant that reports a score with
# its corresponding classification (according to ENIGMA/ClinVar/etc.).

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018 (Repo)/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------
sep1 = mf.separator_csv_or_tsv(sys.argv[1])
sep2 = mf.separator_csv_or_tsv(sys.argv[2])

pathogenicity_dataframe = pd.read_csv(sys.argv[1], sep=sep1, header=0)
score_dataframe = pd.read_csv(sys.argv[2], sep=sep2, header=0)
#write_file = open(sys.argv[3], 'w+')

mf.print_columns_with_index(pathogenicity_dataframe)
pathogenicity_index  = mf.get_int_answer('What column states the pathogenicity? ')
pathogenicity_column = list(pathogenicity_dataframe.columns)[pathogenicity_index - 1]
genomic_coordinate_column1 = list(pathogenicity_dataframe.columns)[0]

mf.print_columns_with_index(score_dataframe)
score_index = mf.get_int_answer('What column gives the scores? ')
score_column = list(score_dataframe.columns)[score_index - 1]
genomic_coordinate_column2 = list(score_dataframe.columns)[0]

revel_scores = {'pathogenicity': [], 'scores': []}
chromosome_list = []

for index, row in score_dataframe.iterrows():
	to_parse = score_dataframe[score_column].iloc[index]
	phrase = 'REVEL_score='
	before, at, after = to_parse.partition(phrase)
	if ( after != ''):
		if ( score_dataframe[genomic_coordinate_column2].iloc[index] not in chromosome_list ):
			chromosome_list.append(score_dataframe[genomic_coordinate_column2].iloc[index])
			revel_scores['scores'].append(float(after))
			genomic_coordinate = chromosome_list[-1]
			pathogenicity = pathogenicity_dataframe[pathogenicity_dataframe[genomic_coordinate_column1] == genomic_coordinate][pathogenicity_column]
			revel_scores['pathogenicity'].append(pathogenicity)

print(revel_scores['pathogenicity'][18])

#df = pd.DataFrame.from_dict(revel_scores)

#boxplt = df.boxplot(by=patho_col)

#plt.show()