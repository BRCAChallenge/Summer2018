################################################################################################
# This script counts the number of unique elements in a specified column in a VEP-formatted file.
# Call the script as:
# python CountUniqueElementsColumn.py <file to read from> <index of column>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018 (Repo)/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

sep = mf.determine_separator(sys.argv[1])
df = pd.read_csv(sys.argv[1], sep=sep, header=0)

mf.print_columns_with_index(df)
column_number = mf.get_int_answer('What column should be accumulated? ')
column_name = list(df.columns)[column_number - 1]

print(len(pd.unique(df[column_name])))
