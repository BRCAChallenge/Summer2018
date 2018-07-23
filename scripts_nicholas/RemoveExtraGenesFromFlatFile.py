################################################################################################
# This script removes every variant that is not contained within BRCA1 and BRCA2 in the list of
# variants in a VEP-formatted file.
# Call the script as:
# python RemoveExtraGenesVEP.py <file to modify>
################################################################################################

#----------------------------------------------------------------------------------------------
import sys # For command-line arguments
#----------------------------------------------------------------------------------------------

fileRead = open(sys.argv[1], "r")
lines = fileRead.readlines()
fileRead.close()

lines.sort()

fileWrite = open(sys.argv[1], "w")
for line in lines:
	if ( "BRCA1" in line or "BRCA2" in line or line[0] == '#' ):
		fileWrite.write(line)
fileWrite.close()