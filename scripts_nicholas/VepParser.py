"""
Script that searches through the data file provided by the VEP Web Tool for: (1) the genomic
coordinate of the variant for hg38, (2) the pathogenicity of the variant. Outputs both formatted
into a file called VEPScoresOut.txt on the desktop.
"""
#------------------------------------------------------------------------------------------------
# Open files for read/write
fileR = open('/Users/nicholaslenz/Desktop/VEPScores.txt', 'r')
fileW = open('/Users/nicholaslenz/Desktop/VEPScoresOut.txt', 'w')

for line in fileR: # Iterates through each line in the file
	new_list = line.split('\t')    # Each tab delineated string becomes an element of a list
	fileW.write(new_list[0] + '\t') # Prints the genomic coordinate
	for item in new_list: # Iterates through the line looking for key words
		newer_list = item.split(",") # Each comma dilineated string becomes an element of a newer list
		if ( "benign" in newer_list or "likely_benign" in newer_list or \
		"uncertain_significance" in newer_list or "pathogenic" in newer_list or \
		"likely_pathogenic" in newer_list ): # Check if a keyword is in a line
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
