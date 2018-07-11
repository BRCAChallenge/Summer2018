################################################################################################
# Script that searches through a csv file (with a specific format!) that returns the genomic
# coordinate of each variant in the file.
# Call the script as:
# python GetGenomicCoordinate.py <file to read from> <file to write to>
################################################################################################

#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------
# Opens csv file for read/write
with open(sys.argv[1], newline='') as csvfile:
	writeFile = open(sys.argv[2], 'w+') # Opens file for write.
	reader    = csv.reader(csvfile, delimiter=' ', quotechar='|') # Creates csv reader
	count = 0 
	for variant in reader: # Writes the genomic coordinate of every variant to the file
		if ( count != 0 ): # Ignores the first line because it is only a header.
			variantProperies = variant[0].split(",")
			for i in range(0, len(variantProperies[1])):
				if ( i > 2 ):
					writeFile.write(variantProperies[1][i])
			writeFile.write('\n')
		count += 1
	writeFile.close()