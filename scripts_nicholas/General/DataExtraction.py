################################################################################################
# Call the script as:
# python DataExtraction.py <file to read from> <file to write to>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf # adds misc functions
#------------------------------------------------------------------------------------------------

## Extracts the variant identifier (HGVS, genomic coordinate, etc.) and pathogenicity of each
#      variant in a csv-like file.
#  @param read_file  : The file as input to the script. The file should be tab dilimited and have
#                      no header. The first line of the file should be the title of each column.
#                      One column must contain some variant identification, and another should
#                      contain pathogenicity classification.
#  @param write_file : The file to write data to. The file should be a tsv file, as the output
#                      is tab-delimited.
#
def DataExtraction(read_file, write_file):
	# Creates a dataframe from read_file and opens a new file for writing.
	sep = mf.determine_separator(read_file)
	df = pd.read_csv(read_file, sep=sep, header=0)
	write_file = open(write_file, 'w+')

	# Prints the columns of the file to the console. Gets the name of the column to extract
	# variant identifiers from. Optionally writes the pathogenicity into a second column.
	mf.print_columns_with_index(df)
	col1 = mf.get_int_answer('What is the number of the column to sort by? ')
	coordinate_column = list(df.columns)[col1 - 1]
	df.sort_values(by=df.columns[col1-1])
	first_question = mf.get_yes_no('Write pathogenicity (y/n)? ')
	if ( (first_question == 'y') | (first_question == "Y") ):
		second_question = mf.get_int_answer('Pathogenicity\'s column number? ')
		pathogenicity_column = list(df.columns)[second_question - 1]

	# Writes the variant identifier and the pathogencity to output_file.
	for index, row in df.iterrows():
		write_file.write(df[coordinate_column].iloc[index] + ',')
		if ( (first_question == 'y') | (first_question == "Y") ):
			write_file.write(df[pathogenicity_column].iloc[index])
		write_file.write('\n')

	write_file.close()

################################ Main ################################

# arg1 : path to csv-like file to extract variant identifier (and pathogenicity) from.
# arg2 : file to write write to, a tsv file.
DataExtraction(sys.argv[1], sys.argv[2])



