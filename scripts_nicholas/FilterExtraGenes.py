################################################################################################
# Call the script as:
# python FilterExtraGenes.py <file to modify>
################################################################################################

#----------------------------------------------------------------------------------------------
import sys # For command-line arguments
#----------------------------------------------------------------------------------------------

## Removes all variants from a flat file that do not refer to the genes BRCA1 and BRCA2.
#  @param file : The file as input to the script. The file can be any basic flat file, but each
#                variant must reference the gene it is contained in.
def FilterExtraGenes(file):
	# Reads the lines of a flat file (this should be changed to load in chunks).
	fileRead = open(sys.argv[1], "r")
	lines = fileRead.readlines()
	fileRead.close()

	lines.sort()

	# Writes the filtered variants to the same file.
	fileWrite = open(sys.argv[1], "w")
	for line in lines:
		if ( "BRCA1" in line or "BRCA2" in line or line[0] == '#' ):
			fileWrite.write(line)
	fileWrite.close()

################################ Main ################################

# arg1 : The file to filter the extra genes from. It can be any flat file.
FilterExtraGenes(sys.argv[1])