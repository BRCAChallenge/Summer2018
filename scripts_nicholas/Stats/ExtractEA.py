################################################################################################
# Call the script as:
# python ExtractEA.py <classification file> <score file> <output file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

def ExtractEA(classification_file, score_file):
	sep1 = ','
	sep2 = '\t'

	pathogenicity_dataframe = pd.read_csv(classification_file, sep=sep1, header=0)
	score_dataframe = pd.read_csv(score_file, sep=sep2, header=0)

	ID_INFO_dataframe = score_dataframe[['ID', 'INFO']]
	pathogenicity_dataframe = pathogenicity_dataframe.rename(index=str, columns={'#Coordinate' : 'ID', 'Pathogenicity' : 'Pathogenicity'})

	merged = pathogenicity_dataframe.merge(ID_INFO_dataframe, on='ID')
	print(merged)
	for index,row in merged.iterrows():
		if ( ('NM_007294' in str(row)) | ('NM_000059' in str(row)) ):
			info = row.values[-1].split('|')
			isoform_scores = info[1].split(',')
			score = isoform_scores[0][-5:].strip()
			merged.iloc[index, 2] = score
	merged = merged.loc[ ((merged['INFO'].apply(lambda x: len(x))) <= 5) & (merged['INFO'] != ':STOP') ]
	merged['INFO'] = merged['INFO'].apply(lambda x: round((float(x)/100), 4))
	merged = merged.rename(index=str, columns={'ID': 'Variant', 'Pathogenicity' : 'Pathogenicity', 'INFO' : 'Score'})

	if ( len(sys.argv) == 4 ):
		merged.to_csv(sys.argv[3], index=False, index_label=False)

################################ Main ################################

# arg1 : path to the classification file.
# arg2 : path to the EA-formatted file.
# arg2 : file to write write to, a tsv file.
ExtractEA(sys.argv[1], sys.argv[2])