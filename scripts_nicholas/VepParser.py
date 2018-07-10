"""
Script that searches through the data file provided by the VEP Web Tool for: (1) the genomic
coordinate of the variant for hg38, (2) the pathogenicity of the variant. Outputs are then 
formatted into file with path specified by the command-line.
Call the script as:
python VepParser.py <file to read from> <file to write to>
"""

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------
# Open files for read/write
fileR = open(sys.argv[1], 'r')
fileW = open(sys.argv[2], 'w+')

for line in fileR: # Iterates through each line in the file
	new_list = line.split('\t')    # Each tab delineated string becomes an element of a list
	fileW.write( new_list[0] + '\t' )
	newString = new_list[3]
	#fileW.write() # Prints the genomic coordinate
	fileW.write(newString.ljust(50))
	for item in new_list: # Iterates through the line looking for key words
		newer_list = item.split(",") # Each comma dilineated string becomes an element of a newer list
		if ( "benign" in newer_list ): # Checks if the variant is benign
			fileW.write("benign ")
		if ( "likely_benign" in newer_list ): # Checks if the variant is "likely benign"
			fileW.write("likely_benign ")
		if ( "uncertain_significance " in newer_list ): # Checks if the variant is "uncertain"
			fileW.write("uncertain_significance ")
		if ( "pathogenic" in newer_list ): # Checks if the variant is pathogenic
			fileW.write("pathogenic ")
		if ( "likely_pathogenic" in newer_list ): # Checks if the variant is "likely pathogenic"
			fileW.write("likely_pathogenic ")
	fileW.write('\n')
fileR.close()
fileW.close()
