################################################################################################
# Call the script as:
# python CountUniqueElementsColumn.py <input file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

## Counts the number of unique items in a specified column of the file. Additionally, displays
#      every unique element in the column and the count of each item.
#  @param file : The file as input to the script. The file should be tab dilimited and have no
#                header. The first line of the file should be the title of each column.
def CountUniqueElementsColumn(file):
	# Creates a csv file from file.
	sep = mf.determine_separator(file)
	df = pd.read_csv(file, sep=sep, header=0)

	# Print the columns of the file to the console. Gets the name of the column to be printed
	# from the user.
	mf.print_columns_with_index(df)
	column_number = mf.get_int_answer('What column should be accumulated? ')
	column_name = list(df.columns)[column_number - 1]

	# Creates a list of the unique values from the specified column. Prints its length, and
	# optionally each item and its frequency.
	unique_values = pd.unique(df[column_name])
	print('Number of unique items: ' + str(len(unique_values)))
	show_items = mf.get_yes_no('Show item/counts (y/n)? ')
	if ( (show_items == 'y') | (show_items == 'Y') ):
		for item in unique_values:
			print(str(item) + ': ' + str(df[df[column_name] == item].shape[0]))

################################ Main ################################
CountUniqueElementsColumn(sys.argv[1])



