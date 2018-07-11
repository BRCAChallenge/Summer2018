################################################################################################
# Script that formats the output from VAI into a readable format.
# Call the script as:
# python VaiParser.py <file to read from> <file to write to>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------

## Updates integerList so that each element in integerList is equal or larger than the length
# of the string in the same (by index) element in otherList.
#       @param integerlist : A list that contains the width of each column.
#       @param otherList   : A list that will update integerList so that each element in 
#                            otherList fits in column of width specified by integerList.
#
def UpdateMaxPerElement(integerList, otherList):
	for index in range(0, len(integerList)):
		if ( len(otherList[index]) > integerList[index] ):
			integerList[index] = len(otherList[index])

## Returns the length of a tab-delineated list.
#		@param someLine : The line to determine the number of elements in.
#		@return : The size of the tab-delineated list 
# 
def SetNumberOfColumns(someLine):
	parsedList = someLine.split('\t')
	return len(parsedList)

# Open files for read/write.
fileR = open(sys.argv[1], 'r')
fileW = open(sys.argv[2], 'w+')

# Sets firstLine to header line of the file.
firstLine = "#"
while ( firstLine[0] == "#"):
	firstLine = fileR.readline()

# Sets numberColumns to the number of columns in the header line.
numberColumns = SetNumberOfColumns(firstLine)
listOfWidths  = [0] * numberColumns

fileR.seek(0) # Resets the pointer to the position in the file to the start.
for line in fileR: # Iterates through each line in the file.
	if ( line[0] != "#" ): # Checks if the line is not a comment.
		parsedLine = line.split('\t')
		UpdateMaxPerElement(listOfWidths, parsedLine) # Updates the approriate width for each column
fileR.seek(0) # Resets the pointer to the position in the file to the start.
for line in fileR: # Iterates through each line in the file.
	if ( line[0] != "#" ): # Checks if the line is not a comment.
		parsedLine = line.split('\t')
		for index in range(0, len(parsedLine)): # Writes the columns with appropriate spacing.
			fileW.write(parsedLine[index].ljust(listOfWidths[index]) + "    ")
		fileW.write('\n')

fileR.close()
fileW.close()
