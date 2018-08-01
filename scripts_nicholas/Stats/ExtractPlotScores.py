################################################################################################
# Call the script as:
# python ExtractPlotScores.py <classification file> <score file> <output file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
import matplotlib.pyplot as plt
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

## Script that exctracts the REVEL scores from a VEP formatted file and its classified
#      pathogenicity and plots the scores partitioned by pathogenicity as a boxplot.
#  @param classification_file : A csv-like file that contains both a variant identifier and a
#                               pathogenicity for each variant.
#  @param score_file          : A csv-like file that contains both a variant identifier and a
#                               score for each variant.
def ExtractPlotScores(classification_file, score_file):
	# Determines the separators for both files.
	sep1 = mf.determine_separator(classification_file)
	sep2 = mf.determine_separator(score_file)

	# Creates dataframes from both files.
	pathogenicity_dataframe = pd.read_csv(classification_file, sep=sep1, header=0)
	score_dataframe = pd.read_csv(score_file, sep=sep2, header=0)

	# Inquires about which column in the curated file contains pathogenicity data. Sets the variant
	# identifier to the first column.
	mf.print_columns_with_index(pathogenicity_dataframe)
	pathogenicity_index  = mf.get_int_answer('What column states the pathogenicity? ')
	pathogenicity_column = list(pathogenicity_dataframe.columns)[pathogenicity_index - 1]
	coordinate_index_1  = mf.get_int_answer('What column identifies the variant? ')
	genomic_coordinate_column1 = list(pathogenicity_dataframe.columns)[coordinate_index_1 - 1]

	# Inquires about which column in the output file of the predictor method contains pathogenicity
	# scores. Sets the variant identifier to the first column, which must match a value in the first
	# column of the curated file.
	mf.print_columns_with_index(score_dataframe)
	score_index = mf.get_int_answer('What column gives the scores? ')
	score_column = list(score_dataframe.columns)[score_index - 1]
	coordinate_index_2  = mf.get_int_answer('What column identifies the variant? ')
	genomic_coordinate_column2 = list(score_dataframe.columns)[coordinate_index_2 - 1]

	# Creates a dictionary to store each variant's pathogenicity and pathogenicity score. Creates
	# a list that stores each variant identifier associated with a reported score.
	scores = {'pathogenicity': [], 'scores': []}
	chromosome_list = []

	for index, row in score_dataframe.iterrows(): # Iterates through each variant in the output file.
		# Determines if the given variant in the outfile has a score. If so, the variable
		# 'after' contains the variant's score. Otherwise, 'after' is empty.
		to_parse = score_dataframe[score_column].iloc[index]
		phrase = 'REVEL_score='
		before, at, after = to_parse.partition(phrase)

		if ( after != ''): # If the variant reports a score.
			# And the variant has no previously reported score.
			if ( score_dataframe[genomic_coordinate_column2].iloc[index] not in chromosome_list ):
				# Add the variant to the list of scored variants. Then append the score to the list
				# of scores and append the variants pathogenicity to the list of pathogencities.
				chromosome_list.append(score_dataframe[genomic_coordinate_column2].iloc[index])
				scores['scores'].append(float(after))
				genomic_coordinate = chromosome_list[-1]
				pathogenicity = pathogenicity_dataframe[pathogenicity_dataframe[genomic_coordinate_column1] == genomic_coordinate][pathogenicity_column]
				if ( (pathogenicity.values[0] == 'Benign') | (pathogenicity.values[0] == 'Likely_benign') ):
					scores['pathogenicity'].append("Benign")
				elif ( (pathogenicity.values[0] == 'Pathogenic') | (pathogenicity.values[0] == 'Likely_pathogenic') ):
					scores['pathogenicity'].append('Pathogenic')

	# Construct a dataframe from the dictionary, and then we create a boxplot from the data.
	df = pd.DataFrame.from_dict(scores)
	if ( len(sys.argv) == 4 ):
		df.to_csv(output_file)
	print('variants scored:', df.shape[0], '/', pathogenicity_dataframe.shape[0])
	#  , '/', len((pathogenicity_dataframe.shape())[1])
	boxplt = df.boxplot(by='pathogenicity')
	plt.show()

################################ Main ################################

# arg1 : The file that contains both a variant identifier and a pathogenicity for each variant.
# arg2 : The file that contains both a variant identifier and a score for each variant.
# Optionally adding a third argument will result in the creation of a csv file with name of the
# third argument passed. 
ExtractPlotScores(sys.argv[1], sys.argv[2])
