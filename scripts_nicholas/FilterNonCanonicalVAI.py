################################################################################################
# Script that removes the variants that don't have canonical (IDs) <- Change to better word
# To call this script:
# python RemoveExtraGenes.py <file to modify>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------

readFile = open(sys.argv[1], 'r') # Opens the given file for reading.
lines = readFile.readlines() # Copies every line into a list called lines.
readFile.close()

writeFile = open(sys.argv[1], 'w') # Opens the given file for writing.
for line in lines: # Checks every line for "BRCA1" or "BRCA1". If not present removes the line.
	if ( ('NM_000059.3' in line) | ('NM_007294.3' in line) | (line[0] == '#') ):
			writeFile.write(line)
writeFile.close()