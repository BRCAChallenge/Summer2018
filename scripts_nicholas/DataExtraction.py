################################################################################################
# Script that extracts the genomic coordinate (and) pathogenicity of all variants from a csv/tsv
# file and writes the contents to a new file (preferable a txt file).
# Call the script as:
# python data_extraction.py <file to read from> <file to write to>
################################################################################################

#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
import sys # For command-line arguments
import pandas as pd
import re
#------------------------------------------------------------------------------------------------

## Prints each column of a dataframe with its corresponding index (indexed like a matrix).
#       @param _dataframe : The dataframe to print contents from.
#
def print_columns_with_index(_dataframe):
	for index in range(len(_dataframe.columns)):
		print( '(' + str((index + 1)) + ') ' + _dataframe.columns[index])

## Asks the user for an answer, repeats asking until the user provides 'y', 'Y', 'n', or 'N'
#       @param phrase  : The phrase to ask.
#		@return answer : The user's valid answer.
#
def get_yes_no(phrase):
	answer = ''
	while ( not ((answer == 'y') | (answer == 'Y') | (answer == 'n') | (answer == 'N')) ):
		answer = input(phrase)
	return answer

## Asks the user for an answer, repeats asking until the user provides an integer type answer.
#       @param phrase  : The phrase to ask.
#		@return answer : The user's valid answer.
#
def get_int_answer(phrase):
	answer = ''
	while ( not isinstance(answer, int) ):
		answer = input(phrase)
		if( answer.isdigit() ):
			answer = int(answer)
	return answer

#------------------------------------------------------------------------------------------------
# Records the appropriate separator for the flat file.
if ( re.search('(?<=.)csv', sys.argv[1]) ):
  sep = ','
elif ( re.search('(?<=.)tsv', sys.argv[1]) ):
  sep = '\t'

# Opens flat file for reading, opens file for writing.
df = pd.read_csv(sys.argv[1], sep=sep, header=0)
write_file = open(sys.argv[2], 'w+')

# Prompts the user for input.
print_columns_with_index(df)
col1 = get_int_answer('What is the number of the column to sort by? ')
coordinate_column = list(df.columns)[col1 - 1]
df.sort_values(by=df.columns[col1-1])
first_question = get_yes_no('Write pathogenicity (y/n)? ')
second_question = get_int_answer('Pathogenicity\'s column number? ')
pathogenicity_column = list(df.columns)[second_question - 1]

# For each row in the dataframe, writes the genomic coordinate and pathogenciity to the output file.
for index, row in df.iterrows():
	write_file.write(df[coordinate_column].iloc[index] + '\t')
	if ( (first_question == 'y') | (first_question == "Y") ):
		write_file.write(df[pathogenicity_column].iloc[index]+ '\n')

write_file.close()