################################################################################################
# Call the script as:
# python removeExtraColumns.py <file to modify>
################################################################################################

#----------------------------------------------------------------------------------------------
import sys # For command-line arguments
#----------------------------------------------------------------------------------------------

"""
This function removes the extra columns from the output of a Mutalyzer batch conversion between
    different HGVS formats. The result is a single column with the genomic coordinates IDs of
    each variant.
    @param file : The file to remove the extra columns from, which is the output of a batch job
                  from Mutalyzer on HGVSg notations of variants.
"""
def removeExtraColumns(file):
	# Reads the lines of a flat file (this should be changed to load in chunks).
	fileRead = open(sys.argv[1], "r")
	lines = fileRead.readlines()
	fileRead.close()

	# Generates the genomic coordinate ID's for each variant from the HGVSg notation. Ignores
	# the first line of the file.
	fileWrite = open(sys.argv[1], "w")
	count = 0
	for line in lines:
		if( count > 0 ):
			headings = line.split('\t')
			ending = headings[2][-14:-3] + ':' + headings[2][-3:] + '\n'
			if( headings[0][0:11] == 'NM_000059.3'):
				fileWrite.write('chr13' + ending)
			else:
				fileWrite.write('chr17' + ending)
		else:
			headings = line.split('\t')
			fileWrite.write(headings[0] + '\t' + headings[1] + '\t' + headings[2] + '\n')
		count = count + 1
	fileWrite.close()

################################ Main ################################

# arg1 : File to remove columns from. It should be the output of a batch job from Mutalyzer on
#        HGVSg notations of variants.
removeExtraColumns(sys.argv[1])