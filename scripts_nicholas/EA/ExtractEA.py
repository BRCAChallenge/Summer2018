################################################################################################
# Call the script as:
# python ExtractEA.py <classification file> <score file> <output file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf # adds misc functions
#------------------------------------------------------------------------------------------------

"""
This function extracts both the clincally-classified pathogenic of a variant, and its pathogenicity
    score from EA from two file. Both these fields are inserted into a new file, with the genomic
    coordinate ID as the identifier.
    @param classification_file : The file that contains the clincal classifications of the variants.
    @param score_file : The file that contains the EA scores on the variants.
"""
def ExtractEA(classification_file, score_file):
	# Separators for both file types.
	sep1 = ','
	sep2 = '\t'

	# Creates two dataframes, one to hold the classifications, the other to hold the scores.
	pathogenicity_dataframe = pd.read_csv(classification_file, sep=sep1, header=0)
	score_dataframe = pd.read_csv(score_file, sep=sep2, header=0)

	# Prepares the dataframes for merging, then merges them.
	ID_INFO_dataframe = score_dataframe[['ID', 'INFO']]
	pathogenicity_dataframe = pathogenicity_dataframe.rename(index=str, columns={'#Coordinate' : 'ID', 'Pathogenicity' : 'Pathogenicity'})
	merged = pathogenicity_dataframe.merge(ID_INFO_dataframe, on='ID')
	
	# Strips the INFO field of the merged data from of everything but the scores of the variants
	# scored by EA. The field is then renamed to "Score".
	for index,row in merged.iterrows():
		if ( ('NM_007294' in str(row)) | ('NM_000059' in str(row)) ):
			info = row.values[-1].split('|')
			isoform_scores = info[1].split(',')
			score = isoform_scores[0][-5:].strip()
			merged.iloc[index, 2] = score
	merged = merged.loc[ ((merged['INFO'].apply(lambda x: len(x))) <= 5) & (merged['INFO'] != ':STOP') ]
	merged['INFO'] = merged['INFO'].apply(lambda x: round((float(x)/100), 4))
	merged = merged.rename(index=str, columns={'ID': 'Variant', 'Pathogenicity' : 'Pathogenicity', 'INFO' : 'Score'})

	# If there's a fourth command line argument, outputs the merged dataframe to the path indicated
	# by the fourth argument.
	if ( len(sys.argv) == 4 ):
		merged.to_csv(sys.argv[3], index=False, index_label=False)

################################ Main ################################

# arg1 : path to the classification file.
# arg2 : path to the EA-formatted file.
# arg3 : file to write write to, a csv file. Make sure to end its name in ".csv"
ExtractEA(sys.argv[1], sys.argv[2])