################################################################################################
# Script that searches through a csv file (with a specific format!) that returns the genomic
# coordinate of each variant in the file.
# Call the script as:
# python GetGenomicCoordinate!!!.py <file to read from> <file to write to>
################################################################################################

#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------
# Opens csv file for read/write
with open(sys.argv[1], newline='') as csvfile:
	writeFile = open(sys.argv[2], 'w+') # Opens file for write.
	reader    = csv.reader(csvfile, delimiter=' ', quotechar='|') # Creates csv reader
	for variant in reader: # Writes the genomic coordinate of every variant to the file
		variantProperies = variant[0].split(",")
		writeFile.write(variantProperies[0] + '\n')
	writeFile.close()