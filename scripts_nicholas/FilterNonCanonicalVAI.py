################################################################################################
# To call this script:
# python RemoveExtraGenes.py <file to modify>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------

## Removes the variants from a flat file that don't have canonical IDs. This only works with
#      variants that are identified in HGVS notation.
#  @param file : The flat file to remove variants with non-canonocal HGVS identifications.
def RemoveExtraGenes(file):

	# Creates a list containing each line (A lot of RAM!)
	readFile = open(sys.argv[1], 'r')
	lines = readFile.readlines()
	readFile.close()

	# Writes every line that contains a variant with a conanical HGVS identification or is a
	# header
	writeFile = open(sys.argv[1], 'w')
	for line in lines:
		if ( ('NM_000059.3' in line) | ('NM_007294.3' in line) | (line[0] == '#') ):
				writeFile.write(line)
	writeFile.close()

################################ Main ################################

# arg1 : path to flat file to modify.
RemoveExtraGenes(sys.argv[1])