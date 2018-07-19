################################################################################################
# Script that removes the genes other than BRCA1 and BRCA2 from a VEP-formatted file
# Call the script as:
# python RemoveExtraGenes.py <file to modify>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------

readFile = open(sys.argv[1], "r") # Opens the given file for reading.
lines = readFile.readlines() # Copies every line into a list called lines.
readFile.close()

writeFile = open(sys.argv[1], "w") # Opens the given file for writing.
for line in lines: # Checks every line for "BRCA1" or "BRCA1". If not present removes the line.
	parsedLine = line.split('\t')
	if ( "BRCA1" in parsedLine or "BRCA2" in parsedLine ):
		writeFile.write(line)
writeFile.close()