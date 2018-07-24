################################################################################################
# This script counts the number of unique elements in a specified column in a VEP-formatted file.
# Call the script as:
# python CountUniqueElementsColumn.py <file to read from> <index of column>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018 (Repo)/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

fileRead = open(sys.argv[1], "r")
column_number = mf.get_int_answer('What column should be accumulated? ')

variants = []
for variant in fileRead: # Adds every string in a given column to the list variants.
	parsedVariant = variant.split('\t')
	variants.append(parsedVariant[column_number])

fileRead.close()
print (len(set(variants))) # Construction of the set removes the duplicates in variants.
