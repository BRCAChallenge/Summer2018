################################################################################################
# This script counts the number of unique elements in a specified column in a VEP-formatted file.
# Call the script as:
# python CountUniqueElementsColumn.py <file to read from>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

sep = mf.determine_separator(sys.argv[1])
df = pd.read_csv(sys.argv[1], sep=sep, header=0)

mf.print_columns_with_index(df)
column_number = mf.get_int_answer('What column should be accumulated? ')
column_name = list(df.columns)[column_number - 1]

unique_values = pd.unique(df[column_name])

print('Number of unique items: ' + str(len(unique_values)))

show_items = mf.get_yes_no('Show item/counts (y/n)? ')
if ( (show_items == 'y') | (show_items == 'Y') ):
	for item in unique_values:
		print(str(item) + ': ' + str(df[df[column_name] == item].shape[0]))