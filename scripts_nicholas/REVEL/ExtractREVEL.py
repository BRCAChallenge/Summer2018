################################################################################################
# Call the script as:
# python ExtractPlotScores.py <classification file> <score file> <output file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf # adds misc functions
#------------------------------------------------------------------------------------------------

"""
This function extracts both the clincally-classified pathogenic of a variant, and its
    pathogenicity score from REVEL from two file. Both these fields are inserted into a new file,
    with the genomic coordinate ID as the identifier.
    @param classification_file : The file that contains the clincal classifications of the
        variants.
    @param score_file : The file that contains the REVEL scores on the variants.
"""
def ExtractPlotScores(classification_file, score_file):
	# Separators for both file types.
	sep1 = ','
	sep2 = '\t'

	# Creates two dataframes, one to hold the classifications, the other to hold the scores.
	pathogenicity_dataframe = pd.read_csv(classification_file, sep=sep1, header=0)
	score_dataframe = pd.read_csv(score_file, sep=sep2, header=0)

	# Prepares the dataframes for merging, then merges them.
	ID_INFO_dataframe = score_dataframe[['#Uploaded_variation', 'Extra']]
	ID_INFO_dataframe = ID_INFO_dataframe.rename(index=str, columns={'#Uploaded_variation' : 'ID', 'Extra' : 'Extra'})
	pathogenicity_dataframe = pathogenicity_dataframe.rename(index=str, columns={'#Coordinate' : 'ID', 'Pathogenicity' : 'Pathogenicity'})
	merged = pathogenicity_dataframe.merge(ID_INFO_dataframe, on='ID')

	# Strips the INFO field of the merged data from of everything but the scores of the variants
	# scored by EA. The field is then renamed to "Score".
	for index,row in merged.iterrows():
		to_check = row.values[-1].split(',')[-1]
		phrase = 'REVEL_score='
		before, at, after = to_check.partition(phrase)
		if ( mf.check_float(after) ):
			merged.iloc[index, 2] = float(after)
	merged = merged.loc[ ((merged['Extra'].apply(lambda x: len(str(x)))) <= 5) ]
	
	merged = merged.rename(index=str, columns={'ID': 'Variant', 'Pathogenicity' : 'Pathogenicity', 'Extra' : 'Score'})
	merged = merged.drop_duplicates()

	# Construct a dataframe from the dictionary, and then we create a boxplot from the data.
	#df = pd.DataFrame.from_dict(scores)
	if ( len(sys.argv) == 4 ):
		merged.to_csv(sys.argv[3], index=False, index_label=False)
################################ Main ################################

# arg1 : The file that contains both a variant identifier and a pathogenicity for each variant.
# arg2 : The file that contains both a variant identifier and a score for each variant.
# Optionally adding a third argument will result in the creation of a csv file with name of the
# third argument passed. 
ExtractPlotScores(sys.argv[1], sys.argv[2])
