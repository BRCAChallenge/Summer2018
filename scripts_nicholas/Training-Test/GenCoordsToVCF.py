################################################################################################
# Call the script as:
# python ConvertHGVSToGenCoords.py <file to read><file to write>
################################################################################################

#----------------------------------------------------------------------------------------------
import sys # For command-line arguments
#----------------------------------------------------------------------------------------------

"""
This function generates a vcf file from a file with genomic coordinate IDs.
    @param read_file  : The file to read the genomic coordinate IDs from. Each variant/ID
                        should occupy its own line.
    @param write_file : The vcf file to write/create.
"""
def ConvertHGVSToGenCoords(read_file, write_file):
	# Reads the lines of a flat file (this should be changed to load in chunks).
	fileRead = open(sys.argv[1], "r")
	lines = fileRead.readlines()
	fileRead.close()

	# Writes the appropriate columns of the vcf file.
	fileWrite = open(sys.argv[2], "w")
	for line in lines:
		fileWrite.write(line[3:5] + '\t'
			          + line[8:16] + '\t'
			          + line[0:-1] + '\t'
			          + line[-4] + '\t'
			          + line[-2] + '\t'
			          + '.\t' + 'PASS\t' + '.\n'
					   )
	fileWrite.close()

################################ Main ################################

# arg1 : The file to read from. It should contain genomic coordinate IDs of all the variants to
#        be processed, where each ID is on its own line.
# arg2 : The vcf file to write to/create. Make sure to end the file name in ".vcf"
ConvertHGVSToGenCoords(sys.argv[1], sys.argv[2])