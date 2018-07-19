################################################################################################
# Script that removes the variants that don't have canonical (IDs) <- Change to better word
# To call this script:
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
	if ( parsedLine[3] == "BRCA2" ):
		if ( parsedLine[4] == "NM_000059.3" ):
			writeFile.write(line)
	else: 
		if ( parsedLine[4] == "NM_007294.3"):
			writeFile.write(line)
writeFile.close()