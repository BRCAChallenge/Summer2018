################################################################################################
# Call the script as:
# python removeExtraColumns.py <file to modify>
################################################################################################

#----------------------------------------------------------------------------------------------
import sys # For command-line arguments
#----------------------------------------------------------------------------------------------

def removeExtraColumns(file):
	# Reads the lines of a flat file (this should be changed to load in chunks).
	fileRead = open(sys.argv[1], "r")
	lines = fileRead.readlines()
	fileRead.close()

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

# arg1 : 
removeExtraColumns(sys.argv[1])