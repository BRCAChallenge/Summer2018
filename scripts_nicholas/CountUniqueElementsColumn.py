################################################################################################
# This script counts the number of unique elements in a specified column in a VEP-formatted file.
# Call the script as:
# python CountUniqueElementsColumn.py <file to read from> <index of column>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------

fileRead = open(sys.argv[1], "r") # Opens given file for reading.

variants = []
for variant in fileRead: # Adds every string in a given column to the list variants.
	parsedVariant = variant.split('\t')
	variants.append(parsedVariant[int(sys.argv[2])])

fileRead.close()
print (len(set(variants))) # Construction of the set removes the duplicates in variants.
