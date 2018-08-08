################################################################################################
# Call the script as:
# python ConvertHGVSToGenCoords.py <file to read><file to write>
################################################################################################

#----------------------------------------------------------------------------------------------
import sys # For command-line arguments
#----------------------------------------------------------------------------------------------

def ConvertHGVSToGenCoords(read_file, write_file):
	# Reads the lines of a flat file (this should be changed to load in chunks).
	fileRead = open(sys.argv[1], "r")
	lines = fileRead.readlines()
	fileRead.close()

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

# arg1 :
# arg2 : 
ConvertHGVSToGenCoords(sys.argv[1], sys.argv[2])