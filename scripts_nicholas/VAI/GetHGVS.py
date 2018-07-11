################################################################################################
# Script that searches through a csv file (with a specific format!) that returns the genomic
# coordinate of each variant in the file in HGVS format.
# Call the script as:
# python GetHGVS.py <file to read from> <file to write to>
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
			#parsedGenomicCoordinate = variantProperies[3].split(":")
			writeFile.write(variantProperies[3])
			writeFile.write('\n')
		count += 1
	writeFile.close()