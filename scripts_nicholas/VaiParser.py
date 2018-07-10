"""
Script that formats the output from VAI into a readable format.
Call the script as:
python VaiParser.py <file to read from> <file to write to>
"""

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------
def UpdateMaxPerElement(integerList, otherList):
	for index in range(0, len(integerList)):
		if ( len(otherList[index]) > integerList[index] ):
			integerList[index] = len(otherList[index])

def SetNumberOfColumns(someList):
	parsedList = someList.split('\t')
	return len(parsedList)

# Open files for read/write
fileR = open(sys.argv[1], 'r')
fileW = open(sys.argv[2], 'w+')


firstLine = "#"
while ( firstLine[0] == "#"):
	firstLine = fileR.readline()

numberColumns = SetNumberOfColumns(firstLine)
listOfWidths  = [0] * numberColumns

fileR.seek(0)
for line in fileR:
	if ( line[0] != "#" ):
		parsedLine = line.split('\t')
		UpdateMaxPerElement(listOfWidths, parsedLine)
fileR.seek(0)
for line in fileR:
	if ( line[0] != "#" ):
		parsedLine = line.split('\t')
		for index in range(0, len(parsedLine)):
			fileW.write(parsedLine[index].ljust(listOfWidths[index]) + "    ")
		fileW.write('\n')

fileR.close()
fileW.close()
