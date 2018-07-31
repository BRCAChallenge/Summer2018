################################################################################################
# This contains multiple functions that I found myself repeating through-out the process
# The functions are organized alphabetically.
################################################################################################

#-----------------------------------------------------------------------------------------------
import pandas as pd # For dataframes
import re # To process regex.
#-----------------------------------------------------------------------------------------------

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

## Asks the user for an answer, repeats asking until the user provides 'y', 'Y', 'n', or 'N'
#       @param phrase  : The phrase to ask.
#		@return answer : The user's valid answer.
#
def get_yes_no(phrase):
	answer = ''
	while ( not ((answer == 'y') | (answer == 'Y') | (answer == 'n') | (answer == 'N')) ):
		answer = input(phrase)
	return answer

## Prints each column of a dataframe with its corresponding index (indexed like a matrix).
#       @param _dataframe : The dataframe to print contents from.
#
def print_columns_with_index(dataframe):
	for index in range(len(dataframe.columns)):
		print( '(' + str((index + 1)) + ') ' + dataframe.columns[index] )

## Returns the appropriate separator for several file formats.
#       @param filename : The file to assess.
#		@return sep     : The separator associated with the filetype of named file.
def determine_separator(filename):
	sep = ''
	if ( re.search('(?<=.)csv', filename) ):
		sep = ','
	elif ( re.search('(?<=.)tsv', filename) ):
		sep = '\t'
	elif ( re.search('(?<=.)vep.txt', filename) ):
		sep = '\t'
	return sep
	
