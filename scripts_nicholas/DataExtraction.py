################################################################################################
# Script that extracts the genomic coordinate (and) pathogenicity of all variants from a csv/tsv
# file and writes the contents to a new file (preferable a txt file).
# Call the script as:
# python data_extraction.py <file to read from> <file to write to>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------
sep = mf.determine_separator(sys.argv[1])

# Opens flat file for reading, opens file for writing.
df = pd.read_csv(sys.argv[1], sep=sep, header=0)
write_file = open(sys.argv[2], 'w+')

# Prompts the user for input.
mf.print_columns_with_index(df)
col1 = mf.get_int_answer('What is the number of the column to sort by? ')
coordinate_column = list(df.columns)[col1 - 1]
df.sort_values(by=df.columns[col1-1])
first_question = mf.get_yes_no('Write pathogenicity (y/n)? ')
if ( (first_question == 'y') | (first_question == "Y") ):
	second_question = mf.get_int_answer('Pathogenicity\'s column number? ')
	pathogenicity_column = list(df.columns)[second_question - 1]

# For each row in the dataframe, writes the genomic coordinate (and pathogenicity) to the output file.
for index, row in df.iterrows():
	write_file.write(df[coordinate_column].iloc[index] + '\t')
	if ( (first_question == 'y') | (first_question == "Y") ):
		write_file.write(df[pathogenicity_column].iloc[index])
	write_file.write('\n')

write_file.close()